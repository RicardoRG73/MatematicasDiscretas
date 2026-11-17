import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches


def draw_panel(ax, x, y, w, h, title, bg_color, border_color, title_color):
    rect = patches.FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0.06",
        facecolor=bg_color,
        edgecolor=border_color,
        linewidth=1.8
    )
    ax.add_patch(rect)
    ax.text(
        x + w / 2, y + h - 0.25, title,
        ha='center', va='center',
        fontsize=10.2, fontweight='bold', color=title_color
    )
    ax.plot([x + 0.12, x + w - 0.12], [y + h - 0.45, y + h - 0.45], color=border_color, linewidth=1.0, alpha=0.65)


def main():
    fig, ax = plt.subplots(figsize=(13.5, 8.2), dpi=180)
    ax.set_xlim(0, 13.5)
    ax.set_ylim(0, 8.2)
    ax.axis('off')

    # Main Title
    ax.text(
        6.75, 7.88,
        r"Álgebra Booleana $\langle B, +, \cdot, ', 0, 1 \rangle$: Postulados de Huntington, Teoremas y Dualidad",
        ha='center', va='center', fontsize=13.8, fontweight='bold', color='#0f172a'
    )
    ax.text(
        6.75, 7.52,
        r"Estructura algebraica sobre señales binarias $B = \{0, 1\}$   |   Suma lógica OR ($+$), Producto lógico AND ($\cdot$), Complemento NOT ($'$)",
        ha='center', va='center', fontsize=9.8, color='#334155'
    )

    # Panel 1: Postulados de Huntington (Top-Left)
    draw_panel(ax, 0.25, 4.45, 6.35, 2.8, "1. Postulados de Huntington (Axiomas Fundamentales)", '#eff6ff', '#2563eb', '#1d4ed8')
    postulados = [
        (r"P1. Identidad (Neutros):", r"$x + 0 = x$", r"$x \cdot 1 = x$"),
        (r"P2. Conmutatividad:", r"$x + y = y + x$", r"$x \cdot y = y \cdot x$"),
        (r"P3. Distributividad:", r"$x + (y \cdot z) = (x+y)(x+z)$", r"$x \cdot (y + z) = (x \cdot y) + (x \cdot z)$"),
        (r"P4. Complemento:", r"$x + x' = 1$", r"$x \cdot x' = 0$"),
        (r"P5. Asociatividad:", r"$x + (y + z) = (x+y) + z$", r"$x \cdot (y \cdot z) = (x \cdot y) \cdot z$"),
    ]
    ax.text(1.5, 6.58, "Postulado", ha='center', va='center', fontsize=8.8, fontweight='bold', color='#1e3a8a')
    ax.text(3.65, 6.58, "Forma Suma (OR)", ha='center', va='center', fontsize=8.8, fontweight='bold', color='#1e3a8a')
    ax.text(5.55, 6.58, "Forma Dual Producto (AND)", ha='center', va='center', fontsize=8.8, fontweight='bold', color='#1e3a8a')
    for idx, (p_name, f_or, f_and) in enumerate(postulados):
        ry = 6.22 - idx * 0.38
        if idx % 2 == 1:
            ax.add_patch(patches.Rectangle((0.38, ry - 0.16), 6.08, 0.34, facecolor='#dbeafe', alpha=0.5, edgecolor='none'))
        ax.text(0.45, ry, p_name, ha='left', va='center', fontsize=8.6, fontweight='bold', color='#1e293b')
        ax.text(3.65, ry, f_or, ha='center', va='center', fontsize=8.7, color='#0f172a')
        ax.text(5.55, ry, f_and, ha='center', va='center', fontsize=8.7, color='#0f172a')

    # Panel 2: Principio de Dualidad y Precedencia (Top-Right)
    draw_panel(ax, 6.9, 4.45, 6.35, 2.8, "2. Principio de Dualidad y Jerarquía de Operadores", '#fdf4ff', '#9333ea', '#7e22ce')
    dual_lines = [
        r"$\bullet$ Teorema de Dualidad: El dual de cualquier teorema booleano también es un teorema.",
        r"$\bullet$ Regla para obtener el Dual de una expresión o identidad booleana:",
        r"   1) Intercambiar sumas por productos:   $+ \;\longleftrightarrow\; \cdot$",
        r"   2) Intercambiar elementos neutros:      $0 \;\longleftrightarrow\; 1$",
        r"   3) NO complementar las variables ($A$ se queda $A$, $A'$ se queda $A'$).",
        r"$\bullet$ Jerarquía de evaluación:  $1^\circ$ Paréntesis $(\;)$   $\rightarrow$   $2^\circ$ NOT ($'$)   $\rightarrow$   $3^\circ$ AND ($\cdot$)   $\rightarrow$   $4^\circ$ OR ($+$)"
    ]
    for idx, line in enumerate(dual_lines):
        ry = 6.52 - idx * 0.36
        weight = 'bold' if idx in (0, 5) else 'normal'
        color = '#6b21a8' if idx == 4 else '#1e293b'
        ax.text(7.1, ry, line, ha='left', va='center', fontsize=8.65, fontweight=weight, color=color)

    # Panel 3: Teoremas del Álgebra de Boole (Bottom-Left)
    draw_panel(ax, 0.25, 0.3, 7.65, 3.88, "3. Teoremas Fundamentales del Álgebra de Boole (Tabla 5.1)", '#f8fafc', '#475569', '#0f172a')
    headers_t = ["Nombre / Ley", "Teorema (Forma a)", "Dual (Forma b)"]
    col_xt = [1.55, 4.35, 6.55]
    for cx, ht in zip(col_xt, headers_t):
        ax.text(cx, 3.52, ht, ha='center', va='center', fontsize=8.9, fontweight='bold', color='#0f172a')
    ax.plot([0.4, 7.75], [3.35, 3.35], color='#64748b', linewidth=1.1)

    teoremas = [
        ("Acotamiento (Dominación)", r"$A \cdot 0 = 0$", r"$A + 1 = 1$"),
        ("Idempotencia", r"$A \cdot A = A$", r"$A + A = A$"),
        ("Involución y Neutros", r"$(A')' = A, \quad 0' = 1$", r"$1' = 0$"),
        ("Leyes de De Morgan", r"$(A \cdot B)' = A' + B'$", r"$(A + B)' = A' \cdot B'$"),
        ("Adyacencia (Combinación)", r"$AB + AB' = A$", r"$(A + B)(A + B') = A$"),
        ("Absorción", r"$A + AB = A$", r"$A(A + B) = A$"),
        ("Eliminación Redundancia", r"$A + A'B = A + B$", r"$A(A' + B) = AB$"),
        ("Teorema del Consenso", r"$AB + A'C + BC = AB + A'C$", r"$(A+B)(A'+C)(B+C) = (A+B)(A'+C)$"),
    ]
    for idx, (t_name, ta, tb) in enumerate(teoremas):
        ry = 3.12 - idx * 0.345
        if idx % 2 == 1:
            ax.add_patch(patches.Rectangle((0.38, ry - 0.15), 7.36, 0.31, facecolor='#e2e8f0', alpha=0.45, edgecolor='none'))
        ax.text(0.45, ry, t_name, ha='left', va='center', fontsize=8.4, fontweight='bold', color='#334155')
        ax.text(4.35, ry, ta, ha='center', va='center', fontsize=8.45, color='#0f766e')
        ax.text(6.55, ry, tb, ha='center', va='center', fontsize=8.45, color='#1d4ed8')

    # Panel 4: Isomorfismo entre Sistemas (Bottom-Right)
    draw_panel(ax, 8.15, 0.3, 5.1, 3.88, "4. Isomorfismo de Estructuras Booleanas", '#ecfdf5', '#059669', '#047857')
    iso_headers = ["Concepto", "Álgebra Boole", "Lógica Prop.", "Conjuntos"]
    iso_x = [8.95, 10.25, 11.45, 12.55]
    for cx, ht in zip(iso_x, iso_headers):
        ax.text(cx, 3.52, ht, ha='center', va='center', fontsize=8.6, fontweight='bold', color='#065f46')
    ax.plot([8.3, 13.1], [3.35, 3.35], color='#059669', linewidth=1.1)

    iso_rows = [
        ("Dominio", r"$B = \{0, 1\}$", r"$\{0, 1\}$ o $\{F, V\}$", r"$\mathcal{P}(U)$"),
        ("Suma / Unión", r"$A + B$", r"$p \vee q$", r"$A \cup B$"),
        ("Prod. / Inter.", r"$A \cdot B$", r"$p \wedge q$", r"$A \cap B$"),
        ("Complemento", r"$A'$", r"$p'$ o $\neg p$", r"$A'$ o $A^c$"),
        ("Elemento 0", r"$0$", r"Contradicción $0$", r"Vacío $\emptyset$"),
        ("Elemento 1", r"$1$", r"Tautología $1$", r"Universo $U$"),
        ("Orden parcial", r"$A \leq B \;(A+B=B)$", r"$p \Rightarrow q$", r"$A \subseteq B$"),
    ]
    for idx, (c_label, c_boole, c_log, c_set) in enumerate(iso_rows):
        ry = 3.08 - idx * 0.37
        if idx % 2 == 1:
            ax.add_patch(patches.Rectangle((8.28, ry - 0.16), 4.84, 0.33, facecolor='#d1fae5', alpha=0.5, edgecolor='none'))
        ax.text(8.35, ry, c_label, ha='left', va='center', fontsize=8.2, fontweight='bold', color='#1e293b')
        ax.text(10.25, ry, c_boole, ha='center', va='center', fontsize=8.3, color='#0f172a')
        ax.text(11.45, ry, c_log, ha='center', va='center', fontsize=8.3, color='#0f172a')
        ax.text(12.55, ry, c_set, ha='center', va='center', fontsize=8.3, color='#0f172a')

    ax.text(
        10.7, 0.52,
        r"Teorema de Stone: Toda álgebra booleana finita tiene $|B| = 2^n$ elementos.",
        ha='center', va='center', fontsize=8.2, fontweight='bold', color='#047857'
    )

    plt.tight_layout()
    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "postulados-y-teoremas-algebra-booleana.png")
    plt.savefig(out_path, dpi=180, bbox_inches='tight', facecolor='white')
    plt.close()


if __name__ == "__main__":
    main()
