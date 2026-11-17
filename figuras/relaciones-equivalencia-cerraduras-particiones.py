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
        fontsize=9.8, fontweight='bold', color=title_color
    )
    ax.plot([x + 0.12, x + w - 0.12], [y + h - 0.45, y + h - 0.45], color=border_color, linewidth=1.0, alpha=0.65)


def main():
    fig, ax = plt.subplots(figsize=(13.6, 8.2), dpi=180)
    ax.set_xlim(0, 13.6)
    ax.set_ylim(0, 8.2)
    ax.axis('off')

    # Main Title
    ax.text(
        6.8, 7.88,
        r"Relaciones de Equivalencia, Clases de Equivalencia $[a]$, Particiones y Cerraduras",
        ha='center', va='center', fontsize=13.5, fontweight='bold', color='#0f172a'
    )
    ax.text(
        6.8, 7.52,
        r"$R$ es Relación de Equivalencia $\Longleftrightarrow$ es Reflexiva, Simétrica y Transitiva   |   Divide al conjunto $A$ en subgrafos completos disjuntos",
        ha='center', va='center', fontsize=9.6, color='#334155'
    )

    # Top-Left Panel: Clases de Equivalencia y Partición (Ejemplo 6.8 de Jiménez Murillo)
    draw_panel(ax, 0.25, 4.15, 6.45, 3.1, r"1. Clases de Equivalencia y Partición (Ejemplo 6.8 en $A=\{1,2,3,4,5\}$)", '#eff6ff', '#2563eb', '#1d4ed8')
    eq_lines = [
        r"$\bullet$ Relación de Equivalencia $R$: cumple Reflexiva + Simétrica + Transitiva.",
        r"$\bullet$ Clase de equivalencia de $a \in A$:  $[a] = \{b \in A \mid (a, b) \in R\} \neq \emptyset$.",
        r"$\bullet$ En el Ejemplo 6.8: $R = \{(1,1),(1,2),(1,5),(2,1),(2,2),(2,5),(5,1),(5,2),(5,5),(3,3),(3,4),(4,3),(4,4)\}$",
        r"   Clases:  $[1] = [2] = [5] = \{1, 2, 5\} \qquad\text{y}\qquad [3] = [4] = \{3, 4\}$",
        r"$\bullet$ Partición $X = \{[1], [3]\} = \{\{1, 2, 5\},\; \{3, 4\}\}$:",
        r"   1) Unión igual a $A$: $\{1,2,5\} \cup \{3,4\} = A$.   2) Disjuntas: $\{1,2,5\} \cap \{3,4\} = \emptyset$."
    ]
    for idx, ln in enumerate(eq_lines):
        ry = 6.50 - idx * 0.36
        w_f = 'bold' if idx in (3, 4) else 'normal'
        c_f = '#1e3a8a' if idx in (3, 4) else '#1e293b'
        ax.text(0.42, ry, ln, ha='left', va='center', fontsize=8.3, fontweight=w_f, color=c_f)

    # Top-Right Panel: Subgrafos Completos y Matriz por Bloques de una Partición
    draw_panel(ax, 6.95, 4.15, 6.4, 3.1, "2. Grafo de una Partición (Subgrafos Completos Disjuntos)", '#ecfdf5', '#059669', '#047857')
    # Draw Partition Set Box
    part_box1 = patches.FancyBboxPatch((7.25, 4.45), 2.75, 2.1, boxstyle="round,pad=0.05", facecolor='#ffffff', edgecolor='#059669', linewidth=1.5)
    part_box2 = patches.FancyBboxPatch((10.25, 4.45), 2.8, 2.1, boxstyle="round,pad=0.05", facecolor='#ffffff', edgecolor='#2563eb', linewidth=1.5)
    ax.add_patch(part_box1)
    ax.add_patch(part_box2)
    ax.text(8.62, 6.32, r"Clase $[1] = \{1, 2, 5\}$ ($K_3$)", ha='center', va='center', fontsize=8.6, fontweight='bold', color='#065f46')
    ax.text(11.65, 6.32, r"Clase $[3] = \{3, 4\}$ ($K_2$)", ha='center', va='center', fontsize=8.6, fontweight='bold', color='#1e3a8a')

    # Triangle for {1, 2, 5}
    p1_pts = [(8.62, 5.88), (7.85, 4.82), (9.40, 4.82)]
    for i in range(3):
        for j in range(i + 1, 3):
            ax.plot([p1_pts[i][0], p1_pts[j][0]], [p1_pts[i][1], p1_pts[j][1]], color='#059669', linewidth=2.0)
    for (px, py), lbl in zip(p1_pts, ["1", "2", "5"]):
        ax.add_patch(patches.Circle((px, py), 0.21, facecolor='#d1fae5', edgecolor='#047857', linewidth=1.8, zorder=4))
        ax.text(px, py, lbl, ha='center', va='center', fontsize=9.2, fontweight='bold', color='#065f46', zorder=5)

    # Edge for {3, 4}
    p2_pts = [(11.0, 5.32), (12.3, 5.32)]
    ax.plot([p2_pts[0][0], p2_pts[1][0]], [p2_pts[0][1], p2_pts[1][1]], color='#2563eb', linewidth=2.2)
    for (px, py), lbl in zip(p2_pts, ["3", "4"]):
        ax.add_patch(patches.Circle((px, py), 0.21, facecolor='#dbeafe', edgecolor='#1d4ed8', linewidth=1.8, zorder=4))
        ax.text(px, py, lbl, ha='center', va='center', fontsize=9.2, fontweight='bold', color='#1e3a8a', zorder=5)
    ax.text(11.65, 4.68, "Cada clase es una componente\nconexa completa (sin flechas)", ha='center', va='center', fontsize=7.9, color='#334155')

    # Bottom Panel: Las Tres Cerraduras de una Relación (Ejemplo 6.9 de Jiménez Murillo)
    draw_panel(ax, 0.25, 0.3, 13.1, 3.58, "3. Cerraduras de una Relación: Reflexiva, Simétrica y Transitiva (Conversión a Relación de Equivalencia — Ejemplo 6.9)", '#fffbeb', '#d97706', '#b45309')

    # 3 Sub-boxes inside Bottom Panel
    b1 = patches.FancyBboxPatch((0.48, 0.55), 3.95, 2.65, boxstyle="round,pad=0.05", facecolor='#ffffff', edgecolor='#d97706', linewidth=1.5)
    b2 = patches.FancyBboxPatch((4.68, 0.55), 3.95, 2.65, boxstyle="round,pad=0.05", facecolor='#ffffff', edgecolor='#2563eb', linewidth=1.5)
    b3 = patches.FancyBboxPatch((8.88, 0.55), 4.22, 2.65, boxstyle="round,pad=0.05", facecolor='#ffffff', edgecolor='#059669', linewidth=1.5)
    ax.add_patch(b1)
    ax.add_patch(b2)
    ax.add_patch(b3)

    ax.text(2.45, 2.95, "Paso 1: Cerradura Reflexiva", ha='center', va='center', fontsize=9.2, fontweight='bold', color='#b45309')
    s1_lines = [
        r"Fórmula conjuntista:  $R_r = R \cup I$",
        r"Fórmula matricial:    $M_{R_r} = M_R \cup I_n$",
        r"$\bullet$ Se agrega la relación identidad",
        r"  $I = \{(a, a) \mid a \in A\}$.",
        r"$\bullet$ En la matriz $M_R$, equivale a",
        r"  colocar $1\mathrm{s}$ en toda la diagonal",
        r"  principal ($m_{ii} \leftarrow 1$)."
    ]
    for idx, ln in enumerate(s1_lines):
        ax.text(0.62, 2.60 - idx * 0.29, ln, ha='left', va='center', fontsize=8.1, fontweight='bold' if idx < 2 else 'normal', color='#1e293b')

    ax.text(6.65, 2.95, "Paso 2: Cerradura Simétrica", ha='center', va='center', fontsize=9.2, fontweight='bold', color='#1d4ed8')
    s2_lines = [
        r"Fórmula conjuntista:  $R_s = R \cup R^{-1}$",
        r"Fórmula matricial:    $M_{R_s} = M_R \cup M_R^T$",
        r"$\bullet$ Se agrega la relación inversa",
        r"  $R^{-1} = \{(b, a) \mid (a, b) \in R\}$.",
        r"$\bullet$ En la matriz $M_R$, si $m_{ij} = 1$,",
        r"  se asigna también $m_{ji} \leftarrow 1$",
        r"  (haciendo la matriz simétrica)."
    ]
    for idx, ln in enumerate(s2_lines):
        ax.text(4.82, 2.60 - idx * 0.29, ln, ha='left', va='center', fontsize=8.1, fontweight='bold' if idx < 2 else 'normal', color='#1e293b')

    ax.text(10.99, 2.95, "Paso 3: Cerradura Transitiva ($R^*$)", ha='center', va='center', fontsize=9.2, fontweight='bold', color='#047857')
    s3_lines = [
        r"Algoritmo Iterativo Matricial:",
        r"Repetir:   $M_R \leftarrow M_R \cup (M_R \odot M_R)$",
        r"hasta que  $M_R = M_R \cup M_R^2$  (estabilidad).",
        r"$\bullet$ Equivalencia cerrada (Ej. 6.9):",
        r"  $R = \{(1,1),(1,4),(2,3),(6,1)\}$ en $\{1..6\}$",
        r"  tras las 3 cerraduras genera la partición:",
        r"  $X = \{\{1, 4, 6\},\; \{2, 3\},\; \{5\}\}$."
    ]
    for idx, ln in enumerate(s3_lines):
        ax.text(9.02, 2.60 - idx * 0.29, ln, ha='left', va='center', fontsize=8.1, fontweight='bold' if idx in (1, 6) else 'normal', color='#1e293b')

    plt.tight_layout()
    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "relaciones-equivalencia-cerraduras-particiones.png")
    plt.savefig(out_path, dpi=180, bbox_inches='tight', facecolor='white')
    plt.close()


if __name__ == "__main__":
    main()
