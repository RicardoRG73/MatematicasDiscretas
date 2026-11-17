import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches


def draw_panel(ax, x, y, w, h, title, bg_color, border_color, title_color):
    rect = patches.FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0.06",
        facecolor=bg_color,
        edgecolor=border_color,
        linewidth=1.8
    )
    ax.add_patch(rect)
    ax.text(
        x + w / 2, y + h - 0.25, title,
        ha='center', va='center',
        fontsize=9.8, fontweight='bold', color=title_color
    )
    ax.plot([x + 0.12, x + w - 0.12], [y + h - 0.45, y + h - 0.45], color=border_color, linewidth=1.0, alpha=0.65)


def main():
    fig, ax = plt.subplots(figsize=(13.6, 8.2), dpi=180)
    ax.set_xlim(0, 13.6)
    ax.set_ylim(0, 8.2)
    ax.axis('off')

    # Main Title
    ax.text(
        6.8, 7.88,
        r"Producto Cartesiano ($A \times B$), Relación Binaria ($R \subseteq A \times B$) y sus Cuatro Representaciones",
        ha='center', va='center', fontsize=13.5, fontweight='bold', color='#0f172a'
    )
    ax.text(
        6.8, 7.52,
        r"Toda relación binaria $R: A \to B$ es un subconjunto de pares ordenados $(a, b) \in A \times B$ con Dominio $\mathrm{Dom}(R) \subseteq A$ y Codominio $\mathrm{Cod}(R) \subseteq B$",
        ha='center', va='center', fontsize=9.5, color='#334155'
    )

    # Panel 1: Producto Cartesiano y Conjunto de Pares Ordenados (Top-Left)
    draw_panel(ax, 0.25, 4.25, 6.45, 3.0, "1. Representación por Conjunto de Pares Ordenados y Tabla", '#eff6ff', '#2563eb', '#1d4ed8')
    lines_p1 = [
        r"$\bullet$ Producto Cartesiano ($A \times B$): combinación de todo $a \in A$ con todo $b \in B$:",
        r"   $A \times B = \{(a, b) \mid a \in A \;\wedge\; b \in B\}, \qquad |A \times B| = |A| \cdot |B|$",
        r"$\bullet$ Relación Binaria ($R \subseteq A \times B$): existen $2^{|A|\cdot|B|}$ relaciones posibles de $A$ en $B$.",
        r"$\bullet$ Ejemplo ($A = B = \{1, 2, 3, 4\}$ con $a R b \Longleftrightarrow a \leq b$ y $a \neq 4$):",
        r"   $R = \{(1,1),\; (1,2),\; (1,3),\; (1,4),\; (2,2),\; (2,3),\; (2,4),\; (3,3),\; (3,4)\}$",
        r"   $\mathrm{Dom}(R) = \{1, 2, 3\} \subset A \qquad\text{y}\qquad \mathrm{Cod}(R) = \{1, 2, 3, 4\} = B$"
    ]
    for idx, line in enumerate(lines_p1):
        ry = 6.52 - idx * 0.36
        w_f = 'bold' if idx in (4, 5) else 'normal'
        c_f = '#1e3a8a' if idx in (4, 5) else '#1e293b'
        ax.text(0.45, ry, line, ha='left', va='center', fontsize=8.45, fontweight=w_f, color=c_f)

    # Panel 2: Diagrama de Flechas Sagital (Top-Right)
    draw_panel(ax, 6.95, 4.25, 6.4, 3.0, r"2. Diagrama de Flechas (Sagital) de $R: A \to B$", '#ecfdf5', '#059669', '#047857')
    # Draw two ellipses for A and B
    el_a = patches.Ellipse((8.65, 5.52), 1.35, 2.0, facecolor='#ffffff', edgecolor='#059669', linewidth=1.8)
    el_b = patches.Ellipse((11.55, 5.52), 1.35, 2.0, facecolor='#ffffff', edgecolor='#059669', linewidth=1.8)
    ax.add_patch(el_a)
    ax.add_patch(el_b)
    ax.text(8.65, 6.62, r"Conjunto $A$", ha='center', va='center', fontsize=8.8, fontweight='bold', color='#065f46')
    ax.text(11.55, 6.62, r"Conjunto $B$", ha='center', va='center', fontsize=8.8, fontweight='bold', color='#065f46')

    a_nodes = [("1", 6.12), ("2", 5.52), ("3", 4.92)]
    b_nodes = [("x", 5.88), ("y", 5.16)]
    for lbl, ny in a_nodes:
        ax.scatter([8.65], [ny], color='#047857', s=32, zorder=4)
        ax.text(8.38, ny, lbl, ha='right', va='center', fontsize=9.2, fontweight='bold', color='#0f172a')
    for lbl, ny in b_nodes:
        ax.scatter([11.55], [ny], color='#1d4ed8', s=32, zorder=4)
        ax.text(11.82, ny, lbl, ha='left', va='center', fontsize=9.2, fontweight='bold', color='#0f172a')

    # Arrows for R = {(1,x), (1,y), (2,y), (3,x)} (Ejemplo 6.5 Jiménez Murillo)
    arrows = [(6.12, 5.88), (6.12, 5.16), (5.52, 5.16), (4.92, 5.88)]
    for y_start, y_end in arrows:
        ax.annotate(
            "", xy=(11.45, y_end), xytext=(8.75, y_start),
            arrowprops=dict(arrowstyle="->", color='#0f766e', lw=1.6, shrinkA=2, shrinkB=2)
        )
    ax.text(10.15, 4.42, r"Ejemplo 6.5: $R = \{(1,x),\; (1,y),\; (2,y),\; (3,x)\}$", ha='center', va='center', fontsize=8.4, fontweight='bold', color='#065f46')

    # Panel 3: Representación Matricial Booleana (Bottom-Left) - Ejemplo 6.6 Jiménez Murillo
    draw_panel(ax, 0.25, 0.3, 6.45, 3.68, r"3. Matriz Booleana de una Relación ($M_R = [m_{ij}]$)", '#f8fafc', '#475569', '#0f172a')
    ax.text(
        3.47, 3.28,
        r"Regla: $m_{ij} = 1\;\text{si }(a_i, b_j) \in R;\quad m_{ij} = 0\;\text{si }(a_i, b_j) \notin R$   (Ejemplo 6.6 en $A=\{1,2,3,4,5\}$)",
        ha='center', va='center', fontsize=8.3, color='#334155'
    )

    # Draw 5x5 matrix from Ejemplo 6.6: R = {(1,1),(1,3),(1,4),(2,1),(2,4),(2,5),(3,3),(3,4),(3,5),(4,2),(4,4),(5,1),(5,3),(5,5)}
    mat = [
        [1, 0, 1, 1, 0],
        [1, 0, 0, 1, 1],
        [0, 0, 1, 1, 1],
        [0, 1, 0, 1, 0],
        [1, 0, 1, 0, 1],
    ]
    mx0, my0 = 1.65, 0.65
    cw, ch = 0.62, 0.42
    ax.text(mx0 - 0.65, my0 + 2.5 * ch, r"$M_R =$", ha='center', va='center', fontsize=10.5, fontweight='bold', color='#0f172a')
    for i in range(5):
        ax.text(mx0 + (i + 0.5) * cw, my0 + 5 * ch + 0.16, str(i + 1), ha='center', va='center', fontsize=8.8, fontweight='bold', color='#1d4ed8')
        ax.text(mx0 - 0.2, my0 + (4.5 - i) * ch, str(i + 1), ha='center', va='center', fontsize=8.8, fontweight='bold', color='#1d4ed8')
        for j in range(5):
            val = mat[i][j]
            cx = mx0 + j * cw
            cy = my0 + (4 - i) * ch
            bg_c = '#dbeafe' if (i == j and val == 1) else ('#f1f5f9' if val == 1 else '#ffffff')
            ax.add_patch(patches.Rectangle((cx, cy), cw, ch, facecolor=bg_c, edgecolor='#cbd5e1', linewidth=1.0))
            ax.text(cx + cw / 2, cy + ch / 2, str(val), ha='center', va='center',
                    fontsize=9.0, fontweight='bold' if val == 1 else 'normal',
                    color='#1d4ed8' if val == 1 else '#94a3b8')

    # Matrix notes on right side of Panel 3
    m_notes = [
        r"$\bullet$ Dimensión: $|A| \times |B|$.",
        r"$\bullet$ Si $A = B$, $M_R$ es cuadrada.",
        r"$\bullet$ Los $1\mathrm{s}$ en la diagonal",
        r"   principal $(i, i)$ indican",
        r"   lazos $(i, i) \in R$.",
        r"$\bullet$ Ideal para algoritmos y",
        r"   operaciones booleanas."
    ]
    for idx, mn in enumerate(m_notes):
        ax.text(4.92, 2.75 - idx * 0.31, mn, ha='left', va='center', fontsize=8.0, color='#1e293b')

    # Panel 4: Grafo Dirigido (Dígrafo) de la Relación (Bottom-Right) - Ejemplo 6.6
    draw_panel(ax, 6.95, 0.3, 6.4, 3.68, r"4. Grafo Dirigido (Dígrafo) de $R \subseteq A \times A$ (Ejemplo 6.6)", '#fffbeb', '#d97706', '#b45309')

    # Place 5 nodes in a pentagon around center (9.45, 1.95)
    center_x, center_y = 9.35, 1.92
    radius = 1.08
    angles = [np.pi / 2 - k * 2 * np.pi / 5 for k in range(5)]
    coords = [(center_x + radius * np.cos(a), center_y + radius * np.sin(a)) for a in angles]

    # Draw directed edges for mat[i][j] == 1
    for i in range(5):
        for j in range(5):
            if mat[i][j] == 1:
                x1, y1 = coords[i]
                x2, y2 = coords[j]
                if i == j:
                    # Self-loop outward
                    ux = (x1 - center_x) / radius
                    uy = (y1 - center_y) / radius
                    lx = x1 + 0.28 * ux
                    ly = y1 + 0.28 * uy
                    loop = patches.Circle((lx, ly), 0.17, facecolor='none', edgecolor='#d97706', linewidth=1.6, zorder=2)
                    ax.add_patch(loop)
                else:
                    rad_curve = 0.14 if mat[j][i] == 1 else 0.05
                    ax.annotate(
                        "", xy=(x2, y2), xytext=(x1, y1),
                        arrowprops=dict(
                            arrowstyle="->", color='#475569', lw=1.4,
                            shrinkA=12, shrinkB=12,
                            connectionstyle=f"arc3,rad={rad_curve}"
                        ),
                        zorder=3
                    )

    for idx, (nx, ny) in enumerate(coords):
        c_node = patches.Circle((nx, ny), 0.21, facecolor='#fef3c7', edgecolor='#b45309', linewidth=1.8, zorder=5)
        ax.add_patch(c_node)
        ax.text(nx, ny, str(idx + 1), ha='center', va='center', fontsize=9.5, fontweight='bold', color='#78350f', zorder=6)

    g_notes = [
        r"$\bullet$ Nodos: elementos de $A$.",
        r"$\bullet$ Flecha $a \to b$: par $(a, b) \in R$.",
        r"$\bullet$ Lazo en $a$: par $(a, a) \in R$",
        r"   (nodos $1, 3, 4, 5$).",
        r"$\bullet$ Doble flecha $a \leftrightarrow b$:",
        r"   pares simétricos $(1,3),(3,1)$."
    ]
    for idx, gn in enumerate(g_notes):
        ax.text(10.88, 2.85 - idx * 0.34, gn, ha='left', va='center', fontsize=8.0, color='#1e293b')

    plt.tight_layout()
    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "representacion-de-relaciones-binarias.png")
    plt.savefig(out_path, dpi=180, bbox_inches='tight', facecolor='white')
    plt.close()


if __name__ == "__main__":
    main()
