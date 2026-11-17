import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def box(ax, x, y, w, h, text, bg="#e0f2fe", border="#0284c7", fontsize=8.8):
    p = patches.FancyBboxPatch((x - w/2, y - h/2), w, h, boxstyle="round,pad=0.05",
                               facecolor=bg, edgecolor=border, linewidth=1.6)
    ax.add_patch(p)
    ax.text(x, y, text, ha='center', va='center', fontsize=fontsize, fontweight='bold', color='#0f172a')

def main():
    fig, ax = plt.subplots(figsize=(11.5, 6.4), dpi=180)
    ax.set_xlim(0, 11.5)
    ax.set_ylim(0, 6.4)
    ax.axis('off')

    ax.text(5.75, 6.05, "Comparación de los Algoritmos de División Binaria (Registros A, Q, M)",
            ha='center', va='center', fontsize=13, fontweight='bold', color='#0f172a')

    # Left panel: Restoring Division
    ax.text(2.8, 5.5, "A) División con Restauración", ha='center', va='center',
            fontsize=11.5, fontweight='bold', color='#1d4ed8')

    box(ax, 2.8, 4.85, 4.6, 0.65, "1. Inicializar: A ← 0, Q ← Dividendo, M ← Divisor, Cont ← n",
        bg="#dbeafe", border="#2563eb")
    ax.annotate('', xy=(2.8, 4.15), xytext=(2.8, 4.5), arrowprops=dict(arrowstyle='->', lw=1.5))

    box(ax, 2.8, 3.8, 4.6, 0.6, "2. Desplazar par [A, Q] 1 bit a la izquierda\nRestar divisor:  A ← A - M",
        bg="#eff6ff", border="#2563eb")
    ax.annotate('', xy=(2.8, 3.1), xytext=(2.8, 3.48), arrowprops=dict(arrowstyle='->', lw=1.5))

    box(ax, 2.8, 2.6, 4.6, 0.85,
        "3. ¿Signo de A?\n" + r"• Si A ≥ 0 (MSB=0):  $Q_0 \leftarrow 1$ (No se restaura)" + "\n" + r"• Si A < 0 (MSB=1):  $Q_0 \leftarrow 0$ y Restaurar $A \leftarrow A + M$",
        bg="#fef3c7", border="#d97706")
    ax.annotate('', xy=(2.8, 1.75), xytext=(2.8, 2.15), arrowprops=dict(arrowstyle='->', lw=1.5))

    box(ax, 2.8, 1.4, 4.6, 0.55, "4. Decrementar Cont. Repetir pasos 2–3 hasta Cont = 0",
        bg="#f3e8ff", border="#7c3aed")
    ax.annotate('', xy=(2.8, 0.8), xytext=(2.8, 1.1), arrowprops=dict(arrowstyle='->', lw=1.5))

    box(ax, 2.8, 0.45, 4.6, 0.55, "Resultado: Cociente en Q,  Residuo en A",
        bg="#dcfce7", border="#15803d")

    # Vertical separator
    ax.plot([5.75, 5.75], [0.2, 5.65], linestyle='--', color='#94a3b8', lw=1.5)

    # Right panel: Non-Restoring Division
    ax.text(8.7, 5.5, "B) División sin Restauración (Estilo Booth)", ha='center', va='center',
            fontsize=11.5, fontweight='bold', color='#be185d')

    box(ax, 8.7, 4.85, 4.6, 0.65, "1. Inicializar: A ← 0, Q ← Dividendo, M ← Divisor, Cont ← n",
        bg="#fce7f3", border="#db2777")
    ax.annotate('', xy=(8.7, 4.15), xytext=(8.7, 4.5), arrowprops=dict(arrowstyle='->', lw=1.5))

    box(ax, 8.7, 3.75, 4.6, 0.72,
        "2. Según el signo previo de A, desplazar [A, Q] a la izq.:\n• Si A ≥ 0:  Desplazar y Restar  (A ← A - M)\n• Si A < 0:  Desplazar y Sumar   (A ← A + M)",
        bg="#fdf2f8", border="#db2777")
    ax.annotate('', xy=(8.7, 3.05), xytext=(8.7, 3.38), arrowprops=dict(arrowstyle='->', lw=1.5))

    box(ax, 8.7, 2.6, 4.6, 0.75,
        "3. Evaluar nuevo signo de A (sin restaurar):\n" + r"• Si A ≥ 0 (MSB=0):  $Q_0 \leftarrow 1$" + "\n" + r"• Si A < 0 (MSB=1):  $Q_0 \leftarrow 0$",
        bg="#fef3c7", border="#d97706")
    ax.annotate('', xy=(8.7, 1.85), xytext=(8.7, 2.2), arrowprops=dict(arrowstyle='->', lw=1.5))

    box(ax, 8.7, 1.4, 4.6, 0.72,
        "4. Repetir n ciclos. Al finalizar los n ciclos:\n" + r"• Si A < 0, hacer ajuste final único: $A \leftarrow A + M$",
        bg="#f3e8ff", border="#7c3aed")
    ax.annotate('', xy=(8.7, 0.8), xytext=(8.7, 1.02), arrowprops=dict(arrowstyle='->', lw=1.5))

    box(ax, 8.7, 0.45, 4.6, 0.55, "Resultado: Cociente en Q,  Residuo corregido en A",
        bg="#dcfce7", border="#15803d")

    plt.tight_layout()
    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "flujo-division-binaria-restauracion.png")
    plt.savefig(out_path, dpi=180, bbox_inches='tight', facecolor='white')
    plt.close()

if __name__ == "__main__":
    main()
