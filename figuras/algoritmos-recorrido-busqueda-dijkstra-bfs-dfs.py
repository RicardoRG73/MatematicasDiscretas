import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches


def draw_panel(ax, x, y, w, h, title, bg_color, border_color, title_color):
    rect = patches.FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0.05",
        facecolor=bg_color,
        edgecolor=border_color,
        linewidth=1.7
    )
    ax.add_patch(rect)
    ax.text(
        x + w / 2, y + h - 0.24, title,
        ha='center', va='center',
        fontsize=9.8, fontweight='bold', color=title_color
    )
    ax.plot([x + 0.12, x + w - 0.12], [y + h - 0.44, y + h - 0.44], color=border_color, linewidth=1.0, alpha=0.6)


def draw_node(ax, x, y, lbl, dist_lbl=None, bg='#dbeafe', border='#1d4ed8', tcol='#1e3a8a', r=0.20):
    ax.add_patch(patches.Circle((x, y), r, facecolor=bg, edgecolor=border, linewidth=1.8, zorder=5))
    ax.text(x, y, lbl, ha='center', va='center', fontsize=9.0, fontweight='bold', color=tcol, zorder=6)
    if dist_lbl is not None:
        ax.text(x, y + r + 0.14, dist_lbl, ha='center', va='center', fontsize=7.8, fontweight='bold', color='#dc2626', zorder=7)


def main():
    fig, ax = plt.subplots(figsize=(13.6, 8.2), dpi=180)
    ax.set_xlim(0, 13.6)
    ax.set_ylim(0, 8.2)
    ax.axis('off')

    # Main Title
    ax.text(
        6.8, 7.88,
        "Algoritmos de Recorrido y Búsqueda en Grafos: Camino Más Corto (Dijkstra), BFS y DFS",
        ha='center', va='center', fontsize=13.5, fontweight='bold', color='#0f172a'
    )
    ax.text(
        6.8, 7.52,
        r"Optimización de rutas en grafos ponderados ($O(|V|^2)$) y obtención de Árboles Generadores mediante Búsqueda a lo Ancho (Cola FIFO) y en Profundidad (Pila LIFO)",
        ha='center', va='center', fontsize=9.4, color='#334155'
    )

    # Top Panel: Algoritmo de Dijkstra (Ejemplo 7.23 de Jiménez Murillo, pp. 330-332)
    draw_panel(ax, 0.25, 4.05, 13.1, 3.2, "1. El Camino Más Corto: Algoritmo de Dijkstra y Matriz de Iteraciones (Ejemplo 7.23 de Jiménez Murillo)", '#eff6ff', '#2563eb', '#1d4ed8')

    # Left inside Top Panel: Weighted Graph of Ejemplo 7.23
    pts = {
        "a": (0.85, 5.45),
        "b": (2.05, 6.28),
        "c": (2.05, 4.62),
        "d": (3.45, 6.28),
        "e": (3.45, 4.62),
        "f": (4.75, 6.28),
        "g": (5.55, 5.45),
    }
    w_edges = [
        ("a", "b", "2", True), ("a", "c", "1", True),
        ("b", "c", "3", False), ("b", "d", "2", True), ("b", "e", "1", True),
        ("c", "d", "4", False), ("c", "e", "4", False),
        ("d", "e", "2", False), ("d", "f", "1", True), ("d", "g", "4", False),
        ("e", "f", "3", False), ("f", "g", "1", True),
    ]
    for u, v, w_str, is_short in w_edges:
        x1, y1 = pts[u]
        x2, y2 = pts[v]
        col = '#dc2626' if is_short else '#64748b'
        lw = 2.4 if is_short else 1.4
        ax.plot([x1, x2], [y1, y2], color=col, linewidth=lw, zorder=2)
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        offset_y = 0.13 if y1 == y2 else 0.0
        offset_x = -0.14 if x1 == x2 else 0.0
        ax.text(mx + offset_x, my + offset_y, w_str, ha='center', va='center', fontsize=8.0, fontweight='bold',
                color='#b91c1c' if is_short else '#334155',
                bbox=dict(boxstyle="round,pad=0.12", facecolor='white', edgecolor='none', alpha=0.85))

    dists_final = {"a": "d=0", "b": "d=2", "c": "d=1", "d": "d=4", "e": "d=3", "f": "d=5", "g": "d=6"}
    for k, (px, py) in pts.items():
        draw_node(ax, px, py, k, dists_final[k], bg='#fef3c7' if k in ("a", "g") else '#dbeafe',
                  border='#d97706' if k in ("a", "g") else '#1d4ed8', r=0.19)

    ax.text(3.2, 4.22, r"En rojo: Árbol de rutas más cortas desde el origen $a$ ($a \to b \to d \to f \to g$, distancia mínima $= 6$)",
            ha='center', va='center', fontsize=8.0, fontweight='bold', color='#b91c1c')

    # Right inside Top Panel: Iteration Table of Ejemplo 7.23
    tx0, ty0 = 6.25, 4.32
    t_headers = ["Iter.", "a", "b", "c", "d", "e", "f", "g", "Actual", "Seleccionados"]
    col_w = [0.52, 0.48, 0.48, 0.48, 0.48, 0.48, 0.48, 0.48, 0.68, 2.25]
    cur_x = tx0
    col_centers = []
    for cw in col_w:
        col_centers.append(cur_x + cw / 2)
        cur_x += cw

    for cx, ht in zip(col_centers, t_headers):
        ax.text(cx, 6.52, ht, ha='center', va='center', fontsize=7.9, fontweight='bold', color='#1e3a8a')
    ax.plot([tx0, cur_x], [6.36, 6.36], color='#2563eb', lw=1.1)

    d_rows = [
        ["0", "0*", r"$\infty$", r"$\infty$", r"$\infty$", r"$\infty$", r"$\infty$", r"$\infty$", "a", "a"],
        ["1", "0", "2", "1*", r"$\infty$", r"$\infty$", r"$\infty$", r"$\infty$", "c", "a, c"],
        ["2", "0", "2*", "1", "5", "5", r"$\infty$", r"$\infty$", "b", "a, c, b"],
        ["3", "0", "2", "1", "4", "3*", r"$\infty$", r"$\infty$", "e", "a, c, b, e"],
        ["4", "0", "2", "1", "4*", "3", "6", r"$\infty$", "d", "a, c, b, e, d"],
        ["5", "0", "2", "1", "4", "3", "5*", "8", "f", "a, c, b, e, d, f"],
        ["6", "0", "2", "1", "4", "3", "5", "6*", "g", "a, c, b, e, d, f, g"],
    ]
    for r_i, r_vals in enumerate(d_rows):
        ry = 6.14 - r_i * 0.285
        if r_i % 2 == 1:
            ax.add_patch(patches.Rectangle((tx0, ry - 0.13), sum(col_w), 0.26, facecolor='#dbeafe', alpha=0.45, edgecolor='none'))
        for c_i, val in enumerate(r_vals):
            is_star = val.endswith("*")
            ax.text(col_centers[c_i], ry, val, ha='center', va='center', fontsize=7.75,
                    fontweight='bold' if (is_star or c_i >= 8) else 'normal',
                    color='#dc2626' if is_star else '#0f172a')

    # Bottom-Left Panel: Búsqueda a lo Ancho (BFS) - Secc. 8.6.1 y 8.6.3 Jiménez Murillo
    draw_panel(ax, 0.25, 0.3, 6.45, 3.5, "2. Búsqueda a lo Ancho (BFS — Breadth-First Search)", '#ecfdf5', '#059669', '#047857')
    bfs_lines = [
        r"$\bullet$ Principio: Explora el grafo o árbol por NIVELES concéntricos ($L_0, L_1, L_2, \dots$).",
        r"  Primero visita la raíz $v_0$, luego todos sus vecinos a distancia $1$, luego los",
        r"  vecinos de éstos a distancia $2$ (de izquierda a derecha o en orden alfabético).",
        r"$\bullet$ Estructura de datos auxiliar: COLA (Queue — política FIFO: First-In, First-Out).",
        r"$\bullet$ Propiedades fundamentales del Árbol Generador BFS:",
        r"  1) Conecta los $|V|$ vértices con exactamente $|V| - 1$ aristas sin formar ciclos.",
        r"  2) En grafos NO ponderados, garantiza encontrar el camino con MENOR",
        r"     número de aristas desde el nodo origen hasta cualquier otro nodo.",
        r"$\bullet$ Ejemplo 8.5 (prioridad alfabética desde $a$):  Nivel 0: $\{a\}$ $\to$ Nivel 1: $\{b, d, g\}$",
        r"  $\to$ Nivel 2 (desde $b$): $\{c, e, f\}$ $\to$ Nivel 3 (desde $c, f$): $\{h, i\}$."
    ]
    for idx, bl in enumerate(bfs_lines):
        ry = 3.10 - idx * 0.275
        w_f = 'bold' if idx in (0, 3, 6, 8) else 'normal'
        ax.text(0.42, ry, bl, ha='left', va='center', fontsize=7.95, fontweight=w_f, color='#1e293b')

    # Bottom-Right Panel: Búsqueda en Profundidad (DFS) - Secc. 8.6.2 y 8.6.3 Jiménez Murillo
    draw_panel(ax, 6.95, 0.3, 6.4, 3.5, "3. Búsqueda en Profundidad (DFS — Depth-First Search)", '#fffbeb', '#d97706', '#b45309')
    dfs_lines = [
        r"$\bullet$ Principio: Avanza desde la raíz profundizando por una sola rama (eligiendo el",
        r"  vecino no visitado de menor orden alfabético/numérico) hasta llegar a un nodo",
        r"  sin salida (donde cualquier arista formaría ciclo).",
        r"$\bullet$ Retroceso (Backtracking): Al bloquearse, retrocede al vértice inmediato anterior",
        r"  que aún tenga vecinos sin visitar y abre una nueva rama hasta cubrir todo $V$.",
        r"$\bullet$ Estructura de datos auxiliar: PILA (Stack — política LIFO) o Recursión.",
        r"$\bullet$ Aplicaciones clave en Ciencias de la Computación:",
        r"  Detección de ciclos, componentes conexas, ordenamiento topológico y laberintos.",
        r"$\bullet$ Ejemplo 8.5 (camino en profundidad desde $a$): $a \to b \to c \to e \to d$ (tope)",
        r"  $\to$ retrocede a $e \to f \to g \to h$ (tope) $\to$ retrocede a $f \to i$."
    ]
    for idx, dl in enumerate(dfs_lines):
        ry = 3.10 - idx * 0.275
        w_f = 'bold' if idx in (0, 3, 5, 8) else 'normal'
        ax.text(7.12, ry, dl, ha='left', va='center', fontsize=7.95, fontweight=w_f, color='#1e293b')

    plt.tight_layout()
    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "algoritmos-recorrido-busqueda-dijkstra-bfs-dfs.png")
    plt.savefig(out_path, dpi=180, bbox_inches='tight', facecolor='white')
    plt.close()


if __name__ == "__main__":
    main()
