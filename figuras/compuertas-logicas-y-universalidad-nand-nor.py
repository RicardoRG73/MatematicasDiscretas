import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.path import Path


def draw_and_gate(ax, cx, cy, w=0.9, h=0.6, bubble=False, color='#1d4ed8', bg='#dbeafe'):
    x0 = cx - w / 2
    y0 = cy - h / 2
    # Left rectangle + right semicircle
    verts = [
        (x0, y0),
        (x0 + w * 0.5, y0),
    ]
    codes = [Path.MOVETO, Path.LINETO]
    theta = np.linspace(-np.pi / 2, np.pi / 2, 30)
    r = h / 2
    for t in theta[1:]:
        verts.append((x0 + w * 0.5 + r * np.cos(t), cy + r * np.sin(t)))
        codes.append(Path.LINETO)
    verts.append((x0, y0 + h))
    codes.append(Path.LINETO)
    verts.append((x0, y0))
    codes.append(Path.CLOSEPOLY)
    path = Path(verts, codes)
    ax.add_patch(patches.PathPatch(path, facecolor=bg, edgecolor=color, linewidth=1.8))

    # Input lines
    ax.plot([x0 - 0.32, x0], [cy + 0.15, cy + 0.15], color='#334155', linewidth=1.6)
    ax.plot([x0 - 0.32, x0], [cy - 0.15, cy - 0.15], color='#334155', linewidth=1.6)
    out_x = x0 + w * 0.5 + r
    if bubble:
        b_r = 0.065
        ax.add_patch(patches.Circle((out_x + b_r, cy), b_r, facecolor='white', edgecolor=color, linewidth=1.8, zorder=4))
        ax.plot([out_x + 2 * b_r, out_x + 2 * b_r + 0.28], [cy, cy], color='#334155', linewidth=1.6)
    else:
        ax.plot([out_x, out_x + 0.32], [cy, cy], color='#334155', linewidth=1.6)


def draw_or_gate(ax, cx, cy, w=0.95, h=0.6, bubble=False, xor=False, color='#047857', bg='#d1fae5'):
    x0 = cx - w / 2
    y0 = cy - h / 2
    t = np.linspace(0, 1, 25)
    # Bottom curve
    bx = x0 + w * t
    by = y0 + (h / 2) * (t ** 2.1)
    # Top curve
    tx = x0 + w * (1 - t)
    ty = y0 + h - (h / 2) * ((1 - t) ** 2.1)
    # Back curve
    s = np.linspace(1, -1, 25)
    back_x = x0 + 0.16 * (1 - s ** 2)
    back_y = cy + (h / 2) * s

    verts = list(zip(bx, by)) + list(zip(tx, ty)) + list(zip(back_x, back_y)) + [(bx[0], by[0])]
    codes = [Path.MOVETO] + [Path.LINETO] * (len(verts) - 2) + [Path.CLOSEPOLY]
    ax.add_patch(patches.PathPatch(Path(verts, codes), facecolor=bg, edgecolor=color, linewidth=1.8))

    if xor:
        xor_x = back_x - 0.11
        ax.plot(xor_x, back_y, color=color, linewidth=1.8)
        in_end = x0 - 0.04
    else:
        in_end = x0 + 0.11

    ax.plot([x0 - 0.34, in_end], [cy + 0.15, cy + 0.15], color='#334155', linewidth=1.6)
    ax.plot([x0 - 0.34, in_end], [cy - 0.15, cy - 0.15], color='#334155', linewidth=1.6)

    out_x = x0 + w
    if bubble:
        b_r = 0.065
        ax.add_patch(patches.Circle((out_x + b_r, cy), b_r, facecolor='white', edgecolor=color, linewidth=1.8, zorder=4))
        ax.plot([out_x + 2 * b_r, out_x + 2 * b_r + 0.26], [cy, cy], color='#334155', linewidth=1.6)
    else:
        ax.plot([out_x, out_x + 0.32], [cy, cy], color='#334155', linewidth=1.6)


def draw_not_gate(ax, cx, cy, w=0.65, h=0.52, color='#b45309', bg='#fef3c7'):
    x0 = cx - w / 2
    verts = [(x0, cy - h / 2), (x0 + w, cy), (x0, cy + h / 2), (x0, cy - h / 2)]
    codes = [Path.MOVETO, Path.LINETO, Path.LINETO, Path.CLOSEPOLY]
    ax.add_patch(patches.PathPatch(Path(verts, codes), facecolor=bg, edgecolor=color, linewidth=1.8))
    b_r = 0.065
    ax.add_patch(patches.Circle((x0 + w + b_r, cy), b_r, facecolor='white', edgecolor=color, linewidth=1.8, zorder=4))
    ax.plot([x0 - 0.32, x0], [cy, cy], color='#334155', linewidth=1.6)
    ax.plot([x0 + w + 2 * b_r, x0 + w + 2 * b_r + 0.28], [cy, cy], color='#334155', linewidth=1.6)


def main():
    fig, ax = plt.subplots(figsize=(13.6, 8.2), dpi=180)
    ax.set_xlim(0, 13.6)
    ax.set_ylim(0, 8.2)
    ax.axis('off')

    # Main Title
    ax.text(
        6.8, 7.88,
        "Compuertas Lógicas Básicas y Compuestas, Tablas de Verdad y Universalidad NAND / NOR",
        ha='center', va='center', fontsize=13.5, fontweight='bold', color='#0f172a'
    )
    ax.text(
        6.8, 7.52,
        r"Estándar gráfico ANSI/IEEE   |   Las compuertas $\mathrm{NAND}$ y $\mathrm{NOR}$ son funcionalmente completas (universales)",
        ha='center', va='center', fontsize=9.8, color='#334155'
    )

    # Top Panel: Basic Gates (AND, OR, NOT, XOR)
    p_top = patches.FancyBboxPatch((0.25, 4.35), 8.25, 2.9, boxstyle="round,pad=0.06", facecolor='#f8fafc', edgecolor='#2563eb', linewidth=1.7)
    ax.add_patch(p_top)
    ax.text(4.37, 7.0, "1. Compuertas Lógicas Básicas (Tablas 5.2 y 5.3)", ha='center', va='center', fontsize=10.0, fontweight='bold', color='#1d4ed8')

    # 4 columns in top panel
    # 1) AND
    draw_and_gate(ax, 1.25, 5.95, bubble=False, color='#1d4ed8', bg='#dbeafe')
    ax.text(1.25, 6.52, "AND (Producto)", ha='center', va='center', fontsize=9.0, fontweight='bold', color='#1e3a8a')
    ax.text(1.25, 5.32, r"$F = A \cdot B = AB$", ha='center', va='center', fontsize=8.8, fontweight='bold', color='#0f172a')
    ax.text(1.25, 4.92, r"$F = 1$ sólo si $A=1, B=1$", ha='center', va='center', fontsize=7.9, color='#334155')
    ax.text(1.25, 4.58, r"Tabla: $[0, 0, 0, 1]$", ha='center', va='center', fontsize=8.0, fontweight='bold', color='#1d4ed8')

    # 2) OR
    draw_or_gate(ax, 3.35, 5.95, bubble=False, xor=False, color='#047857', bg='#d1fae5')
    ax.text(3.35, 6.52, "OR (Suma lógica)", ha='center', va='center', fontsize=9.0, fontweight='bold', color='#065f46')
    ax.text(3.35, 5.32, r"$F = A + B$", ha='center', va='center', fontsize=8.8, fontweight='bold', color='#0f172a')
    ax.text(3.35, 4.92, r"$F = 0$ sólo si $A=0, B=0$", ha='center', va='center', fontsize=7.9, color='#334155')
    ax.text(3.35, 4.58, r"Tabla: $[0, 1, 1, 1]$", ha='center', va='center', fontsize=8.0, fontweight='bold', color='#047857')

    # 3) NOT
    draw_not_gate(ax, 5.35, 5.95, color='#b45309', bg='#fef3c7')
    ax.text(5.35, 6.52, "NOT (Inversor)", ha='center', va='center', fontsize=9.0, fontweight='bold', color='#92400e')
    ax.text(5.35, 5.32, r"$F = A'$", ha='center', va='center', fontsize=8.8, fontweight='bold', color='#0f172a')
    ax.text(5.35, 4.92, r"Invierte el bit ($0 \leftrightarrow 1$)", ha='center', va='center', fontsize=7.9, color='#334155')
    ax.text(5.35, 4.58, r"Tabla: $[1, 0]$", ha='center', va='center', fontsize=8.0, fontweight='bold', color='#b45309')

    # 4) XOR
    draw_or_gate(ax, 7.35, 5.95, bubble=False, xor=True, color='#7e22ce', bg='#f3e8ff')
    ax.text(7.35, 6.52, "XOR (OR Exclusivo)", ha='center', va='center', fontsize=9.0, fontweight='bold', color='#6b21a8')
    ax.text(7.35, 5.32, r"$F = A \oplus B = A'B + AB'$", ha='center', va='center', fontsize=8.5, fontweight='bold', color='#0f172a')
    ax.text(7.35, 4.92, r"$F = 1$ cuando $A \neq B$", ha='center', va='center', fontsize=7.9, color='#334155')
    ax.text(7.35, 4.58, r"Tabla: $[0, 1, 1, 0]$", ha='center', va='center', fontsize=8.0, fontweight='bold', color='#7e22ce')

    # Bottom-Left Panel: Compound Gates (NAND, NOR, XNOR)
    p_bot = patches.FancyBboxPatch((0.25, 0.3), 8.25, 3.8, boxstyle="round,pad=0.06", facecolor='#f8fafc', edgecolor='#be123c', linewidth=1.7)
    ax.add_patch(p_bot)
    ax.text(4.37, 3.84, "2. Compuertas Compuestas (NAND, NOR, XNOR) y Tabla de Verdad Comparativa", ha='center', va='center', fontsize=9.8, fontweight='bold', color='#be123c')

    # NAND
    draw_and_gate(ax, 1.35, 2.95, bubble=True, color='#be123c', bg='#ffe4e6')
    ax.text(1.35, 3.45, "NAND (NOT-AND)", ha='center', va='center', fontsize=8.8, fontweight='bold', color='#9f1239')
    ax.text(1.35, 2.38, r"$F = (AB)' = A' + B'$", ha='center', va='center', fontsize=8.4, fontweight='bold', color='#0f172a')

    # NOR
    draw_or_gate(ax, 3.65, 2.95, bubble=True, xor=False, color='#0f766e', bg='#ccfbf1')
    ax.text(3.65, 3.45, "NOR (NOT-OR)", ha='center', va='center', fontsize=8.8, fontweight='bold', color='#115e59')
    ax.text(3.65, 2.38, r"$F = (A+B)' = A'B'$", ha='center', va='center', fontsize=8.4, fontweight='bold', color='#0f172a')

    # XNOR
    draw_or_gate(ax, 6.25, 2.95, bubble=True, xor=True, color='#4338ca', bg='#e0e7ff')
    ax.text(6.25, 3.45, "XNOR (Equivalencia)", ha='center', va='center', fontsize=8.8, fontweight='bold', color='#3730a3')
    ax.text(6.25, 2.38, r"$F = (A \oplus B)' = AB + A'B'$", ha='center', va='center', fontsize=8.4, fontweight='bold', color='#0f172a')

    # Master Truth Table inside Bottom-Left Panel
    th_cols = ["$A$", "$B$", "$A'$", "AND", "OR", "XOR", "NAND", "NOR", "XNOR"]
    th_x = [0.75, 1.35, 2.05, 2.85, 3.7, 4.55, 5.5, 6.5, 7.55]
    ax.plot([0.45, 8.2], [1.85, 1.85], color='#64748b', linewidth=1.1)
    for cx, ht in zip(th_x, th_cols):
        ax.text(cx, 2.0, ht, ha='center', va='center', fontsize=8.4, fontweight='bold', color='#1e293b')

    t_rows = [
        ["0", "0", "1", "0", "0", "0", "1", "1", "1"],
        ["0", "1", "1", "0", "1", "1", "1", "0", "0"],
        ["1", "0", "0", "0", "1", "1", "1", "0", "0"],
        ["1", "1", "0", "1", "1", "0", "0", "0", "1"],
    ]
    for r_i, r_vals in enumerate(t_rows):
        ry = 1.62 - r_i * 0.31
        if r_i % 2 == 1:
            ax.add_patch(patches.Rectangle((0.45, ry - 0.14), 7.75, 0.28, facecolor='#e2e8f0', alpha=0.45, edgecolor='none'))
        for c_i, (cx, val) in enumerate(zip(th_x, r_vals)):
            col_c = '#1d4ed8' if (val == '1' and c_i >= 2) else ('#0f172a' if c_i < 2 else '#64748b')
            ax.text(cx, ry, val, ha='center', va='center', fontsize=8.4, fontweight='bold' if c_i >= 2 else 'normal', color=col_c)

    # Right Panel: Universalidad de NAND y NOR (Problemas 5.9 y 5.10 Jiménez Murillo)
    p_right = patches.FancyBboxPatch((8.75, 0.3), 4.6, 6.95, boxstyle="round,pad=0.06", facecolor='#ecfdf5', edgecolor='#059669', linewidth=1.8)
    ax.add_patch(p_right)
    ax.text(11.05, 6.98, "3. Universalidad de Compuertas", ha='center', va='center', fontsize=10.2, fontweight='bold', color='#047857')
    ax.text(11.05, 6.68, "Construcción de toda operación con NAND o NOR", ha='center', va='center', fontsize=8.4, color='#065f46')
    ax.plot([8.9, 13.2], [6.48, 6.48], color='#059669', linewidth=1.0, alpha=0.65)

    # Section A: Using ONLY NAND
    ax.text(11.05, 6.22, "A) Exclusivamente con Compuertas NAND:", ha='center', va='center', fontsize=8.9, fontweight='bold', color='#be123c')
    nand_equivs = [
        (r"1. Inversor ($\mathrm{NOT}$):", r"$A' = (A \cdot A)'$  (1 compuerta NAND)"),
        (r"2. Producto ($\mathrm{AND}$):", r"$AB = [(AB)']'$  (2 compuertas NAND)"),
        (r"3. Suma ($\mathrm{OR}$):", r"$A + B = (A' \cdot B')' = [(AA)'(BB)']'$  (3 NAND)"),
        (r"4. $\mathrm{NOR}$:", r"$(A+B)' = [((AA)'(BB)')']'$  (4 NAND)"),
        (r"5. $\mathrm{XOR}$:", r"$A \oplus B = [(A(AB)')' \cdot (B(AB)')']'$  (4 NAND)"),
    ]
    for idx, (op_title, eq_str) in enumerate(nand_equivs):
        ry = 5.84 - idx * 0.50
        ax.add_patch(patches.Rectangle((8.92, ry - 0.21), 4.26, 0.42, facecolor='#ffffff', alpha=0.85, edgecolor='#cbd5e1', linewidth=0.9))
        ax.text(9.02, ry + 0.08, op_title, ha='left', va='center', fontsize=8.1, fontweight='bold', color='#9f1239')
        ax.text(9.02, ry - 0.10, eq_str, ha='left', va='center', fontsize=7.95, color='#1e293b')

    # Section B: Using ONLY NOR
    ax.text(11.05, 3.25, "B) Exclusivamente con Compuertas NOR:", ha='center', va='center', fontsize=8.9, fontweight='bold', color='#0f766e')
    nor_equivs = [
        (r"1. Inversor ($\mathrm{NOT}$):", r"$A' = (A + A)'$  (1 compuerta NOR)"),
        (r"2. Suma ($\mathrm{OR}$):", r"$A + B = [(A + B)']'$  (2 compuertas NOR)"),
        (r"3. Producto ($\mathrm{AND}$):", r"$AB = (A' + B')' = [(A+A)' + (B+B)']'$  (3 NOR)"),
        (r"4. $\mathrm{NAND}$:", r"$(AB)' = [((A+A)' + (B+B)')']'$  (4 NOR)"),
        (r"5. $\mathrm{XNOR}$:", r"$(A \oplus B)' = [(A+(A+B)')' + (B+(A+B)')']'$"),
    ]
    for idx, (op_title, eq_str) in enumerate(nor_equivs):
        ry = 2.86 - idx * 0.50
        ax.add_patch(patches.Rectangle((8.92, ry - 0.21), 4.26, 0.42, facecolor='#ffffff', alpha=0.85, edgecolor='#cbd5e1', linewidth=0.9))
        ax.text(9.02, ry + 0.08, op_title, ha='left', va='center', fontsize=8.1, fontweight='bold', color='#115e59')
        ax.text(9.02, ry - 0.10, eq_str, ha='left', va='center', fontsize=7.9, color='#1e293b')

    ax.text(
        11.05, 0.48,
        r"Regla práctica: SOP $\longrightarrow$ 2 niveles NAND;   POS $\longrightarrow$ 2 niveles NOR.",
        ha='center', va='center', fontsize=8.0, fontweight='bold', color='#047857'
    )

    plt.tight_layout()
    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "compuertas-logicas-y-universalidad-nand-nor.png")
    plt.savefig(out_path, dpi=180, bbox_inches='tight', facecolor='white')
    plt.close()


if __name__ == "__main__":
    main()
