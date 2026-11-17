import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_venn_panel(ax, title, subtitle, mode):
    ax.set_xlim(0, 4.2)
    ax.set_ylim(0, 3.4)
    ax.set_aspect('equal')
    ax.axis('off')

    # Grid for exact shading inside the Universe box [0.2, 4.0] x [0.55, 2.75]
    x = np.linspace(0.2, 4.0, 380)
    y = np.linspace(0.55, 2.75, 220)
    X, Y = np.meshgrid(x, y)

    c1 = (1.65, 1.65)
    c2 = (2.55, 1.65)
    r = 0.78

    in_A = (X - c1[0])**2 + (Y - c1[1])**2 <= r**2
    in_B = (X - c2[0])**2 + (Y - c2[1])**2 <= r**2

    if mode == 'union':
        mask = in_A | in_B
        rgba = (0.23, 0.51, 0.96, 0.42)
    elif mode == 'inter':
        mask = in_A & in_B
        rgba = (0.08, 0.64, 0.29, 0.48)
    elif mode == 'comp_a':
        mask = ~in_A
        rgba = (0.96, 0.62, 0.04, 0.38)
    elif mode == 'diff_ab':
        mask = in_A & (~in_B)
        rgba = (0.93, 0.28, 0.60, 0.42)
    elif mode == 'diff_ba':
        mask = in_B & (~in_A)
        rgba = (0.02, 0.71, 0.83, 0.42)
    elif mode == 'symdiff':
        mask = in_A ^ in_B
        rgba = (0.55, 0.36, 0.96, 0.44)

    # Background image for shaded region
    img = np.ones((Y.shape[0], X.shape[1], 4))
    img[:, :, 0] = np.where(mask, rgba[0], 0.97)
    img[:, :, 1] = np.where(mask, rgba[1], 0.98)
    img[:, :, 2] = np.where(mask, rgba[2], 0.99)
    img[:, :, 3] = np.where(mask, rgba[3], 1.0)

    ax.imshow(img, extent=[0.2, 4.0, 0.55, 2.75], origin='lower', zorder=1)

    # Universe border
    rect = patches.Rectangle((0.2, 0.55), 3.8, 2.2, fill=False, edgecolor='#334155', linewidth=1.8, zorder=3)
    ax.add_patch(rect)
    ax.text(3.8, 2.52, r"$U$", ha='center', va='center', fontsize=10.5, fontweight='bold', color='#1e293b', zorder=4)

    # Circle borders
    circ1 = patches.Circle(c1, r, fill=False, edgecolor='#1e293b', linewidth=1.6, zorder=3)
    circ2 = patches.Circle(c2, r, fill=False, edgecolor='#1e293b', linewidth=1.6, zorder=3)
    ax.add_patch(circ1)
    ax.add_patch(circ2)

    # Labels A and B
    ax.text(0.82, 2.32, r"$A$", ha='center', va='center', fontsize=11, fontweight='bold', color='#0f172a', zorder=4)
    ax.text(3.38, 2.32, r"$B$", ha='center', va='center', fontsize=11, fontweight='bold', color='#0f172a', zorder=4)

    # Title and formula
    ax.text(2.1, 3.05, title, ha='center', va='center', fontsize=11, fontweight='bold', color='#1e293b')
    ax.text(2.1, 0.24, subtitle, ha='center', va='center', fontsize=9.5, color='#334155')

def main():
    fig, axes = plt.subplots(2, 3, figsize=(12, 7.2), dpi=180)
    fig.suptitle("Operaciones Fundamentales con Conjuntos mediante Diagramas de Venn",
                 fontsize=14, fontweight='bold', color='#1e293b', y=0.98)

    panels = [
        ("1. Unión ($A \\cup B$)", r"$\{x \mid x \in A \;\text{o}\; x \in B\}$", 'union'),
        ("2. Intersección ($A \\cap B$)", r"$\{x \mid x \in A \;\text{y}\; x \in B\}$", 'inter'),
        ("3. Complemento ($A'$ o $A^c$)", r"$\{x \in U \mid x \notin A\}$", 'comp_a'),
        ("4. Diferencia ($A - B$)", r"$\{x \mid x \in A \;\text{y}\; x \notin B\}$", 'diff_ab'),
        ("5. Diferencia ($B - A$)", r"$\{x \mid x \in B \;\text{y}\; x \notin A\}$", 'diff_ba'),
        ("6. Diferencia Simétrica ($A \\oplus B$)", r"$(A - B) \cup (B - A) = (A \cup B) - (A \cap B)$", 'symdiff'),
    ]

    for ax, (title, sub, mode) in zip(axes.flat, panels):
        draw_venn_panel(ax, title, sub, mode)

    plt.tight_layout(rect=[0, 0, 1, 0.94])
    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "diagramas-venn-operaciones-conjuntos.png")
    plt.savefig(out_path, dpi=180, bbox_inches='tight', facecolor='white')
    plt.close()

if __name__ == "__main__":
    main()
