import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_bit_row(ax, x_start, y, bits, label_left, label_right, sign_bg="#fee2e2", mag_bg="#dbeafe"):
    ax.text(x_start - 0.2, y + 0.25, label_left, ha='right', va='center', fontsize=10, fontweight='bold', color='#1e293b')
    for i, b in enumerate(bits):
        x = x_start + i * 0.58
        bg = sign_bg if i == 0 else mag_bg
        edge = '#dc2626' if i == 0 else '#2563eb'
        rect = patches.FancyBboxPatch((x, y), 0.5, 0.5, boxstyle="round,pad=0.03",
                                      facecolor=bg, edgecolor=edge, linewidth=1.5)
        ax.add_patch(rect)
        ax.text(x + 0.25, y + 0.25, b, ha='center', va='center', fontsize=11.5, fontweight='bold', color='#0f172a')
    ax.text(x_start + len(bits)*0.58 + 0.15, y + 0.25, label_right, ha='left', va='center', fontsize=9.8, color='#334155')

def main():
    fig, ax = plt.subplots(figsize=(11, 5.8), dpi=180)
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 5.8)
    ax.axis('off')

    ax.text(5.5, 5.4, "Obtención del Complemento a 2 (8 bits) para Representar Números Negativos",
            ha='center', va='center', fontsize=13, fontweight='bold', color='#0f172a')

    # Column labels for bits
    x0 = 3.1
    ax.text(x0 + 0.25, 4.88, "Signo\n($b_7$)", ha='center', va='center', fontsize=8.5, fontweight='bold', color='#dc2626')
    for i in range(1, 8):
        ax.text(x0 + i*0.58 + 0.25, 4.88, f"$b_{7-i}$", ha='center', va='center', fontsize=9, color='#1d4ed8')

    # Step 1: +45 in 8 bits
    draw_bit_row(ax, x0, 4.1, "00101101", "1) Magnitud positiva (+45):", "= +45 en decimal (bit de signo 0)")

    # Arrow 1 -> 2
    ax.annotate('', xy=(5.4, 3.35), xytext=(5.4, 4.02),
                arrowprops=dict(arrowstyle='->', lw=1.8, color='#7c3aed'))
    ax.text(5.55, 3.68, "Invertir todos los bits (0 ↔ 1) → Complemento a 1",
            ha='left', va='center', fontsize=9.2, fontweight='bold', color='#7c3aed')

    # Step 2: 1's complement
    draw_bit_row(ax, x0, 2.75, "11010010", "2) Complemento a 1:", "Bits invertidos (NOT bit a bit)",
                 sign_bg="#fee2e2", mag_bg="#f3e8ff")

    # Arrow 2 -> 3
    ax.annotate('', xy=(5.4, 2.0), xytext=(5.4, 2.67),
                arrowprops=dict(arrowstyle='->', lw=1.8, color='#15803d'))
    ax.text(5.55, 2.33, "Sumar +1 al bit menos significativo (LSB)",
            ha='left', va='center', fontsize=9.2, fontweight='bold', color='#15803d')

    # Step 3: 2's complement
    draw_bit_row(ax, x0, 1.4, "11010011", "3) Complemento a 2 (-45):", "= -45 en complemento a 2",
                 sign_bg="#fee2e2", mag_bg="#dcfce7")

    # Verification box at bottom
    ax.text(5.5, 0.55,
            r"Verificación con pesos en Complemento a 2 ($-128, +64, +32, +16, +8, +4, +2, +1$):" + "\n" +
            r"$-1\cdot 2^7 + 1\cdot 2^6 + 0\cdot 2^5 + 1\cdot 2^4 + 0\cdot 2^3 + 0\cdot 2^2 + 1\cdot 2^1 + 1\cdot 2^0 = -128 + 64 + 16 + 2 + 1 = -45_{(10)}$",
            ha='center', va='center', fontsize=9.8, color='#0f172a',
            bbox=dict(boxstyle='round,pad=0.35', facecolor='#f8fafc', edgecolor='#94a3b8', lw=1.5))

    plt.tight_layout()
    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "complemento-a-dos-y-desbordamiento.png")
    plt.savefig(out_path, dpi=180, bbox_inches='tight', facecolor='white')
    plt.close()

if __name__ == "__main__":
    main()
