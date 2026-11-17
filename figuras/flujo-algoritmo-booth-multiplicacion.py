import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def box(ax, x, y, w, h, text, bg="#e0f2fe", border="#0284c7", fontsize=9.5):
    p = patches.FancyBboxPatch((x - w/2, y - h/2), w, h, boxstyle="round,pad=0.06",
                               facecolor=bg, edgecolor=border, linewidth=1.8)
    ax.add_patch(p)
    ax.text(x, y, text, ha='center', va='center', fontsize=fontsize, fontweight='bold', color='#0f172a')

def diamond(ax, x, y, w, h, text, bg="#fef3c7", border="#d97706", fontsize=9.5):
    pts = [(x, y + h/2), (x + w/2, y), (x, y - h/2), (x - w/2, y)]
    p = patches.Polygon(pts, closed=True, facecolor=bg, edgecolor=border, linewidth=1.8)
    ax.add_patch(p)
    ax.text(x, y, text, ha='center', va='center', fontsize=fontsize, fontweight='bold', color='#0f172a')

def arrow(ax, x1, y1, x2, y2, label=""):
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='->', lw=1.7, color='#334155'))
    if label:
        ax.text((x1+x2)/2, (y1+y2)/2 + 0.15, label, ha='center', va='center',
                fontsize=8.5, fontweight='bold', color='#1e293b')

def main():
    fig, ax = plt.subplots(figsize=(11, 7.2), dpi=180)
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 7.2)
    ax.axis('off')

    ax.text(5.5, 6.85, "Diagrama de Flujo del Algoritmo de Booth para Multiplicación Binaria con Signo",
            ha='center', va='center', fontsize=13, fontweight='bold', color='#0f172a')

    # Start & Initialization
    box(ax, 5.5, 6.1, 5.6, 0.75,
        "Inicio / Inicialización (n bits):\nA ← 00...0,   Q ← Multiplicador,   M ← Multiplicando\n$Q_{-1}$ ← 0,   Contador ← n",
        bg="#dbeafe", border="#2563eb", fontsize=9.2)

    arrow(ax, 5.5, 5.72, 5.5, 5.05)

    # Decision on (Q_0, Q_-1)
    diamond(ax, 5.5, 4.45, 3.2, 1.15, "Evaluar par\n$(Q_0, Q_{-1})$", bg="#fef3c7", border="#d97706", fontsize=10)

    # Three branches: (1,0), (0,0)/(1,1), (0,1)
    # Left branch: (1,0) -> A = A - M
    ax.plot([3.9, 2.2, 2.2], [4.45, 4.45, 3.65], color='#334155', lw=1.7)
    ax.annotate('', xy=(2.2, 3.6), xytext=(2.2, 3.7), arrowprops=dict(arrowstyle='->', lw=1.7, color='#334155'))
    ax.text(3.0, 4.65, "$(Q_0, Q_{-1}) = (1, 0)$", ha='center', va='center', fontsize=9, fontweight='bold', color='#dc2626')
    box(ax, 2.2, 3.2, 2.7, 0.7, "Restar M:\n" + r"$A \leftarrow A + (-M)$", bg="#fee2e2", border="#dc2626")

    # Center branch: (0,0) or (1,1) -> No operation
    arrow(ax, 5.5, 3.87, 5.5, 2.55, "$(0, 0)$ ó $(1, 1)$\n(Sin suma)")

    # Right branch: (0,1) -> A = A + M
    ax.plot([7.1, 8.8, 8.8], [4.45, 4.45, 3.65], color='#334155', lw=1.7)
    ax.annotate('', xy=(8.8, 3.6), xytext=(8.8, 3.7), arrowprops=dict(arrowstyle='->', lw=1.7, color='#334155'))
    ax.text(8.0, 4.65, "$(Q_0, Q_{-1}) = (0, 1)$", ha='center', va='center', fontsize=9, fontweight='bold', color='#16a34a')
    box(ax, 8.8, 3.2, 2.7, 0.7, "Sumar M:\n" + r"$A \leftarrow A + M$", bg="#dcfce7", border="#16a34a")

    # Merge into ASD
    ax.plot([2.2, 2.2, 4.1], [2.85, 2.15, 2.15], color='#334155', lw=1.7)
    ax.plot([8.8, 8.8, 6.9], [2.85, 2.15, 2.15], color='#334155', lw=1.7)

    box(ax, 5.5, 2.15, 4.8, 0.75,
        "Desplazamiento Aritmético a la Derecha (ASD)\nde $[A, Q, Q_{-1}]$ (conservando bit de signo $A_{n-1}$)\nContador ← Contador - 1",
        bg="#f3e8ff", border="#7c3aed", fontsize=9)

    arrow(ax, 5.5, 1.77, 5.5, 1.25)

    diamond(ax, 5.5, 0.85, 2.6, 0.75, "¿Contador = 0?", bg="#fef3c7", border="#d97706", fontsize=9.5)

    # Loop back No
    ax.plot([4.2, 0.55, 0.55, 5.5], [0.85, 0.85, 5.35, 5.35], color='#334155', lw=1.6, linestyle='--')
    ax.annotate('', xy=(5.5, 5.1), xytext=(5.5, 5.35), arrowprops=dict(arrowstyle='->', lw=1.6, color='#334155'))
    ax.text(2.4, 1.02, "No (Siguiente ciclo)", ha='center', va='center', fontsize=9, fontweight='bold', color='#475569')

    # Yes -> Finish
    arrow(ax, 6.8, 0.85, 8.1, 0.85, "Sí")
    box(ax, 9.35, 0.85, 2.3, 0.7, "Fin:\nProducto en $[A, Q]$\n(2n bits)", bg="#dcfce7", border="#15803d", fontsize=9.2)

    plt.tight_layout()
    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "flujo-algoritmo-booth-multiplicacion.png")
    plt.savefig(out_path, dpi=180, bbox_inches='tight', facecolor='white')
    plt.close()

if __name__ == "__main__":
    main()
