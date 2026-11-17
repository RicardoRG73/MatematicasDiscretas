import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches


def draw_func_box(ax, x, y, w, h, title, subtitle, a_vals, b_vals, edges, footer, bg, border, t_col):
    rect = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.05", facecolor=bg, edgecolor=border, linewidth=1.7)
    ax.add_patch(rect)
    ax.text(x + w / 2, y + h - 0.24, title, ha='center', va='center', fontsize=9.8, fontweight='bold', color=t_col)
    ax.text(x + w / 2, y + h - 0.48, subtitle, ha='center', va='center', fontsize=8.0, color='#334155')
    ax.plot([x + 0.1, x + w - 0.1], [y + h - 0.64, y + h - 0.64], color=border, linewidth=1.0, alpha=0.6)

    # Two ellipses inside
    cx_a = x + w * 0.28
    cx_b = x + w * 0.72
    cy_mid = y + h * 0.44
    el_a = patches.Ellipse((cx_a, cy_mid), 0.95, 1.55, facecolor='#ffffff', edgecolor=border, linewidth=1.5)
    el_b = patches.Ellipse((cx_b, cy_mid), 0.95, 1.55, facecolor='#ffffff', edgecolor=border, linewidth=1.5)
    ax.add_patch(el_a)
    ax.add_patch(el_b)
    ax.text(cx_a, cy_mid + 0.90, r"$A$", ha='center', va='center', fontsize=8.8, fontweight='bold', color=t_col)
    ax.text(cx_b, cy_mid + 0.90, r"$B$", ha='center', va='center', fontsize=8.8, fontweight='bold', color=t_col)

    na = len(a_vals)
    nb = len(b_vals)
    ay = [cy_mid + 0.48 - i * (0.96 / max(na - 1, 1)) for i in range(na)]
    by = [cy_mid + 0.52 - j * (1.04 / max(nb - 1, 1)) for j in range(nb)]

    for i, val in enumerate(a_vals):
        ax.scatter([cx_a], [ay[i]], color=t_col, s=26, zorder=4)
        ax.text(cx_a - 0.18, ay[i], val, ha='right', va='center', fontsize=8.5, fontweight='bold', color='#0f172a')
    for j, val in enumerate(b_vals):
        ax.scatter([cx_b], [by[j]], color='#0f172a', s=26, zorder=4)
        ax.text(cx_b + 0.18, by[j], val, ha='left', va='center', fontsize=8.5, fontweight='bold', color='#0f172a')

    for i_idx, j_idx in edges:
        ax.annotate(
            "", xy=(cx_b - 0.06, by[j_idx]), xytext=(cx_a + 0.06, ay[i_idx]),
            arrowprops=dict(arrowstyle="->", color=t_col, lw=1.5, shrinkA=2, shrinkB=2)
        )

    ax.text(x + w / 2, y + 0.22, footer, ha='center', va='center', fontsize=8.0, fontweight='bold', color=t_col)


def main():
    fig, ax = plt.subplots(figsize=(13.6, 8.2), dpi=180)
    ax.set_xlim(0, 13.6)
    ax.set_ylim(0, 8.2)
    ax.axis('off')

    # Main Title
    ax.text(
        6.8, 7.88,
        r"Funciones ($f: A \to B$): Clasificación (Inyectiva, Suprayectiva, Biyectiva) y Aplicaciones en Computación",
        ha='center', va='center', fontsize=13.4, fontweight='bold', color='#0f172a'
    )
    ax.text(
        6.8, 7.52,
        r"Condición de Función: 1) $\mathrm{Dom}(f) = A$   y   2) $(a, b) \in f \wedge (a, c) \in f \Rightarrow b = c$  (cada elemento de $A$ tiene una única imagen $b = f(a)$)",
        ha='center', va='center', fontsize=9.5, color='#334155'
    )

    # Top Row: 3 Function Types (Ejemplo 6.17 de Jiménez Murillo)
    draw_func_box(
        ax, 0.25, 4.15, 4.2, 3.1,
        "1. Función Inyectiva (Uno a Uno)",
        r"$f(a_1) = f(a_2) \Rightarrow a_1 = a_2$",
        ["a", "b", "c"], ["1", "2", "3", "4"],
        [(0, 0), (1, 2), (2, 1)],
        r"Elementos distintos tienen imágenes distintas ($|A| \leq |B|$)",
        '#eff6ff', '#2563eb', '#1d4ed8'
    )

    draw_func_box(
        ax, 4.7, 4.15, 4.2, 3.1,
        "2. Función Suprayectiva (Sobre)",
        r"$\mathrm{Cod}(f) = f(A) = B \quad (\forall b \in B,\, \exists a \in A)$",
        ["a", "b", "c", "d"], ["1", "2", "3"],
        [(0, 0), (1, 2), (2, 1), (3, 2)],
        r"Todo elemento de $B$ es imagen de al menos un $a \in A$",
        '#fffbeb', '#d97706', '#b45309'
    )

    draw_func_box(
        ax, 9.15, 4.15, 4.2, 3.1,
        "3. Función Biyectiva (Invertible)",
        r"Inyectiva y Suprayectiva a la vez ($|A| = |B|$)",
        ["a", "b", "c", "d"], ["1", "2", "3", "4"],
        [(0, 1), (1, 3), (2, 0), (3, 2)],
        r"Existe la función inversa biyectiva $f^{-1}: B \to A$",
        '#ecfdf5', '#059669', '#047857'
    )

    # Bottom-Left Panel: Composición de Funciones e Inversa
    p_bl = patches.FancyBboxPatch((0.25, 0.3), 6.2, 3.55, boxstyle="round,pad=0.06", facecolor='#fdf4ff', edgecolor='#9333ea', linewidth=1.7)
    ax.add_patch(p_bl)
    ax.text(3.35, 3.60, r"4. Composición de Funciones $(g \circ f)(a) = g(f(a))$ e Inversa $f^{-1}$", ha='center', va='center', fontsize=9.6, fontweight='bold', color='#7e22ce')
    ax.plot([0.38, 6.32], [3.38, 3.38], color='#9333ea', linewidth=1.0, alpha=0.6)

    comp_lines = [
        r"$\bullet$ Si $f: A \to B$ y $g: B \to C$, la función compuesta $g \circ f: A \to C$ se evalúa",
        r"   de adentro hacia afuera:   $(g \circ f)(a) = g(f(a))$.",
        r"$\bullet$ En programación permite anidar llamadas en una sola instrucción:",
        r"   $\mathtt{w := abs(sqrt(cos(x - 3 * y)))}$   $\longrightarrow$   $(h \circ g \circ f)(x, y)$.",
        r"$\bullet$ Teorema de Invertibilidad (Secc. 6.8.3): Una función $f: A \to B$ posee",
        r"   función inversa $f^{-1}: B \to A$ tal que $f^{-1}(f(a)) = a$ si y sólo si $f$ es",
        r"   BIYECTIVA (uno a uno y sobre). En tal caso, $(f^{-1})^{-1} = f$."
    ]
    for idx, ln in enumerate(comp_lines):
        ax.text(0.42, 3.05 - idx * 0.36, ln, ha='left', va='center', fontsize=8.15, fontweight='bold' if idx in (1, 6) else 'normal', color='#1e293b')

    # Bottom-Right Panel: Aplicaciones en Computación (Listas Enlazadas, Bases de Datos y Hashing)
    p_br = patches.FancyBboxPatch((6.7, 0.3), 6.65, 3.55, boxstyle="round,pad=0.06", facecolor='#f8fafc', edgecolor='#334155', linewidth=1.7)
    ax.add_patch(p_br)
    ax.text(10.02, 3.60, "5. Aplicaciones en Computación: Listas Enlazadas, BD y Hashing", ha='center', va='center', fontsize=9.6, fontweight='bold', color='#0f172a')
    ax.plot([6.82, 13.22], [3.38, 3.38], color='#475569', linewidth=1.0, alpha=0.6)

    # Visual mini-table of Linked List from Ejemplo 6.7.1 (Ana -> Jaime -> Juan -> María -> Pedro)
    ax.text(8.35, 3.12, r"A) Lista Enlazada ($X = 3$):", ha='center', va='center', fontsize=8.4, fontweight='bold', color='#1d4ed8')
    ll_rows = [
        ("Pos", "Arreglo A", "Apunt. P"),
        ("1", "María", "4"),
        ("2", "Juan", "1"),
        ("3", "Ana", "5"),
        ("4", "Pedro", "*"),
        ("5", "Jaime", "2"),
    ]
    for r_i, (c1, c2, c3) in enumerate(ll_rows):
        ry = 2.82 - r_i * 0.34
        bg_c = '#dbeafe' if r_i == 0 else ('#f1f5f9' if r_i % 2 == 1 else '#ffffff')
        ax.add_patch(patches.Rectangle((6.9, ry - 0.15), 2.9, 0.31, facecolor=bg_c, edgecolor='#cbd5e1', linewidth=0.8))
        ax.text(7.2, ry, c1, ha='center', va='center', fontsize=7.9, fontweight='bold' if r_i == 0 else 'normal', color='#0f172a')
        ax.text(8.2, ry, c2, ha='center', va='center', fontsize=7.9, fontweight='bold' if r_i == 0 else 'normal', color='#0f172a')
        ax.text(9.35, ry, c3, ha='center', va='center', fontsize=7.9, fontweight='bold', color='#1d4ed8')
    ax.text(8.35, 0.58, r"Orden: Ana(3)$\to$Jaime(5)$\to$Juan(2)$\to$María(1)$\to$Pedro(4)$\to *$", ha='center', va='center', fontsize=7.5, fontweight='bold', color='#047857')

    # Right column inside Bottom-Right Panel: Databases & Hashing
    app_lines = [
        r"B) Bases de Datos Relacionales:",
        r"   Cada tabla es una relación $n$-aria",
        r"   $R \subseteq D_1 \times D_2 \times \dots \times D_n$.",
        r"   Consultas mediante Álgebra",
        r"   Relacional ($\cup, \cap, ', \sigma, \pi, \bowtie$).",
        r"C) Funciones Hash (Dispersión):",
        r"   $h(k) = k \;\mathrm{mod}\; m$ asigna una",
        r"   clave $k$ a una dirección de",
        r"   memoria en tiempo $O(1)$."
    ]
    for idx, ln in enumerate(app_lines):
        ry = 3.05 - idx * 0.28
        w_f = 'bold' if idx in (0, 5) else 'normal'
        c_f = '#b45309' if idx in (0, 5) else '#1e293b'
        ax.text(10.02, ry, ln, ha='left', va='center', fontsize=8.0, fontweight=w_f, color=c_f)

    plt.tight_layout()
    out_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "clasificacion-y-composicion-de-funciones.png")
    plt.savefig(out_path, dpi=180, bbox_inches='tight', facecolor='white')
    plt.close()


if __name__ == "__main__":
    main()
