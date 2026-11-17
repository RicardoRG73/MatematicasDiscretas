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


def main():
    fig, ax = plt.subplots(figsize=(13.6, 8.2), dpi=180)
    ax.set_xlim(0, 13.6)
    ax.set_ylim(0, 8.2)
    ax.axis('off')

    # Main Title
    ax.text(
        6.8, 7.88,
        r"Representación Matemática y Computacional de los Grafos ($M_a,\; M_i$ y Listas de Adyacencia)",
        ha='center', va='center', fontsize=13.5, fontweight='bold', color='#0f172a'
    )
    ax.text(
        6.8, 7.52,
        r"Comparación estructural entre Matriz de Adyacencia ($|V|\times|V|$), Matriz de Incidencia ($|V|\times|L|$) y Estructuras Enlazadas en Memoria",
        ha='center', va='center', fontsize=9.5, color='#334155'
    )

    # Panel 1: Matriz de Adyacencia (Top-Left) - Ejemplo 7.7 Jiménez Murillo
    draw_panel(ax, 0.25, 4.15, 6.45, 3.1, r"1. Matriz de Adyacencia ($M_a$) — Representación Vértice a Vértice", '#eff6ff', '#2563eb', '#1d4ed8')
    # Draw 5x5 matrix from Ejemplo 7.7
    v_lbls = ["a", "b", "c", "d", "e"]
    ma = [
        [1, 1, 1, 0, 1],
        [1, 0, 1, 1, 0],
        [1, 1, 1, 1, 0],
        [0, 1, 1, 0, 1],
        [1, 0, 0, 1, 0],
    ]
    mx0, my0 = 0.85, 4.48
    cw, ch = 0.48, 0.36
    ax.text(mx0 - 0.42, my0 + 2.5 * ch, r"$M_a=$", ha='center', va='center', fontsize=9.5, fontweight='bold', color='#1d4ed8')
    for i in range(5):
        ax.text(mx0 + (i + 0.5) * cw, my0 + 5 * ch + 0.14, v_lbls[i], ha='center', va='center', fontsize=8.6, fontweight='bold', color='#1e3a8a')
        ax.text(mx0 - 0.16, my0 + (4.5 - i) * ch, v_lbls[i], ha='center', va='center', fontsize=8.6, fontweight='bold', color='#1e3a8a')
        for j in range(5):
            val = ma[i][j]
            cx = mx0 + j * cw
            cy = my0 + (4 - i) * ch
            bg_c = '#dbeafe' if val == 1 else '#ffffff'
            ax.add_patch(patches.Rectangle((cx, cy), cw, ch, facecolor=bg_c, edgecolor='#94a3b8', linewidth=0.9))
            ax.text(cx + cw / 2, cy + ch / 2, str(val), ha='center', va='center', fontsize=8.4,
                    fontweight='bold' if val == 1 else 'normal', color='#1d4ed8' if val == 1 else '#64748b')

    ma_notes = [
        r"$\bullet$ Matriz cuadrada $|V| \times |V|$.",
        r"$\bullet$ $m_{ij} = 1$ si $(v_i, v_j) \in L$, y $0$ si no.",
        r"$\bullet$ En grafos no dirigidos es simétrica",
        r"  ($M_a = M_a^T$). Los lazos ponen $1$ en",
        r"  la diagonal ($a$ y $c$).",
        r"$\bullet$ Limitación: en su forma binaria no",
        r"  distingue lados paralelos (Cap. 7.4)."
    ]
    for idx, mn in enumerate(ma_notes):
        ax.text(3.42, 6.42 - idx * 0.30, mn, ha='left', va='center', fontsize=7.95, color='#1e293b')

    # Panel 2: Matriz de Incidencia (Top-Right) - Ejemplo 7.8 Jiménez Murillo
    draw_panel(ax, 6.95, 4.15, 6.4, 3.1, r"2. Matriz de Incidencia ($M_i$) — Filas: Vértices, Columnas: Aristas", '#ecfdf5', '#059669', '#047857')
    r_lbls = ["r1", "r2", "r3", "r4", "r5", "r6", "r7", "r8", "Val"]
    mi = [
        [1, 1, 0, 0, 1, 1, 1, 0, 5],
        [1, 1, 1, 0, 0, 0, 0, 0, 3],
        [0, 0, 0, 0, 0, 0, 1, 0, 1],
        [0, 0, 0, 1, 0, 0, 0, 0, 1],
        [0, 0, 0, 1, 1, 1, 0, 1, 4],
    ]
    col_sums = [2, 2, 1, 2, 2, 2, 2, 1, 14]
    ix0, iy0 = 7.45, 4.65
    icw, ich = 0.42, 0.31
    for c_i, rl in enumerate(r_lbls):
        ax.text(ix0 + (c_i + 0.5) * icw, iy0 + 5 * ich + 0.14, rl, ha='center', va='center',
                fontsize=7.8, fontweight='bold', color='#b45309' if c_i == 8 else '#065f46')
    for r_i in range(5):
        ax.text(ix0 - 0.16, iy0 + (4.5 - r_i) * ich, v_lbls[r_i], ha='center', va='center', fontsize=8.4, fontweight='bold', color='#065f46')
        for c_i in range(9):
            val = mi[r_i][c_i]
            cx = ix0 + c_i * icw
            cy = iy0 + (4 - r_i) * ich
            bg_c = '#fef3c7' if c_i == 8 else ('#d1fae5' if val == 1 else '#ffffff')
            ax.add_patch(patches.Rectangle((cx, cy), icw, ich, facecolor=bg_c, edgecolor='#94a3b8', linewidth=0.85))
            ax.text(cx + icw / 2, cy + ich / 2, str(val), ha='center', va='center', fontsize=8.0,
                    fontweight='bold' if (val >= 1 or c_i == 8) else 'normal',
                    color='#b45309' if c_i == 8 else ('#047857' if val == 1 else '#94a3b8'))
    # Bottom sum row
    ax.text(ix0 - 0.25, iy0 - 0.5 * ich, "Suma", ha='center', va='center', fontsize=7.5, fontweight='bold', color='#1d4ed8')
    for c_i, s_val in enumerate(col_sums):
        cx = ix0 + c_i * icw
        cy = iy0 - ich
        ax.add_patch(patches.Rectangle((cx, cy), icw, ich, facecolor='#dbeafe', edgecolor='#94a3b8', linewidth=0.85))
        ax.text(cx + icw / 2, cy + ich / 2, str(s_val), ha='center', va='center', fontsize=7.8, fontweight='bold', color='#1e3a8a')

    mi_notes = [
        r"$\bullet$ Sí registra lados paralelos",
        r"  ($r_1, r_2$ y $r_5, r_6$).",
        r"$\bullet$ Suma de fila $=$ valencia",
        r"  del vértice (con lazo $=1$).",
        r"$\bullet$ Suma de columna $= 2$ en",
        r"  arista normal y $= 1$ en",
        r"  un lazo ($r_3, r_8$)."
    ]
    for idx, mn in enumerate(mi_notes):
        ax.text(11.35, 6.42 - idx * 0.30, mn, ha='left', va='center', fontsize=7.75, color='#1e293b')

    # Panel 3: Representación Computacional (Listas de Adyacencia y Complejidad) - Bottom
    draw_panel(ax, 0.25, 0.3, 13.1, 3.58, "3. Representación Computacional: Listas de Adyacencia vs. Matrices en Memoria", '#fffbeb', '#d97706', '#b45309')

    # Draw Adjacency List visual on left side of Panel 3
    ax.text(3.35, 3.22, "Estructura de Listas de Adyacencia (Arreglo de Cabeceras + Nodos Enlazados)", ha='center', va='center', fontsize=8.8, fontweight='bold', color='#92400e')
    adj_data = [
        ("a", ["b", "c", "e"]),
        ("b", ["a", "c", "d"]),
        ("c", ["a", "b", "d"]),
        ("d", ["b", "c", "e"]),
        ("e", ["a", "d"]),
    ]
    for r_i, (head_v, nbrs) in enumerate(adj_data):
        ry = 2.75 - r_i * 0.46
        # Header cell
        ax.add_patch(patches.Rectangle((0.6, ry - 0.16), 0.55, 0.32, facecolor='#fef3c7', edgecolor='#b45309', lw=1.4))
        ax.text(0.87, ry, head_v, ha='center', va='center', fontsize=8.8, fontweight='bold', color='#78350f')
        prev_x = 1.15
        for n_idx, nb in enumerate(nbrs):
            nx = 1.65 + n_idx * 1.15
            ax.annotate("", xy=(nx, ry), xytext=(prev_x, ry), arrowprops=dict(arrowstyle="->", color='#475569', lw=1.4))
            ax.add_patch(patches.Rectangle((nx, ry - 0.15), 0.52, 0.30, facecolor='#ffffff', edgecolor='#2563eb', lw=1.3))
            ax.add_patch(patches.Rectangle((nx + 0.52, ry - 0.15), 0.24, 0.30, facecolor='#dbeafe', edgecolor='#2563eb', lw=1.3))
            ax.text(nx + 0.26, ry, nb, ha='center', va='center', fontsize=8.4, fontweight='bold', color='#1e3a8a')
            nxt_sym = "*" if n_idx == len(nbrs) - 1 else ""
            ax.text(nx + 0.64, ry, nxt_sym, ha='center', va='center', fontsize=8.5, fontweight='bold', color='#dc2626')
            prev_x = nx + 0.76

    # Comparison table on right side of Panel 3
    t_box = patches.FancyBboxPatch((6.45, 0.52), 6.65, 2.82, boxstyle="round,pad=0.04", facecolor='#ffffff', edgecolor='#cbd5e1', lw=1.3)
    ax.add_patch(t_box)
    ax.text(9.77, 3.12, "Comparación de Eficiencia Computacional ($|V|$ vértices, $|L|$ aristas)", ha='center', va='center', fontsize=8.8, fontweight='bold', color='#0f172a')
    ax.plot([6.6, 12.95], [2.92, 2.92], color='#94a3b8', lw=1.0)

    comp_rows = [
        ("Criterio / Operación", "Matriz Adyacencia", "Matriz Incidencia", "Lista Adyacencia"),
        ("Espacio en memoria", r"$O(|V|^2)$", r"$O(|V| \cdot |L|)$", r"$O(|V| + |L|)$"),
        (r"Verificar si $(u,v) \in L$", r"$O(1)$ directo", r"$O(|L|)$", r"$O(\delta(u))$"),
        ("Recorrer vecinos de $u$", r"$O(|V|)$", r"$O(|L|)$", r"$O(\delta(u))$ óptimo"),
        ("Tipo de grafo ideal", "Grafos densos", "Multigrafos / Redes", "Grafos dispersos"),
        ("Detección de Isomorfismo", r"$G_1 \cong G_2 \Longleftrightarrow$ igual $|V|, |L|$, secuencia de grados y ciclos.", "", "")
    ]
    cx_cols = [7.65, 9.45, 10.95, 12.3]
    for r_i, row in enumerate(comp_rows):
        ry = 2.70 - r_i * 0.39
        if r_i == 5:
            ax.text(9.77, ry - 0.05, row[1], ha='center', va='center', fontsize=8.0, fontweight='bold', color='#047857')
        else:
            for c_i, val in enumerate(row):
                w_f = 'bold' if (r_i == 0 or c_i == 0) else 'normal'
                c_f = '#1d4ed8' if r_i == 0 else '#1e293b'
                ax.text(cx_cols[c_i], ry, val, ha='center', va='center', fontsize=7.95, fontweight=w_f, color=c_f)

    plt.tight_layout()
    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "representacion-matematica-y-computacional-grafos.png")
    plt.savefig(out_path, dpi=180, bbox_inches='tight', facecolor='white')
    plt.close()


if __name__ == "__main__":
    main()
