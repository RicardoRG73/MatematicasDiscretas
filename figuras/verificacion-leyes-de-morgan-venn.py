import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_2set(ax, title, mode, rgb):
    ax.set_xlim(0, 4.0)
    ax.set_ylim(0, 3.1)
    ax.set_aspect('equal')
    ax.axis('off')

    x = np.linspace(0.2, 3.8, 320)
    y = np.linspace(0.4, 2.5, 200)
    X, Y = np.meshgrid(x, y)
    c1, c2, r = (1.55, 1.45), (2.45, 1.45), 0.72
    in_A = (X - c1[0])**2 + (Y - c1[1])**2 <= r**2
    in_B = (X - c2[0])**2 + (Y - c2[1])**2 <= r**2

    if mode == 'union':
        mask = in_A | in_B
    elif mode == 'not_union':
        mask = ~(in_A | in_B)
    elif mode == 'not_A':
        mask = ~in_A
    elif mode == 'not_B':
        mask = ~in_B

    img = np.ones((Y.shape[0], X.shape[1], 4))
    img[:, :, 0] = np.where(mask, rgb[0], 0.97)
    img[:, :, 1] = np.where(mask, rgb[1], 0.98)
    img[:, :, 2] = np.where(mask, rgb[2], 0.99)
    img[:, :, 3] = np.where(mask, 0.42, 1.0)
    ax.imshow(img, extent=[0.2, 3.8, 0.4, 2.5], origin='lower', zorder=1)

    ax.add_patch(patches.Rectangle((0.2, 0.4), 3.6, 2.1, fill=False, edgecolor='#334155', lw=1.6, zorder=3))
    ax.add_patch(patches.Circle(c1, r, fill=False, edgecolor='#1e293b', lw=1.5, zorder=3))
    ax.add_patch(patches.Circle(c2, r, fill=False, edgecolor='#1e293b', lw=1.5, zorder=3))
    ax.text(3.6, 2.3, r"$U$", fontsize=9.5, fontweight='bold', color='#1e293b', ha='center', va='center')
    ax.text(0.82, 2.08, r"$A$", fontsize=10, fontweight='bold', color='#0f172a', ha='center', va='center')
    ax.text(3.18, 2.08, r"$B$", fontsize=10, fontweight='bold', color='#0f172a', ha='center', va='center')
    ax.text(2.0, 2.78, title, fontsize=10.5, fontweight='bold', color='#1e293b', ha='center', va='center')

def draw_3set_regions(ax):
    ax.set_xlim(0, 4.4)
    ax.set_ylim(0, 3.4)
    ax.set_aspect('equal')
    ax.axis('off')

    ax.add_patch(patches.Rectangle((0.2, 0.25), 4.0, 2.65, facecolor='#f8fafc', edgecolor='#334155', lw=1.8))
    cA, cB, cC, r = (1.75, 1.85), (2.65, 1.85), (2.2, 1.12), 0.78

    ax.add_patch(patches.Circle(cA, r, facecolor='#dbeafe', edgecolor='#1d4ed8', lw=1.5, alpha=0.45))
    ax.add_patch(patches.Circle(cB, r, facecolor='#dcfce7', edgecolor='#15803d', lw=1.5, alpha=0.45))
    ax.add_patch(patches.Circle(cC, r, facecolor='#fef3c7', edgecolor='#b45309', lw=1.5, alpha=0.45))

    ax.text(3.98, 2.68, r"$U$", fontsize=10, fontweight='bold', color='#1e293b', ha='center', va='center')
    ax.text(1.02, 2.42, r"$A$", fontsize=11, fontweight='bold', color='#1d4ed8', ha='center', va='center')
    ax.text(3.38, 2.42, r"$B$", fontsize=11, fontweight='bold', color='#15803d', ha='center', va='center')
    ax.text(3.08, 0.55, r"$C$", fontsize=11, fontweight='bold', color='#b45309', ha='center', va='center')

    # Fundamental products P1..P8
    ax.text(2.20, 1.62, r"$P_1$", fontsize=9, fontweight='bold', color='#0f172a', ha='center', va='center')
    ax.text(2.20, 2.15, r"$P_2$", fontsize=9, fontweight='bold', color='#0f172a', ha='center', va='center')
    ax.text(1.72, 1.32, r"$P_3$", fontsize=9, fontweight='bold', color='#0f172a', ha='center', va='center')
    ax.text(1.38, 1.98, r"$P_4$", fontsize=9, fontweight='bold', color='#0f172a', ha='center', va='center')
    ax.text(2.68, 1.32, r"$P_5$", fontsize=9, fontweight='bold', color='#0f172a', ha='center', va='center')
    ax.text(3.02, 1.98, r"$P_6$", fontsize=9, fontweight='bold', color='#0f172a', ha='center', va='center')
    ax.text(2.20, 0.75, r"$P_7$", fontsize=9, fontweight='bold', color='#0f172a', ha='center', va='center')
    ax.text(0.65, 0.55, r"$P_8$", fontsize=9, fontweight='bold', color='#475569', ha='center', va='center')

    ax.text(2.2, 3.12, "Productos Fundamentales ($2^3 = 8$ regiones)",
            fontsize=10.5, fontweight='bold', color='#1e293b', ha='center', va='center')

def main():
    fig = plt.figure(figsize=(12.2, 6.2), dpi=180)
    gs = fig.add_gridspec(2, 3, width_ratios=[1, 1, 1.15])

    fig.suptitle("Verificación Visual de la Ley de De Morgan $(A \\cup B)' = A' \\cap B'$ y Regiones Disjuntas",
                 fontsize=13.5, fontweight='bold', color='#1e293b', y=0.98)

    ax1 = fig.add_subplot(gs[0, 0])
    ax2 = fig.add_subplot(gs[0, 1])
    ax3 = fig.add_subplot(gs[1, 0])
    ax4 = fig.add_subplot(gs[1, 1])
    ax5 = fig.add_subplot(gs[:, 2])

    draw_2set(ax1, r"Paso 1a: Unión $A \cup B$", 'union', (0.23, 0.51, 0.96))
    draw_2set(ax2, r"Resultado Izq.: $(A \cup B)'$", 'not_union', (0.86, 0.15, 0.15))
    draw_2set(ax3, r"Paso 1b: Complemento $A'$", 'not_A', (0.96, 0.62, 0.04))
    draw_2set(ax4, r"Resultado Der.: $A' \cap B' = (A \cup B)'$", 'not_union', (0.86, 0.15, 0.15))

    draw_3set_regions(ax5)
    legend_txt = (
        r"$P_1 = A \cap B \cap C$" + "\n" +
        r"$P_2 = A \cap B \cap C'$" + "\n" +
        r"$P_3 = A \cap B' \cap C$" + "\n" +
        r"$P_4 = A \cap B' \cap C'$" + "\n" +
        r"$P_5 = A' \cap B \cap C$" + "\n" +
        r"$P_6 = A' \cap B \cap C'$" + "\n" +
        r"$P_7 = A' \cap B' \cap C$" + "\n" +
        r"$P_8 = A' \cap B' \cap C'$"
    )
    ax5.text(2.2, -0.35, legend_txt, ha='center', va='top', fontsize=8.8, color='#334155',
             bbox=dict(boxstyle='round,pad=0.35', facecolor='#f1f5f9', edgecolor='#cbd5e1'))

    plt.tight_layout(rect=[0, 0.02, 1, 0.93])
    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "verificacion-leyes-de-morgan-venn.png")
    plt.savefig(out_path, dpi=180, bbox_inches='tight', facecolor='white')
    plt.close()

if __name__ == "__main__":
    main()
