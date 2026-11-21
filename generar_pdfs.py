#!/usr/bin/env python3
"""Generador de PDF para las notas de Matemáticas Discretas (LISSI0211).

Convierte los apuntes en Markdown ubicados en ``notas/*.md`` a documentos PDF
en ``notas/pdf/*.pdf`` mediante Pandoc (con filtro Lua embebido) y XeLaTeX,
conservando el tema de color y el diseño tipográfico del curso.

Requisitos del sistema:
    - Python 3.9+ (solo biblioteca estándar)
    - Pandoc (nativo o incluido con Quarto)
    - XeLaTeX (TeX Live con fontspec, xcolor, tcolorbox, unicode-math, etc.)

Ejemplos de uso:
    python3 generar_pdfs.py                 # Solo notas nuevas o modificadas
    python3 generar_pdfs.py --forzar        # Regenera todas las notas
    python3 generar_pdfs.py 1-1 3-2         # Genera notas específicas
    python3 generar_pdfs.py --unidad 4      # Genera toda la Unidad 4
"""

from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
import glob
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import time
from typing import Iterable


# Paleta de colores extraída directamente de los PDF vigentes en notas/pdf/
TEMA_COLOR: dict[str, str] = {
    "TextoCuerpo": "1E293B",          # Slate 800 — texto principal y celdas
    "TituloPrincipal": "0F172A",      # Slate 900 — H1, H3, encabezados de tabla, bloque de código
    "TituloSeccion": "1E3A8A",        # Blue 900  — H2 y texto de citas/callouts
    "TituloSubnivel": "334155",       # Slate 700 — H4
    "Acento": "2563EB",               # Blue 600  — línea H1 (2pt), borde izq. cita (3.5pt), enlaces
    "Borde": "CBD5E1",                # Slate 300 — bordes de tabla, separadores, línea H2, borde código
    "BordeFigura": "E2E8F0",          # Slate 200 — marco de tarjeta de figuras
    "FondoTablaEncabezado": "F1F5F9", # Slate 100 — fondo cabecera de tablas y código en línea
    "FondoTablaCebra": "F8FAFC",      # Slate 50  — filas pares de tablas y fondo bloques de código
    "FondoCita": "EFF6FF",            # Blue 50   — fondo de citas/callouts
    "CodigoTexto": "BE123C",          # Rose 700  — texto de código en línea
    "PiePagina": "64748B",            # Slate 500 — numeración opcional de páginas
}

FORMATOS_PANDOC_ENTRADA = (
    "markdown"
    "+tex_math_dollars"
    "+pipe_tables"
    "+lists_without_preceding_blankline"
    "+backtick_code_blocks"
    "+raw_html"
    "-implicit_figures"
)

RE_CERCA_CODIGO = re.compile(r"^\s*```")
RE_APERTURA_COMENTARIO = re.compile(r"^\s*<!--\s*$")
RE_CIERRE_COMENTARIO = re.compile(r"^\s*-->\s*$")
RE_COMENTARIO_INLINE = re.compile(r"<!--.*?-->")
RE_IMAGEN_MD = re.compile(r"!\[([^\]]*)\]\(([^)\s]+)(?:\s+\"([^\"]*)\")?\)")
RE_TITULO_H1 = re.compile(r"^#\s+(.+?)\s*$")
RE_NOT_MATHREL = re.compile(r"\\not\\mathrel\{([^}]+)\}")


FILTRO_LUA = r"""
local utils = require("pandoc.utils")

local REEMPLAZOS_UNICODE_CODIGO = {
  ["∩"] = "\\ensuremath{\\cap}",
  ["∪"] = "\\ensuremath{\\cup}",
  ["×"] = "\\ensuremath{\\times}",
  ["÷"] = "\\ensuremath{\\div}",
  ["≤"] = "\\ensuremath{\\le}",
  ["≥"] = "\\ensuremath{\\ge}",
  ["≠"] = "\\ensuremath{\\neq}",
  ["→"] = "\\ensuremath{\\rightarrow}",
  ["←"] = "\\ensuremath{\\leftarrow}",
  ["↔"] = "\\ensuremath{\\leftrightarrow}",
  ["∀"] = "\\ensuremath{\\forall}",
  ["∃"] = "\\ensuremath{\\exists}",
  ["∅"] = "\\ensuremath{\\emptyset}",
  ["∈"] = "\\ensuremath{\\in}",
  ["∉"] = "\\ensuremath{\\notin}",
  ["⊆"] = "\\ensuremath{\\subseteq}",
  ["∧"] = "\\ensuremath{\\land}",
  ["∨"] = "\\ensuremath{\\lor}",
  ["¬"] = "\\ensuremath{\\neg}",
  ["⊕"] = "\\ensuremath{\\oplus}",
  ["≈"] = "\\ensuremath{\\approx}",
  ["•"] = "\\ensuremath{\\bullet}",
}

local ESCAPES_LATEX = {
  ["\\"] = "\\textbackslash{}",
  ["{"] = "\\{",
  ["}"] = "\\}",
  ["$"] = "\\$",
  ["&"] = "\\&",
  ["#"] = "\\#",
  ["%"] = "\\%",
  ["_"] = "\\_",
  ["^"] = "\\textasciicircum{}",
  ["~"] = "\\textasciitilde{}",
}

local function escapar_codigo_latex(texto, con_cortes)
  local partes = {}
  for _, cp in utf8.codes(texto) do
    local ch = utf8.char(cp)
    if REEMPLAZOS_UNICODE_CODIGO[ch] then
      table.insert(partes, REEMPLAZOS_UNICODE_CODIGO[ch])
    elseif ESCAPES_LATEX[ch] then
      local esc = ESCAPES_LATEX[ch]
      if con_cortes and ch == "_" then
        esc = esc .. "\\allowbreak{}"
      end
      table.insert(partes, esc)
    else
      table.insert(partes, ch)
      if con_cortes and (ch == " " or ch == "." or ch == "," or ch == "/") then
        table.insert(partes, "\\allowbreak{}")
      end
    end
  end
  return table.concat(partes)
end

local function limpiar_ruta_latex(ruta)
  local s = ruta:gsub("\\", "/")
  s = s:gsub("%%", "\\%%")
  s = s:gsub("#", "\\#")
  return s
end

local function a_latex_crudo(bloques)
  local doc = pandoc.Pandoc(bloques)
  local s = pandoc.write(doc, "latex")
  return (s:gsub("^%s+", ""):gsub("%s+$", ""))
end

local function es_salto_br(el)
  if el.t == "RawInline" and el.format:match("^html") then
    return el.text:match("^%s*<[bB][rR]%s*/?>%s*$") ~= nil
  end
  return false
end

local function ancho_visible_celda(celda)
  local s = a_latex_crudo(celda.contents)
  -- Dividir por saltos explícitos de línea para medir la línea más ancha
  s = s:gsub("\\NLCELL%s*", "\n"):gsub("\\\\", "\n")
  -- Simplificar comandos LaTeX comunes; el código en línea en monoespaciado es más ancho
  s = s:gsub("\\inlinecodelong%b{}", function(m) return m:sub(16, -2) end)
  s = s:gsub("\\inlinecode%b{}", function(m)
    local inner = m:sub(12, -2)
    return inner .. string.rep("x", math.ceil(#inner * 0.3))
  end)
  s = s:gsub("\\text%b{}", function(m) return m:sub(7, -2) end)
  s = s:gsub("\\textbf%b{}", function(m) return m:sub(9, -2) end)
  s = s:gsub("\\textit%b{}", function(m) return m:sub(9, -2) end)
  s = s:gsub("\\mathbf%b{}", function(m) return m:sub(9, -2) end)
  s = s:gsub("\\mathbb%b{}", function(m) return m:sub(9, -2) end)
  s = s:gsub("\\operatorname%b{}", function(m) return m:sub(15, -2) end)
  s = s:gsub("\\allowbreak%s*", "")
  s = s:gsub("\\[a-zA-Z]+", "x")
  s = s:gsub("[{}%$\\]", "")

  local max_linea = 0
  for linea in (s .. "\n"):gmatch("(.-)\n") do
    local limpia = linea:gsub("^%s+", ""):gsub("%s+$", "")
    local largo = utf8.len(limpia) or #limpia
    if largo > max_linea then
      max_linea = largo
    end
  end
  return math.max(max_linea, 4)
end

local function letra_alineacion(al)
  if al == pandoc.AlignCenter then
    return "c"
  elseif al == pandoc.AlignRight then
    return "r"
  end
  return "l"
end

local function prefijo_alineacion_p(al)
  if al == pandoc.AlignCenter then
    return ">{\\hspace{0pt}\\centering\\arraybackslash}"
  elseif al == pandoc.AlignRight then
    return ">{\\hspace{0pt}\\raggedleft\\arraybackslash}"
  end
  return ">{\\hspace{0pt}\\raggedright\\arraybackslash}"
end

local function dividir_por_nlcell(s)
  local partes = {}
  local inicio = 1
  while true do
    local i, j = s:find("\\NLCELL%s*", inicio)
    if not i then
      table.insert(partes, s:sub(inicio))
      break
    end
    table.insert(partes, s:sub(inicio, i - 1))
    inicio = j + 1
  end
  return partes
end

local function formatear_celda_natural(celda, al, es_encabezado)
  local s = a_latex_crudo(celda.contents)
  local al_chr = letra_alineacion(al)
  if s:find("\\NLCELL") then
    local lineas = dividir_por_nlcell(s)
    local env_ini = "{\\begin{tabular}[c]{@{}" .. al_chr .. "@{}}"
    if es_encabezado then
      for idx, lin in ipairs(lineas) do
        lineas[idx] = "{\\bfseries\\color{TituloPrincipal}" .. lin .. "}"
      end
    end
    return env_ini .. table.concat(lineas, " \\\\ ") .. "\\end{tabular}}"
  end
  if es_encabezado then
    return "{\\bfseries\\color{TituloPrincipal}" .. s .. "}"
  end
  return s
end

local function formatear_celda_par(celda, es_encabezado)
  local s = a_latex_crudo(celda.contents)
  s = s:gsub("\\NLCELL%s*", "\\newline ")
  if es_encabezado then
    return "{\\bfseries\\color{TituloPrincipal}" .. s .. "}"
  end
  return s
end

local function calcular_pesos_columnas(tbl)
  local ncols = #tbl.colspecs
  local maximos = {}
  for c = 1, ncols do
    maximos[c] = 4
  end

  local function actualizar(filas, factor)
    for _, fila in ipairs(filas) do
      for c = 1, math.min(ncols, #fila.cells) do
        local w = ancho_visible_celda(fila.cells[c]) * factor
        if w > maximos[c] then
          maximos[c] = w
        end
      end
    end
  end

  actualizar(tbl.head.rows, 1.08)
  for _, cuerpo in ipairs(tbl.bodies) do
    actualizar(cuerpo.head, 1.05)
    actualizar(cuerpo.body, 1.0)
  end

  -- Compresión suave para evitar que una columna larga aplaste columnas cortas
  local pesos = {}
  local suma = 0
  for c = 1, ncols do
    pesos[c] = math.sqrt(maximos[c]) + 0.18 * maximos[c]
    suma = suma + pesos[c]
  end

  local min_frac = math.min(0.08, 0.55 / ncols)
  local fracs = {}
  local suma_f = 0
  for c = 1, ncols do
    fracs[c] = math.max(pesos[c] / suma, min_frac)
    suma_f = suma_f + fracs[c]
  end
  for c = 1, ncols do
    fracs[c] = (fracs[c] / suma_f) * 0.992
  end
  return fracs
end

local function extraer_filas(tbl)
  local filas_head = {}
  for _, r in ipairs(tbl.head.rows) do
    table.insert(filas_head, r)
  end
  local filas_body = {}
  for _, cuerpo in ipairs(tbl.bodies) do
    for _, r in ipairs(cuerpo.head) do
      table.insert(filas_body, r)
    end
    for _, r in ipairs(cuerpo.body) do
      table.insert(filas_body, r)
    end
  end
  return filas_head, filas_body
end

local function renderizar_tabla(tbl, en_anidado)
  local ncols = #tbl.colspecs
  local filas_head, filas_body = extraer_filas(tbl)
  local nrows = #filas_body

  local usar_escalado_natural = (ncols >= 8 and nrows <= 24)
  local usar_tabular_ancho = en_anidado or usar_escalado_natural

  local out = {}
  if usar_escalado_natural then
    -- Tabla ancha (8 a 16 columnas): columnas naturales + ajuste automático a \linewidth
    local spec = "|"
    for c = 1, ncols do
      spec = spec .. letra_alineacion(tbl.colspecs[c][1]) .. "|"
    end
    table.insert(out, "\\begin{center}")
    table.insert(out, "\\begingroup")
    table.insert(out, "\\footnotesize")
    table.insert(out, "\\setlength{\\tabcolsep}{4pt}")
    table.insert(out, "\\renewcommand{\\arraystretch}{1.35}")
    table.insert(out, "\\arrayrulecolor{Borde}")
    table.insert(out, "\\begin{adjustbox}{max width=\\linewidth}")
    table.insert(out, "\\begin{tabular}{" .. spec .. "}")
    table.insert(out, "\\hline")
    for _, fila in ipairs(filas_head) do
      local celdas = {}
      for c = 1, ncols do
        local cel = fila.cells[c]
        table.insert(celdas, cel and formatear_celda_natural(cel, tbl.colspecs[c][1], true) or "")
      end
      table.insert(out, "\\rowcolor{FondoTablaEncabezado}")
      table.insert(out, table.concat(celdas, " & ") .. " \\\\ \\hline")
    end
    for idx, fila in ipairs(filas_body) do
      local celdas = {}
      for c = 1, ncols do
        local cel = fila.cells[c]
        table.insert(celdas, cel and formatear_celda_natural(cel, tbl.colspecs[c][1], false) or "")
      end
      if idx % 2 == 0 then
        table.insert(out, "\\rowcolor{FondoTablaCebra}")
      else
        table.insert(out, "\\rowcolor{white}")
      end
      table.insert(out, table.concat(celdas, " & ") .. " \\\\ \\hline")
    end
    table.insert(out, "\\end{tabular}")
    table.insert(out, "\\end{adjustbox}")
    table.insert(out, "\\endgroup")
    table.insert(out, "\\end{center}")
  else
    -- Tabla estándar o multipágina: anchos proporcionales a \linewidth
    local fracs = calcular_pesos_columnas(tbl)
    local spec = "|"
    for c = 1, ncols do
      local pref = prefijo_alineacion_p(tbl.colspecs[c][1])
      spec = spec .. pref .. string.format("p{\\dimexpr %.4f\\linewidth - 2\\tabcolsep - 2\\arrayrulewidth\\relax}|", fracs[c])
    end

    local env = usar_tabular_ancho and "tabular" or "longtable"
    local tabsep = (ncols >= 5) and "5pt" or "6pt"
    local fsize = (ncols >= 5) and "\\small" or "\\fontsize{9.5pt}{13pt}\\selectfont"

    if usar_tabular_ancho then
      table.insert(out, "\\begin{center}")
    end
    table.insert(out, "\\begingroup")
    table.insert(out, fsize)
    table.insert(out, "\\setlength{\\tabcolsep}{" .. tabsep .. "}")
    table.insert(out, "\\renewcommand{\\arraystretch}{1.35}")
    table.insert(out, "\\arrayrulecolor{Borde}")
    if not usar_tabular_ancho then
      table.insert(out, "\\setlength{\\LTleft}{0pt}")
      table.insert(out, "\\setlength{\\LTright}{0pt}")
      table.insert(out, "\\setlength{\\LTpre}{6pt}")
      table.insert(out, "\\setlength{\\LTpost}{8pt}")
    end
    table.insert(out, "\\begin{" .. env .. "}{" .. spec .. "}")
    table.insert(out, "\\hline")
    for _, fila in ipairs(filas_head) do
      local celdas = {}
      for c = 1, ncols do
        local cel = fila.cells[c]
        table.insert(celdas, cel and formatear_celda_par(cel, true) or "")
      end
      table.insert(out, "\\rowcolor{FondoTablaEncabezado}")
      table.insert(out, table.concat(celdas, " & ") .. " \\\\ \\hline")
    end
    if not usar_tabular_ancho and #filas_head > 0 then
      table.insert(out, "\\endhead")
    end
    for idx, fila in ipairs(filas_body) do
      local celdas = {}
      for c = 1, ncols do
        local cel = fila.cells[c]
        table.insert(celdas, cel and formatear_celda_par(cel, false) or "")
      end
      if idx % 2 == 0 then
        table.insert(out, "\\rowcolor{FondoTablaCebra}")
      else
        table.insert(out, "\\rowcolor{white}")
      end
      table.insert(out, table.concat(celdas, " & ") .. " \\\\ \\hline")
    end
    table.insert(out, "\\end{" .. env .. "}")
    table.insert(out, "\\endgroup")
    if usar_tabular_ancho then
      table.insert(out, "\\end{center}")
    end
  end

  return pandoc.RawBlock("latex", table.concat(out, "\n"))
end

-- Paso 1: transformación de elementos en línea (incluidos los que están dentro de tablas)
local filtro_linea = {
  Link = function(el)
    local tgt = el.target
    if not tgt:match("^https?://") and not tgt:match("^mailto:") and not tgt:match("^#") then
      local nuevo = tgt:gsub("%.md(#.*)$", ".pdf%1"):gsub("%.md$", ".pdf")
      el.target = nuevo
    end
    return el
  end,

  RawInline = function(el)
    if es_salto_br(el) then
      return pandoc.RawInline("latex", "\\NLCELL ")
    end
    if el.format:match("^html") then
      return {}
    end
    return el
  end,

  Code = function(el)
    local txt = el.text
    local largo = utf8.len(txt) or #txt
    local tiene_espacio = txt:find("%s") ~= nil
    if (not tiene_espacio and largo <= 24) or (tiene_espacio and largo <= 20) then
      return pandoc.RawInline("latex", "\\inlinecode{" .. escapar_codigo_latex(txt, false) .. "}")
    end
    return pandoc.RawInline("latex", "\\inlinecodelong{" .. escapar_codigo_latex(txt, true) .. "}")
  end,
}

-- Paso 2: transformación estructural de bloques con seguimiento de anidamiento
local function recortar_espacios_extremos(inlines)
  local ini = 1
  local fin = #inlines
  while ini <= fin and (inlines[ini].t == "Space" or inlines[ini].t == "SoftBreak") do
    ini = ini + 1
  end
  while fin >= ini and (inlines[fin].t == "Space" or inlines[fin].t == "SoftBreak") do
    fin = fin - 1
  end
  local out = {}
  for i = ini, fin do
    table.insert(out, inlines[i])
  end
  return out
end

local function emitir_display_math(texto)
  local tex = "{\\centering\\vspace{2pt}\\par\\noindent\\begin{adjustbox}{max width=\\linewidth}$\\displaystyle "
    .. texto .. "$\\end{adjustbox}\\par\\vspace{2pt}}"
  return pandoc.RawBlock("latex", tex)
end

local function expandir_para_con_display_math(blk)
  local tiene_dm = false
  for _, inl in ipairs(blk.content) do
    if inl.t == "Math" and inl.mathtype == "DisplayMath" then
      tiene_dm = true
      break
    end
  end
  if not tiene_dm then
    return { blk }
  end

  local bloques = {}
  local actual = {}
  local ctor = (blk.t == "Plain") and pandoc.Plain or pandoc.Para
  for _, inl in ipairs(blk.content) do
    if inl.t == "Math" and inl.mathtype == "DisplayMath" then
      local limpio = recortar_espacios_extremos(actual)
      if #limpio > 0 then
        table.insert(bloques, ctor(limpio))
      end
      actual = {}
      table.insert(bloques, emitir_display_math(inl.text))
    else
      table.insert(actual, inl)
    end
  end
  local cola = recortar_espacios_extremos(actual)
  if #cola > 0 then
    table.insert(bloques, ctor(cola))
  end
  return bloques
end

local function transformar_bloques(bloques, en_anidado)
  local resultado = {}
  for _, blk in ipairs(bloques) do
    if blk.t == "Table" then
      table.insert(resultado, renderizar_tabla(blk, en_anidado))
    elseif blk.t == "BlockQuote" then
      local internos = transformar_bloques(blk.content, true)
      local latex = a_latex_crudo(internos)
      table.insert(resultado, pandoc.RawBlock("latex", "\\begin{citabox}\n" .. latex .. "\n\\end{citabox}"))
    elseif blk.t == "CodeBlock" then
      local contenido = blk.text:gsub("%s+$", "")
      local codigo = "\\begin{codeblock}\n\\begin{Verbatim}[fontsize=\\small]\n" .. contenido .. "\n\\end{Verbatim}\n\\end{codeblock}"
      table.insert(resultado, pandoc.RawBlock("latex", codigo))
    elseif blk.t == "HorizontalRule" then
      table.insert(resultado, pandoc.RawBlock("latex", "\\separador"))
    elseif blk.t == "Para" and #blk.content == 1 and blk.content[1].t == "Image" then
      local src = limpiar_ruta_latex(blk.content[1].src)
      local fig = "\\begin{figurabox}\n\\centering\n\\includegraphics[max width=\\linewidth,max height=0.45\\textheight,keepaspectratio]{" .. src .. "}\n\\end{figurabox}"
      table.insert(resultado, pandoc.RawBlock("latex", fig))
    elseif blk.t == "Para" or blk.t == "Plain" then
      for _, b in ipairs(expandir_para_con_display_math(blk)) do
        table.insert(resultado, b)
      end
    elseif blk.t == "BulletList" then
      local items = {}
      for _, item in ipairs(blk.content) do
        table.insert(items, transformar_bloques(item, true))
      end
      blk.content = items
      table.insert(resultado, blk)
    elseif blk.t == "OrderedList" then
      local items = {}
      for _, item in ipairs(blk.content) do
        table.insert(items, transformar_bloques(item, true))
      end
      blk.content = items
      table.insert(resultado, blk)
    elseif blk.t == "Div" then
      blk.content = transformar_bloques(blk.content, en_anidado)
      table.insert(resultado, blk)
    elseif blk.t == "RawBlock" and blk.format:match("^html") then
      -- Omitir bloques HTML crudos residuales
    else
      table.insert(resultado, blk)
    end
  end
  return resultado
end

return {
  filtro_linea,
  {
    Pandoc = function(doc)
      doc.blocks = transformar_bloques(doc.blocks, false)
      return doc
    end,
  },
}
"""


PLANTILLA_LATEX = r"""\documentclass[10pt,letterpaper]{article}

\usepackage[letterpaper, margin=18mm]{geometry}
\usepackage{fontspec}
\usepackage{amsmath,mathtools}
\usepackage{unicode-math}
\usepackage[spanish,es-noshorthands,es-noquoting]{babel}
\usepackage[table]{xcolor}
\usepackage[skins,breakable]{tcolorbox}
\usepackage{fancyvrb}
\usepackage{longtable}
\usepackage{array}
\usepackage{colortbl}
\usepackage[export]{adjustbox}
\usepackage{enumitem}
\usepackage{parskip}
\usepackage{titlesec}
\usepackage{needspace}
\usepackage{tikz}
\usepackage{fancyhdr}
\usepackage{lastpage}
\usepackage{hyperref}

% Definición de la paleta de colores del tema del curso
\definecolor{TextoCuerpo}{HTML}{@@TextoCuerpo@@}
\definecolor{TituloPrincipal}{HTML}{@@TituloPrincipal@@}
\definecolor{TituloSeccion}{HTML}{@@TituloSeccion@@}
\definecolor{TituloSubnivel}{HTML}{@@TituloSubnivel@@}
\definecolor{Acento}{HTML}{@@Acento@@}
\definecolor{Borde}{HTML}{@@Borde@@}
\definecolor{BordeFigura}{HTML}{@@BordeFigura@@}
\definecolor{FondoTablaEncabezado}{HTML}{@@FondoTablaEncabezado@@}
\definecolor{FondoTablaCebra}{HTML}{@@FondoTablaCebra@@}
\definecolor{FondoCita}{HTML}{@@FondoCita@@}
\definecolor{CodigoTexto}{HTML}{@@CodigoTexto@@}
\definecolor{PiePagina}{HTML}{@@PiePagina@@}

% Tipografía portátil con detección de fuentes instaladas
\IfFontExistsTF{Segoe UI}{%
  \setsansfont[Scale=1.02]{Segoe UI}%
}{%
  \IfFontExistsTF{Open Sans}{%
    \setsansfont[Scale=1.02]{Open Sans}%
  }{%
    \IfFontExistsTF{Noto Sans}{%
      \setsansfont[Scale=1.02]{Noto Sans}%
    }{%
      \IfFontExistsTF{Carlito}{%
        \setsansfont[Scale=1.02]{Carlito}%
      }{%
        \setsansfont{Liberation Sans}%
      }%
    }%
  }%
}
\renewcommand{\familydefault}{\sfdefault}

\IfFontExistsTF{DejaVu Sans Mono}{%
  \setmonofont[Scale=0.86]{DejaVu Sans Mono}%
}{%
  \IfFontExistsTF{Consolas}{%
    \setmonofont[Scale=0.88]{Consolas}%
  }{%
    \IfFontExistsTF{Noto Sans Mono}{%
      \setmonofont[Scale=0.86]{Noto Sans Mono}%
    }{%
      \setmonofont[Scale=0.86]{Liberation Mono}%
    }%
  }%
}

\IfFontExistsTF{latinmodern-math.otf}{%
  \setmathfont{latinmodern-math.otf}%
}{}

% Símbolo de barra rectangular para transiciones en Redes de Petri y cuadro QED
\AtBeginDocument{%
  \renewcommand{\talloblong}{%
    \mathord{\tikz[baseline=-0.1ex]\draw[line width=0.55pt](0,0) rectangle (0.32em,0.88em);}%
  }%
  \providecommand{\blacksquare}{%
    \mathord{\rule{0.52em}{0.52em}}%
  }%
  \color{TextoCuerpo}%
}

% Interlineado, párrafos y tolerancia tipográfica
\linespread{1.22}
\setlength{\parindent}{0pt}
\setlength{\parskip}{6pt}
\setlength{\emergencystretch}{2.5em}
\sloppy

% Encabezados sin numeración automática (la numeración ya viene en los títulos Markdown)
\setcounter{secnumdepth}{0}

\titleformat{\section}
  {\normalfont\fontsize{19.5pt}{24pt}\selectfont\bfseries\color{TituloPrincipal}}
  {}{0pt}{}
  [\vspace{4pt}{\color{Acento}\hrule height 2pt}]
\titlespacing*{\section}{0pt}{4pt}{12pt}

\titleformat{\subsection}
  {\normalfont\fontsize{14.5pt}{19pt}\selectfont\bfseries\color{TituloSeccion}}
  {}{0pt}{}
  [\vspace{3pt}{\color{Borde}\hrule height 0.75pt}]
\titlespacing*{\subsection}{0pt}{14pt}{8pt}

\titleformat{\subsubsection}
  {\normalfont\fontsize{12pt}{16pt}\selectfont\bfseries\color{TituloPrincipal}}
  {}{0pt}{}
\titlespacing*{\subsubsection}{0pt}{11pt}{5pt}

\titleformat{\paragraph}[hang]
  {\needspace{3\baselineskip}\normalfont\fontsize{10.8pt}{14.5pt}\selectfont\bfseries\color{TituloSubnivel}}
  {}{0pt}{}
\titlespacing*{\paragraph}{0pt}{8pt}{3pt}

% Listas limpias y compactas
\setlist[itemize,1]{leftmargin=1.6em, itemsep=3pt, topsep=4pt, parsep=2pt}
\setlist[itemize,2]{leftmargin=1.4em, itemsep=2pt, topsep=2pt, parsep=1pt}
\setlist[enumerate,1]{leftmargin=1.8em, itemsep=3pt, topsep=4pt, parsep=2pt}
\setlist[enumerate,2]{leftmargin=1.5em, itemsep=2pt, topsep=2pt, parsep=1pt}
\providecommand{\tightlist}{\setlength{\itemsep}{2pt}\setlength{\parskip}{1pt}}
\providecommand{\passthrough}[1]{#1}
\newcommand{\NLCELL}{\newline }

% Código en línea
\newcommand{\inlinecode}[1]{%
  \tcbox[
    on line,
    boxsep=1pt,
    left=2.5pt,
    right=2.5pt,
    top=0.6pt,
    bottom=0.6pt,
    colback=FondoTablaEncabezado,
    colframe=FondoTablaEncabezado,
    arc=2pt,
    boxrule=0pt
  ]{\ttfamily\small\color{CodigoTexto}#1}%
}

\newcommand{\inlinecodelong}[1]{%
  {\ttfamily\small\color{CodigoTexto}#1}%
}

% Bloque de código con borde y fondo sutil
\newtcolorbox{codeblock}{
  enhanced,
  breakable,
  colback=FondoTablaCebra,
  colframe=Borde,
  coltext=TituloPrincipal,
  boxrule=0.75pt,
  arc=4pt,
  left=10pt,
  right=10pt,
  top=8pt,
  bottom=8pt,
  before skip=8pt,
  after skip=8pt
}

% Citas / callouts con barra lateral azul acento
\newtcolorbox{citabox}{
  enhanced,
  breakable,
  colback=FondoCita,
  colframe=FondoCita,
  coltext=TituloSeccion,
  borderline west={3.5pt}{0pt}{Acento},
  boxrule=0pt,
  arc=3pt,
  sharp corners=west,
  left=12pt,
  right=10pt,
  top=8pt,
  bottom=8pt,
  before skip=8pt,
  after skip=8pt,
  fontupper=\small
}

% Tarjeta contenedora para figuras
\newtcolorbox{figurabox}{
  enhanced,
  colback=white,
  colframe=BordeFigura,
  boxrule=0.75pt,
  arc=4pt,
  left=8pt,
  right=8pt,
  top=8pt,
  bottom=8pt,
  before skip=10pt,
  after skip=10pt
}

% Regla horizontal divisoria
\newcommand{\separador}{%
  \par\vspace{6pt}%
  {\color{Borde}\hrule height 0.75pt}%
  \vspace{6pt}\par%
}

% Estilo de página (vacío por defecto, o pie discreto con --numerar-paginas)
@@ESTILO_PAGINA@@

% Enlaces internos y externos
\hypersetup{
  colorlinks=true,
  linkcolor=Acento,
  urlcolor=Acento,
  filecolor=Acento,
  pdftitle={@@TITULO_PDF@@},
  pdfsubject={Matemáticas Discretas (LISSI0211)},
  pdfcreator={generar_pdfs.py (Pandoc + XeLaTeX)}
}

\begin{document}
@@CUERPO@@
\end{document}
"""


@dataclass
class ResultadoCompilacion:
    """Resultado de compilar o verificar una nota individual."""

    archivo_md: Path
    archivo_pdf: Path
    estado: str  # "generado", "omitido", "error"
    duracion_s: float = 0.0
    detalle: str = ""
    advertencias: tuple[str, ...] = ()


def encontrar_pandoc() -> list[str]:
    """Localiza el ejecutable de Pandoc (nativo o incluido con Quarto)."""
    pandoc = shutil.which("pandoc")
    if pandoc:
        return [pandoc]

    quarto = shutil.which("quarto")
    candidatos: list[Path] = []
    if quarto:
        raiz_quarto = Path(quarto).resolve().parent
        candidatos.extend(sorted(raiz_quarto.glob("tools/*/pandoc")))
        candidatos.extend(sorted(raiz_quarto.glob("tools/*/pandoc.exe")))

    candidatos.extend([
        Path("/opt/quarto/bin/tools/x86_64/pandoc"),
        Path("/opt/quarto/bin/tools/aarch64/pandoc"),
    ])

    for ruta in candidatos:
        if ruta.is_file() and os.access(ruta, os.X_OK):
            return [str(ruta)]

    if quarto:
        return [quarto, "pandoc"]

    raise FileNotFoundError(
        "No se encontró 'pandoc' ni 'quarto' en el PATH. "
        "Instale Pandoc (p. ej. mediante el gestor de paquetes del sistema) o Quarto."
    )


def encontrar_xelatex() -> str:
    """Localiza el ejecutable de XeLaTeX."""
    xelatex = shutil.which("xelatex")
    if xelatex:
        return xelatex
    raise FileNotFoundError(
        "No se encontró 'xelatex' en el PATH. "
        "Instale TeX Live con soporte XeTeX (p. ej. texlive-xetex y texlive-latexextra)."
    )


def limpiar_comentarios_html(texto: str) -> str:
    """Elimina comentarios HTML sin romperse cuando contienen '-->' en su interior.

    Las soluciones de los ejercicios de tarea están en bloques delimitados por
    líneas con ``<!--`` y ``-->`` solos, y varias de ellas usan ``-->`` como
    flecha de texto dentro de la explicación.
    """
    lineas_limpias: list[str] = []
    en_codigo = False
    en_comentario = False

    for linea in texto.splitlines(keepends=True):
        if not en_comentario and RE_CERCA_CODIGO.match(linea):
            en_codigo = not en_codigo
            lineas_limpias.append(linea)
            continue

        if en_codigo:
            lineas_limpias.append(linea)
            continue

        if en_comentario:
            if RE_CIERRE_COMENTARIO.match(linea):
                en_comentario = False
            continue

        if RE_APERTURA_COMENTARIO.match(linea):
            en_comentario = True
            continue

        # Eliminar posibles comentarios HTML de una sola línea
        linea_sin_inline = RE_COMENTARIO_INLINE.sub("", linea)
        if linea_sin_inline.strip() == "" and linea.strip() != "":
            continue

        # Si abre comentario al final/inicio con texto pero sin cierre en la misma línea
        if "<!--" in linea_sin_inline:
            antes, _, _ = linea_sin_inline.partition("<!--")
            if antes.strip():
                lineas_limpias.append(antes.rstrip() + "\n")
            en_comentario = True
            continue

        lineas_limpias.append(linea_sin_inline)

    return "".join(lineas_limpias)


def asegurar_espacio_antes_bloques_codigo(texto: str) -> str:
    """Inserta una línea en blanco antes de cercas ```` ``` ```` pegadas al párrafo previo."""
    lineas = texto.splitlines(keepends=True)
    salida: list[str] = []
    en_codigo = False

    for linea in lineas:
        if RE_CERCA_CODIGO.match(linea):
            if not en_codigo and salida and salida[-1].strip() != "":
                salida.append("\n")
            en_codigo = not en_codigo
        salida.append(linea)

    return "".join(salida)


def extraer_titulo_h1(texto: str, respaldo: str) -> str:
    """Extrae el primer encabezado H1 limpio para los metadatos del PDF."""
    for linea in texto.splitlines():
        m = RE_TITULO_H1.match(linea.strip())
        if m:
            titulo = m.group(1)
            titulo = re.sub(r"\$([^$]+)\$", r"\1", titulo)
            titulo = titulo.replace("`", "").replace("*", "")
            return titulo.strip()
    return respaldo


def escapar_valor_latex(texto: str) -> str:
    """Escapa texto plano para usarlo en metadatos LaTeX (como ``pdftitle``)."""
    reemplazos = {
        "\\": "\\textbackslash{}",
        "{": "\\{",
        "}": "\\}",
        "$": "\\$",
        "&": "\\&",
        "#": "\\#",
        "%": "\\%",
        "_": "\\_",
    }
    return "".join(reemplazos.get(c, c) for c in texto)


def preprocesar_markdown(contenido: str, ruta_md: Path) -> tuple[str, str, list[Path]]:
    """Prepara el Markdown en memoria para Pandoc y recolecta imágenes locales."""
    texto = contenido.replace("\r\n", "\n")
    texto = limpiar_comentarios_html(texto)
    texto = asegurar_espacio_antes_bloques_codigo(texto)
    texto = RE_NOT_MATHREL.sub(r"\\mathrel{\\not \1}", texto)

    imagenes_referenciadas: list[Path] = []
    dir_md = ruta_md.resolve().parent

    def reemplazar_imagen(match: re.Match[str]) -> str:
        alt, destino, titulo = match.group(1), match.group(2), match.group(3)
        if not destino.startswith(("http://", "https://", "/")):
            candidato = (dir_md / destino).resolve()
            if candidato.is_file():
                imagenes_referenciadas.append(candidato)
                destino = candidato.as_posix()
        if titulo is not None:
            return f'![{alt}]({destino} "{titulo}")'
        return f"![{alt}]({destino})"

    texto = RE_IMAGEN_MD.sub(reemplazar_imagen, texto)
    titulo_h1 = extraer_titulo_h1(texto, ruta_md.stem)
    return texto, titulo_h1, imagenes_referenciadas


def extraer_rutas_imagenes(ruta_md: Path) -> list[Path]:
    """Obtiene rutas locales de imágenes referenciadas fuera de comentarios HTML."""
    contenido = ruta_md.read_text(encoding="utf-8").replace("\r\n", "\n")
    contenido = limpiar_comentarios_html(contenido)
    dir_md = ruta_md.resolve().parent
    rutas: list[Path] = []
    for match in RE_IMAGEN_MD.finditer(contenido):
        destino = match.group(2)
        if not destino.startswith(("http://", "https://", "/")):
            candidato = (dir_md / destino).resolve()
            if candidato.is_file():
                rutas.append(candidato)
    return rutas


def necesita_regenerar(ruta_md: Path, ruta_pdf: Path, forzar: bool) -> bool:
    """Determina si el PDF falta o es más antiguo que la nota o sus figuras."""
    if forzar or not ruta_pdf.is_file():
        return True
    mtime_pdf = ruta_pdf.stat().st_mtime
    if ruta_md.stat().st_mtime > mtime_pdf:
        return True
    for img in extraer_rutas_imagenes(ruta_md):
        if img.stat().st_mtime > mtime_pdf:
            return True
    return False


def construir_documento_tex(cuerpo_latex: str, titulo_pdf: str, numerar_paginas: bool) -> str:
    """Inserta colores, estilo de página, título y cuerpo en la plantilla XeLaTeX."""
    if numerar_paginas:
        estilo_pagina = (
            "\\pagestyle{fancy}\n"
            "\\fancyhf{}\n"
            "\\renewcommand{\\headrulewidth}{0pt}\n"
            "\\renewcommand{\\footrulewidth}{0pt}\n"
            "\\fancyfoot[C]{\\small\\color{PiePagina} "
            "Página \\thepage\\ de \\pageref{LastPage}}"
        )
    else:
        estilo_pagina = "\\pagestyle{empty}"

    doc = PLANTILLA_LATEX
    for clave, valor in TEMA_COLOR.items():
        doc = doc.replace(f"@@{clave}@@", valor)
    doc = doc.replace("@@ESTILO_PAGINA@@", estilo_pagina)
    doc = doc.replace("@@TITULO_PDF@@", escapar_valor_latex(titulo_pdf))
    doc = doc.replace("@@CUERPO@@", cuerpo_latex)
    return doc


def resumir_advertencias_tex(log_texto: str) -> tuple[str, ...]:
    """Extrae avisos relevantes de XeLaTeX (caracteres faltantes y desbordamientos graves)."""
    avisos: list[str] = []
    for linea in log_texto.splitlines():
        if "Missing character:" in linea:
            avisos.append(linea.strip())
        elif "Overfull \\hbox" in linea:
            m = re.search(r"\((\d+(?:\.\d+)?)pt too wide\)", linea)
            if m and float(m.group(1)) > 15.0:
                avisos.append(linea.strip())
    return tuple(avisos)


def requiere_segunda_pasada(log_texto: str, numerar_paginas: bool) -> bool:
    """Indica si XeLaTeX requiere recompilar para estabilizar anchos o referencias."""
    if numerar_paginas:
        return True
    indicadores = (
        "Rerun to get",
        "Table widths have changed",
        "Label(s) may have changed",
        "may have changed. Rerun",
    )
    return any(ind in log_texto for ind in indicadores)


def compilar_nota(
    ruta_md: Path,
    ruta_pdf: Path,
    cmd_pandoc: list[str],
    ruta_xelatex: str,
    ruta_filtro_lua: Path,
    numerar_paginas: bool,
    dir_tex: Path | None,
) -> ResultadoCompilacion:
    """Convierte una nota Markdown a PDF usando Pandoc y XeLaTeX."""
    inicio = time.monotonic()
    contenido = ruta_md.read_text(encoding="utf-8")
    md_procesado, titulo_h1, _ = preprocesar_markdown(contenido, ruta_md)

    res_pandoc = subprocess.run(
        [
            *cmd_pandoc,
            "-f",
            FORMATOS_PANDOC_ENTRADA,
            "-t",
            "latex",
            "--lua-filter",
            str(ruta_filtro_lua),
        ],
        input=md_procesado,
        text=True,
        encoding="utf-8",
        capture_output=True,
    )
    if res_pandoc.returncode != 0:
        err = res_pandoc.stderr.strip() or res_pandoc.stdout.strip()
        return ResultadoCompilacion(
            archivo_md=ruta_md,
            archivo_pdf=ruta_pdf,
            estado="error",
            duracion_s=time.monotonic() - inicio,
            detalle=f"Error de Pandoc: {err[:400]}",
        )

    documento_tex = construir_documento_tex(res_pandoc.stdout, titulo_h1, numerar_paginas)

    if dir_tex is not None:
        dir_tex.mkdir(parents=True, exist_ok=True)
        (dir_tex / f"{ruta_md.stem}.tex").write_text(documento_tex, encoding="utf-8")

    with tempfile.TemporaryDirectory(prefix="md_pdf_") as tmp_dir:
        tmp_path = Path(tmp_dir)
        archivo_tex = tmp_path / f"{ruta_md.stem}.tex"
        archivo_tex.write_text(documento_tex, encoding="utf-8")

        cmd_tex = [
            ruta_xelatex,
            "-interaction=nonstopmode",
            "-halt-on-error",
            "-output-directory",
            str(tmp_path),
            str(archivo_tex),
        ]

        res_tex = subprocess.run(cmd_tex, text=True, encoding="utf-8", errors="replace", capture_output=True)
        archivo_log = tmp_path / f"{ruta_md.stem}.log"
        log_texto = archivo_log.read_text(encoding="utf-8", errors="replace") if archivo_log.is_file() else res_tex.stdout

        if res_tex.returncode != 0:
            lineas_error = [
                l for l in log_texto.splitlines()
                if l.startswith("!") or "Emergency stop" in l or "Fatal error" in l
            ]
            resumen = " | ".join(lineas_error[:4]) or res_tex.stdout[-400:]
            return ResultadoCompilacion(
                archivo_md=ruta_md,
                archivo_pdf=ruta_pdf,
                estado="error",
                duracion_s=time.monotonic() - inicio,
                detalle=f"Error de XeLaTeX: {resumen}",
            )

        if requiere_segunda_pasada(log_texto, numerar_paginas):
            res_tex2 = subprocess.run(cmd_tex, text=True, encoding="utf-8", errors="replace", capture_output=True)
            log_texto = archivo_log.read_text(encoding="utf-8", errors="replace") if archivo_log.is_file() else res_tex2.stdout
            if res_tex2.returncode != 0:
                lineas_error = [l for l in log_texto.splitlines() if l.startswith("!")]
                resumen = " | ".join(lineas_error[:4]) or res_tex2.stdout[-400:]
                return ResultadoCompilacion(
                    archivo_md=ruta_md,
                    archivo_pdf=ruta_pdf,
                    estado="error",
                    duracion_s=time.monotonic() - inicio,
                    detalle=f"Error de XeLaTeX (2.ª pasada): {resumen}",
                )

        pdf_generado = tmp_path / f"{ruta_md.stem}.pdf"
        if not pdf_generado.is_file() or pdf_generado.stat().st_size == 0:
            return ResultadoCompilacion(
                archivo_md=ruta_md,
                archivo_pdf=ruta_pdf,
                estado="error",
                duracion_s=time.monotonic() - inicio,
                detalle="XeLaTeX finalizó sin producir un archivo PDF válido.",
            )

        ruta_pdf.parent.mkdir(parents=True, exist_ok=True)
        # Copia atómica para no dejar PDFs corruptos si ocurre una interrupción
        fd, tmp_dest = tempfile.mkstemp(prefix=f".{ruta_pdf.stem}.", suffix=".pdf.tmp", dir=str(ruta_pdf.parent))
        os.close(fd)
        try:
            shutil.copy2(pdf_generado, tmp_dest)
            os.replace(tmp_dest, ruta_pdf)
        finally:
            if os.path.exists(tmp_dest):
                os.unlink(tmp_dest)

        advertencias = resumir_advertencias_tex(log_texto)
        return ResultadoCompilacion(
            archivo_md=ruta_md,
            archivo_pdf=ruta_pdf,
            estado="generado",
            duracion_s=time.monotonic() - inicio,
            advertencias=advertencias,
        )


def resolver_notas_seleccionadas(
    dir_entrada: Path,
    objetivos: Iterable[str],
    unidades: list[int] | None,
) -> list[Path]:
    """Resuelve la lista ordenada de archivos ``.md`` a procesar según los filtros CLI."""
    todas = sorted(p for p in dir_entrada.glob("*.md") if p.is_file())
    if not todas:
        raise FileNotFoundError(f"No se encontraron archivos Markdown en '{dir_entrada}'.")

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
                    f"El objetivo '{obj}' coincide con múltiples notas ({nombres}). "
                    "Especifique el nombre completo o use --unidad."
                )
            else:
                raise FileNotFoundError(f"No se encontró ninguna nota que coincida con '{obj}'.")
    else:
        seleccion = todas

    if unidades:
        prefijos = tuple(f"{u}-" for u in unidades)
        seleccion = [p for p in seleccion if p.name.startswith(prefijos)]

    return seleccion


def crear_parser() -> argparse.ArgumentParser:
    """Construye el analizador de argumentos de línea de comandos."""
    raiz = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(
        prog="generar_pdfs.py",
        description=(
            "Genera los archivos PDF de las notas de Matemáticas Discretas "
            "conservando el tema de color institucional del curso."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Ejemplos:\n"
            "  python3 generar_pdfs.py                 # Compila solo notas modificadas\n"
            "  python3 generar_pdfs.py --forzar        # Regenera todas las notas\n"
            "  python3 generar_pdfs.py 1-1 3-2         # Compila notas específicas\n"
            "  python3 generar_pdfs.py --unidad 3      # Compila toda la Unidad 3\n"
        ),
    )
    parser.add_argument(
        "objetivos",
        nargs="*",
        help="Notas específicas a generar (ej. 1-1, 3-2-logica-de-predicados o ruta al .md).",
    )
    parser.add_argument(
        "-f",
        "--forzar",
        "--todos",
        action="store_true",
        dest="forzar",
        help="Regenera los PDF seleccionados aunque estén actualizados.",
    )
    parser.add_argument(
        "-u",
        "--unidad",
        type=int,
        choices=[1, 2, 3, 4, 5, 6],
        action="append",
        help="Filtra las notas por número de unidad (1 a 6). Puede repetirse.",
    )
    parser.add_argument(
        "-e",
        "--entrada",
        type=Path,
        default=raiz / "notas",
        help="Directorio con las notas en Markdown (por defecto: notas/).",
    )
    parser.add_argument(
        "-o",
        "--salida",
        type=Path,
        default=raiz / "notas" / "pdf",
        help="Directorio de salida para los PDF (por defecto: notas/pdf/).",
    )
    parser.add_argument(
        "-j",
        "--trabajos",
        type=int,
        default=min(8, os.cpu_count() or 4),
        help="Número máximo de compilaciones en paralelo.",
    )
    parser.add_argument(
        "--numerar-paginas",
        action="store_true",
        help="Incluye numeración discreta 'Página X de Y' en el pie de página.",
    )
    parser.add_argument(
        "--mantener-tex",
        type=Path,
        default=None,
        help="Directorio opcional donde conservar los archivos .tex intermedios.",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Muestra detalles por cada archivo omitido y advertencias de LaTeX.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    """Punto de entrada principal del generador de PDF."""
    parser = crear_parser()
    args = parser.parse_args(argv)

    dir_entrada = args.entrada.resolve()
    dir_salida = args.salida.resolve()
    dir_tex = args.mantener_tex.resolve() if args.mantener_tex else None

    if not dir_entrada.is_dir():
        print(f"Error: el directorio de entrada '{dir_entrada}' no existe.", file=sys.stderr)
        return 1

    try:
        notas = resolver_notas_seleccionadas(dir_entrada, args.objetivos, args.unidad)
    except (FileNotFoundError, ValueError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    if not notas:
        print("No se encontraron notas que coincidan con los filtros indicados.")
        return 0

    # Si se indicaron objetivos explícitos en la CLI, siempre se compilan
    forzar_compilacion = args.forzar or bool(args.objetivos)
    por_compilar: list[tuple[Path, Path]] = []
    omitidos: list[Path] = []

    for nota_md in notas:
        destino_pdf = dir_salida / f"{nota_md.stem}.pdf"
        if necesita_regenerar(nota_md, destino_pdf, forzar_compilacion):
            por_compilar.append((nota_md, destino_pdf))
        else:
            omitidos.append(nota_md)

    if args.verbose:
        for nota_md in omitidos:
            print(f"[OMITIDO]  {nota_md.name} (PDF actualizado)")

    if not por_compilar:
        print(
            f"Todos los PDF ({len(omitidos)}/{len(notas)}) están actualizados en '{dir_salida}'. "
            "Use --forzar para regenerarlos."
        )
        return 0

    try:
        cmd_pandoc = encontrar_pandoc()
        ruta_xelatex = encontrar_xelatex()
    except FileNotFoundError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    print(f"Generando {len(por_compilar)} PDF en '{dir_salida}'...")
    t_inicio = time.monotonic()
    resultados: list[ResultadoCompilacion] = []

    with tempfile.NamedTemporaryFile(
        mode="w",
        encoding="utf-8",
        prefix="filtro_notas_",
        suffix=".lua",
        delete=False,
    ) as archivo_lua:
        archivo_lua.write(FILTRO_LUA)
        ruta_filtro_lua = Path(archivo_lua.name)

    try:
        trabajos = max(1, min(args.trabajos, len(por_compilar)))
        with ThreadPoolExecutor(max_workers=trabajos) as ejecutor:
            futuros = {
                ejecutor.submit(
                    compilar_nota,
                    nota_md,
                    destino_pdf,
                    cmd_pandoc,
                    ruta_xelatex,
                    ruta_filtro_lua,
                    args.numerar_paginas,
                    dir_tex,
                ): nota_md
                for nota_md, destino_pdf in por_compilar
            }
            for futuro in as_completed(futuros):
                res = futuro.result()
                resultados.append(res)
                if res.estado == "generado":
                    marca_aviso = f" ({len(res.advertencias)} aviso(s))" if res.advertencias else ""
                    print(f"[OK]       {res.archivo_pdf.name} ({res.duracion_s:.2f}s){marca_aviso}")
                    if args.verbose:
                        for aviso in res.advertencias:
                            print(f"           ! {aviso}")
                else:
                    print(f"[ERROR]    {res.archivo_md.name}: {res.detalle}", file=sys.stderr)
    finally:
        if ruta_filtro_lua.exists():
            ruta_filtro_lua.unlink()

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
