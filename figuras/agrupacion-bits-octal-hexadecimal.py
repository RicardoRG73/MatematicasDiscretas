import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def main():
    fig, ax = plt.subplots(figsize=(11, 5.6), dpi=180)
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 5.6)
    ax.axis('off')

    ax.text(5.5, 5.25, "Agrupación de Bits a partir del Punto Radical (Binario ↔ Octal y Hexadecimal)",
            ha='center', va='center', fontsize=13, fontweight='bold', color='#0f172a')

    # Example 1: Binary to Octal (groups of 3)
    ax.text(0.5, 4.55, "A) Conversión Binario → Octal (bloques de 3 bits hacia izquierda y derecha del punto):",
            ha='left', va='center', fontsize=10.5, fontweight='bold', color='#1d4ed8')

    oct_blocks = [
        ("010", "2", "#dbeafe", "#2563eb", "Cero de\nrelleno izq."),
        ("110", "6", "#eff6ff", "#2563eb", ""),
        ("101", "5", "#dbeafe", "#2563eb", ""),
        (".", ".", "#fef3c7", "#d97706", "Punto"),
        ("101", "5", "#dcfce7", "#16a34a", ""),
        ("100", "4", "#f0fdf4", "#16a34a", "Ceros de\nrelleno der."),
    ]

    x_cursor = 1.1
    for bits, oct_d, bg, border, note in oct_blocks:
        w = 0.55 if bits == "." else 1.45
        rect = patches.FancyBboxPatch((x_cursor, 3.65), w, 0.6, boxstyle="round,pad=0.04",
                                      facecolor=bg, edgecolor=border, linewidth=1.6)
        ax.add_patch(rect)
        ax.text(x_cursor + w/2, 3.95, bits, ha='center', va='center', fontsize=12, fontweight='bold', color='#0f172a')

        if bits != ".":
            ax.annotate('', xy=(x_cursor + w/2, 3.05), xytext=(x_cursor + w/2, 3.6),
                        arrowprops=dict(arrowstyle='->', color=border, lw=1.5))
        ax.text(x_cursor + w/2, 2.85, oct_d, ha='center', va='center', fontsize=13, fontweight='bold', color=border)
        if note and bits != ".":
            ax.text(x_cursor + w/2, 4.38, note, ha='center', va='center', fontsize=7.8, color='#64748b')
        x_cursor += w + 0.18

    ax.text(9.5, 3.45, r"$10110101.1011_{(2)}$" + "\n" + r"$= 265.54_{(8)}$",
            ha='center', va='center', fontsize=11, fontweight='bold', color='#1e293b',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#f8fafc', edgecolor='#94a3b8'))

    # Divider
    ax.plot([0.5, 10.5], [2.4, 2.4], linestyle='--', color='#cbd5e1', lw=1.2)

    # Example 2: Binary to Hexadecimal (groups of 4)
    ax.text(0.5, 2.05, "B) Conversión del mismo número Binario → Hexadecimal (bloques de 4 bits):",
            ha='left', va='center', fontsize=10.5, fontweight='bold', color='#be185d')

    hex_blocks = [
        ("1011", "B (11)", "#fce7f3", "#db2777"),
        ("0101", "5", "#fdf2f8", "#db2777"),
        (".", ".", "#fef3c7", "#d97706"),
        ("1011", "B (11)", "#dcfce7", "#16a34a"),
    ]

    x_cursor = 1.6
    for bits, hex_d, bg, border in hex_blocks:
        w = 0.55 if bits == "." else 1.85
        rect = patches.FancyBboxPatch((x_cursor, 1.15), w, 0.6, boxstyle="round,pad=0.04",
                                      facecolor=bg, edgecolor=border, linewidth=1.6)
        ax.add_patch(rect)
        ax.text(x_cursor + w/2, 1.45, bits, ha='center', va='center', fontsize=12, fontweight='bold', color='#0f172a')

        if bits != ".":
            ax.annotate('', xy=(x_cursor + w/2, 0.55), xytext=(x_cursor + w/2, 1.1),
                        arrowprops=dict(arrowstyle='->', color=border, lw=1.5))
        ax.text(x_cursor + w/2, 0.35, hex_d, ha='center', va='center', fontsize=12, fontweight='bold', color=border)
        x_cursor += w + 0.22

    ax.text(9.3, 0.95, r"$10110101.1011_{(2)}$" + "\n" + r"$= \mathrm{B5.B}_{(16)}$",
            ha='center', va='center', fontsize=11, fontweight='bold', color='#1e293b',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#f8fafc', edgecolor='#94a3b8'))

    plt.tight_layout()
    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "agrupacion-bits-octal-hexadecimal.png")
    plt.savefig(out_path, dpi=180, bbox_inches='tight', facecolor='white')
    plt.close()

if __name__ == "__main__":
    main()
