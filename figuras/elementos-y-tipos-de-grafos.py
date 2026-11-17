import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches


def draw_panel(ax, x, y, w, h, title, bg_color, border_color, title_color):
    rect = patches.FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0.05",
        facecolor=bg_color,
        edgecolor=border_color,
        linewidth=1.7
    )
    ax.add_patch(rect)
    ax.text(
        x + w / 2, y + h - 0.24, title,
        ha='center', va='center',
        fontsize=9.6, fontweight='bold', color=title_color
    )
    ax.plot([x + 0.1, x + w - 0.1], [y + h - 0.44, y + h - 0.44], color=border_color, linewidth=1.0, alpha=0.6)


def draw_node(ax, x, y, lbl, bg='#dbeafe', border='#1d4ed8', tcol='#1e3a8a', r=0.19):
    ax.add_patch(patches.Circle((x, y), r, facecolor=bg, edgecolor=border, linewidth=1.7, zorder=5))
    ax.text(x, y, lbl, ha='center', va='center', fontsize=8.8, fontweight='bold', color=tcol, zorder=6)


def main():
    fig, ax = plt.subplots(figsize=(13.6, 8.2), dpi=180)
    ax.set_xlim(0, 13.6)
    ax.set_ylim(0, 8.2)
    ax.axis('off')

    # Main Title
    ax.text(
        6.8, 7.88,
        r"Teoría de Grafos $G = (V, L)$: Componentes Fundamentales y Clasificación de los Grafos",
        ha='center', va='center', fontsize=13.6, fontweight='bold', color='#0f172a'
    )
    ax.text(
        6.8, 7.52,
        r"Vértices ($V$), Aristas o Lados ($L$), Lazos, Lados Paralelos, Valencia $\delta(v)$ y Teorema de la Suma de Grados $\sum \delta(v) = 2|L|$",
        ha='center', va='center', fontsize=9.5, color='#334155'
    )

    # Panel 1: Componentes de un Grafo (Top-Left) - Secc. 7.2 Jiménez Murillo
    draw_panel(ax, 0.25, 4.15, 4.2, 3.1, "1. Componentes de un Grafo y Valencia", '#eff6ff', '#2563eb', '#1d4ed8')
    # Draw multigraph with loop and parallel edges on nodes a, b, c, d
    na, nb, nc, nd = (0.95, 6.05), (2.25, 6.05), (0.95, 5.05), (2.25, 5.05)
    # Edges: (a,c)=1, parallel (a,b)=2,3, (b,c)=4, (b,d)=5, loop on d=6
    ax.plot([na[0], nc[0]], [na[1], nc[1]], color='#334155', lw=1.7)
    ax.plot([nb[0], nc[0]], [nb[1], nc[1]], color='#334155', lw=1.7)
    ax.plot([nb[0], nd[0]], [nb[1], nd[1]], color='#334155', lw=1.7)
    # Parallel edges between a and b
    ax.annotate("", xy=nb, xytext=na, arrowprops=dict(arrowstyle="-", color='#1d4ed8', lw=1.8, connectionstyle="arc3,rad=0.28"))
    ax.annotate("", xy=nb, xytext=na, arrowprops=dict(arrowstyle="-", color='#1d4ed8', lw=1.8, connectionstyle="arc3,rad=-0.22"))
    # Loop on d
    ax.add_patch(patches.Circle((nd[0] + 0.24, nd[1] - 0.14), 0.18, facecolor='none', edgecolor='#dc2626', linewidth=1.8))

    for pt, lb in [(na, "a"), (nb, "b"), (nc, "c"), (nd, "d")]:
        draw_node(ax, pt[0], pt[1], lb)

    ax.text(1.6, 6.46, "Lados paralelos", ha='center', va='center', fontsize=7.6, fontweight='bold', color='#1d4ed8')
    ax.text(2.68, 4.72, "Lazo", ha='center', va='center', fontsize=7.8, fontweight='bold', color='#dc2626')

    comp_txt = [
        r"$V = \{a, b, c, d\}$ (4 vértices)",
        r"Valencias (Cap. 7.2):",
        r"$\mathrm{Val}(a)=3,\; \mathrm{Val}(b)=4$",
        r"$\mathrm{Val}(c)=2,\; \mathrm{Val}(d)=2\;\text{o}\;3$",
        r"Simple: sin lazos ni paralelos."
    ]
    for idx, ct in enumerate(comp_txt):
        ax.text(2.85, 6.22 - idx * 0.34, ct, ha='left', va='center', fontsize=7.65, color='#1e293b')
    ax.text(2.35, 4.35, r"Puentes de Königsberg (Euler, 1735): origen de la teoría", ha='center', va='center', fontsize=7.8, fontweight='bold', color='#1e3a8a')

    # Panel 2: Grafo Completo Kn y Complemento G' (Top-Middle)
    draw_panel(ax, 4.7, 4.15, 4.2, 3.1, r"2. Grafo Completo ($K_n$) y Complemento ($G'$)", '#ecfdf5', '#059669', '#047857')
    # Draw K5 pentagon
    cx, cy, r_k = 5.75, 5.55, 0.78
    angs = [np.pi / 2 - k * 2 * np.pi / 5 for k in range(5)]
    k5_pts = [(cx + r_k * np.cos(a), cy + r_k * np.sin(a)) for a in angs]
    for i in range(5):
        for j in range(i + 1, 5):
            ax.plot([k5_pts[i][0], k5_pts[j][0]], [k5_pts[i][1], k5_pts[j][1]], color='#059669', lw=1.4, alpha=0.85)
    for idx, (px, py) in enumerate(k5_pts):
        draw_node(ax, px, py, str(idx + 1), bg='#d1fae5', border='#047857', tcol='#065f46', r=0.16)
    ax.text(5.75, 4.42, r"$K_5$: $|L| = \frac{5(4)}{2} = 10$", ha='center', va='center', fontsize=8.3, fontweight='bold', color='#065f46')

    k_info = [
        r"$\bullet$ En $K_n$ todo vértice se",
        r"  conecta con los demás.",
        r"$\bullet$ Valencia: $\delta(v) = n - 1$.",
        r"$\bullet$ Total de aristas:",
        r"  $|L| = \frac{n(n - 1)}{2}$",
        r"$\bullet$ Complemento $G'$: aristas",
        r"  que faltan a $G$ para ser $K_n$:",
        r"  $G \cup G' = K_n$."
    ]
    for idx, ki in enumerate(k_info):
        ax.text(6.82, 6.42 - idx * 0.27, ki, ha='left', va='center', fontsize=7.8, color='#1e293b')

    # Panel 3: Grafo Bipartido y Bipartido Completo Kn,m (Top-Right)
    draw_panel(ax, 9.15, 4.15, 4.2, 3.1, r"3. Grafo Bipartido y Bipartido Completo ($K_{n,m}$)", '#fdf4ff', '#9333ea', '#7e22ce')
    # Draw K3,3
    a_bip = [(9.85, 6.22), (9.85, 5.55), (9.85, 4.88)]
    b_bip = [(11.25, 6.22), (11.25, 5.55), (11.25, 4.88)]
    for pa in a_bip:
        for pb in b_bip:
            ax.plot([pa[0], pb[0]], [pa[1], pb[1]], color='#9333ea', lw=1.35, alpha=0.75)
    for idx, pa in enumerate(a_bip):
        draw_node(ax, pa[0], pa[1], f"a{idx+1}", bg='#f3e8ff', border='#7e22ce', tcol='#581c87', r=0.17)
    for idx, pb in enumerate(b_bip):
        draw_node(ax, pb[0], pb[1], f"b{idx+1}", bg='#fae8ff', border='#a21caf', tcol='#701a75', r=0.17)
    ax.text(10.55, 4.42, r"$K_{3,3}$: $|L| = 3 \times 3 = 9$", ha='center', va='center', fontsize=8.3, fontweight='bold', color='#6b21a8')

    b_info = [
        r"$\bullet$ Partición $V = A \cup B$",
        r"  con $A \cap B = \emptyset$.",
        r"$\bullet$ Ninguna arista une",
        r"  vértices del mismo grupo.",
        r"$\bullet$ Criterio: NO contiene",
        r"  ciclos de longitud impar.",
        r"$\bullet$ En $K_{n,m}$: $|L| = n \cdot m$."
    ]
    for idx, bi in enumerate(b_info):
        ax.text(11.62, 6.35 - idx * 0.28, bi, ha='left', va='center', fontsize=7.75, color='#1e293b')

    # Panel 4: Grafos Planos, Fórmula de Euler y Kuratowski (Bottom-Left)
    draw_panel(ax, 0.25, 0.3, 6.45, 3.58, r"4. Grafos Planos, Ecuación de Euler ($A = L - V + 2$) y Kuratowski", '#fffbeb', '#d97706', '#b45309')
    # Draw planar K4 without crossings
    p_top = (1.55, 2.95)
    p_bl = (0.75, 1.45)
    p_br = (2.35, 1.45)
    p_mid = (1.55, 2.02)
    for u, v in [(p_top, p_bl), (p_top, p_br), (p_bl, p_br), (p_top, p_mid), (p_bl, p_mid), (p_br, p_mid)]:
        ax.plot([u[0], v[0]], [u[1], v[1]], color='#b45309', lw=1.8)
    for pt, lb in [(p_top, "a"), (p_bl, "b"), (p_br, "c"), (p_mid, "d")]:
        draw_node(ax, pt[0], pt[1], lb, bg='#fef3c7', border='#b45309', tcol='#78350f', r=0.16)
    ax.text(1.32, 2.18, "R1", fontsize=7.5, fontweight='bold', color='#d97706')
    ax.text(1.78, 2.18, "R2", fontsize=7.5, fontweight='bold', color='#d97706')
    ax.text(1.55, 1.65, "R3", fontsize=7.5, fontweight='bold', color='#d97706')
    ax.text(2.35, 2.65, "R4 (ext.)", fontsize=7.5, fontweight='bold', color='#d97706')
    ax.text(1.55, 0.65, r"$K_4$ plano: $V=4, L=6, A=4$" + "\n" + r"$A = 6 - 4 + 2 = 4$", ha='center', va='center', fontsize=8.0, fontweight='bold', color='#92400e')

    pl_info = [
        r"$\bullet$ Grafo Plano: se puede dibujar en el plano sin",
        r"  que sus aristas se crucen entre sí.",
        r"$\bullet$ Fórmula de Euler (grafo plano y conexo):",
        r"  $A = L - V + 2 \quad \Longleftrightarrow \quad V - L + A = 2$",
        r"  donde $A$ es el número de áreas/regiones (incluyendo",
        r"  la región exterior infinita). Cada lado es frontera",
        r"  de como máximo $2$ áreas ($L \leq 3V - 6$).",
        r"$\bullet$ Teorema de Kuratowski: $G$ es plano si y sólo si",
        r"  NO contiene un subgrafo homeomorfo a $K_5$ ni a $K_{3,3}$."
    ]
    for idx, pli in enumerate(pl_info):
        ax.text(2.82, 3.12 - idx * 0.30, pli, ha='left', va='center', fontsize=7.95, fontweight='bold' if idx in (3, 7) else 'normal', color='#1e293b')

    # Panel 5: Grafos Conexos, Ponderados, Euler y Hamilton (Bottom-Right)
    draw_panel(ax, 6.95, 0.3, 6.4, 3.58, "5. Grafos Conexos, Ponderados, Circuitos de Euler y de Hamilton", '#f8fafc', '#334155', '#0f172a')
    eh_info = [
        r"$\bullet$ Grafo Conexo: existe al menos un camino entre cualquier par de vértices $w, x \in V$.",
        r"$\bullet$ Grafo Ponderado (con peso): cada arista $e = (u, v)$ tiene asignado un valor numérico",
        r"  $w(e) > 0$ que representa distancia, costo, tiempo o capacidad de transmisión.",
        r"$\bullet$ Camino de Euler: recorre TODAS las aristas exactamente una vez. Existe si y sólo si",
        r"  el grafo es conexo y tiene exactamente $2$ vértices de valencia impar (inicio y fin).",
        r"$\bullet$ Circuito de Euler: ciclo cerrado que recorre TODAS las aristas una sola vez.",
        r"  Teorema de Euler: existe $\Longleftrightarrow$ $G$ es conexo y TODOS sus vértices tienen valencia PAR.",
        r"$\bullet$ Circuito de Hamilton: ciclo que visita TODOS los vértices exactamente una vez.",
        r"$\bullet$ Coloración y Número Cromático $\chi(G)$: mínimo de colores para que vértices adyacentes",
        r"  tengan distinto color. Teorema de los 4 Colores (Appel-Haken): en todo grafo plano $\chi(G) \leq 4$."
    ]
    for idx, ehi in enumerate(eh_info):
        ry = 3.16 - idx * 0.28
        w_f = 'bold' if idx in (0, 1, 5, 6, 7, 8) else 'normal'
        c_f = '#1d4ed8' if idx in (6, 7) else '#1e293b'
        ax.text(7.12, ry, ehi, ha='left', va='center', fontsize=7.9, fontweight=w_f, color=c_f)

    plt.tight_layout()
    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "elementos-y-tipos-de-grafos.png")
    plt.savefig(out_path, dpi=180, bbox_inches='tight', facecolor='white')
    plt.close()


if __name__ == "__main__":
    main()
