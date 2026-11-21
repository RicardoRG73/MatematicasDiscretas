#!/usr/bin/env python3
"""Exportador en lote para las diapositivas Marp de Matemáticas Discretas (LISSI0211).

Convierte las presentaciones Markdown en ``diapositivas/*.md`` a PDF (por
defecto), PPTX o HTML mediante ``@marp-team/marp-cli`` de forma incremental,
conservando el tema de color y diseño definidos en cada presentación.

Requisitos del sistema:
    - Python 3.9+ (solo biblioteca estándar)
    - ``marp`` (``@marp-team/marp-cli``) o ``npx`` con Node.js instalado
    - Para exportar a PDF o PPTX: Chrome/Chromium, Edge o Firefox

Ejemplos de uso:
    python3 generar_diapositivas.py                   # Solo presentaciones modificadas (PDF)
    python3 generar_diapositivas.py 1-1 3-2           # Exporta presentaciones específicas
    python3 generar_diapositivas.py --unidad 4        # Exporta toda la Unidad 4
    python3 generar_diapositivas.py --formato pptx    # Exporta a PowerPoint (.pptx)
    python3 generar_diapositivas.py --forzar          # Regenera todas las diapositivas
"""

from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import time
from typing import Iterable


RE_IMAGEN_MD = re.compile(r"!\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
RE_CODIGO_CERCADO = re.compile(r"^\s*```")


@dataclass
class ResultadoExportacion:
    """Resultado de exportar o verificar una presentación individual."""

    archivo_md: Path
    archivo_salida: Path
    estado: str  # "generado", "omitido", "error"
    duracion_s: float = 0.0
    detalle: str = ""
    registro: str = ""


def encontrar_marp() -> tuple[list[str], bool]:
    """Localiza ``marp`` o ``npx`` para invocar ``@marp-team/marp-cli``.

    Retorna una tupla ``(comando_base, usa_npx)``.
    """
    marp = shutil.which("marp")
    if marp:
        return [marp], False

    raiz = Path(__file__).resolve().parent
    candidatos = [
        Path.home() / ".local" / "bin" / "marp",
        Path.home() / ".npm-global" / "bin" / "marp",
        raiz / "node_modules" / ".bin" / "marp",
    ]
    for ruta in candidatos:
        if ruta.is_file() and os.access(ruta, os.X_OK):
            return [str(ruta)], False

    npx = shutil.which("npx")
    if npx:
        return [npx, "--yes", "@marp-team/marp-cli"], True

    raise FileNotFoundError(
        "No se encontró 'marp' ni 'npx' en el PATH. "
        "Instale '@marp-team/marp-cli' (p. ej. 'npm install -g @marp-team/marp-cli') "
        "o Node.js para usar 'npx'."
    )


def detectar_navegador(preferencia: str, navegador_ruta: Path | None) -> str:
    """Determina el navegador compatible con Marp CLI para exportar PDF/PPTX."""
    if preferencia != "auto":
        return preferencia

    if navegador_ruta is not None:
        nombre = navegador_ruta.name.lower()
        if "firefox" in nombre:
            return "firefox"
        if "edge" in nombre or "msedge" in nombre:
            return "edge"
        return "chrome"

    candidatos = (
        (("google-chrome", "chromium", "chromium-browser", "chrome"), "chrome"),
        (("microsoft-edge", "microsoft-edge-stable", "msedge"), "edge"),
        (("firefox", "firefox-esr"), "firefox"),
    )
    for binarios, etiqueta in candidatos:
        for binario in binarios:
            if shutil.which(binario):
                return etiqueta

    raise FileNotFoundError(
        "No se encontró un navegador compatible (Chrome, Chromium, Edge o Firefox) "
        "para exportar PDF/PPTX. Instale uno de ellos, indique '--navegador-ruta' "
        "o exporte con '--formato html'."
    )


def extraer_rutas_imagenes(ruta_md: Path) -> list[Path]:
    """Extrae rutas locales de imágenes referenciadas fuera de bloques de código."""
    texto = ruta_md.read_text(encoding="utf-8").replace("\r\n", "\n")
    dir_md = ruta_md.resolve().parent
    rutas: list[Path] = []
    en_codigo = False

    for linea in texto.splitlines():
        if RE_CODIGO_CERCADO.match(linea):
            en_codigo = not en_codigo
            continue
        if en_codigo:
            continue
        for match in RE_IMAGEN_MD.finditer(linea):
            destino = match.group(1)
            if not destino.startswith(("http://", "https://", "/")):
                candidato = (dir_md / destino).resolve()
                if candidato.is_file():
                    rutas.append(candidato)
    return rutas


def necesita_regenerar(
    ruta_md: Path,
    ruta_salida: Path,
    forzar: bool,
    ruta_tema: Path | None = None,
) -> bool:
    """Indica si el archivo exportado falta o es anterior al Markdown, tema o figuras."""
    if forzar or not ruta_salida.is_file():
        return True
    mtime_salida = ruta_salida.stat().st_mtime
    if ruta_md.stat().st_mtime > mtime_salida:
        return True
    if ruta_tema is not None and ruta_tema.is_file() and ruta_tema.stat().st_mtime > mtime_salida:
        return True
    for img in extraer_rutas_imagenes(ruta_md):
        if img.stat().st_mtime > mtime_salida:
            return True
    return False


def resolver_diapositivas(
    dir_entrada: Path,
    objetivos: Iterable[str],
    unidades: list[int] | None,
) -> list[Path]:
    """Resuelve la lista ordenada de presentaciones ``.md`` a exportar."""
    todas = sorted(p for p in dir_entrada.glob("*.md") if p.is_file())
    if not todas:
        raise FileNotFoundError(f"No se encontraron presentaciones Markdown en '{dir_entrada}'.")

    seleccion: list[Path] = []
    objetivos_lista = list(objetivos)

    if objetivos_lista:
        por_nombre = {p.name: p for p in todas}
        por_stem = {p.stem: p for p in todas}
        agregados: set[Path] = set()

        for obj in objetivos_lista:
            ruta_obj = Path(obj)
            if ruta_obj.is_file() and ruta_obj.suffix.lower() == ".md":
                resuelta = ruta_obj.resolve()
                if resuelta not in agregados:
                    seleccion.append(resuelta)
                    agregados.add(resuelta)
                continue

            if obj in por_nombre:
                p = por_nombre[obj]
                if p not in agregados:
                    seleccion.append(p)
                    agregados.add(p)
                continue

            if obj in por_stem:
                p = por_stem[obj]
                if p not in agregados:
                    seleccion.append(p)
                    agregados.add(p)
                continue

            coincidencias = [p for p in todas if p.stem.startswith(f"{obj}-") or p.stem.startswith(obj)]
            if len(coincidencias) == 1:
                p = coincidencias[0]
                if p not in agregados:
                    seleccion.append(p)
                    agregados.add(p)
            elif len(coincidencias) > 1:
                nombres = ", ".join(c.name for c in coincidencias)
                raise ValueError(
                    f"El objetivo '{obj}' coincide con múltiples presentaciones ({nombres}). "
                    "Especifique el nombre completo o use --unidad."
                )
            else:
                raise FileNotFoundError(f"No se encontró ninguna presentación que coincida con '{obj}'.")
    else:
        seleccion = todas

    if unidades:
        prefijos = tuple(f"{u}-" for u in unidades)
        seleccion = [p for p in seleccion if p.name.startswith(prefijos)]

    return seleccion


def preparar_cache_marp(cmd_marp: list[str]) -> None:
    """Calienta la caché de ``npx`` antes de ejecutar exportaciones en paralelo."""
    res = subprocess.run(
        [*cmd_marp, "--version"],
        text=True,
        encoding="utf-8",
        errors="replace",
        capture_output=True,
    )
    if res.returncode != 0:
        detalle = res.stderr.strip() or res.stdout.strip()
        raise RuntimeError(f"No se pudo inicializar '@marp-team/marp-cli': {detalle}")


def exportar_diapositiva(
    ruta_md: Path,
    ruta_salida: Path,
    cmd_marp: list[str],
    formato: str,
    navegador: str | None,
    navegador_ruta: Path | None,
    timeout_s: int,
    ruta_tema: Path | None = None,
) -> ResultadoExportacion:
    """Exporta una presentación Marp al formato solicitado usando escritura atómica."""
    inicio = time.monotonic()

    with tempfile.TemporaryDirectory(prefix="marp_exp_") as tmp_dir:
        archivo_tmp = Path(tmp_dir) / f"{ruta_md.stem}.{formato}"
        cmd = [*cmd_marp, str(ruta_md), "--allow-local-files", "--output", str(archivo_tmp)]
        if ruta_tema is not None:
            cmd.extend(["--theme-set", str(ruta_tema)])

        if formato in ("pdf", "pptx"):
            cmd.append(f"--{formato}")
            if navegador:
                cmd.extend(["--browser", navegador])
                if navegador == "firefox":
                    cmd.extend(["--browser-protocol", "webdriver-bidi"])
            if navegador_ruta is not None:
                cmd.extend(["--browser-path", str(navegador_ruta)])
            cmd.extend(["--browser-timeout", str(timeout_s)])

        res = subprocess.run(
            cmd,
            text=True,
            encoding="utf-8",
            errors="replace",
            capture_output=True,
        )
        salida_cli = "\n".join(p for p in (res.stdout.strip(), res.stderr.strip()) if p)

        if res.returncode != 0:
            resumen = salida_cli[-450:] if salida_cli else f"código de salida {res.returncode}"
            return ResultadoExportacion(
                archivo_md=ruta_md,
                archivo_salida=ruta_salida,
                estado="error",
                duracion_s=time.monotonic() - inicio,
                detalle=f"Error de Marp CLI: {resumen}",
                registro=salida_cli,
            )

        if not archivo_tmp.is_file() or archivo_tmp.stat().st_size == 0:
            return ResultadoExportacion(
                archivo_md=ruta_md,
                archivo_salida=ruta_salida,
                estado="error",
                duracion_s=time.monotonic() - inicio,
                detalle=f"Marp CLI finalizó sin generar '{archivo_tmp.name}'.",
                registro=salida_cli,
            )

        ruta_salida.parent.mkdir(parents=True, exist_ok=True)
        fd, tmp_dest = tempfile.mkstemp(
            prefix=f".{ruta_salida.stem}.",
            suffix=f".{formato}.tmp",
            dir=str(ruta_salida.parent),
        )
        os.close(fd)
        try:
            shutil.copy2(archivo_tmp, tmp_dest)
            os.replace(tmp_dest, ruta_salida)
        finally:
            if os.path.exists(tmp_dest):
                os.unlink(tmp_dest)

        return ResultadoExportacion(
            archivo_md=ruta_md,
            archivo_salida=ruta_salida,
            estado="generado",
            duracion_s=time.monotonic() - inicio,
            registro=salida_cli,
        )


def crear_parser() -> argparse.ArgumentParser:
    """Construye el analizador de argumentos de línea de comandos."""
    raiz = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(
        prog="generar_diapositivas.py",
        description=(
            "Exporta en lote las presentaciones Marp de diapositivas/ a PDF, "
            "PPTX o HTML conservando el tema de color y tamaño de letra del curso."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Ejemplos:\n"
            "  python3 generar_diapositivas.py                 # Exporta solo modificadas (PDF)\n"
            "  python3 generar_diapositivas.py 1-1 3-2         # Exporta presentaciones específicas\n"
            "  python3 generar_diapositivas.py --unidad 4      # Exporta toda la Unidad 4\n"
            "  python3 generar_diapositivas.py --formato pptx  # Exporta a PowerPoint (.pptx)\n"
            "  python3 generar_diapositivas.py --forzar        # Regenera todas desde cero\n"
        ),
    )
    parser.add_argument(
        "objetivos",
        nargs="*",
        help="Presentaciones específicas a exportar (ej. 1-1, 3-2-logica-de-predicados o ruta al .md).",
    )
    parser.add_argument(
        "-t",
        "--formato",
        choices=("pdf", "pptx", "html"),
        default="pdf",
        help="Formato de exportación (por defecto: pdf).",
    )
    parser.add_argument(
        "-f",
        "--forzar",
        "--todos",
        action="store_true",
        dest="forzar",
        help="Regenera las salidas seleccionadas aunque estén actualizadas.",
    )
    parser.add_argument(
        "-u",
        "--unidad",
        type=int,
        choices=[1, 2, 3, 4, 5, 6],
        action="append",
        help="Filtra las presentaciones por número de unidad (1 a 6). Puede repetirse.",
    )
    parser.add_argument(
        "-e",
        "--entrada",
        type=Path,
        default=raiz / "diapositivas",
        help="Directorio con las presentaciones Marp (por defecto: diapositivas/).",
    )
    parser.add_argument(
        "-o",
        "--salida",
        type=Path,
        default=None,
        help="Directorio de salida (por defecto: diapositivas/<formato>/, p. ej. diapositivas/pdf/).",
    )
    parser.add_argument(
        "--tema",
        type=Path,
        default=None,
        help="Archivo CSS de tema Marp (--theme-set). Por defecto usa <entrada>/tema-discretas.css si existe.",
    )
    parser.add_argument(
        "--navegador",
        choices=("auto", "chrome", "edge", "firefox"),
        default="auto",
        help="Navegador usado por Marp CLI para PDF/PPTX (por defecto: auto).",
    )
    parser.add_argument(
        "--navegador-ruta",
        type=Path,
        default=None,
        help="Ruta explícita al ejecutable del navegador (--browser-path).",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=60,
        help="Tiempo máximo en segundos por operación del navegador (por defecto: 60).",
    )
    parser.add_argument(
        "-j",
        "--trabajos",
        type=int,
        default=min(4, os.cpu_count() or 2),
        help="Número máximo de exportaciones en paralelo (por defecto: min(4, CPU)).",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Muestra archivos omitidos y salida detallada de Marp CLI.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    """Punto de entrada principal del exportador de diapositivas."""
    parser = crear_parser()
    args = parser.parse_args(argv)

    dir_entrada = args.entrada.resolve()
    dir_salida = (args.salida or (dir_entrada / args.formato)).resolve()
    navegador_ruta = args.navegador_ruta.resolve() if args.navegador_ruta else None

    if not dir_entrada.is_dir():
        print(f"Error: el directorio de entrada '{dir_entrada}' no existe.", file=sys.stderr)
        return 1

    if navegador_ruta is not None and not navegador_ruta.is_file():
        print(f"Error: el ejecutable del navegador '{navegador_ruta}' no existe.", file=sys.stderr)
        return 1

    if args.tema is not None:
        ruta_tema = args.tema.resolve()
        if not ruta_tema.is_file():
            print(f"Error: el archivo de tema '{ruta_tema}' no existe.", file=sys.stderr)
            return 1
    else:
        candidato_tema = dir_entrada / "tema-discretas.css"
        ruta_tema = candidato_tema if candidato_tema.is_file() else None

    try:
        presentaciones = resolver_diapositivas(dir_entrada, args.objetivos, args.unidad)
    except (FileNotFoundError, ValueError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    if not presentaciones:
        print("No se encontraron presentaciones que coincidan con los filtros indicados.")
        return 0

    forzar_exportacion = args.forzar or bool(args.objetivos)
    por_exportar: list[tuple[Path, Path]] = []
    omitidos: list[Path] = []

    for ruta_md in presentaciones:
        destino = dir_salida / f"{ruta_md.stem}.{args.formato}"
        if necesita_regenerar(ruta_md, destino, forzar_exportacion, ruta_tema):
            por_exportar.append((ruta_md, destino))
        else:
            omitidos.append(ruta_md)

    if args.verbose:
        for ruta_md in omitidos:
            print(f"[OMITIDO]  {ruta_md.name} ({args.formato.upper()} actualizado)")

    if not por_exportar:
        print(
            f"Todas las salidas {args.formato.upper()} ({len(omitidos)}/{len(presentaciones)}) "
            f"están actualizadas en '{dir_salida}'. Use --forzar para regenerarlas."
        )
        return 0

    try:
        cmd_marp, usa_npx = encontrar_marp()
        navegador = detectar_navegador(args.navegador, navegador_ruta) if args.formato in ("pdf", "pptx") else None
        if usa_npx and len(por_exportar) > 1:
            preparar_cache_marp(cmd_marp)
    except (FileNotFoundError, RuntimeError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    info_nav = f" (navegador: {navegador})" if navegador else ""
    print(f"Exportando {len(por_exportar)} presentación(es) a {args.formato.upper()}{info_nav} en '{dir_salida}'...")
    t_inicio = time.monotonic()
    resultados: list[ResultadoExportacion] = []

    trabajos = max(1, min(args.trabajos, len(por_exportar)))
    with ThreadPoolExecutor(max_workers=trabajos) as ejecutor:
        futuros = {
            ejecutor.submit(
                exportar_diapositiva,
                ruta_md,
                destino,
                cmd_marp,
                args.formato,
                navegador,
                navegador_ruta,
                args.timeout,
                ruta_tema,
            ): ruta_md
            for ruta_md, destino in por_exportar
        }
        for futuro in as_completed(futuros):
            res = futuro.result()
            resultados.append(res)
            if res.estado == "generado":
                print(f"[OK]       {res.archivo_salida.name} ({res.duracion_s:.2f}s)")
                if args.verbose and res.registro:
                    for linea in res.registro.splitlines():
                        print(f"           {linea}")
            else:
                print(f"[ERROR]    {res.archivo_md.name}: {res.detalle}", file=sys.stderr)

    generados = sum(1 for r in resultados if r.estado == "generado")
    errores = sum(1 for r in resultados if r.estado == "error")
    duracion_total = time.monotonic() - t_inicio

    print(
        f"\nResumen: {generados} generado(s), {len(omitidos)} omitido(s), "
        f"{errores} error(es) en {duracion_total:.2f}s."
    )
    return 1 if errores else 0


if __name__ == "__main__":
    sys.exit(main())

