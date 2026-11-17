import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.path import Path


def draw_gate_and(ax, cx, cy, w=0.78, h=0.52, bubble=False, color='#1d4ed8', bg='#dbeafe'):
    x0 = cx - w / 2
    y0 = cy - h / 2
    verts = [(x0, y0), (x0 + w * 0.5, y0)]
    codes = [Path.MOVETO, Path.LINETO]
    theta = np.linspace(-np.pi / 2, np.pi / 2, 25)
    r = h / 2
    for t in theta[1:]:
        verts.append((x0 + w * 0.5 + r * np.cos(t), cy + r * np.sin(t)))
        codes.append(Path.LINETO)
    verts.extend([(x0, y0 + h), (x0, y0)])
    codes.extend([Path.LINETO, Path.CLOSEPOLY])
    ax.add_patch(patches.PathPatch(Path(verts, codes), facecolor=bg, edgecolor=color, linewidth=1.7, zorder=3))
    out_x = x0 + w * 0.5 + r
    if bubble:
        b_r = 0.055
        ax.add_patch(patches.Circle((out_x + b_r, cy), b_r, facecolor='white', edgecolor=color, linewidth=1.7, zorder=4))
        return x0, out_x + 2 * b_r
    return x0, out_x


def draw_gate_or(ax, cx, cy, w=0.82, h=0.52, xor=False, color='#047857', bg='#d1fae5'):
    x0 = cx - w / 2
    y0 = cy - h / 2
    t = np.linspace(0, 1, 22)
    bx = x0 + w * t
    by = y0 + (h / 2) * (t ** 2.1)
    tx = x0 + w * (1 - t)
    ty = y0 + h - (h / 2) * ((1 - t) ** 2.1)
    s = np.linspace(1, -1, 22)
    back_x = x0 + 0.14 * (1 - s ** 2)
    back_y = cy + (h / 2) * s
    verts = list(zip(bx, by)) + list(zip(tx, ty)) + list(zip(back_x, back_y)) + [(bx[0], by[0])]
    codes = [Path.MOVETO] + [Path.LINETO] * (len(verts) - 2) + [Path.CLOSEPOLY]
    ax.add_patch(patches.PathPatch(Path(verts, codes), facecolor=bg, edgecolor=color, linewidth=1.7, zorder=3))
    if xor:
        ax.plot(back_x - 0.09, back_y, color=color, linewidth=1.7, zorder=3)
        return x0 - 0.04, x0 + w
    return x0 + 0.09, x0 + w


def draw_gate_not(ax, cx, cy, w=0.45, h=0.38, color='#b45309', bg='#fef3c7'):
    x0 = cx - w / 2
    verts = [(x0, cy - h / 2), (x0 + w, cy), (x0, cy + h / 2), (x0, cy - h / 2)]
    codes = [Path.MOVETO, Path.LINETO, Path.LINETO, Path.CLOSEPOLY]
    ax.add_patch(patches.PathPatch(Path(verts, codes), facecolor=bg, edgecolor=color, linewidth=1.6, zorder=3))
    b_r = 0.05
    ax.add_patch(patches.Circle((x0 + w + b_r, cy), b_r, facecolor='white', edgecolor=color, linewidth=1.6, zorder=4))
    return x0, x0 + w + 2 * b_r


def main():
    fig, ax = plt.subplots(figsize=(13.6, 8.2), dpi=180)
    ax.set_xlim(0, 13.6)
    ax.set_ylim(0, 8.2)
    ax.axis('off')

    # Main Title
    ax.text(
        6.8, 7.88,
        "Representación de Expresiones Booleanas en Circuitos Lógicos y Sumadores Binarios (ALU)",
        ha='center', va='center', fontsize=13.5, fontweight='bold', color='#0f172a'
    )
    ax.text(
        6.8, 7.52,
        r"Implementación de dos niveles ($\mathrm{AND\text{-}OR}$ vs. $\mathrm{NAND\text{-}NAND}$) y bloques aritméticos fundamentales (Semisumador y Sumador Completo)",
        ha='center', va='center', fontsize=9.6, color='#334155'
    )

    # Top-Left Panel: Circuito con compuertas básicas AND-OR-NOT para F = AC'D' + BC (Ejemplo 5.14f)
    p1 = patches.FancyBboxPatch((0.25, 4.15), 6.45, 3.1, boxstyle="round,pad=0.06", facecolor='#f8fafc', edgecolor='#2563eb', linewidth=1.7)
    ax.add_patch(p1)
    ax.text(3.47, 7.0, r"1. Circuito Básico $\mathrm{AND\text{-}OR\text{-}NOT}$ para $F = AC'D' + BC$", ha='center', va='center', fontsize=9.8, fontweight='bold', color='#1d4ed8')

    # Inputs A, C, D, B
    in_x = 0.65
    ax.text(in_x - 0.15, 6.35, r"$A$", ha='right', va='center', fontsize=9.5, fontweight='bold', color='#0f172a')
    ax.text(in_x - 0.15, 5.95, r"$C$", ha='right', va='center', fontsize=9.5, fontweight='bold', color='#0f172a')
    ax.text(in_x - 0.15, 5.50, r"$D$", ha='right', va='center', fontsize=9.5, fontweight='bold', color='#0f172a')
    ax.text(in_x - 0.15, 4.85, r"$B$", ha='right', va='center', fontsize=9.5, fontweight='bold', color='#0f172a')

    # NOT gates for C' and D'
    n1_in, n1_out = draw_gate_not(ax, 1.55, 5.95)
    n2_in, n2_out = draw_gate_not(ax, 1.55, 5.50)
    ax.plot([in_x, n1_in], [5.95, 5.95], color='#334155', linewidth=1.6)
    ax.plot([in_x, n2_in], [5.50, 5.50], color='#334155', linewidth=1.6)
    # Tap from C before NOT gate down to lower AND gate
    ax.plot([1.02, 1.02], [5.95, 5.10], color='#334155', linewidth=1.5)
    ax.scatter([1.02], [5.95], color='#0f172a', s=18, zorder=5)
    ax.text(2.02, 6.13, r"$C'$", ha='center', va='center', fontsize=8.2, color='#b45309', fontweight='bold')
    ax.text(2.02, 5.68, r"$D'$", ha='center', va='center', fontsize=8.2, color='#b45309', fontweight='bold')

    # Upper AND gate (AC'D') and Lower AND gate (BC)
    a1_in, a1_out = draw_gate_and(ax, 2.95, 5.95, w=0.82, h=0.62)
    a2_in, a2_out = draw_gate_and(ax, 2.95, 4.98, w=0.82, h=0.52)
    # Wires to upper AND
    ax.plot([in_x, 2.25, 2.25, a1_in], [6.35, 6.35, 6.15, 6.15], color='#334155', linewidth=1.6)
    ax.plot([n1_out, a1_in], [5.95, 5.95], color='#334155', linewidth=1.6)
    ax.plot([n2_out, 2.25, 2.25, a1_in], [5.50, 5.50, 5.75, 5.75], color='#334155', linewidth=1.6)
    # Wires to lower AND
    ax.plot([1.02, a2_in], [5.10, 5.10], color='#334155', linewidth=1.6)
    ax.plot([in_x, a2_in], [4.85, 4.85], color='#334155', linewidth=1.6)

    ax.text(3.85, 6.15, r"$AC'D'$", ha='center', va='center', fontsize=8.5, fontweight='bold', color='#1d4ed8')
    ax.text(3.75, 4.78, r"$BC$", ha='center', va='center', fontsize=8.5, fontweight='bold', color='#1d4ed8')

    # Final OR gate
    or_in, or_out = draw_gate_or(ax, 4.75, 5.48, w=0.88, h=0.58)
    ax.plot([a1_out, 4.05, 4.05, or_in], [5.95, 5.95, 5.62, 5.62], color='#334155', linewidth=1.6)
    ax.plot([a2_out, 4.05, 4.05, or_in], [4.98, 4.98, 5.34, 5.34], color='#334155', linewidth=1.6)
    ax.plot([or_out, 5.55], [5.48, 5.48], color='#334155', linewidth=1.8)
    ax.text(5.65, 5.48, r"$F = AC'D' + BC$", ha='left', va='center', fontsize=9.2, fontweight='bold', color='#047857')

    ax.text(3.47, 4.38, r"Arquitectura de 2 niveles: 1er nivel compuertas $\mathrm{AND}$ $\rightarrow$ 2do nivel compuerta $\mathrm{OR}$", ha='center', va='center', fontsize=8.2, color='#334155')

    # Top-Right Panel: Circuito Equivalente SOLO con Compuertas NAND (Ejemplo 5.14g)
    p2 = patches.FancyBboxPatch((6.9, 4.15), 6.45, 3.1, boxstyle="round,pad=0.06", facecolor='#fff1f2', edgecolor='#be123c', linewidth=1.7)
    ax.add_patch(p2)
    ax.text(10.12, 7.0, r"2. Circuito Equivalente Exclusivamente con $\mathrm{NAND}$: $F = [(AC'D')'(BC)']'$", ha='center', va='center', fontsize=9.3, fontweight='bold', color='#be123c')

    in_x2 = 7.3
    ax.text(in_x2 - 0.12, 6.35, r"$A$", ha='right', va='center', fontsize=9.2, fontweight='bold', color='#0f172a')
    ax.text(in_x2 - 0.12, 5.95, r"$C$", ha='right', va='center', fontsize=9.2, fontweight='bold', color='#0f172a')
    ax.text(in_x2 - 0.12, 5.48, r"$D$", ha='right', va='center', fontsize=9.2, fontweight='bold', color='#0f172a')
    ax.text(in_x2 - 0.12, 4.85, r"$B$", ha='right', va='center', fontsize=9.2, fontweight='bold', color='#0f172a')

    # 1-input NANDs (acting as inverters) for C' and D'
    nd_c_in, nd_c_out = draw_gate_and(ax, 8.25, 5.95, w=0.58, h=0.38, bubble=True, color='#be123c', bg='#ffe4e6')
    nd_d_in, nd_d_out = draw_gate_and(ax, 8.25, 5.48, w=0.58, h=0.38, bubble=True, color='#be123c', bg='#ffe4e6')
    ax.plot([in_x2, nd_c_in], [5.95, 5.95], color='#334155', linewidth=1.6)
    ax.plot([in_x2, nd_d_in], [5.48, 5.48], color='#334155', linewidth=1.6)
    ax.plot([7.62, 7.62], [5.95, 5.10], color='#334155', linewidth=1.5)
    ax.scatter([7.62], [5.95], color='#0f172a', s=18, zorder=5)

    # First-level NANDs
    nd1_in, nd1_out = draw_gate_and(ax, 9.6, 5.95, w=0.78, h=0.60, bubble=True, color='#be123c', bg='#ffe4e6')
    nd2_in, nd2_out = draw_gate_and(ax, 9.6, 4.98, w=0.78, h=0.50, bubble=True, color='#be123c', bg='#ffe4e6')
    ax.plot([in_x2, 8.95, 8.95, nd1_in], [6.35, 6.35, 6.14, 6.14], color='#334155', linewidth=1.6)
    ax.plot([nd_c_out, nd1_in], [5.95, 5.95], color='#334155', linewidth=1.6)
    ax.plot([nd_d_out, 8.95, 8.95, nd1_in], [5.48, 5.48, 5.76, 5.76], color='#334155', linewidth=1.6)
    ax.plot([7.62, nd2_in], [5.10, 5.10], color='#334155', linewidth=1.6)
    ax.plot([in_x2, nd2_in], [4.85, 4.85], color='#334155', linewidth=1.6)

    ax.text(10.48, 6.18, r"$(AC'D')'$", ha='center', va='center', fontsize=8.0, fontweight='bold', color='#be123c')
    ax.text(10.42, 4.76, r"$(BC)'$", ha='center', va='center', fontsize=8.0, fontweight='bold', color='#be123c')

    # Second-level NAND
    nd3_in, nd3_out = draw_gate_and(ax, 11.4, 5.48, w=0.82, h=0.56, bubble=True, color='#be123c', bg='#ffe4e6')
    ax.plot([nd1_out, 10.75, 10.75, nd3_in], [5.95, 5.95, 5.62, 5.62], color='#334155', linewidth=1.6)
    ax.plot([nd2_out, 10.75, 10.75, nd3_in], [4.98, 4.98, 5.34, 5.34], color='#334155', linewidth=1.6)
    ax.plot([nd3_out, 12.15], [5.48, 5.48], color='#334155', linewidth=1.8)
    ax.text(12.22, 5.48, r"$F = AC'D' + BC$", ha='left', va='center', fontsize=8.8, fontweight='bold', color='#be123c')

    ax.text(10.12, 4.38, r"Por doble negación y De Morgan: $F = (F')' = [(AC'D' + BC)']' = [(AC'D')' \cdot (BC)']'$", ha='center', va='center', fontsize=8.1, color='#9f1239')

    # Bottom-Left Panel: Half Adder (Semisumador) - Johnsonbaugh Fig 11.5.8 / Epp Cap 2.5
    p3 = patches.FancyBboxPatch((0.25, 0.3), 5.65, 3.55, boxstyle="round,pad=0.06", facecolor='#ecfdf5', edgecolor='#059669', linewidth=1.7)
    ax.add_patch(p3)
    ax.text(3.07, 3.60, "3. Aplicación en la ALU: Semisumador (Half Adder)", ha='center', va='center', fontsize=9.8, fontweight='bold', color='#047857')
    ax.text(3.07, 3.30, r"Suma dos bits $x, y \in \{0, 1\}$ produciendo Suma ($S$) y Acarreo ($C$)", ha='center', va='center', fontsize=8.2, color='#334155')

    # Half adder diagram
    hx = 0.85
    ax.text(hx - 0.15, 2.65, r"$x$", ha='right', va='center', fontsize=9.5, fontweight='bold', color='#0f172a')
    ax.text(hx - 0.15, 2.25, r"$y$", ha='right', va='center', fontsize=9.5, fontweight='bold', color='#0f172a')
    xor_in, xor_out = draw_gate_or(ax, 2.25, 2.45, w=0.82, h=0.52, xor=True, color='#7e22ce', bg='#f3e8ff')
    ha_in, ha_out = draw_gate_and(ax, 2.25, 1.55, w=0.78, h=0.50, color='#1d4ed8', bg='#dbeafe')

    ax.plot([hx, xor_in], [2.60, 2.60], color='#334155', linewidth=1.6)
    ax.plot([hx, xor_in], [2.30, 2.30], color='#334155', linewidth=1.6)
    # Taps down to AND gate
    ax.plot([1.22, 1.22, ha_in], [2.60, 1.68, 1.68], color='#334155', linewidth=1.5)
    ax.plot([1.48, 1.48, ha_in], [2.30, 1.42, 1.42], color='#334155', linewidth=1.5)
    ax.scatter([1.22, 1.48], [2.60, 2.30], color='#0f172a', s=18, zorder=5)

    ax.plot([xor_out, 3.05], [2.45, 2.45], color='#334155', linewidth=1.7)
    ax.plot([ha_out, 3.05], [1.55, 1.55], color='#334155', linewidth=1.7)
    ax.text(3.12, 2.45, r"$S = x \oplus y = x'y + xy'$", ha='left', va='center', fontsize=8.4, fontweight='bold', color='#6b21a8')
    ax.text(3.12, 1.55, r"$C = x \cdot y$  (Acarreo)", ha='left', va='center', fontsize=8.4, fontweight='bold', color='#1d4ed8')

    # Mini truth table at bottom of p3
    ax.text(3.07, 0.92, r"Tabla del Semisumador:   $(0,0)\to CS=00,\;\; (0,1)\to 01,\;\; (1,0)\to 01,\;\; (1,1)\to 10_2$",
            ha='center', va='center', fontsize=8.2, fontweight='bold', color='#065f46')
    ax.text(3.07, 0.56, r"Minitérminos:  $S = \sum m(1, 2)$   y   $C = \sum m(3)$",
            ha='center', va='center', fontsize=8.2, color='#1e293b')

    # Bottom-Right Panel: Full Adder (Sumador Completo) - Johnsonbaugh Fig 11.5.9
    p4 = patches.FancyBboxPatch((6.15, 0.3), 7.2, 3.55, boxstyle="round,pad=0.06", facecolor='#fffbeb', edgecolor='#d97706', linewidth=1.7)
    ax.add_patch(p4)
    ax.text(9.75, 3.60, r"4. Sumador Completo (Full Adder) de 3 Bits ($x, y, c_{\mathrm{in}}$)", ha='center', va='center', fontsize=9.8, fontweight='bold', color='#b45309')
    ax.text(9.75, 3.30, r"Suma dos bits $x, y$ más el acarreo de entrada $c_{\mathrm{in}}$ de la columna anterior", ha='center', va='center', fontsize=8.2, color='#334155')

    # Equations and architecture summary box inside p4
    eq_box = patches.FancyBboxPatch((6.35, 1.55), 6.8, 1.52, boxstyle="round,pad=0.04", facecolor='#ffffff', edgecolor='#cbd5e1', linewidth=1.2)
    ax.add_patch(eq_box)
    fa_lines = [
        r"$\bullet$ Ecuación booleana del bit de Suma ($S$):   $S = x \oplus y \oplus c_{\mathrm{in}} = \sum m(1, 2, 4, 7)$",
        r"   ($S = 1$ cuando hay un número impar de entradas iguales a $1$).",
        r"$\bullet$ Ecuación booleana del Acarreo de Salida ($C_{\mathrm{out}}$):   $C_{\mathrm{out}} = \sum m(3, 5, 6, 7)$",
        r"   Simplificada por Karnaugh/Teoremas:   $C_{\mathrm{out}} = xy + xc_{\mathrm{in}} + yc_{\mathrm{in}} = xy + c_{\mathrm{in}}(x \oplus y)$"
    ]
    for idx, fl in enumerate(fa_lines):
        ry = 2.82 - idx * 0.32
        w_f = 'bold' if idx in (0, 3) else 'normal'
        c_f = '#92400e' if idx in (0, 3) else '#1e293b'
        ax.text(6.5, ry, fl, ha='left', va='center', fontsize=8.2, fontweight=w_f, color=c_f)

    # Block cascade diagram at bottom of p4 (2 Half Adders + 1 OR gate = 1 Full Adder)
    b1 = patches.FancyBboxPatch((6.6, 0.55), 1.75, 0.72, boxstyle="round,pad=0.03", facecolor='#dbeafe', edgecolor='#2563eb', linewidth=1.5)
    b2 = patches.FancyBboxPatch((9.0, 0.55), 1.75, 0.72, boxstyle="round,pad=0.03", facecolor='#dbeafe', edgecolor='#2563eb', linewidth=1.5)
    b3 = patches.FancyBboxPatch((11.35, 0.55), 1.5, 0.72, boxstyle="round,pad=0.03", facecolor='#d1fae5', edgecolor='#059669', linewidth=1.5)
    ax.add_patch(b1)
    ax.add_patch(b2)
    ax.add_patch(b3)
    ax.text(7.47, 0.91, "Semisumador 1\n" + r"$x, y \to (s_1, c_1)$", ha='center', va='center', fontsize=7.8, fontweight='bold', color='#1e3a8a')
    ax.text(9.87, 0.91, "Semisumador 2\n" + r"$s_1, c_{\mathrm{in}} \to (S, c_2)$", ha='center', va='center', fontsize=7.8, fontweight='bold', color='#1e3a8a')
    ax.text(12.1, 0.91, "Compuerta OR\n" + r"$C_{\mathrm{out}} = c_1 + c_2$", ha='center', va='center', fontsize=7.8, fontweight='bold', color='#065f46')
    ax.annotate("", xy=(8.98, 0.91), xytext=(8.38, 0.91), arrowprops=dict(arrowstyle="->", color='#334155', lw=1.6))
    ax.annotate("", xy=(11.33, 0.91), xytext=(10.78, 0.91), arrowprops=dict(arrowstyle="->", color='#334155', lw=1.6))

    plt.tight_layout()
    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "circuitos-combinatorios-y-sumadores-binarios.png")
    plt.savefig(out_path, dpi=180, bbox_inches='tight', facecolor='white')
    plt.close()


if __name__ == "__main__":
    main()
