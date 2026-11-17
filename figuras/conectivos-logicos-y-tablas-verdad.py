import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches


def draw_box(ax, x, y, w, h, title, lines, bg_color, border_color, title_color):
    rect = patches.FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0.06",
        facecolor=bg_color,
        edgecolor=border_color,
        linewidth=1.8
    )
    ax.add_patch(rect)
    ax.text(
        x + w / 2, y + h - 0.26, title,
        ha='center', va='center',
        fontsize=10.2, fontweight='bold', color=title_color
    )
    ax.plot([x + 0.12, x + w - 0.12], [y + h - 0.46, y + h - 0.46], color=border_color, linewidth=1.0, alpha=0.6)
    n = len(lines)
    top_y = y + h - 0.68
    step = (h - 0.82) / max(n, 1)
    for idx, line in enumerate(lines):
        ax.text(
            x + w / 2, top_y - idx * step, line,
            ha='center', va='center',
            fontsize=8.9, color='#1e293b'
        )


def main():
    fig, ax = plt.subplots(figsize=(13.0, 7.6), dpi=180)
    ax.set_xlim(0, 13.0)
    ax.set_ylim(0, 7.6)
    ax.axis('off')

    # Main title
    ax.text(
        6.5, 7.28,
        "Conectivos Lógicos, Tablas de Verdad y Variantes de la Condicional",
        ha='center', va='center', fontsize=14, fontweight='bold', color='#0f172a'
    )
    ax.text(
        6.5, 6.92,
        r"Convención binaria: $1 = \mathrm{Verdadero}\;(V)$,   $0 = \mathrm{Falso}\;(F)$   |   Número de filas para $n$ variables: $2^n$",
        ha='center', va='center', fontsize=10.2, color='#334155'
    )

    # Top row: 3 boxes for Basic Operators + Conditional + Biconditional
    draw_box(
        ax, 0.3, 4.15, 3.9, 2.45,
        r"1. Negación ($p'$ o $\neg p$) y Conjunción ($p \wedge q$)",
        [
            r"Negación: invierte el valor ($1' = 0,\; 0' = 1$)",
            r"Conjunción ($\wedge$, AND): verdadera sólo si $p=1$ y $q=1$",
            r"$0 \wedge 0 = 0,\quad 0 \wedge 1 = 0,\quad 1 \wedge 0 = 0,\quad 1 \wedge 1 = 1$",
            r"Equivale a la multiplicación lógica y a $A \cap B$"
        ],
        '#eff6ff', '#2563eb', '#1d4ed8'
    )

    draw_box(
        ax, 4.55, 4.15, 3.9, 2.45,
        r"2. Disyunción Inclusiva ($\vee$) y Exclusiva ($\oplus$)",
        [
            r"Inclusiva ($\vee$, OR): falsa sólo cuando $p=0$ y $q=0$",
            r"$0 \vee 0 = 0,\quad 0 \vee 1 = 1,\quad 1 \vee 0 = 1,\quad 1 \vee 1 = 1$",
            r"Exclusiva ($\oplus$, XOR): verdadera si $p \neq q$",
            r"$p \oplus q \equiv (p \wedge q') \vee (p' \wedge q) \equiv (p \leftrightarrow q)'$"
        ],
        '#ecfdf5', '#059669', '#047857'
    )

    draw_box(
        ax, 8.8, 4.15, 3.9, 2.45,
        r"3. Condicional ($\rightarrow$) y Bicondicional ($\leftrightarrow$)",
        [
            r"Condicional ($p \rightarrow q$): falsa sólo si $p=1$ y $q=0$",
            r"$0 \rightarrow 0 = 1,\quad 0 \rightarrow 1 = 1,\quad 1 \rightarrow 0 = 0,\quad 1 \rightarrow 1 = 1$",
            r"Bicondicional ($p \leftrightarrow q$): verdadera si $p = q$",
            r"$0 \leftrightarrow 0 = 1,\quad 0 \leftrightarrow 1 = 0,\quad 1 \leftrightarrow 0 = 0,\quad 1 \leftrightarrow 1 = 1$"
        ],
        '#fdf4ff', '#9333ea', '#7e22ce'
    )

    # Bottom-left: Master truth table panel
    rect_tbl = patches.FancyBboxPatch(
        (0.3, 0.35), 6.25, 3.45,
        boxstyle="round,pad=0.06",
        facecolor='#f8fafc', edgecolor='#475569', linewidth=1.8
    )
    ax.add_patch(rect_tbl)
    ax.text(
        3.42, 3.55,
        "Tabla de Verdad Maestra de los Conectivos Binarios",
        ha='center', va='center', fontsize=10.5, fontweight='bold', color='#0f172a'
    )

    headers = [r"$p$", r"$q$", r"$p'$", r"$p \wedge q$", r"$p \vee q$", r"$p \oplus q$", r"$p \rightarrow q$", r"$p \leftrightarrow q$"]
    col_x = [0.7, 1.3, 1.95, 2.75, 3.55, 4.35, 5.2, 6.05]
    ax.plot([0.48, 6.4], [3.05, 3.05], color='#64748b', linewidth=1.2)
    for cx, h_text in zip(col_x, headers):
        ax.text(cx, 3.22, h_text, ha='center', va='center', fontsize=9.5, fontweight='bold', color='#1e293b')

    rows = [
        ["0", "0", "1", "0", "0", "0", "1", "1"],
        ["0", "1", "1", "0", "1", "1", "1", "0"],
        ["1", "0", "0", "0", "1", "1", "0", "0"],
        ["1", "1", "0", "1", "1", "0", "1", "1"],
    ]
    row_y = [2.72, 2.25, 1.78, 1.31]
    for r_idx, (ry, r_vals) in enumerate(zip(row_y, rows)):
        if r_idx % 2 == 1:
            band = patches.Rectangle((0.48, ry - 0.2), 5.92, 0.42, facecolor='#e2e8f0', alpha=0.45, edgecolor='none')
            ax.add_patch(band)
        for c_idx, (cx, val) in enumerate(zip(col_x, r_vals)):
            color = '#b91c1c' if (c_idx == 6 and r_idx == 2) else ('#15803d' if val == '1' else '#475569')
            weight = 'bold' if (c_idx >= 3) else 'normal'
            ax.text(cx, ry, val, ha='center', va='center', fontsize=9.5, fontweight=weight, color=color)

    ax.text(
        3.42, 0.68,
        r"Nota clave: $p \rightarrow q$ sólo es falsa ($0$) cuando el antecedente $p=1$ y el consecuente $q=0$.",
        ha='center', va='center', fontsize=8.7, fontweight='bold', color='#b91c1c'
    )

    # Bottom-right top: Operator precedence hierarchy
    draw_box(
        ax, 6.85, 2.15, 5.85, 1.65,
        "Jerarquía de Operación (Precedencia de Conectivos)",
        [
            r"$1^\circ$ Paréntesis y corchetes $(\;),\; [\;]$ (de adentro hacia afuera)",
            r"$2^\circ$ Negación o complemento ($p'$ o $\neg p$)   $\longrightarrow$   $3^\circ$ Conjunción ($\wedge$)",
            r"$4^\circ$ Disyunción ($\vee,\; \oplus$)   $\longrightarrow$   $5^\circ$ Condicional ($\rightarrow$) y Bicondicional ($\leftrightarrow$)"
        ],
        '#fffbeb', '#d97706', '#b45309'
    )

    # Bottom-right bottom: Associated conditionals
    draw_box(
        ax, 6.85, 0.35, 5.85, 1.62,
        r"Proposiciones Asociadas a la Condicional Directa ($p \rightarrow q$)",
        [
            r"Directa: $p \rightarrow q$   $\equiv$   Contrapositiva: $q' \rightarrow p'$  (¡Lógicamente equivalentes!)",
            r"Recíproca: $q \rightarrow p$   $\equiv$   Inversa (Contraria): $p' \rightarrow q'$  (Equivalentes entre sí)",
            r"Bicondicional: $(p \leftrightarrow q) \equiv (p \rightarrow q) \wedge (q \rightarrow p) \equiv (p' \vee q) \wedge (q' \vee p)$"
        ],
        '#fff1f2', '#e11d48', '#be123c'
    )

    plt.tight_layout()
    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "conectivos-logicos-y-tablas-verdad.png")
    plt.savefig(out_path, dpi=180, bbox_inches='tight', facecolor='white')
    plt.close()


if __name__ == "__main__":
    main()
