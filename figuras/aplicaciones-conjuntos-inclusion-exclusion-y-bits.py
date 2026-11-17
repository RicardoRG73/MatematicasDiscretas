import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def main():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12.4, 5.8), dpi=180,
                                   gridspec_kw={'width_ratios': [1.05, 1.15]})

    # --- Panel 1: Principio de Inclusión-Exclusión (Ejemplo Biblioteca 103 libros) ---
    ax1.set_xlim(0, 6.0)
    ax1.set_ylim(0, 5.6)
    ax1.axis('off')

    ax1.text(3.0, 5.25, "Principio de Inclusión-Exclusión (3 Conjuntos)",
             ha='center', va='center', fontsize=12, fontweight='bold', color='#1e293b')
    ax1.text(3.0, 4.88, r"$|A \cup B \cup C| = |A|+|B|+|C|-|A\cap B|-|A\cap C|-|B\cap C|+|A\cap B\cap C|$",
             ha='center', va='center', fontsize=8.8, color='#334155')

    # Universe box
    ax1.add_patch(patches.FancyBboxPatch((0.25, 0.65), 5.5, 3.85, boxstyle="round,pad=0.06",
                                         facecolor='#f8fafc', edgecolor='#334155', lw=1.8))
    ax1.text(5.35, 4.25, r"$|U| = 103$", fontsize=10, fontweight='bold', color='#1e293b', ha='center', va='center')

    cA, cB, cC, r = (2.35, 2.88), (3.65, 2.88), (3.0, 1.82), 1.02
    ax1.add_patch(patches.Circle(cA, r, facecolor='#dbeafe', edgecolor='#1d4ed8', lw=1.6, alpha=0.48))
    ax1.add_patch(patches.Circle(cB, r, facecolor='#dcfce7', edgecolor='#15803d', lw=1.6, alpha=0.48))
    ax1.add_patch(patches.Circle(cC, r, facecolor='#fef3c7', edgecolor='#b45309', lw=1.6, alpha=0.48))

    ax1.text(1.05, 4.02, "Compiladores\n" + r"$|A| = 50$", fontsize=9.0, fontweight='bold', color='#1d4ed8', ha='center', va='center')
    ax1.text(4.82, 4.02, "Est. de Datos\n" + r"$|B| = 54$", fontsize=9.0, fontweight='bold', color='#15803d', ha='center', va='center')
    ax1.text(4.58, 1.12, "Redes\n" + r"$|C| = 51$", fontsize=9.0, fontweight='bold', color='#b45309', ha='center', va='center')

    # Exact counts per region (Jimenez Murillo Ej. 3.18)
    ax1.text(3.00, 2.52, "19", fontsize=11.5, fontweight='bold', color='#dc2626', ha='center', va='center')
    ax1.text(3.00, 3.25, "11", fontsize=10.5, fontweight='bold', color='#0f172a', ha='center', va='center')
    ax1.text(2.40, 2.12, "13", fontsize=10.5, fontweight='bold', color='#0f172a', ha='center', va='center')
    ax1.text(3.60, 2.12, "16", fontsize=10.5, fontweight='bold', color='#0f172a', ha='center', va='center')
    ax1.text(1.85, 3.05, "7",  fontsize=10.5, fontweight='bold', color='#1d4ed8', ha='center', va='center')
    ax1.text(4.15, 3.05, "8",  fontsize=10.5, fontweight='bold', color='#15803d', ha='center', va='center')
    ax1.text(3.00, 1.25, "3",  fontsize=10.5, fontweight='bold', color='#b45309', ha='center', va='center')
    ax1.text(1.05, 1.10, "Ninguno: 26", fontsize=9.5, fontweight='bold', color='#475569', ha='center', va='center',
             bbox=dict(boxstyle='round,pad=0.2', facecolor='#e2e8f0', edgecolor='#94a3b8'))

    ax1.text(3.0, 0.28, r"$|A \cup B \cup C| = 50 + 54 + 51 - 30 - 32 - 35 + 19 = 77 \;\Rightarrow\; |(A \cup B \cup C)'| = 103 - 77 = 26$",
             ha='center', va='center', fontsize=8.8, fontweight='bold', color='#1e293b')

    # --- Panel 2: Representación Computacional mediante Vectores de Bits (Bitmasks) ---
    ax2.set_xlim(0, 6.5)
    ax2.set_ylim(0, 5.6)
    ax2.axis('off')

    ax2.text(3.25, 5.25, "Representación de Conjuntos con Cadenas de Bits",
             ha='center', va='center', fontsize=12, fontweight='bold', color='#1e293b')
    ax2.text(3.25, 4.88, r"Universo ordenado: $U = \{1, 2, 3, 4, 5, 6, 7, 8\}$",
             ha='center', va='center', fontsize=10, color='#334155')

    rows = [
        ("Elemento $u_i \\in U$", ["1", "2", "3", "4", "5", "6", "7", "8"], "#f1f5f9", "#334155"),
        ("$A = \\{1, 3, 4, 7\\}$", ["1", "0", "1", "1", "0", "0", "1", "0"], "#dbeafe", "#1d4ed8"),
        ("$B = \\{2, 3, 4, 6\\}$", ["0", "1", "1", "1", "0", "1", "0", "0"], "#dcfce7", "#15803d"),
        ("$A \\cup B$ (OR bit a bit)", ["1", "1", "1", "1", "0", "1", "1", "0"], "#fef3c7", "#b45309"),
        ("$A \\cap B$ (AND bit a bit)", ["0", "0", "1", "1", "0", "0", "0", "0"], "#ede9fe", "#6d28d9"),
        ("$A \\oplus B$ (XOR bit a bit)", ["1", "1", "0", "0", "0", "1", "1", "0"], "#fce7f3", "#be185d"),
        ("$A'$ (NOT bit a bit)", ["0", "1", "0", "0", "1", "1", "0", "1"], "#fee2e2", "#b91c1c"),
    ]

    y_start = 4.25
    dy = 0.56
    x0 = 2.45
    dx = 0.46

    for r_idx, (label, bits, bg, fg) in enumerate(rows):
        y = y_start - r_idx * dy
        ax2.text(0.15, y, label, ha='left', va='center', fontsize=9.5, fontweight='bold', color=fg)
        for c_idx, b in enumerate(bits):
            x = x0 + c_idx * dx
            cell_bg = bg if (b == "1" or r_idx == 0) else "#ffffff"
            cell_fg = fg if (b == "1" or r_idx == 0) else "#94a3b8"
            rect = patches.FancyBboxPatch((x, y - 0.19), 0.38, 0.38, boxstyle="round,pad=0.02",
                                          facecolor=cell_bg, edgecolor='#cbd5e1', lw=1.2)
            ax2.add_patch(rect)
            ax2.text(x + 0.19, y, b, ha='center', va='center', fontsize=10, fontweight='bold', color=cell_fg)

    ax2.text(3.25, 0.28, "Complejidad en CPU: Unión (A | B), Intersección (A & B), Dif. Simétrica (A ^ B) en O(1) ciclos",
             ha='center', va='center', fontsize=8.8, fontweight='bold', color='#334155',
             bbox=dict(boxstyle='round,pad=0.25', facecolor='#f1f5f9', edgecolor='#cbd5e1'))

    plt.tight_layout()
    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "aplicaciones-conjuntos-inclusion-exclusion-y-bits.png")
    plt.savefig(out_path, dpi=180, bbox_inches='tight', facecolor='white')
    plt.close()

if __name__ == "__main__":
    main()
