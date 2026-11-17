import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches


def draw_panel(ax, x, y, w, h, title, subtitle, headers, rows, footer, bg, border, title_col, badge_col):
    rect = patches.FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0.06",
        facecolor=bg, edgecolor=border, linewidth=1.9
    )
    ax.add_patch(rect)

    ax.text(x + w / 2, y + h - 0.28, title, ha='center', va='center', fontsize=10.8, fontweight='bold', color=title_col)
    ax.text(x + w / 2, y + h - 0.62, subtitle, ha='center', va='center', fontsize=8.8, color='#334155')

    # Table header
    n_cols = len(headers)
    col_w = (w - 0.36) / n_cols
    col_x = [x + 0.18 + col_w * (i + 0.5) for i in range(n_cols)]

    header_y = y + h - 1.05
    ax.plot([x + 0.16, x + w - 0.16], [header_y - 0.18, header_y - 0.18], color=border, linewidth=1.2)
    for cx, h_txt in zip(col_x, headers):
        ax.text(cx, header_y, h_txt, ha='center', va='center', fontsize=8.8, fontweight='bold', color='#0f172a')

    # Rows
    start_y = header_y - 0.45
    step_y = 0.44
    for r_i, row in enumerate(rows):
        ry = start_y - r_i * step_y
        if r_i % 2 == 1:
            band = patches.Rectangle((x + 0.16, ry - 0.19), w - 0.32, 0.38, facecolor='#ffffff', alpha=0.55, edgecolor='none')
            ax.add_patch(band)
        for c_i, (cx, val) in enumerate(zip(col_x, row)):
            is_last = (c_i == n_cols - 1)
            col = badge_col if is_last else '#1e293b'
            wt = 'bold' if is_last else 'normal'
            ax.text(cx, ry, val, ha='center', va='center', fontsize=9.2, fontweight=wt, color=col)

    # Footer box
    foot_rect = patches.FancyBboxPatch(
        (x + 0.18, y + 0.18), w - 0.36, 0.72,
        boxstyle="round,pad=0.04",
        facecolor='#ffffff', edgecolor=border, linewidth=1.1
    )
    ax.add_patch(foot_rect)
    ax.text(x + w / 2, y + 0.54, footer[0], ha='center', va='center', fontsize=8.7, fontweight='bold', color=title_col)
    ax.text(x + w / 2, y + 0.31, footer[1], ha='center', va='center', fontsize=8.3, color='#334155')


def main():
    fig, ax = plt.subplots(figsize=(13.2, 7.2), dpi=180)
    ax.set_xlim(0, 13.2)
    ax.set_ylim(0, 7.2)
    ax.axis('off')

    ax.text(
        6.6, 6.88,
        "Clasificación Semántica de Proposiciones Compuestas y Equivalencia Lógica",
        ha='center', va='center', fontsize=13.8, fontweight='bold', color='#0f172a'
    )
    ax.text(
        6.6, 6.53,
        r"Según los valores de la columna final de su tabla de verdad ($2^n$ combinaciones)",
        ha='center', va='center', fontsize=10.2, color='#334155'
    )

    # 1. Tautology
    draw_panel(
        ax, 0.3, 2.2, 4.05, 4.05,
        "1. Tautología (Ley Lógica)",
        r"Ejemplo: $(p \rightarrow q) \leftrightarrow (q' \rightarrow p')$",
        [r"$p$", r"$q$", r"$p \rightarrow q$", r"$q' \rightarrow p'$", "Resultado"],
        [
            ["0", "0", "1", "1", "1 (V)"],
            ["0", "1", "1", "1", "1 (V)"],
            ["1", "0", "0", "0", "1 (V)"],
            ["1", "1", "1", "1", "1 (V)"],
        ],
        [
            "Todos los valores finales son 1 (Verdadero)",
            r"Caso elemental: Tercero excluido $(p \vee p' \equiv 1)$"
        ],
        '#ecfdf5', '#059669', '#047857', '#15803d'
    )

    # 2. Contradiction
    draw_panel(
        ax, 4.58, 2.2, 4.05, 4.05,
        "2. Contradicción (Absurdo)",
        r"Ejemplo: $(p \wedge q) \wedge (p \rightarrow q')$",
        [r"$p$", r"$q$", r"$p \wedge q$", r"$p \rightarrow q'$", "Resultado"],
        [
            ["0", "0", "0", "1", "0 (F)"],
            ["0", "1", "0", "1", "0 (F)"],
            ["1", "0", "0", "1", "0 (F)"],
            ["1", "1", "1", "0", "0 (F)"],
        ],
        [
            "Todos los valores finales son 0 (Falso)",
            r"Caso elemental: No contradicción $(p \wedge p' \equiv 0)$"
        ],
        '#fef2f2', '#dc2626', '#b91c1c', '#dc2626'
    )

    # 3. Contingency
    draw_panel(
        ax, 8.85, 2.2, 4.05, 4.05,
        "3. Contingencia (Consistente)",
        r"Ejemplo: $[(q' \vee p) \rightarrow p'] \wedge q$",
        [r"$p$", r"$q$", r"$q' \vee p$", r"$(q' \vee p)\rightarrow p'$", "Resultado"],
        [
            ["0", "0", "1", "1", "0 (F)"],
            ["0", "1", "0", "1", "1 (V)"],
            ["1", "0", "1", "0", "0 (F)"],
            ["1", "1", "1", "0", "0 (F)"],
        ],
        [
            "Combina al menos un 1 y al menos un 0",
            "Su verdad depende de los valores de entrada"
        ],
        '#eff6ff', '#2563eb', '#1d4ed8', '#1d4ed8'
    )

    # Bottom banner: Logical Equivalence & Implication connection
    bot = patches.FancyBboxPatch(
        (0.3, 0.28), 12.6, 1.62,
        boxstyle="round,pad=0.06",
        facecolor='#fffbeb', edgecolor='#d97706', linewidth=1.8
    )
    ax.add_patch(bot)
    ax.text(
        6.6, 1.62,
        r"Relación Fundamental con la Equivalencia Lógica ($P \equiv Q$ o $P \Leftrightarrow Q$) y la Implicación Lógica ($P \Rightarrow Q$)",
        ha='center', va='center', fontsize=10.6, fontweight='bold', color='#b45309'
    )
    ax.text(
        6.6, 1.12,
        r"• Dos proposiciones $P$ y $Q$ son lógicamente equivalentes ($P \equiv Q$) si y sólo si sus columnas finales son idénticas, es decir, si $(P \leftrightarrow Q)$ es una TAUTOLOGÍA.",
        ha='center', va='center', fontsize=9.3, color='#1e293b'
    )
    ax.text(
        6.6, 0.65,
        r"• Una proposición $P$ implica lógicamente a $Q$ ($P \Rightarrow Q$, argumento válido) si y sólo si la condicional $(P \rightarrow Q)$ es una TAUTOLOGÍA (nunca ocurre $P=1$ con $Q=0$).",
        ha='center', va='center', fontsize=9.3, color='#1e293b'
    )

    plt.tight_layout()
    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "clasificacion-proposiciones-tautologia-contradiccion-contingencia.png")
    plt.savefig(out_path, dpi=180, bbox_inches='tight', facecolor='white')
    plt.close()


if __name__ == "__main__":
    main()
