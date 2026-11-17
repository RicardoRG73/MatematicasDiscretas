import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches


def main():
    fig, ax = plt.subplots(figsize=(13.2, 7.6), dpi=180)
    ax.set_xlim(0, 13.2)
    ax.set_ylim(0, 7.6)
    ax.axis('off')

    # Title
    ax.text(
        6.6, 7.28,
        "Lógica de Predicados: Cuantificadores, Conjuntos de Verdad y Leyes de Negación",
        ha='center', va='center', fontsize=13.8, fontweight='bold', color='#0f172a'
    )
    ax.text(
        6.6, 6.92,
        r"Sea $U$ el Universo del Discurso y $p(x)$ una función proposicional con conjunto de verdad $T_p = \{x \in U \mid p(x)\text{ es verdadera}\}$",
        ha='center', va='center', fontsize=10.1, color='#334155'
    )

    # Top Left: Universal Quantifier
    rect_u = patches.FancyBboxPatch(
        (0.3, 3.65), 6.15, 2.95,
        boxstyle="round,pad=0.06",
        facecolor='#eff6ff', edgecolor='#2563eb', linewidth=1.8
    )
    ax.add_patch(rect_u)
    ax.text(3.37, 6.32, r"1. Cuantificador Universal:   $\forall x\, p(x)$   («Para todo $x \in U$»)",
            ha='center', va='center', fontsize=10.6, fontweight='bold', color='#1d4ed8')
    ax.plot([0.48, 6.27], [6.08, 6.08], color='#2563eb', linewidth=1.1, alpha=0.6)

    u_lines = [
        r"• Lectura: «Para todo $x$», «Todo $x$», «Cada $x$», «Cualquiera que sea $x$».",
        r"• Condición de verdad: Verdadera ($1$) si y sólo si $T_p = U$",
        r"  (es decir, $p(a)$ se cumple para TODOS los elementos $a \in U$).",
        r"• Equivalencia en dominio finito $U = \{a_1, a_2, \dots, a_n\}$:",
        r"  $\forall x\, p(x) \;\equiv\; p(a_1) \wedge p(a_2) \wedge \dots \wedge p(a_n)$   (Conjunción reiterada).",
        r"• Refutación: Basta un solo CONTRAEJEMPLO $x_0 \in U$ tal que $p'(x_0) = 1$."
    ]
    for i, line in enumerate(u_lines):
        ax.text(0.48, 5.75 - i * 0.37, line, ha='left', va='center', fontsize=8.8, color='#0f172a')

    # Top Right: Existential Quantifier
    rect_e = patches.FancyBboxPatch(
        (6.75, 3.65), 6.15, 2.95,
        boxstyle="round,pad=0.06",
        facecolor='#ecfdf5', edgecolor='#059669', linewidth=1.8
    )
    ax.add_patch(rect_e)
    ax.text(9.82, 6.32, r"2. Cuantificador Existencial:   $\exists x\, p(x)$   («Existe algún $x \in U$»)",
            ha='center', va='center', fontsize=10.6, fontweight='bold', color='#047857')
    ax.plot([6.93, 12.72], [6.08, 6.08], color='#059669', linewidth=1.1, alpha=0.6)

    e_lines = [
        r"• Lectura: «Existe al menos un $x$», «Para algún $x$», «Algunos $x$».",
        r"• Condición de verdad: Verdadera ($1$) si y sólo si $T_p \neq \emptyset$",
        r"  (es decir, existe por lo menos un testigo $x_0 \in U$ tal que $p(x_0) = 1$).",
        r"• Equivalencia en dominio finito $U = \{a_1, a_2, \dots, a_n\}$:",
        r"  $\exists x\, p(x) \;\equiv\; p(a_1) \vee p(a_2) \vee \dots \vee p(a_n)$   (Disyunción reiterada).",
        r"• Existencia única ($\exists! x\, p(x)$): Existe exactamente un único $x \in U$ que cumple $p(x)$."
    ]
    for i, line in enumerate(e_lines):
        ax.text(6.93, 5.75 - i * 0.37, line, ha='left', va='center', fontsize=8.8, color='#0f172a')

    # Bottom Left: De Morgan for Quantifiers & Categorical Translations
    rect_dm = patches.FancyBboxPatch(
        (0.3, 0.3), 6.15, 3.05,
        boxstyle="round,pad=0.06",
        facecolor='#fffbeb', edgecolor='#d97706', linewidth=1.8
    )
    ax.add_patch(rect_dm)
    ax.text(3.37, 3.07, "3. Negación de Cuantificadores y Enunciados Categóricos",
            ha='center', va='center', fontsize=10.5, fontweight='bold', color='#b45309')
    ax.plot([0.48, 6.27], [2.83, 2.83], color='#d97706', linewidth=1.1, alpha=0.6)

    dm_lines = [
        r"• Leyes de De Morgan generalizadas (estándar lógico universal):",
        r"  $\neg [\forall x\, p(x)] \;\equiv\; \exists x\, \neg p(x)$     («No todos cumplen $p$» $\equiv$ «Alguno no cumple $p$»)",
        r"  $\neg [\exists x\, p(x)] \;\equiv\; \forall x\, \neg p(x)$     («No existe quien cumpla $p$» $\equiv$ «Ninguno cumple $p$»)",
        r"• Representación de enunciados categóricos de Aristóteles en $U$:",
        r"  Todo $A$ es $B$:  $\forall x\, [A(x) \rightarrow B(x)]$      |      Algún $A$ es $B$:  $\exists x\, [A(x) \wedge B(x)]$",
        r"  Ningún $A$ es $B$:  $\forall x\, [A(x) \rightarrow B'(x)]$   |      Algún $A$ no es $B$:  $\exists x\, [A(x) \wedge B'(x)]$"
    ]
    for i, line in enumerate(dm_lines):
        ax.text(0.48, 2.52 - i * 0.38, line, ha='left', va='center', fontsize=8.7, color='#0f172a')

    # Bottom Right: Multiple / Nested Quantifiers
    rect_mq = patches.FancyBboxPatch(
        (6.75, 0.3), 6.15, 3.05,
        boxstyle="round,pad=0.06",
        facecolor='#fdf4ff', edgecolor='#9333ea', linewidth=1.8
    )
    ax.add_patch(rect_mq)
    ax.text(9.82, 3.07, r"4. Predicados Multivariables $p(x, y)$ y Cuantificadores Anidados",
            ha='center', va='center', fontsize=10.5, fontweight='bold', color='#7e22ce')
    ax.plot([6.93, 12.72], [2.83, 2.83], color='#9333ea', linewidth=1.1, alpha=0.6)

    mq_lines = [
        r"• Conmutatividad de cuantificadores del MISMO tipo (conservando orden en $p(x,y)$):",
        r"  $\forall x \forall y\, p(x, y) \;\equiv\; \forall y \forall x\, p(x, y)$       y       $\exists x \exists y\, p(x, y) \;\equiv\; \exists y \exists x\, p(x, y)$",
        r"• Importancia del orden en cuantificadores MIXTOS y en parámetros:",
        r"  En general:   $\forall x \exists y\, p(x, y)$  (para cada $x$ hay un $y$ que puede depender de $x$)",
        r"  frente a:       $\exists y \forall x\, p(x, y)$  (existe un mismo $y$ fijo que sirve para todos los $x$).",
        r"• Además, si los conjuntos o la relación no son simétricos: $p(x, y) \neq p(y, x)$."
    ]
    for i, line in enumerate(mq_lines):
        ax.text(6.93, 2.52 - i * 0.38, line, ha='left', va='center', fontsize=8.7, color='#0f172a')

    plt.tight_layout()
    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cuantificadores-y-logica-de-predicados.png")
    plt.savefig(out_path, dpi=180, bbox_inches='tight', facecolor='white')
    plt.close()


if __name__ == "__main__":
    main()
