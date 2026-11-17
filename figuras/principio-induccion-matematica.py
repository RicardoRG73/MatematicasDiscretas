import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches


def main():
    fig, ax = plt.subplots(figsize=(13.0, 6.6), dpi=180)
    ax.set_xlim(0, 13.0)
    ax.set_ylim(0, 6.6)
    ax.axis('off')

    # Title
    ax.text(
        6.5, 6.26,
        r"Principio de Inducción Matemática sobre un Predicado $P(n)$ para todo $n \in \mathbb{N}$",
        ha='center', va='center', fontsize=13.6, fontweight='bold', color='#0f172a'
    )
    ax.text(
        6.5, 5.9,
        r"Demostración formal de la proposición universal $\forall n \geq n_0\; P(n)$ en dos etapas rigurosas (analogía del efecto dominó)",
        ha='center', va='center', fontsize=10.0, color='#334155'
    )

    # Top Left: Step 1 (Base Case)
    rect_b = patches.FancyBboxPatch(
        (0.35, 3.1), 5.9, 2.45,
        boxstyle="round,pad=0.06",
        facecolor='#ecfdf5', edgecolor='#059669', linewidth=1.8
    )
    ax.add_patch(rect_b)
    ax.text(3.3, 5.26, r"Etapa 1: Paso Básico (Base de la Inducción)",
            ha='center', va='center', fontsize=10.6, fontweight='bold', color='#047857')
    ax.plot([0.55, 6.05], [5.02, 5.02], color='#059669', linewidth=1.1, alpha=0.6)

    b_lines = [
        r"• Objetivo: Verificar directamente que el predicado $P(n)$ es verdadero",
        r"  para el valor inicial $n = n_0$ (habitualmente $n_0 = 1$ o $n_0 = 0$).",
        r"• En sumatorias $x_1 + x_2 + \dots + t(n) = R(n)$:",
        r"  Se sustituye $n = 1$ en el término $n$-ésimo $t(1)$ y en la fórmula $R(1)$,",
        r"  comprobando que $t(1) = x_1 = R(1)$."
    ]
    for i, line in enumerate(b_lines):
        ax.text(0.55, 4.7 - i * 0.36, line, ha='left', va='center', fontsize=8.8, color='#0f172a')

    # Top Right: Step 2 (Inductive Step)
    rect_i = patches.FancyBboxPatch(
        (6.75, 3.1), 5.9, 2.45,
        boxstyle="round,pad=0.06",
        facecolor='#eff6ff', edgecolor='#2563eb', linewidth=1.8
    )
    ax.add_patch(rect_i)
    ax.text(9.7, 5.26, r"Etapa 2: Paso Inductivo ($P(n) \rightarrow P(n+1)$)",
            ha='center', va='center', fontsize=10.6, fontweight='bold', color='#1d4ed8')
    ax.plot([6.95, 12.45], [5.02, 5.02], color='#2563eb', linewidth=1.1, alpha=0.6)

    i_lines = [
        r"• Hipótesis Inductiva (H.I.): Se supone que $P(n)$ es verdadera para un $n$ fijo.",
        r"• Tesis Inductiva: Se demuestra que $P(k)$ también se cumple para $k = n + 1$.",
        r"• En sumatorias: Se suma el término $t(n+1)$ a ambos lados de la H.I.:",
        r"  $[x_1 + \dots + t(n)] + t(n+1) = R(n) + t(n+1)$",
        r"  y se factoriza algebraicamente hasta obtener exactamente $R(n+1) = R(k)$."
    ]
    for i, line in enumerate(i_lines):
        ax.text(6.95, 4.7 - i * 0.36, line, ha='left', va='center', fontsize=8.8, color='#0f172a')

    # Bottom Panel: Domino Chain & Logical Inference Rule of Mathematical Induction
    rect_d = patches.FancyBboxPatch(
        (0.35, 0.35), 12.3, 2.42,
        boxstyle="round,pad=0.06",
        facecolor='#fffbeb', edgecolor='#d97706', linewidth=1.8
    )
    ax.add_patch(rect_d)
    ax.text(
        6.5, 2.5,
        r"Esquema Lógico de Inferencia de la Inducción:   $[P(1) \;\wedge\; \forall n\,(P(n) \rightarrow P(n+1))] \;\Rightarrow\; \forall n \in \mathbb{N}\, P(n)$",
        ha='center', va='center', fontsize=10.4, fontweight='bold', color='#b45309'
    )

    # Draw domino chain boxes
    dominoes = [
        (0.75, r"$P(1) = 1$", "Paso Básico\n(verificado)", '#dcfce7', '#16a34a'),
        (3.15, r"$P(2) = 1$", r"Por Modus Ponens:" + "\n" + r"$P(1) \wedge (P(1)\rightarrow P(2))$", '#dbeafe', '#2563eb'),
        (5.55, r"$P(3) = 1$", r"Por Modus Ponens:" + "\n" + r"$P(2) \wedge (P(2)\rightarrow P(3))$", '#dbeafe', '#2563eb'),
        (7.95, r"$P(n) = 1$", "Hipótesis\nInductiva (H.I.)", '#fef3c7', '#d97706'),
        (10.35, r"$P(n+1) = 1$", "Tesis Inductiva\n" + r"$k = n + 1$", '#f3e8ff', '#9333ea'),
    ]

    for idx, (dx, top_txt, sub_txt, dbg, dcol) in enumerate(dominoes):
        dbox = patches.FancyBboxPatch(
            (dx, 0.62), 1.85, 1.45,
            boxstyle="round,pad=0.04",
            facecolor=dbg, edgecolor=dcol, linewidth=1.6
        )
        ax.add_patch(dbox)
        ax.text(dx + 0.925, 1.72, top_txt, ha='center', va='center', fontsize=9.8, fontweight='bold', color='#0f172a')
        ax.plot([dx + 0.15, dx + 1.7], [1.45, 1.45], color=dcol, linewidth=1.0, alpha=0.6)
        ax.text(dx + 0.925, 1.02, sub_txt, ha='center', va='center', fontsize=8.0, color='#1e293b')

        if idx < len(dominoes) - 1:
            ax.annotate(
                "", xy=(dx + 2.32, 1.35), xytext=(dx + 1.92, 1.35),
                arrowprops=dict(arrowstyle="->", color='#b45309', lw=2.0)
            )

    plt.tight_layout()
    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "principio-induccion-matematica.png")
    plt.savefig(out_path, dpi=180, bbox_inches='tight', facecolor='white')
    plt.close()


if __name__ == "__main__":
    main()
