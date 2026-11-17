import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_box(ax, x, y, w, h, title, subtitle, bg, border):
    rect = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.08",
                                  facecolor=bg, edgecolor=border, linewidth=2)
    ax.add_patch(rect)
    ax.text(x + w/2, y + h*0.62, title, ha='center', va='center',
            fontsize=11, fontweight='bold', color='#0f172a')
    if subtitle:
        ax.text(x + w/2, y + h*0.28, subtitle, ha='center', va='center',
                fontsize=9, color='#334155')

def main():
    fig, ax = plt.subplots(figsize=(11, 6.2), dpi=180)
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 6.2)
    ax.axis('off')

    ax.text(5.5, 5.85, "Mapa General de Conversiones entre Sistemas Numéricos",
            ha='center', va='center', fontsize=14, fontweight='bold', color='#0f172a')

    # Top row: General method (Base X -> Base 10 -> Base W)
    ax.text(5.5, 5.35, "1. Método General (Válido para cualesquiera bases X y W)",
            ha='center', va='center', fontsize=11, fontweight='bold', color='#1d4ed8')

    draw_box(ax, 0.6, 3.8, 2.5, 1.15, "Sistema Base X", r"$N_{(X)} = d_n\dots d_0 . d_{-1}\dots d_{-k}$", "#dbeafe", "#2563eb")
    draw_box(ax, 4.25, 3.8, 2.5, 1.15, "Sistema Decimal", r"$N_{(10)}$ (Base 10 intermedia)", "#fef3c7", "#d97706")
    draw_box(ax, 7.9, 3.8, 2.5, 1.15, "Sistema Base W", r"$N_{(W)}$ (Resultado final)", "#dcfce7", "#16a34a")

    # Arrows for General Method
    ax.annotate('', xy=(4.2, 4.38), xytext=(3.15, 4.38),
                arrowprops=dict(arrowstyle='->', lw=2.2, color='#1e40af'))
    ax.text(3.67, 4.78, "Notación\nExponencial", ha='center', va='center', fontsize=9, fontweight='bold', color='#1e40af')
    ax.text(3.67, 4.02, r"$\sum d_i \cdot X^i$", ha='center', va='center', fontsize=9.5, color='#334155')

    ax.annotate('', xy=(7.85, 4.38), xytext=(6.8, 4.38),
                arrowprops=dict(arrowstyle='->', lw=2.2, color='#15803d'))
    ax.text(7.32, 4.82, "Enteros: ÷ W\nFracción: × W", ha='center', va='center', fontsize=8.8, fontweight='bold', color='#15803d')
    ax.text(7.32, 3.98, "(Restos / Enteros)", ha='center', va='center', fontsize=8.5, color='#334155')

    # Divider line
    ax.plot([0.5, 10.5], [3.25, 3.25], linestyle='--', color='#94a3b8', linewidth=1.2)

    # Bottom row: Direct method (Octal <-> Binary <-> Hexadecimal)
    ax.text(5.5, 2.9, "2. Conversión Directa por Agrupación de Bits (Potencias de 2: $8 = 2^3$, $16 = 2^4$)",
            ha='center', va='center', fontsize=11, fontweight='bold', color='#7c3aed')

    draw_box(ax, 0.6, 1.1, 2.5, 1.2, "Sistema Octal", "Base 8 (Dígitos 0–7)\n1 dígito octal = 3 bits", "#f3e8ff", "#9333ea")
    draw_box(ax, 4.25, 1.1, 2.5, 1.2, "Sistema Binario", "Base 2 (Bits 0 y 1)\nPuente directo sin aritmética", "#e0f2fe", "#0284c7")
    draw_box(ax, 7.9, 1.1, 2.5, 1.2, "Sistema Hexadecimal", "Base 16 (0–9, A–F)\n1 dígito hex = 4 bits", "#fce7f3", "#db2777")

    # Bidirectional arrows
    ax.annotate('', xy=(4.2, 1.7), xytext=(3.15, 1.7),
                arrowprops=dict(arrowstyle='<->', lw=2.2, color='#7e22ce'))
    ax.text(3.67, 2.08, "Bloques de\n3 bits", ha='center', va='center', fontsize=9.5, fontweight='bold', color='#7e22ce')

    ax.annotate('', xy=(7.85, 1.7), xytext=(6.8, 1.7),
                arrowprops=dict(arrowstyle='<->', lw=2.2, color='#be185d'))
    ax.text(7.32, 2.08, "Bloques de\n4 bits", ha='center', va='center', fontsize=9.5, fontweight='bold', color='#be185d')

    # Footer note
    ax.text(5.5, 0.45, "Nota: Para convertir directamente entre Octal (base 8) y Hexadecimal (base 16), se pasa primero a Binario\ny luego se reagrupan los bits (de 3 en 3 hacia 4 en 4, o viceversa) a partir del punto radical.",
            ha='center', va='center', fontsize=9.2, style='italic', color='#475569',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#f8fafc', edgecolor='#cbd5e1'))

    plt.tight_layout()
    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "diagrama-conversiones-sistemas.png")
    plt.savefig(out_path, dpi=180, bbox_inches='tight', facecolor='white')
    plt.close()

if __name__ == "__main__":
    main()
