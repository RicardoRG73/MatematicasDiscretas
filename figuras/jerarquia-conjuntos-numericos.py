import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def main():
    fig, ax = plt.subplots(figsize=(11.5, 6.5), dpi=180)
    ax.set_xlim(0, 11.5)
    ax.set_ylim(0, 6.5)
    ax.axis('off')

    # Title
    ax.text(5.75, 6.15, "Jerarquía y Clasificación de los Conjuntos Numéricos",
            ha='center', va='center', fontsize=14, fontweight='bold', color='#1e293b')
    ax.text(5.75, 5.78, r"$\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R} \subset \mathbb{C} \qquad (\mathbb{R} = \mathbb{Q} \cup \mathbb{I},\; \mathbb{Q} \cap \mathbb{I} = \emptyset)$",
            ha='center', va='center', fontsize=11.5, color='#334155')

    # Outer box: Complex Numbers C
    rect_c = patches.FancyBboxPatch((0.35, 0.35), 10.8, 5.05, boxstyle="round,pad=0.1",
                                    facecolor='#f8fafc', edgecolor='#334155', linewidth=2.2)
    ax.add_patch(rect_c)
    ax.text(5.75, 5.12, r"Números Complejos ($\mathbb{C} = \{a + bi \mid a, b \in \mathbb{R},\; i^2 = -1\}$)",
            ha='center', va='center', fontsize=11.5, fontweight='bold', color='#1e293b')

    # Left region inside C: Real Numbers R
    rect_r = patches.FancyBboxPatch((0.6, 0.6), 7.55, 4.2, boxstyle="round,pad=0.08",
                                    facecolor='#eff6ff', edgecolor='#1d4ed8', linewidth=2.0)
    ax.add_patch(rect_r)
    ax.text(4.37, 4.55, r"Números Reales ($\mathbb{R}$): $b = 0$",
            ha='center', va='center', fontsize=11, fontweight='bold', color='#1d4ed8')

    # Right region inside C: Imaginary / Non-real Complex Numbers
    rect_im = patches.FancyBboxPatch((8.4, 0.6), 2.5, 4.2, boxstyle="round,pad=0.08",
                                     facecolor='#fdf4ff', edgecolor='#9333ea', linewidth=1.8)
    ax.add_patch(rect_im)
    ax.text(9.65, 4.42, "Complejos no reales\n($b \\neq 0$)",
            ha='center', va='center', fontsize=10, fontweight='bold', color='#7e22ce')
    ax.text(9.65, 3.7, r"$3 + 2i$,  $-1 - 5i$", ha='center', va='center', fontsize=9.5, color='#581c87')

    # Subbox inside Im: Pure Imaginary
    rect_pim = patches.FancyBboxPatch((8.6, 0.9), 2.1, 2.35, boxstyle="round,pad=0.06",
                                      facecolor='#fae8ff', edgecolor='#a855f7', linewidth=1.5, linestyle='--')
    ax.add_patch(rect_pim)
    ax.text(9.65, 2.85, "Imaginarios Puros\n($a = 0,\\; b \\neq 0$)",
            ha='center', va='center', fontsize=9.5, fontweight='bold', color='#6b21a8')
    ax.text(9.65, 2.1, r"$i = \sqrt{-1}$" + "\n" + r"$4i,\; -7i,\; \sqrt{-9} = 3i$",
            ha='center', va='center', fontsize=9.2, color='#581c87')
    ax.text(9.65, 1.25, r"Propiedad: $i^2 = -1$" + "\n" + r"$i^3 = -i,\; i^4 = 1$",
            ha='center', va='center', fontsize=8.5, color='#6b21a8')

    # Inside R: Irrationals I (right side of R)
    rect_irr = patches.FancyBboxPatch((6.1, 0.85), 1.85, 3.35, boxstyle="round,pad=0.06",
                                      facecolor='#fff7ed', edgecolor='#ea580c', linewidth=1.7)
    ax.add_patch(rect_irr)
    ax.text(7.02, 3.85, "Irracionales\n" + r"($\mathbb{I} = \mathbb{R} - \mathbb{Q}$)",
            ha='center', va='center', fontsize=9.8, fontweight='bold', color='#c2410c')
    ax.text(7.02, 2.8, "Decimales infinitos\nno periódicos:",
            ha='center', va='center', fontsize=8.5, color='#9a3412')
    ax.text(7.02, 1.8, r"$\sqrt{2} \approx 1.4142\dots$" + "\n" +
                       r"$\sqrt{3},\; -\sqrt{5}$" + "\n" +
                       r"$\pi \approx 3.14159\dots$" + "\n" +
                       r"$e \approx 2.71828\dots$",
            ha='center', va='center', fontsize=9.2, color='#7c2d12')

    # Inside R: Rationals Q (left side of R)
    rect_q = patches.FancyBboxPatch((0.82, 0.85), 5.05, 3.35, boxstyle="round,pad=0.08",
                                    facecolor='#ecfdf5', edgecolor='#059669', linewidth=1.8)
    ax.add_patch(rect_q)
    ax.text(3.34, 3.92, r"Números Racionales ($\mathbb{Q} = \{\frac{a}{b} \mid a, b \in \mathbb{Z},\; b \neq 0\}$)",
            ha='center', va='center', fontsize=9.8, fontweight='bold', color='#047857')
    ax.text(3.34, 3.55, r"Fracciones exactas y periódicas:  $\frac{3}{4} = 0.75,\; -\frac{5}{2} = -2.5,\; \frac{1}{3} = 0.\overline{3}$",
            ha='center', va='center', fontsize=9.0, color='#065f46')

    # Inside Q: Integers Z
    rect_z = patches.FancyBboxPatch((1.05, 1.05), 4.58, 2.25, boxstyle="round,pad=0.07",
                                    facecolor='#fef9c3', edgecolor='#ca8a04', linewidth=1.7)
    ax.add_patch(rect_z)
    ax.text(3.34, 3.05, r"Números Enteros ($\mathbb{Z} = \{\dots, -3, -2, -1, 0, 1, 2, 3, \dots\}$)",
            ha='center', va='center', fontsize=9.5, fontweight='bold', color='#854d0e')
    ax.text(1.82, 2.15, "Enteros negativos\n" + r"($\mathbb{Z}^-$) y el Cero:" + "\n" + r"$\dots, -3, -2, -1,\; 0$",
            ha='center', va='center', fontsize=8.8, color='#713f12')

    # Inside Z: Naturals N
    rect_n = patches.FancyBboxPatch((2.65, 1.22), 2.78, 1.52, boxstyle="round,pad=0.06",
                                    facecolor='#dbeafe', edgecolor='#2563eb', linewidth=1.7)
    ax.add_patch(rect_n)
    ax.text(4.04, 2.42, r"Números Naturales ($\mathbb{N}$)",
            ha='center', va='center', fontsize=9.5, fontweight='bold', color='#1e40af')
    ax.text(4.04, 1.92, r"$\mathbb{N} = \{1, 2, 3, 4, \dots\}$",
            ha='center', va='center', fontsize=9.2, color='#1e3a8a')
    ax.text(4.04, 1.48, r"Enteros no negativos: $\mathbb{Z}^+ = \{0, 1, 2, 3, \dots\}$",
            ha='center', va='center', fontsize=8.2, color='#1d4ed8')

    plt.tight_layout()
    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "jerarquia-conjuntos-numericos.png")
    plt.savefig(out_path, dpi=180, bbox_inches='tight', facecolor='white')
    plt.close()

if __name__ == "__main__":
    main()
