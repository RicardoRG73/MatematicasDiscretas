import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def main():
    fig, ax = plt.subplots(figsize=(11, 5.5), dpi=180)
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 5.5)
    ax.axis('off')

    # Title
    ax.text(5.5, 5.05, "Estructura de un Número en un Sistema Posicional de Base b",
            ha='center', va='center', fontsize=14, fontweight='bold', color='#1e293b')
    ax.text(5.5, 4.65, r"$N_{(b)} = d_{3}d_{2}d_{1}d_{0}\,.\,d_{-1}d_{-2}d_{-3} = \sum_{i=-k}^{n-1} d_i \cdot b^i$",
            ha='center', va='center', fontsize=12, color='#334155')

    # Positions data
    positions = [
        ("3", r"$d_3$", r"$b^3$", "1.2", "#dbeafe", "#1d4ed8", "Parte Entera"),
        ("2", r"$d_2$", r"$b^2$", "2.4", "#dbeafe", "#1d4ed8", "Parte Entera"),
        ("1", r"$d_1$", r"$b^1$", "3.6", "#dbeafe", "#1d4ed8", "Parte Entera"),
        ("0", r"$d_0$", r"$b^0 = 1$", "4.8", "#dbeafe", "#1d4ed8", "Parte Entera"),
        (".", ".", "Punto\nradical", "5.85", "#fef3c7", "#b45309", "Separador"),
        ("-1", r"$d_{-1}$", r"$b^{-1}$", "6.9", "#dcfce7", "#15803d", "Parte Fraccionaria"),
        ("-2", r"$d_{-2}$", r"$b^{-2}$", "8.1", "#dcfce7", "#15803d", "Parte Fraccionaria"),
        ("-3", r"$d_{-3}$", r"$b^{-3}$", "9.3", "#dcfce7", "#15803d", "Parte Fraccionaria"),
    ]

    # Headers on the left
    ax.text(0.3, 3.65, "Posición (i):", ha='left', va='center', fontsize=10, fontweight='bold', color='#475569')
    ax.text(0.3, 2.85, "Dígito:", ha='left', va='center', fontsize=10, fontweight='bold', color='#475569')
    ax.text(0.3, 1.95, "Peso ($b^i$):", ha='left', va='center', fontsize=10, fontweight='bold', color='#475569')
    ax.text(0.3, 1.15, "Ej. Base 2:", ha='left', va='center', fontsize=10, fontweight='bold', color='#475569')

    b2_vals = ["8", "4", "2", "1", ".", "0.5", "0.25", "0.125"]

    for idx, (pos, dig, weight, x_str, bg, fg, group) in enumerate(positions):
        x = float(x_str)
        w = 0.7 if pos == "." else 1.05
        # Position index
        if pos != ".":
            ax.text(x + w/2, 3.65, f"i = {pos}", ha='center', va='center', fontsize=9.5, fontweight='bold', color=fg)
        # Box for digit
        rect = patches.FancyBboxPatch((x, 2.45), w, 0.8, boxstyle="round,pad=0.05",
                                      facecolor=bg, edgecolor=fg, linewidth=1.8)
        ax.add_patch(rect)
        ax.text(x + w/2, 2.85, dig, ha='center', va='center', fontsize=13, fontweight='bold', color=fg)

        # Weight
        ax.text(x + w/2, 1.95, weight, ha='center', va='center', fontsize=10.5, color='#1e293b')
        # Base 2 example weight
        ax.text(x + w/2, 1.15, b2_vals[idx], ha='center', va='center', fontsize=10, color='#475569',
                bbox=dict(boxstyle='round,pad=0.2', facecolor='#f8fafc', edgecolor='#cbd5e1'))

    # Braces / spans for integer and fractional parts
    ax.annotate('', xy=(1.2, 4.15), xytext=(5.85, 4.15),
                arrowprops=dict(arrowstyle='<->', color='#1d4ed8', lw=1.5))
    ax.text(3.52, 4.32, "Parte Entera (pesos con exponente ≥ 0)", ha='center', va='center',
            fontsize=9.5, fontweight='bold', color='#1d4ed8')

    ax.annotate('', xy=(6.9, 4.15), xytext=(10.35, 4.15),
                arrowprops=dict(arrowstyle='<->', color='#15803d', lw=1.5))
    ax.text(8.62, 4.32, "Parte Fraccionaria (exponentes < 0)", ha='center', va='center',
            fontsize=9.5, fontweight='bold', color='#15803d')

    # MSB and LSB annotations
    ax.annotate('Dígito más significativo (MSD / MSB)', xy=(1.72, 2.42), xytext=(2.3, 0.4),
                arrowprops=dict(arrowstyle='->', color='#dc2626', lw=1.5),
                fontsize=9.5, fontweight='bold', color='#dc2626', ha='center')
    ax.annotate('Dígito menos significativo (LSD / LSB)', xy=(9.82, 2.42), xytext=(8.8, 0.4),
                arrowprops=dict(arrowstyle='->', color='#7c3aed', lw=1.5),
                fontsize=9.5, fontweight='bold', color='#7c3aed', ha='center')

    plt.tight_layout()
    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "estructura-posicional-base-b.png")
    plt.savefig(out_path, dpi=180, bbox_inches='tight', facecolor='white')
    plt.close()

if __name__ == "__main__":
    main()
