import os
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
    ax.plot([x + 0.12, x + w - 0.12], [y + h - 0.44, y + h - 0.44], color=border_color, linewidth=1.0, alpha=0.6)


def draw_node(ax, x, y, lbl, bg='#dbeafe', border='#1d4ed8', tcol='#1e3a8a', r=0.20):
    ax.add_patch(patches.Circle((x, y), r, facecolor=bg, edgecolor=border, linewidth=1.8, zorder=5))
    ax.text(x, y, lbl, ha='center', va='center', fontsize=8.8, fontweight='bold', color=tcol, zorder=6)


def main():
    fig, ax = plt.subplots(figsize=(13.6, 8.2), dpi=180)
    ax.set_xlim(0, 13.6)
    ax.set_ylim(0, 8.2)
    ax.axis('off')

    # Main Title
    ax.text(
        6.8, 7.88,
        "Modelos de Redes: Flujo Máximo y Corte Mínimo (Ford-Fulkerson), Pareos (Hall) y Redes de Petri",
        ha='center', va='center', fontsize=13.4, fontweight='bold', color='#0f172a'
    )
    ax.text(
        6.8, 7.52,
        r"Teorema de Flujo Máximo = Corte Mínimo ($\max |F| = \min C(P, \bar{P})$), Acoplamientos Bipartitos y Modelado de Sistemas Concurrentes",
        ha='center', va='center', fontsize=9.5, color='#334155'
    )

    # Top Panel: Red de Transporte, Flujo Máximo y Corte Mínimo (Fig. 10.3.2 de Johnsonbaugh)
    draw_panel(ax, 0.25, 4.15, 13.1, 3.1, r"1. Redes de Transporte: Teorema de Flujo Máximo y Corte Mínimo (Ford-Fulkerson — Cap. 10.1 a 10.3 Johnsonbaugh)", '#eff6ff', '#2563eb', '#1d4ed8')

    # Draw network on left side of Top Panel (Fig 10.1.1 / 10.3.2: a, b, c, d, e, z)
    n_pts = {
        "a": (0.85, 5.52),
        "b": (2.25, 6.32),
        "d": (2.25, 4.72),
        "c": (3.85, 6.32),
        "e": (3.85, 4.72),
        "z": (5.25, 5.52),
    }
    net_edges = [
        ("a", "b", "3, 2", False),
        ("a", "d", "5, 4", False),
        ("b", "c", "2, 2", True),
        ("d", "c", "2, 2", True),
        ("d", "e", "2, 2", True),
        ("c", "z", "4, 4", False),
        ("e", "z", "4, 2", False),
    ]
    for u, v, lbl, is_cut in net_edges:
        x1, y1 = n_pts[u]
        x2, y2 = n_pts[v]
        col = '#dc2626' if is_cut else '#1e3a8a'
        ax.annotate(
            "", xy=(x2, y2), xytext=(x1, y1),
            arrowprops=dict(arrowstyle="->", color=col, lw=2.0 if is_cut else 1.6, shrinkA=12, shrinkB=12),
            zorder=3
        )
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        ax.text(mx, my + 0.16, lbl, ha='center', va='center', fontsize=8.0, fontweight='bold',
                color='#b91c1c' if is_cut else '#1d4ed8',
                bbox=dict(boxstyle="round,pad=0.1", facecolor='white', edgecolor='none', alpha=0.85))

    # Dashed Minimum Cut line separating P = {a, b, d} and P_bar = {c, e, z}
    ax.plot([3.05, 3.05], [4.38, 6.68], color='#dc2626', linestyle='--', linewidth=2.2, zorder=4)
    ax.text(3.05, 4.30, r"Corte mínimo $(P, \bar{P})$: $P=\{a,b,d\},\; \bar{P}=\{c,e,z\}$", ha='center', va='center', fontsize=8.0, fontweight='bold', color='#b91c1c')

    for k, (px, py) in n_pts.items():
        in_p = k in ("a", "b", "d")
        draw_node(ax, px, py, k, bg='#fef3c7' if k in ("a", "z") else ('#dbeafe' if in_p else '#e2e8f0'),
                  border='#d97706' if k in ("a", "z") else ('#1d4ed8' if in_p else '#475569'))

    # Right side of Top Panel: Laws & Ford-Fulkerson Theorem
    ff_lines = [
        r"$\bullet$ Etiqueta de arista $(C_{ij},\; F_{ij})$: Capacidad máxima $C_{ij}$ y Flujo actual $F_{ij}$ ($0 \leq F_{ij} \leq C_{ij}$).",
        r"$\bullet$ Ley de Conservación del Flujo (Kirchhoff): En todo nodo intermedio $j \notin \{a, z\}$:",
        r"  $\sum_i F_{ij}\; (\text{flujo que entra a } j) \;=\; \sum_k F_{jk}\; (\text{flujo que sale de } j)$.",
        r"$\bullet$ Valor del flujo $|F|$: Flujo total que sale de la fuente $a$ $=$ flujo que llega al sumidero $z$:",
        r"  $|F| = F_{ab} + F_{ad} = 2 + 4 = 6 \;=\; F_{cz} + F_{ez} = 4 + 2 = 6$.",
        r"$\bullet$ Capacidad de un Corte $C(P, \bar{P}) = \sum_{i \in P,\, j \in \bar{P}} C_{ij}$: En la figura, $C_{bc} + C_{dc} + C_{de} = 2 + 2 + 2 = 6$.",
        r"$\bullet$ Teorema de Flujo Máximo y Corte Mínimo (Ford-Fulkerson, Teorema 10.3.9):",
        r"  Para todo flujo $F$ y todo corte $(P, \bar{P})$ se cumple $|F| \leq C(P, \bar{P})$. El valor del flujo máximo",
        r"  en cualquier red es EXACTAMENTE IGUAL a la capacidad del corte mínimo ($\max |F| = \min C(P, \bar{P})$)."
    ]
    for idx, fl in enumerate(ff_lines):
        ry = 6.55 - idx * 0.265
        w_f = 'bold' if idx in (1, 6, 8) else 'normal'
        c_f = '#1e3a8a' if idx in (6, 8) else '#1e293b'
        ax.text(5.72, ry, fl, ha='left', va='center', fontsize=7.8, fontweight=w_f, color=c_f)

    # Bottom-Left Panel: Pareos / Acoplamientos Bipartitos (Secc. 10.4 Johnsonbaugh)
    draw_panel(ax, 0.25, 0.3, 6.45, 3.58, "2. Pareos (Acoplamientos / Matchings) y Teorema de Hall", '#ecfdf5', '#059669', '#047857')
    m_lines = [
        r"$\bullet$ Definición de Pareo (Acoplamiento $M$): En un grafo $G=(V, L)$, un pareo",
        r"  $M \subseteq L$ es un conjunto de aristas independientes que NO comparten",
        r"  vértices en común (asigna a cada elemento de $V_1$ a lo sumo una pareja en $V_2$).",
        r"$\bullet$ Pareo Máximo: Aquel que contiene el mayor número posible de aristas $|M|$.",
        r"$\bullet$ Pareo Completo (o Perfecto): Aquel donde TODOS los vértices de $V_1$ quedan",
        r"  emparejados ($|M| = |V_1|$).",
        r"$\bullet$ Reducción a Flujo Máximo (Teorema 10.4.5): Se agrega una superfuente $a$",
        r"  conectada a todo $v \in V_1$, un supersumidero $z$ conectado desde todo $w \in V_2$,",
        r"  y se asigna capacidad $C_{ij} = 1$ a todas las aristas $\Rightarrow \max |M| = \max |F|$.",
        r"$\bullet$ Teorema del Matrimonio de Hall (Teorema 10.4.7): En un grafo bipartito",
        r"  $G = (V_1 \cup V_2, L)$, existe un pareo completo de $V_1$ en $V_2$ si y sólo si:",
        r"  $|S| \leq |R(S)| \quad \text{para todo subconjunto } S \subseteq V_1 \;\;(\text{vecindad } R(S) \subseteq V_2)$."
    ]
    for idx, ml in enumerate(m_lines):
        ry = 3.16 - idx * 0.235
        w_f = 'bold' if idx in (0, 3, 4, 9, 11) else 'normal'
        c_f = '#065f46' if idx == 11 else '#1e293b'
        ax.text(0.42, ry, ml, ha='left', va='center', fontsize=7.8, fontweight=w_f, color=c_f)

    # Bottom-Right Panel: Redes de Petri (Carl Adam Petri, 1962)
    draw_panel(ax, 6.95, 0.3, 6.4, 3.58, "3. Redes de Petri: Modelado de Concurrencia y Sincronización", '#fffbeb', '#d97706', '#b45309')

    # Draw visual Petri Net transition firing at top of Bottom-Right Panel
    # Before firing: P1 (1 token), P2 (1 token) -> Transition t1 -> P3 (0 tokens)
    # Place P1 and P2
    ax.add_patch(patches.Circle((7.55, 2.92), 0.22, facecolor='white', edgecolor='#1d4ed8', lw=1.8))
    ax.add_patch(patches.Circle((7.55, 2.92), 0.06, facecolor='#0f172a'))  # token
    ax.text(7.55, 3.24, r"$p_1$", ha='center', va='center', fontsize=8.2, fontweight='bold', color='#1e3a8a')

    ax.add_patch(patches.Circle((7.55, 2.18), 0.22, facecolor='white', edgecolor='#1d4ed8', lw=1.8))
    ax.add_patch(patches.Circle((7.55, 2.18), 0.06, facecolor='#0f172a'))  # token
    ax.text(7.55, 1.86, r"$p_2$", ha='center', va='center', fontsize=8.2, fontweight='bold', color='#1e3a8a')

    # Transition bar t1
    ax.add_patch(patches.Rectangle((8.42, 2.22), 0.14, 0.66, facecolor='#d97706', edgecolor='#78350f', lw=1.5))
    ax.text(8.49, 3.04, r"$t_1$ (habilitada)", ha='center', va='center', fontsize=7.6, fontweight='bold', color='#b45309')

    # Output place P3
    ax.add_patch(patches.Circle((9.42, 2.55), 0.22, facecolor='white', edgecolor='#059669', lw=1.8))
    ax.text(9.42, 2.88, r"$p_3$", ha='center', va='center', fontsize=8.2, fontweight='bold', color='#065f46')

    ax.annotate("", xy=(8.40, 2.70), xytext=(7.78, 2.90), arrowprops=dict(arrowstyle="->", color='#334155', lw=1.5))
    ax.annotate("", xy=(8.40, 2.40), xytext=(7.78, 2.20), arrowprops=dict(arrowstyle="->", color='#334155', lw=1.5))
    ax.annotate("", xy=(9.18, 2.55), xytext=(8.58, 2.55), arrowprops=dict(arrowstyle="->", color='#334155', lw=1.5))

    petri_info = [
        r"$\bullet$ Estructura $N = (P, T, A, M_0)$:",
        r"  - Lugares $P$ (círculos): estados/condiciones.",
        r"  - Transiciones $T$ (barras): eventos/acciones.",
        r"  - Arcos dirigidos $A \subseteq (P\times T)\cup(T\times P)$.",
        r"  - Marcado $M_0$: tokens (puntos) en cada lugar.",
        r"$\bullet$ Regla de Disparo (Firing Rule):",
        r"  1) Una transición $t \in T$ está HABILITADA si",
        r"     todo lugar de entrada $p \in {}^\bullet t$ tiene al",
        r"     menos tantos tokens como el peso del arco.",
        r"  2) Al dispararse $t$, consume 1 token de cada",
        r"     lugar de entrada ($p_1, p_2$) y deposita 1 token",
        r"     en cada lugar de salida ($p_3$). Modela",
        r"     sistemas distribuidos, protocolos e interbloqueos."
    ]
    for idx, pi in enumerate(petri_info):
        ry = 3.24 - idx * 0.215 if idx >= 5 else 3.24 - idx * 0.215
        x_pos = 9.85 if idx < 5 else 7.12
        y_pos = 3.16 - idx * 0.26 if idx < 5 else 1.56 - (idx - 5) * 0.165
        ax.text(x_pos, y_pos, pi, ha='left', va='center', fontsize=7.55, fontweight='bold' if idx in (0, 5) else 'normal', color='#1e293b')

    plt.tight_layout()
    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "redes-flujo-maximo-corte-minimo-pareos-petri.png")
    plt.savefig(out_path, dpi=180, bbox_inches='tight', facecolor='white')
    plt.close()


if __name__ == "__main__":
    main()
