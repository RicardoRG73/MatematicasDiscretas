import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def main():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5.6), dpi=180,
                                   gridspec_kw={'width_ratios': [1.05, 1.15]})

    # --- Panel 1: Subconjuntos en Diagrama de Venn ---
    ax1.set_xlim(0, 6)
    ax1.set_ylim(0, 5.5)
    ax1.axis('off')
    ax1.text(3.0, 5.15, "Relaciones de Inclusión (Subconjuntos)",
             ha='center', va='center', fontsize=12, fontweight='bold', color='#1e293b')
    ax1.text(3.0, 4.78, r"$B \subset C \subset U,\quad A \subset U,\quad A \cap C = \emptyset$",
             ha='center', va='center', fontsize=10.5, color='#334155')

    # Universe U
    rect_u = patches.FancyBboxPatch((0.3, 0.7), 5.4, 3.75, boxstyle="round,pad=0.06",
                                    facecolor='#f8fafc', edgecolor='#334155', linewidth=2.0)
    ax1.add_patch(rect_u)
    ax1.text(5.45, 4.2, r"$U$", ha='center', va='center', fontsize=13, fontweight='bold', color='#1e293b')

    # Set C (large ellipse on the right)
    ell_c = patches.Ellipse((3.85, 2.55), width=3.1, height=2.95,
                            facecolor='#dbeafe', edgecolor='#1d4ed8', linewidth=1.8, alpha=0.85)
    ax1.add_patch(ell_c)
    ax1.text(4.65, 3.6, r"$C$", ha='center', va='center', fontsize=12, fontweight='bold', color='#1d4ed8')

    # Set B inside C (proper subset)
    ell_b = patches.Ellipse((3.55, 2.25), width=1.85, height=1.6,
                            facecolor='#dcfce7', edgecolor='#15803d', linewidth=1.8)
    ax1.add_patch(ell_b)
    ax1.text(3.55, 2.72, r"$B \subset C$", ha='center', va='center', fontsize=10.5, fontweight='bold', color='#15803d')
    ax1.text(3.55, 2.0, r"$\bullet\, 2 \quad \bullet\, 4$", ha='center', va='center', fontsize=10, color='#14532d')

    # Elements in C \ B
    ax1.text(4.5, 2.85, r"$\bullet\, 6$", ha='center', va='center', fontsize=10, color='#1e3a8a')
    ax1.text(4.65, 1.85, r"$\bullet\, 8$", ha='center', va='center', fontsize=10, color='#1e3a8a')

    # Disjoint set A on the left
    ell_a = patches.Ellipse((1.35, 2.55), width=1.55, height=2.1,
                            facecolor='#fef3c7', edgecolor='#b45309', linewidth=1.8)
    ax1.add_patch(ell_a)
    ax1.text(1.35, 3.22, r"$A$", ha='center', va='center', fontsize=12, fontweight='bold', color='#b45309')
    ax1.text(1.35, 2.45, r"$\bullet\, 1$" + "\n" + r"$\bullet\, 3$", ha='center', va='center', fontsize=10, color='#78350f')

    # Element outside A and C
    ax1.text(2.2, 1.15, r"$\bullet\, 5 \in U$", ha='center', va='center', fontsize=10, color='#475569')

    ax1.text(3.0, 0.3, r"Propiedades: $\emptyset \subseteq B \subseteq C \subseteq U$   y   $B \nsubseteq A$",
             ha='center', va='center', fontsize=9.8, fontweight='bold', color='#334155',
             bbox=dict(boxstyle='round,pad=0.25', facecolor='#f1f5f9', edgecolor='#cbd5e1'))

    # --- Panel 2: Conjunto Potencia P(A) como Retículo (Hasse) ---
    ax2.set_xlim(0, 6.5)
    ax2.set_ylim(0, 5.5)
    ax2.axis('off')
    ax2.text(3.25, 5.15, r"Conjunto Potencia $\mathcal{P}(A)$ para $A = \{a, b, c\}$",
             ha='center', va='center', fontsize=12, fontweight='bold', color='#1e293b')
    ax2.text(3.25, 4.78, r"$|\mathcal{P}(A)| = 2^{|A|} = 2^3 = 8\text{ subconjuntos}$",
             ha='center', va='center', fontsize=10.5, color='#334155')

    nodes = {
        'abc': (3.25, 4.15, r"$\{a,b,c\}$", "111", "#ede9fe", "#6d28d9"),
        'ab':  (1.45, 3.00, r"$\{a,b\}$",   "110", "#dbeafe", "#1d4ed8"),
        'ac':  (3.25, 3.00, r"$\{a,c\}$",   "101", "#dbeafe", "#1d4ed8"),
        'bc':  (5.05, 3.00, r"$\{b,c\}$",   "011", "#dbeafe", "#1d4ed8"),
        'a':   (1.45, 1.75, r"$\{a\}$",     "100", "#dcfce7", "#15803d"),
        'b':   (3.25, 1.75, r"$\{b\}$",     "010", "#dcfce7", "#15803d"),
        'c':   (5.05, 1.75, r"$\{c\}$",     "001", "#dcfce7", "#15803d"),
        'emp': (3.25, 0.60, r"$\emptyset$", "000", "#fee2e2", "#b91c1c"),
    }

    edges = [
        ('emp', 'a'), ('emp', 'b'), ('emp', 'c'),
        ('a', 'ab'), ('a', 'ac'),
        ('b', 'ab'), ('b', 'bc'),
        ('c', 'ac'), ('c', 'bc'),
        ('ab', 'abc'), ('ac', 'abc'), ('bc', 'abc')
    ]

    for u, v in edges:
        x1, y1 = nodes[u][0], nodes[u][1]
        x2, y2 = nodes[v][0], nodes[v][1]
        ax2.plot([x1, x2], [y1, y2], color='#94a3b8', lw=1.5, zorder=1)

    for key, (x, y, label, bits, bg, fg) in nodes.items():
        box = patches.FancyBboxPatch((x - 0.62, y - 0.28), 1.24, 0.56, boxstyle="round,pad=0.04",
                                     facecolor=bg, edgecolor=fg, linewidth=1.6, zorder=3)
        ax2.add_patch(box)
        ax2.text(x, y + 0.07, label, ha='center', va='center', fontsize=10, fontweight='bold', color=fg, zorder=4)
        ax2.text(x, y - 0.14, f"({bits})", ha='center', va='center', fontsize=8, color='#475569', zorder=4)

    # Cardinality labels on the left of Panel 2
    ax2.text(0.32, 4.15, "k = 3\n(1)", ha='center', va='center', fontsize=8.5, fontweight='bold', color='#6d28d9')
    ax2.text(0.32, 3.00, "k = 2\n(3)", ha='center', va='center', fontsize=8.5, fontweight='bold', color='#1d4ed8')
    ax2.text(0.32, 1.75, "k = 1\n(3)", ha='center', va='center', fontsize=8.5, fontweight='bold', color='#15803d')
    ax2.text(0.32, 0.60, "k = 0\n(1)", ha='center', va='center', fontsize=8.5, fontweight='bold', color='#b91c1c')

    plt.tight_layout()
    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "subconjuntos-y-conjunto-potencia.png")
    plt.savefig(out_path, dpi=180, bbox_inches='tight', facecolor='white')
    plt.close()

if __name__ == "__main__":
    main()
