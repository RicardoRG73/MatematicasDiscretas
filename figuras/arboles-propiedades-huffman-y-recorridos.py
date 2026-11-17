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


def draw_tnode(ax, x, y, lbl, bg='#dbeafe', border='#1d4ed8', tcol='#1e3a8a', r=0.18):
    ax.add_patch(patches.Circle((x, y), r, facecolor=bg, edgecolor=border, linewidth=1.6, zorder=5))
    ax.text(x, y, lbl, ha='center', va='center', fontsize=8.4, fontweight='bold', color=tcol, zorder=6)


def main():
    fig, ax = plt.subplots(figsize=(13.6, 8.2), dpi=180)
    ax.set_xlim(0, 13.6)
    ax.set_ylim(0, 8.2)
    ax.axis('off')

    # Main Title
    ax.text(
        6.8, 7.88,
        "Árboles: Componentes, Propiedades, Clasificación, Árboles con Peso (Huffman, MST) y Recorridos",
        ha='center', va='center', fontsize=13.4, fontweight='bold', color='#0f172a'
    )
    ax.text(
        6.8, 7.52,
        r"Definición: Un árbol es un grafo conexo sin ciclos, lazos ni lados paralelos ($|L| = |V| - 1$)   |   Estructura jerárquica por niveles desde la raíz",
        ha='center', va='center', fontsize=9.5, color='#334155'
    )

    # Panel 1: Componentes y Propiedades de un Árbol (Top-Left)
    draw_panel(ax, 0.25, 4.15, 6.45, 3.1, "1. Componentes, Niveles y Propiedades de un Árbol Enraizado", '#eff6ff', '#2563eb', '#1d4ed8')
    # Draw sample rooted tree on left side of Panel 1
    tn = {
        "a": (1.65, 6.42),
        "b": (0.85, 5.72), "c": (1.65, 5.72), "d": (2.45, 5.72),
        "e": (0.55, 5.02), "f": (1.15, 5.02), "g": (1.65, 5.02), "h": (2.25, 5.02),
        "j": (0.85, 4.38), "k": (1.45, 4.38),
    }
    tedges = [("a", "b"), ("a", "c"), ("a", "d"), ("b", "e"), ("b", "f"), ("c", "g"), ("d", "h"), ("f", "j"), ("f", "k")]
    for u, v in tedges:
        ax.plot([tn[u][0], tn[v][0]], [tn[u][1], tn[v][1]], color='#475569', lw=1.6, zorder=2)

    leaves = {"e", "g", "h", "j", "k"}
    for k, (px, py) in tn.items():
        if k == "a":
            draw_tnode(ax, px, py, k, bg='#fef3c7', border='#d97706', tcol='#92400e', r=0.17)
        elif k in leaves:
            draw_tnode(ax, px, py, k, bg='#d1fae5', border='#059669', tcol='#065f46', r=0.17)
        else:
            draw_tnode(ax, px, py, k, bg='#dbeafe', border='#2563eb', tcol='#1e3a8a', r=0.17)

    # Level lines
    for lvl, ly in [(0, 6.42), (1, 5.72), (2, 5.02), (3, 4.38)]:
        ax.text(2.88, ly, f"Nivel {lvl}", ha='left', va='center', fontsize=7.5, fontweight='bold', color='#64748b')

    p1_notes = [
        r"$\bullet$ Raíz ($a$, nivel $0$): único nodo sin padre.",
        r"$\bullet$ Padre e Hijos: $b$ es padre de $\{e, f\}$.",
        r"$\bullet$ Hojas (verdes): nodos sin hijos $\{e,g,h,j,k\}$.",
        r"$\bullet$ Vértices internos: no son hojas $\{a,b,c,d,f\}$.",
        r"$\bullet$ Antecesores de $k$: $\{f, b, a\}$.",
        r"$\bullet$ Altura $h = 3$ (máximo nivel de una hoja).",
        r"$\bullet$ Árbol binario completo ($i$ nodos internos):",
        r"  $\mathrm{Hojas} = i + 1, \quad \mathrm{Total\;vértices} = 2i + 1$."
    ]
    for idx, pn in enumerate(p1_notes):
        ax.text(3.52, 6.48 - idx * 0.275, pn, ha='left', va='center', fontsize=7.85, fontweight='bold' if idx == 7 else 'normal', color='#1e293b')

    # Panel 2: Árboles con Peso: Código de Huffman y Árbol Generador Mínimo (Top-Right)
    draw_panel(ax, 6.95, 4.15, 6.4, 3.1, "2. Árboles con Peso: Código de Huffman y Árbol Generador Mínimo (MST)", '#ecfdf5', '#059669', '#047857')
    p2_notes = [
        r"A) Compresión por Código de Huffman (Ejemplo 8.3):",
        r"   1. Ordenar frecuencias de menor a mayor: $t(3), m(5), d(15), s(16), e(23), a(31)$.",
        r"   2. Unir iterativamente los dos nodos de menor peso en un nodo padre con la suma:",
        r"      $3+5=8 \;\to\; 8+15=23 \;\to\; 16+23=39 \;\to\; 23+31=54 \;\to\; 39+54=93$ (raíz).",
        r"   3. Asignar bit $0$ a cada rama izquierda y bit $1$ a cada rama derecha.",
        r"      Caracteres frecuentes quedan cerca de la raíz (código libre de prefijos).",
        r"B) Árbol Generador Mínimo (MST — conecta $|V|$ nodos con peso total mínimo):",
        r"   $\bullet$ Método de Prim: Crece un solo árbol desde la arista mínima, agregando en cada",
        r"     paso la arista de menor peso $(w, x)$ con $w \in I$ (integrados) y $x \in N$ (no integrados).",
        r"   $\bullet$ Método de Kruskal: Selecciona globalmente las $|V|-1$ aristas de menor peso en",
        r"     orden ascendente cuidando que ninguna forme ciclo con las ya elegidas."
    ]
    for idx, pn in enumerate(p2_notes):
        ry = 6.50 - idx * 0.22
        w_f = 'bold' if idx in (0, 5, 6, 8) else 'normal'
        c_f = '#065f46' if idx in (0, 5) else '#1e293b'
        ax.text(7.12, ry, pn, ha='left', va='center', fontsize=7.8, fontweight=w_f, color=c_f)

    # Panel 3: Recorridos de un Árbol (Preorden, Inorden, Postorden) y Árboles de Búsqueda (Bottom)
    draw_panel(ax, 0.25, 0.3, 13.1, 3.58, "3. Recorridos de un Árbol (Preorden, Inorden, Postorden), Árboles de Expresión y Árboles Binarios de Búsqueda (ABB)", '#fffbeb', '#d97706', '#b45309')

    # Expression Tree on left of Panel 3 for (a + b) * (c - d)
    ex_nodes = {
        "*": (1.65, 2.85),
        "+": (1.0, 2.05), "-": (2.3, 2.05),
        "a": (0.65, 1.25), "b": (1.35, 1.25), "c": (1.95, 1.25), "d": (2.65, 1.25),
    }
    ex_edges = [("*", "+"), ("*", "-"), ("+", "a"), ("+", "b"), ("-", "c"), ("-", "d")]
    for u, v in ex_edges:
        ax.plot([ex_nodes[u][0], ex_nodes[v][0]], [ex_nodes[u][1], ex_nodes[v][1]], color='#475569', lw=1.7, zorder=2)
    for k, (px, py) in ex_nodes.items():
        is_op = k in ("*", "+", "-")
        draw_tnode(ax, px, py, k, bg='#fef3c7' if is_op else '#dbeafe',
                   border='#b45309' if is_op else '#1d4ed8',
                   tcol='#78350f' if is_op else '#1e3a8a', r=0.18)
    ax.text(1.65, 0.62, r"Árbol de expresión: $(a + b) \cdot (c - d)$", ha='center', va='center', fontsize=8.2, fontweight='bold', color='#92400e')

    # Three Traversals Box in center of Panel 3
    tr_box = patches.FancyBboxPatch((3.15, 0.52), 5.35, 2.75, boxstyle="round,pad=0.04", facecolor='#ffffff', edgecolor='#d97706', lw=1.4)
    ax.add_patch(tr_box)
    ax.text(5.82, 3.04, "Los Tres Recorridos Sistemáticos (Cap. 8.7 Jiménez Murillo)", ha='center', va='center', fontsize=8.6, fontweight='bold', color='#b45309')
    tr_lines = [
        r"1. Preorden (Orden Primero):   $\mathbf{Padre} \to \mathrm{Hijo\;Izq.} \to \mathrm{Hijo\;Der.}$",
        r"   Notación Polaca (Prefija):   $*\; +\; a\; b\; -\; c\; d$",
        r"2. Inorden (Orden Segundo):    $\mathrm{Hijo\;Izq.} \to \mathbf{Padre} \to \mathrm{Hijo\;Der.}$",
        r"   Notación Infija usual:        $a + b * c - d \;\;\longrightarrow\;\; (a + b) * (c - d)$",
        r"3. Postorden (Orden Final):    $\mathrm{Hijo\;Izq.} \to \mathrm{Hijo\;Der.} \to \mathbf{Padre}$",
        r"   Polaca Inversa (Postfija/RPN): $a\; b\; +\; c\; d\; -\; *$  (evaluación con Pila)"
    ]
    for idx, tl in enumerate(tr_lines):
        ry = 2.68 - idx * 0.36
        w_f = 'bold' if idx % 2 == 0 else 'normal'
        c_f = '#1e3a8a' if idx % 2 == 1 else '#0f172a'
        ax.text(3.30, ry, tl, ha='left', va='center', fontsize=7.95, fontweight=w_f, color=c_f)

    # Right Box inside Panel 3: Binary Search Trees (ABB), AVL and B-Trees
    abb_box = patches.FancyBboxPatch((8.75, 0.52), 4.38, 2.75, boxstyle="round,pad=0.04", facecolor='#ffffff', edgecolor='#2563eb', lw=1.4)
    ax.add_patch(abb_box)
    ax.text(10.94, 3.04, "Árboles de Búsqueda (ABB, AVL y Árboles B)", ha='center', va='center', fontsize=8.6, fontweight='bold', color='#1d4ed8')
    abb_lines = [
        r"$\bullet$ Regla del ABB (Secc. 8.8.1):",
        r"  Subárbol Izquierdo $<$ Padre $\leq$ Subárbol Derecho.",
        r"$\bullet$ Propiedad clave: El recorrido en INORDEN",
        r"  de un ABB entrega los datos ORDENADOS",
        r"  ascendentemente de forma automática.",
        r"$\bullet$ Complejidad de búsqueda:",
        r"  - ABB desbalanceado (peor caso): $O(n)$.",
        r"  - Árbol AVL (autobalanceado): $O(\log_2 n)$.",
        r"  - Árbol B / B+ (bases de datos en disco):",
        r"    múltiples registros por nodo, altura mínima."
    ]
    for idx, al in enumerate(abb_lines):
        ry = 2.72 - idx * 0.23
        ax.text(8.90, ry, al, ha='left', va='center', fontsize=7.75, fontweight='bold' if idx in (0, 2, 5) else 'normal', color='#1e293b')

    plt.tight_layout()
    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "arboles-propiedades-huffman-y-recorridos.png")
    plt.savefig(out_path, dpi=180, bbox_inches='tight', facecolor='white')
    plt.close()


if __name__ == "__main__":
    main()
