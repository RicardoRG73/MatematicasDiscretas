import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches


def draw_card(ax, x, y, w, h, title, subtitle, lines, mat_rows, bg_color, border_color, title_color):
    rect = patches.FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0.05",
        facecolor=bg_color,
        edgecolor=border_color,
        linewidth=1.7
    )
    ax.add_patch(rect)
    ax.text(x + w / 2, y + h - 0.24, title, ha='center', va='center', fontsize=9.8, fontweight='bold', color=title_color)
    ax.text(x + w / 2, y + h - 0.48, subtitle, ha='center', va='center', fontsize=8.2, fontweight='bold', color='#1e293b')
    ax.plot([x + 0.1, x + w - 0.1], [y + h - 0.63, y + h - 0.63], color=border_color, linewidth=1.0, alpha=0.6)

    for idx, ln in enumerate(lines):
        ax.text(x + 0.14, y + h - 0.86 - idx * 0.28, ln, ha='left', va='center', fontsize=8.0, color='#334155')

    # Draw 3x3 example matrix at bottom right of card
    mx0 = x + w - 1.52
    my0 = y + 0.16
    cw, ch = 0.42, 0.32
    ax.text(mx0 - 0.35, my0 + 1.5 * ch, r"$M_R=$", ha='center', va='center', fontsize=8.4, fontweight='bold', color=title_color)
    for r in range(3):
        for c in range(3):
            val = mat_rows[r][c]
            cx = mx0 + c * cw
            cy = my0 + (2 - r) * ch
            is_diag = (r == c)
            cell_bg = '#dbeafe' if is_diag else '#ffffff'
            ax.add_patch(patches.Rectangle((cx, cy), cw, ch, facecolor=cell_bg, edgecolor='#94a3b8', linewidth=0.9))
            ax.text(cx + cw / 2, cy + ch / 2, str(val), ha='center', va='center',
                    fontsize=8.3, fontweight='bold' if val == '1' else 'normal',
                    color=title_color if val == '1' else '#64748b')


def main():
    fig, ax = plt.subplots(figsize=(13.6, 8.2), dpi=180)
    ax.set_xlim(0, 13.6)
    ax.set_ylim(0, 8.2)
    ax.axis('off')

    # Main Title
    ax.text(
        6.8, 7.88,
        r"Propiedades de las Relaciones Binarias sobre un Conjunto $A$ ($R \subseteq A \times A$)",
        ha='center', va='center', fontsize=13.6, fontweight='bold', color='#0f172a'
    )
    ax.text(
        6.8, 7.52,
        r"Caracterización formal, criterios en la matriz booleana cuadrada $M_R$ y comportamiento en el grafo dirigido (Tabla 6.1)",
        ha='center', va='center', fontsize=9.6, color='#334155'
    )

    # 6 Cards in a 2x3 Grid
    # Row 1: Reflexiva, Irreflexiva, Simétrica
    draw_card(
        ax, 0.25, 4.05, 4.2, 3.15,
        "1. Relación Reflexiva",
        r"$\forall a \in A:\; (a, a) \in R \quad (I \subseteq R)$",
        [
            r"$\bullet$ Todo elemento se relaciona consigo",
            r"   mismo ($a R a$ para todo $a \in A$).",
            r"$\bullet$ Matriz $M_R$: la diagonal principal",
            r"   contiene únicamente unos ($m_{ii} = 1$).",
            r"$\bullet$ Dígrafo: todos los nodos tienen lazo.",
            r"$\bullet$ Basta que falle un $(a,a)$ para no serlo."
        ],
        [["1", "0", "1"], ["0", "1", "0"], ["1", "1", "1"]],
        '#eff6ff', '#2563eb', '#1d4ed8'
    )

    draw_card(
        ax, 4.7, 4.05, 4.2, 3.15,
        "2. Relación Irreflexiva",
        r"$\forall a \in A:\; (a, a) \notin R \quad (R \cap I = \emptyset)$",
        [
            r"$\bullet$ Ningún elemento está relacionado",
            r"   consigo mismo.",
            r"$\bullet$ Matriz $M_R$: la diagonal principal",
            r"   contiene únicamente ceros ($m_{ii} = 0$).",
            r"$\bullet$ Dígrafo: ningún nodo tiene lazo.",
            r"$\bullet$ Si hay $0\mathrm{s}$ y $1\mathrm{s}$ en la diagonal,",
            r"   no es reflexiva ni irreflexiva."
        ],
        [["0", "1", "1"], ["0", "0", "1"], ["1", "0", "0"]],
        '#fff1f2', '#e11d48', '#be123c'
    )

    draw_card(
        ax, 9.15, 4.05, 4.2, 3.15,
        "3. Relación Simétrica",
        r"$(a, b) \in R \Rightarrow (b, a) \in R \quad (R = R^{-1})$",
        [
            r"$\bullet$ Si $a$ se relaciona con $b$, entonces",
            r"   $b$ también se relaciona con $a$.",
            r"$\bullet$ Matriz $M_R$: es igual a su transpuesta",
            r"   ($M_R = M_R^T = M_{R^{-1}}$, $m_{ij} = m_{ji}$).",
            r"$\bullet$ Dígrafo: toda flecha entre nodos",
            r"   distintos es bidireccional ($a \leftrightarrow b$)."
        ],
        [["1", "1", "0"], ["1", "0", "1"], ["0", "1", "1"]],
        '#ecfdf5', '#059669', '#047857'
    )

    # Row 2: Asimétrica, Antisimétrica, Transitiva
    draw_card(
        ax, 0.25, 0.45, 4.2, 3.25,
        "4. Relación Asimétrica",
        r"$(a, b) \in R \Rightarrow (b, a) \notin R$",
        [
            r"$\bullet$ Si $(a,b) \in R$, su inverso $(b,a) \notin R$.",
            r"$\bullet$ Implica que es irreflexiva: la diagonal",
            r"   debe tener sólo ceros ($m_{ii} = 0$).",
            r"$\bullet$ Matriz $M_R$: no hay pares simétricos",
            r"   de unos ($m_{ij} \cdot m_{ji} = 0$) y $m_{ii} = 0$.",
            r"$\bullet$ Dígrafo: sin lazos ni dobles flechas."
        ],
        [["0", "1", "0"], ["0", "0", "1"], ["1", "0", "0"]],
        '#fdf4ff', '#9333ea', '#7e22ce'
    )

    draw_card(
        ax, 4.7, 0.45, 4.2, 3.25,
        "5. Relación Antisimétrica",
        r"$(a, b) \in R \;\wedge\; (b, a) \in R \Rightarrow a = b$",
        [
            r"$\bullet$ Para $a \neq b$, al menos uno de los pares",
            r"   $(a,b)$ o $(b,a)$ NO está en $R$ ($R \cap R^{-1} \subseteq I$).",
            r"$\bullet$ La diagonal NO importa (puede tener",
            r"   ceros o unos indistintamente).",
            r"$\bullet$ Fuera de la diagonal pueden existir",
            r"   pares de $(0,0)$ o $(1,0)$, nunca $(1,1)$."
        ],
        [["1", "1", "0"], ["0", "0", "1"], ["0", "0", "1"]],
        '#fffbeb', '#d97706', '#b45309'
    )

    draw_card(
        ax, 9.15, 0.45, 4.2, 3.25,
        "6. Relación Transitiva",
        r"$(a, b) \in R \;\wedge\; (b, c) \in R \Rightarrow (a, c) \in R$",
        [
            r"$\bullet$ Si hay camino de $a \to b$ y de $b \to c$,",
            r"   debe existir la arista directa $a \to c$.",
            r"$\bullet$ Criterio matricial booleano ($M_R^2 = M_R \odot M_R$):",
            r"   $R\text{ es transitiva} \Longleftrightarrow M_R + M_R^2 = M_R$",
            r"   (es decir, todo $1$ de $M_R^2$ ya está en $M_R$)."
        ],
        [["1", "1", "1"], ["0", "1", "1"], ["0", "0", "1"]],
        '#f8fafc', '#334155', '#0f172a'
    )

    plt.tight_layout()
    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "propiedades-de-las-relaciones-digrafos-matrices.png")
    plt.savefig(out_path, dpi=180, bbox_inches='tight', facecolor='white')
    plt.close()


if __name__ == "__main__":
    main()
