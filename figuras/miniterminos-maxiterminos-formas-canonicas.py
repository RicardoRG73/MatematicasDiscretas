import os
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
        x + w / 2, y + h - 0.26, title,
        ha='center', va='center',
        fontsize=10.2, fontweight='bold', color=title_color
    )
    ax.plot([x + 0.12, x + w - 0.12], [y + h - 0.46, y + h - 0.46], color=border_color, linewidth=1.0, alpha=0.65)


def main():
    fig, ax = plt.subplots(figsize=(13.6, 8.2), dpi=180)
    ax.set_xlim(0, 13.6)
    ax.set_ylim(0, 8.2)
    ax.axis('off')

    # Main Title
    ax.text(
        6.8, 7.88,
        r"Minitérminos ($m_i$), Maxitérminos ($M_i$) y Formas Canónicas de una Función Booleana",
        ha='center', va='center', fontsize=13.6, fontweight='bold', color='#0f172a'
    )
    ax.text(
        6.8, 7.52,
        r"Para $n$ variables existen $2^n$ minitérminos y $2^n$ maxitérminos   |   Relación de dualidad y complemento: $M_i = (m_i)'$",
        ha='center', va='center', fontsize=9.8, color='#334155'
    )

    # Left Panel: Master Table of 3-Variable Minterms & Maxterms + Example Function F
    draw_panel(
        ax, 0.25, 0.3, 7.55, 6.95,
        r"1. Tabla de Minitérminos y Maxitérminos para 3 Variables ($A, B, C$) y Ejemplo $F(A,B,C)$",
        '#f8fafc', '#334155', '#0f172a'
    )

    headers = ["Índice $i$", "$A$", "$B$", "$C$", r"Minitérmino ($m_i$)", r"Maxitérmino ($M_i$)", r"Ej. $F$"]
    col_x = [0.78, 1.42, 1.85, 2.28, 3.65, 5.75, 7.28]
    for cx, ht in zip(col_x, headers):
        ax.text(cx, 6.52, ht, ha='center', va='center', fontsize=8.8, fontweight='bold', color='#1e293b')
    ax.text(3.65, 6.24, r"(Producto: $0 \to X',\; 1 \to X$)", ha='center', va='center', fontsize=7.8, color='#1d4ed8')
    ax.text(5.75, 6.24, r"(Suma: $0 \to X,\; 1 \to X'$)", ha='center', va='center', fontsize=7.8, color='#b91c1c')
    ax.plot([0.4, 7.65], [6.06, 6.06], color='#64748b', linewidth=1.2)

    rows_data = [
        ("0", "0", "0", "0", r"$m_0 = A'B'C'$", r"$M_0 = A + B + C$", "0"),
        ("1", "0", "0", "1", r"$m_1 = A'B'C$", r"$M_1 = A + B + C'$", "1"),
        ("2", "0", "1", "0", r"$m_2 = A'BC'$", r"$M_2 = A + B' + C$", "0"),
        ("3", "0", "1", "1", r"$m_3 = A'BC$", r"$M_3 = A + B' + C'$", "1"),
        ("4", "1", "0", "0", r"$m_4 = AB'C'$", r"$M_4 = A' + B + C$", "1"),
        ("5", "1", "0", "1", r"$m_5 = AB'C$", r"$M_5 = A' + B + C'$", "0"),
        ("6", "1", "1", "0", r"$m_6 = ABC'$", r"$M_6 = A' + B' + C$", "0"),
        ("7", "1", "1", "1", r"$m_7 = ABC$", r"$M_7 = A' + B' + C'$", "1"),
    ]

    for idx, (i_str, a, b, c, m_str, M_str, f_val) in enumerate(rows_data):
        ry = 5.72 - idx * 0.58
        bg_row = '#dbeafe' if f_val == '1' else '#fee2e2'
        ax.add_patch(patches.Rectangle((0.4, ry - 0.24), 7.25, 0.48, facecolor=bg_row, alpha=0.45, edgecolor='none'))
        ax.text(col_x[0], ry, i_str, ha='center', va='center', fontsize=9.0, fontweight='bold', color='#334155')
        ax.text(col_x[1], ry, a, ha='center', va='center', fontsize=9.0, color='#0f172a')
        ax.text(col_x[2], ry, b, ha='center', va='center', fontsize=9.0, color='#0f172a')
        ax.text(col_x[3], ry, c, ha='center', va='center', fontsize=9.0, color='#0f172a')
        ax.text(col_x[4], ry, m_str, ha='center', va='center', fontsize=9.0,
                fontweight='bold' if f_val == '1' else 'normal',
                color='#1d4ed8' if f_val == '1' else '#475569')
        ax.text(col_x[5], ry, M_str, ha='center', va='center', fontsize=9.0,
                fontweight='bold' if f_val == '0' else 'normal',
                color='#b91c1c' if f_val == '0' else '#475569')
        ax.text(col_x[6], ry, f_val, ha='center', va='center', fontsize=9.8, fontweight='bold',
                color='#1d4ed8' if f_val == '1' else '#b91c1c')

    ax.text(
        4.02, 0.92,
        r"Propiedad clave:  $m_i = 1$ únicamente en la fila $i$;     $M_i = 0$ únicamente en la fila $i$.",
        ha='center', va='center', fontsize=8.7, fontweight='bold', color='#0f172a'
    )
    ax.text(
        4.02, 0.55,
        r"En azul: filas donde $F = 1$ (minitérminos de $F$).   En rojo: filas donde $F = 0$ (maxitérminos de $F$).",
        ha='center', va='center', fontsize=8.3, color='#334155'
    )

    # Top-Right Panel: Forma Canónica Disyuntiva (Suma de Minitérminos)
    draw_panel(
        ax, 8.05, 4.48, 5.3, 2.77,
        "2. Forma Canónica Disyuntiva (Suma de Minitérminos)",
        '#eff6ff', '#2563eb', '#1d4ed8'
    )
    sop_lines = [
        r"$\bullet$ Se toman las filas donde la salida es $F = 1$:",
        r"   Índices con $F = 1$:   $i \in \{1, 3, 4, 7\}$",
        r"$\bullet$ Notación compacta y desarrollo algebraico:",
        r"   $F(A,B,C) = \sum m(1, 3, 4, 7) = m_1 + m_3 + m_4 + m_7$",
        r"   $F = A'B'C + A'BC + AB'C' + ABC$",
        r"$\bullet$ Expansión algebraica de un término incompleto:",
        r"   Multiplicar por $(X + X') = 1$ cada variable faltante."
    ]
    for idx, line in enumerate(sop_lines):
        ry = 6.52 - idx * 0.285
        w_font = 'bold' if idx in (3, 4) else 'normal'
        c_font = '#1e3a8a' if idx in (3, 4) else '#1e293b'
        ax.text(8.22, ry, line, ha='left', va='center', fontsize=8.45, fontweight=w_font, color=c_font)

    # Middle-Right Panel: Forma Canónica Conjuntiva (Producto de Maxitérminos)
    draw_panel(
        ax, 8.05, 1.72, 5.3, 2.55,
        "3. Forma Canónica Conjuntiva (Producto de Maxitérminos)",
        '#fff1f2', '#e11d48', '#be123c'
    )
    pos_lines = [
        r"$\bullet$ Se toman las filas donde la salida es $F = 0$:",
        r"   Índices con $F = 0$:   $j \in \{0, 2, 5, 6\}$",
        r"$\bullet$ Notación compacta y desarrollo algebraico:",
        r"   $F(A,B,C) = \prod M(0, 2, 5, 6) = M_0 \cdot M_2 \cdot M_5 \cdot M_6$",
        r"   $F = (A+B+C)(A+B'+C)(A'+B+C')(A'+B'+C)$",
        r"$\bullet$ Expansión algebraica de una suma incompleta:",
        r"   Sumar $(X \cdot X') = 0$ y aplicar distributividad."
    ]
    for idx, line in enumerate(pos_lines):
        ry = 3.55 - idx * 0.265
        w_font = 'bold' if idx in (3, 4) else 'normal'
        c_font = '#9f1239' if idx in (3, 4) else '#1e293b'
        ax.text(8.22, ry, line, ha='left', va='center', fontsize=8.25, fontweight=w_font, color=c_font)

    # Bottom-Right Panel: Conversión Directa entre Formas Canónicas
    draw_panel(
        ax, 8.05, 0.3, 5.3, 1.22,
        "4. Conversión Directa entre Ambas Formas Canónicas",
        '#ecfdf5', '#059669', '#047857'
    )
    ax.text(
        10.7, 0.82,
        r"Conjunto de índices complementario en $\{0, 1, \dots, 2^n - 1\}$:",
        ha='center', va='center', fontsize=8.4, color='#1e293b'
    )
    ax.text(
        10.7, 0.50,
        r"$F = \sum m(1, 3, 4, 7) \;\Longleftrightarrow\; F = \prod M(0, 2, 5, 6)$",
        ha='center', va='center', fontsize=9.1, fontweight='bold', color='#047857'
    )

    plt.tight_layout()
    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "miniterminos-maxiterminos-formas-canonicas.png")
    plt.savefig(out_path, dpi=180, bbox_inches='tight', facecolor='white')
    plt.close()


if __name__ == "__main__":
    main()
