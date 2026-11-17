import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def main():
    fig, ax = plt.subplots(figsize=(11, 5.2), dpi=180)
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 5.2)
    ax.axis('off')

    ax.text(5.5, 4.8, "Estándar IEEE 754 de Punto Flotante de Precisión Simple (32 bits)",
            ha='center', va='center', fontsize=13.5, fontweight='bold', color='#0f172a')
    ax.text(5.5, 4.35, r"Valor real representado:   $N = (-1)^{S} \times (1.\text{Mantisa})_{(2)} \times 2^{(E - 127)}$",
            ha='center', va='center', fontsize=11.5, color='#334155')

    # Sign box (1 bit)
    s_rect = patches.FancyBboxPatch((0.6, 2.55), 1.1, 1.05, boxstyle="round,pad=0.04",
                                    facecolor="#fee2e2", edgecolor="#dc2626", linewidth=2)
    ax.add_patch(s_rect)
    ax.text(1.15, 3.22, "Signo (S)", ha='center', va='center', fontsize=10.5, fontweight='bold', color='#991b1b')
    ax.text(1.15, 2.82, "1 bit\n(Bit 31)", ha='center', va='center', fontsize=9, color='#7f1d1d')

    # Exponent box (8 bits)
    e_rect = patches.FancyBboxPatch((1.85, 2.55), 2.85, 1.05, boxstyle="round,pad=0.04",
                                    facecolor="#dbeafe", edgecolor="#2563eb", linewidth=2)
    ax.add_patch(e_rect)
    ax.text(3.275, 3.22, "Exponente Sesgado (E)", ha='center', va='center', fontsize=10.5, fontweight='bold', color='#1e40af')
    ax.text(3.275, 2.82, "8 bits (Bits 30 a 23)\nExceso a 127 ($E = e + 127$)", ha='center', va='center', fontsize=9, color='#1e3a8a')

    # Mantissa box (23 bits)
    m_rect = patches.FancyBboxPatch((4.85, 2.55), 5.55, 1.05, boxstyle="round,pad=0.04",
                                    facecolor="#dcfce7", edgecolor="#16a34a", linewidth=2)
    ax.add_patch(m_rect)
    ax.text(7.625, 3.22, "Mantisa o Fracción Normalizada (M)", ha='center', va='center', fontsize=10.5, fontweight='bold', color='#166534')
    ax.text(7.625, 2.82, "23 bits (Bits 22 a 0)\nBit entero implícito: $1.M_{(2)}$", ha='center', va='center', fontsize=9, color='#14532d')

    # Concrete Example at the bottom: -13.625
    ax.text(5.5, 1.9, "Ejemplo: Representación de $-13.625_{(10)} = -1101.101_{(2)} = -1.101101_{(2)} \times 2^{3}$",
            ha='center', va='center', fontsize=10.8, fontweight='bold', color='#0f172a')

    # Values for -13.625
    ax.text(1.15, 1.15, "S = 1\n(Negativo)", ha='center', va='center', fontsize=9.5, fontweight='bold', color='#dc2626',
            bbox=dict(boxstyle='round,pad=0.25', facecolor='#fef2f2', edgecolor='#f87171'))
    ax.text(3.275, 1.15, "e = 3 → E = 3 + 127 = 130\n$10000010_{(2)}$", ha='center', va='center', fontsize=9.5, fontweight='bold', color='#1d4ed8',
            bbox=dict(boxstyle='round,pad=0.25', facecolor='#eff6ff', edgecolor='#60a5fa'))
    ax.text(7.625, 1.15, "M = 10110100000000000000000\n(parte fraccionaria tras el 1.)", ha='center', va='center', fontsize=9.5, fontweight='bold', color='#15803d',
            bbox=dict(boxstyle='round,pad=0.25', facecolor='#f0fdf4', edgecolor='#4ade80'))

    ax.text(5.5, 0.35, "Palabra de 32 bits en memoria:  1  10000010  10110100000000000000000  =  C15A0000 (en Hexadecimal)",
            ha='center', va='center', fontsize=9.8, fontweight='bold', color='#1e293b',
            bbox=dict(boxstyle='round,pad=0.25', facecolor='#f8fafc', edgecolor='#94a3b8'))

    plt.tight_layout()
    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "formato-ieee-754-punto-flotante.png")
    plt.savefig(out_path, dpi=180, bbox_inches='tight', facecolor='white')
    plt.close()

if __name__ == "__main__":
    main()
