import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches


def draw_kmap_grid(ax, x0, y0, rows, cols, row_labels, col_labels, row_title, col_title, cell_w=0.72, cell_h=0.62):
    w = cols * cell_w
    h = rows * cell_h
    # Grid cells
    for r in range(rows):
        for c in range(cols):
            cx = x0 + c * cell_w
            cy = y0 + (rows - 1 - r) * cell_h
            rect = patches.Rectangle((cx, cy), cell_w, cell_h, facecolor='white', edgecolor='#64748b', linewidth=1.2)
            ax.add_patch(rect)
    # Row labels
    for r, rl in enumerate(row_labels):
        cy = y0 + (rows - 1 - r) * cell_h + cell_h / 2
        ax.text(x0 - 0.14, cy, rl, ha='right', va='center', fontsize=9.0, fontweight='bold', color='#1e293b')
    # Col labels
    for c, cl in enumerate(col_labels):
        cx = x0 + c * cell_w + cell_w / 2
        ax.text(cx, y0 + h + 0.16, cl, ha='center', va='bottom', fontsize=9.0, fontweight='bold', color='#1e293b')
    # Diagonal corner line
    ax.plot([x0 - 0.52, x0], [y0 + h + 0.45, y0 + h], color='#475569', linewidth=1.2)
    ax.text(x0 - 0.44, y0 + h + 0.08, row_title, ha='center', va='center', fontsize=8.8, fontweight='bold', color='#0f172a')
    ax.text(x0 - 0.14, y0 + h + 0.36, col_title, ha='center', va='center', fontsize=8.8, fontweight='bold', color='#0f172a')


def put_kmap_values(ax, x0, y0, rows, cols, values, cell_w=0.72, cell_h=0.62, highlight_val='1'):
    for r in range(rows):
        for c in range(cols):
            val = values[r][c]
            cx = x0 + c * cell_w + cell_w / 2
            cy = y0 + (rows - 1 - r) * cell_h + cell_h / 2
            if val == highlight_val:
                color = '#1d4ed8' if val == '1' else '#b91c1c'
                weight = 'bold'
                size = 10.2
            else:
                color = '#94a3b8'
                weight = 'normal'
                size = 8.8
            ax.text(cx, cy, val, ha='center', va='center', fontsize=size, fontweight=weight, color=color)


def main():
    fig, ax = plt.subplots(figsize=(13.6, 8.2), dpi=180)
    ax.set_xlim(0, 13.6)
    ax.set_ylim(0, 8.2)
    ax.axis('off')

    # Title
    ax.text(
        6.8, 7.88,
        "Optimización mediante Mapas de Karnaugh: Código Reflejado (Gray), Adyacencia y Agrupación",
        ha='center', va='center', fontsize=13.5, fontweight='bold', color='#0f172a'
    )
    ax.text(
        6.8, 7.52,
        r"Regla fundamental: Agrupar celdas adyacentes en potencias de $2$ ($1, 2, 4, 8, \dots = 2^k$ celdas) $\longrightarrow$ elimina $k$ variables que cambian de estado",
        ha='center', va='center', fontsize=9.6, color='#334155'
    )

    # Panel 1: 3-variable K-Map (Top-Left) - Ejemplo 5.5 de Jiménez Murillo
    p1 = patches.FancyBboxPatch((0.25, 4.15), 4.15, 3.05, boxstyle="round,pad=0.06", facecolor='#f8fafc', edgecolor='#2563eb', linewidth=1.7)
    ax.add_patch(p1)
    ax.text(2.32, 6.96, "1. Mapa de 3 Variables (8 celdas, Código Gray)", ha='center', va='center', fontsize=9.8, fontweight='bold', color='#1d4ed8')
    ax.text(2.32, 6.66, r"Secuencia de columnas $YZ$: $00 \rightarrow 01 \rightarrow 11 \rightarrow 10$ (cambia 1 bit)", ha='center', va='center', fontsize=8.1, color='#334155')

    x1, y1 = 1.05, 4.88
    cw1, ch1 = 0.72, 0.62
    draw_kmap_grid(ax, x1, y1, 2, 4, ["0", "1"], ["00", "01", "11", "10"], r"$X$", r"$YZ$", cw1, ch1)
    vals_3v = [
        ["0", "1", "1", "0"],
        ["0", "1", "1", "1"],
    ]
    put_kmap_values(ax, x1, y1, 2, 4, vals_3v, cw1, ch1, '1')

    # Group 1: 4 cells (col 1 & 2, rows 0 & 1) -> Z
    g1 = patches.FancyBboxPatch((x1 + 1 * cw1 + 0.08, y1 + 0.08), 2 * cw1 - 0.16, 2 * ch1 - 0.16,
                                boxstyle="round,pad=0.04", facecolor='#3b82f6', alpha=0.18, edgecolor='#1d4ed8', linewidth=2.0)
    ax.add_patch(g1)
    ax.add_patch(patches.FancyBboxPatch((x1 + 1 * cw1 + 0.08, y1 + 0.08), 2 * cw1 - 0.16, 2 * ch1 - 0.16,
                                        boxstyle="round,pad=0.04", facecolor='none', edgecolor='#1d4ed8', linewidth=1.8))
    # Group 2: 2 cells (row 1, col 2 & 3) -> XY
    ax.add_patch(patches.FancyBboxPatch((x1 + 2 * cw1 + 0.12, y1 + 0.12), 2 * cw1 - 0.24, ch1 - 0.24,
                                        boxstyle="round,pad=0.04", facecolor='none', edgecolor='#059669', linewidth=2.0, linestyle='--'))

    ax.text(2.32, 4.58, r"$\bullet$ Bloque azul ($4=2^2$ celdas): $Z$  (elimina $X, Y$)", ha='center', va='center', fontsize=8.3, fontweight='bold', color='#1d4ed8')
    ax.text(2.32, 4.30, r"$\bullet$ Bloque verde ($2=2^1$ celdas): $XY$ $\;\Rightarrow\; F = Z + XY$", ha='center', va='center', fontsize=8.3, fontweight='bold', color='#047857')

    # Panel 2: 4-variable K-Map with Corner Wraparound (Top-Center/Right) - Ejemplo 5.6 Jiménez Murillo
    p2 = patches.FancyBboxPatch((4.62, 4.15), 4.35, 3.05, boxstyle="round,pad=0.06", facecolor='#f8fafc', edgecolor='#059669', linewidth=1.7)
    ax.add_patch(p2)
    ax.text(6.8, 6.96, "2. Mapa de 4 Variables (16 celdas y Topología Toroidal)", ha='center', va='center', fontsize=9.6, fontweight='bold', color='#047857')

    x2, y2 = 5.45, 4.58
    cw2, ch2 = 0.65, 0.46
    draw_kmap_grid(ax, x2, y2, 4, 4, ["00", "01", "11", "10"], ["00", "01", "11", "10"], r"$WX$", r"$YZ$", cw2, ch2)
    vals_4v = [
        ["1", "1", "1", "1"],
        ["0", "1", "1", "0"],
        ["0", "0", "0", "1"],
        ["1", "0", "0", "1"],
    ]
    put_kmap_values(ax, x2, y2, 4, 4, vals_4v, cw2, ch2, '1')

    # Center 2x2 group (rows 0,1 and cols 1,2) -> W'Z
    ax.add_patch(patches.FancyBboxPatch((x2 + 1 * cw2 + 0.07, y2 + 2 * ch2 + 0.06), 2 * cw2 - 0.14, 2 * ch2 - 0.12,
                                        boxstyle="round,pad=0.03", facecolor='none', edgecolor='#2563eb', linewidth=1.9))
    # Right 2-cell vertical group (rows 2,3 and col 3) -> WY'Z'
    ax.add_patch(patches.FancyBboxPatch((x2 + 3 * cw2 + 0.09, y2 + 0.06), cw2 - 0.18, 2 * ch2 - 0.12,
                                        boxstyle="round,pad=0.03", facecolor='none', edgecolor='#9333ea', linewidth=1.9, linestyle='--'))
    # 4 corners highlight -> X'Z'
    for (cr, cc) in [(0, 0), (0, 3), (3, 0), (3, 3)]:
        cx_c = x2 + cc * cw2 + 0.05
        cy_c = y2 + (3 - cr) * ch2 + 0.04
        ax.add_patch(patches.Rectangle((cx_c, cy_c), cw2 - 0.10, ch2 - 0.08, facecolor='#fef3c7', alpha=0.55, edgecolor='#d97706', linewidth=1.7))

    ax.text(6.8, 4.30, r"Esquinas ($4$ celdas): $X'Z'$  |  Centro ($4$): $W'Z$  |  Der. ($2$): $WY'Z'$", ha='center', va='center', fontsize=8.0, fontweight='bold', color='#0f172a')

    # Panel 3: Rules of K-Map Simplification (Top-Right)
    p3 = patches.FancyBboxPatch((9.18, 4.15), 4.17, 3.05, boxstyle="round,pad=0.06", facecolor='#fffbeb', edgecolor='#d97706', linewidth=1.7)
    ax.add_patch(p3)
    ax.text(11.26, 6.96, "3. Reglas de Simplificación en Mapas K", ha='center', va='center', fontsize=9.8, fontweight='bold', color='#b45309')
    rules = [
        r"$1^\circ$ Tamaño de bloque $= 2^k \in \{1, 2, 4, 8, 16\}$",
        r"    (Prohibido agrupar 3, 5, 6 celdas o diagonales).",
        r"$2^\circ$Envoltura cilíndrica/toroidal: borde izq. $\leftrightarrow$ der.,",
        r"    borde sup. $\leftrightarrow$ inf., y las $4$ esquinas entre sí.",
        r"$3^\circ$ Bloques lo más grandes posible (implicantes",
        r"    primos): bloque de $2^k$ celdas deja $n - k$ literales.",
        r"$4^\circ$ Mínimo número de bloques que cubran todos",
        r"    los $1\mathrm{s}$ (un $1$ puede compartirse en varios bloques)."
    ]
    for idx, rl in enumerate(rules):
        ry = 6.55 - idx * 0.295
        ax.text(9.34, ry, rl, ha='left', va='center', fontsize=8.15, color='#1e293b')

    # Bottom Row: Comparison SOP (grouping 1s) vs POS (grouping 0s) on Ejemplo 5.14 de Jiménez Murillo
    p4 = patches.FancyBboxPatch((0.25, 0.3), 13.1, 3.58, boxstyle="round,pad=0.06", facecolor='#eff6ff', edgecolor='#475569', linewidth=1.8)
    ax.add_patch(p4)
    ax.text(
        6.8, 3.62,
        r"4. Comparación de Optimización en Suma de Productos (SOP, agrupando $1\mathrm{s}$) frente a Producto de Sumas (POS, agrupando $0\mathrm{s}$) — Ejemplo 5.14",
        ha='center', va='center', fontsize=10.0, fontweight='bold', color='#0f172a'
    )

    # Left sub-map: SOP (1s)
    ax.text(2.4, 3.25, r"a) Agrupación de $1\mathrm{s}$ $\longrightarrow$ Suma de Productos (SOP)", ha='center', va='center', fontsize=9.1, fontweight='bold', color='#1d4ed8')
    xsop, ysop = 1.15, 0.72
    draw_kmap_grid(ax, xsop, ysop, 4, 4, ["00", "01", "11", "10"], ["00", "01", "11", "10"], r"$AB$", r"$CD$", 0.65, 0.46)
    vals_sop = [
        ["0", "0", "0", "0"],
        ["0", "0", "1", "1"],
        ["1", "0", "1", "1"],
        ["1", "0", "0", "0"],
    ]
    put_kmap_values(ax, xsop, ysop, 4, 4, vals_sop, 0.65, 0.46, '1')
    # Group BC (rows 1,2 and cols 2,3)
    ax.add_patch(patches.FancyBboxPatch((xsop + 2 * 0.65 + 0.06, ysop + 1 * 0.46 + 0.05), 2 * 0.65 - 0.12, 2 * 0.46 - 0.10,
                                        boxstyle="round,pad=0.03", facecolor='#3b82f6', alpha=0.18, edgecolor='#1d4ed8', linewidth=2.0))
    # Group AC'D' (rows 2,3 and col 0)
    ax.add_patch(patches.FancyBboxPatch((xsop + 0.07, ysop + 0.05), 0.65 - 0.14, 2 * 0.46 - 0.10,
                                        boxstyle="round,pad=0.03", facecolor='#10b981', alpha=0.18, edgecolor='#059669', linewidth=2.0))
    ax.text(2.45, 0.46, r"$F_{\mathrm{SOP}} = AC'D' + BC$", ha='center', va='center', fontsize=9.5, fontweight='bold', color='#1d4ed8')

    # Middle sub-map: POS (0s)
    ax.text(6.95, 3.25, r"b) Agrupación de $0\mathrm{s}$ $\longrightarrow$ $F'$ y Producto de Sumas (POS)", ha='center', va='center', fontsize=9.1, fontweight='bold', color='#b91c1c')
    xpos, ypos = 5.7, 0.72
    draw_kmap_grid(ax, xpos, ypos, 4, 4, ["00", "01", "11", "10"], ["00", "01", "11", "10"], r"$AB$", r"$CD$", 0.65, 0.46)
    put_kmap_values(ax, xpos, ypos, 4, 4, vals_sop, 0.65, 0.46, '0')
    # Group A'C' (rows 0,1 and cols 0,1)
    ax.add_patch(patches.FancyBboxPatch((xpos + 0.06, ypos + 2 * 0.46 + 0.05), 2 * 0.65 - 0.12, 2 * 0.46 - 0.10,
                                        boxstyle="round,pad=0.03", facecolor='#ef4444', alpha=0.15, edgecolor='#dc2626', linewidth=1.9))
    # Group C'D (rows 0..3, col 1)
    ax.add_patch(patches.FancyBboxPatch((xpos + 1 * 0.65 + 0.09, ypos + 0.05), 0.65 - 0.18, 4 * 0.46 - 0.10,
                                        boxstyle="round,pad=0.03", facecolor='none', edgecolor='#9333ea', linewidth=1.9, linestyle='--'))
    # Group B'C (rows 0 and 3, cols 2,3) -> top and bottom wraparound
    ax.add_patch(patches.Rectangle((xpos + 2 * 0.65 + 0.06, ypos + 3 * 0.46 + 0.04), 2 * 0.65 - 0.12, 0.46 - 0.08,
                                   facecolor='#fef3c7', alpha=0.45, edgecolor='#d97706', linewidth=1.7))
    ax.add_patch(patches.Rectangle((xpos + 2 * 0.65 + 0.06, ypos + 0.04), 2 * 0.65 - 0.12, 0.46 - 0.08,
                                   facecolor='#fef3c7', alpha=0.45, edgecolor='#d97706', linewidth=1.7))
    ax.text(7.0, 0.46, r"$F' = A'C' + B'C + C'D \;\Rightarrow\; F_{\mathrm{POS}} = (A+C)(B+C')(C+D')$", ha='center', va='center', fontsize=8.8, fontweight='bold', color='#b91c1c')

    # Right summary box: Procedure POS and Don't Care
    p5 = patches.FancyBboxPatch((9.15, 0.55), 3.98, 2.55, boxstyle="round,pad=0.05", facecolor='#ffffff', edgecolor='#64748b', linewidth=1.4)
    ax.add_patch(p5)
    ax.text(11.14, 2.86, "Pasos para POS y Condiciones 'No Importa' (X)", ha='center', va='center', fontsize=8.8, fontweight='bold', color='#0f172a')
    pos_steps = [
        r"1. Colocar $0\mathrm{s}$ en las celdas vacías del mapa.",
        r"2. Agrupar los $0\mathrm{s}$ en bloques de $2^k$ celdas.",
        r"3. Leer la suma de productos del complemento $F'$.",
        r"4. Aplicar Ley de De Morgan a ambos miembros:",
        r"   $F = (F')' \longrightarrow$ Producto de Sumas (POS).",
        r"5. Condiciones 'No importa' ($d$ o $X$): pueden",
        r"   tomarse como $1$ o $0$ sólo si agrandan un bloque."
    ]
    for idx, st in enumerate(pos_steps):
        ry = 2.52 - idx * 0.285
        ax.text(9.28, ry, st, ha='left', va='center', fontsize=8.05, color='#334155')

    plt.tight_layout()
    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "mapas-karnaugh-adyacencia-y-agrupacion.png")
    plt.savefig(out_path, dpi=180, bbox_inches='tight', facecolor='white')
    plt.close()


if __name__ == "__main__":
    main()
