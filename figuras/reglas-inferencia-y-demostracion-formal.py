import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches


def main():
    fig, ax = plt.subplots(figsize=(13.4, 7.6), dpi=180)
    ax.set_xlim(0, 13.4)
    ax.set_ylim(0, 7.6)
    ax.axis('off')

    # Main Title
    ax.text(
        6.7, 7.28,
        "Reglas de Inferencia, Validez de Argumentos y Métodos de Demostración Formal",
        ha='center', va='center', fontsize=13.8, fontweight='bold', color='#0f172a'
    )
    ax.text(
        6.7, 6.92,
        r"Estructura de un Teorema o Argumento Deductivo:   $(p_1 \wedge p_2 \wedge \dots \wedge p_n) \Rightarrow q$   (donde $p_i$ son las Hipótesis y $q$ es la Conclusión)",
        ha='center', va='center', fontsize=10.2, color='#334155'
    )

    # Top Left: Principal Rules of Inference
    rect_inf = patches.FancyBboxPatch(
        (0.3, 3.35), 7.55, 3.3,
        boxstyle="round,pad=0.06",
        facecolor='#eff6ff', edgecolor='#2563eb', linewidth=1.8
    )
    ax.add_patch(rect_inf)
    ax.text(4.07, 6.38, "Principales Reglas de Inferencia Válidas (Esquemas Tautológicos)",
            ha='center', va='center', fontsize=10.6, fontweight='bold', color='#1d4ed8')
    ax.plot([0.48, 7.68], [6.14, 6.14], color='#2563eb', linewidth=1.1, alpha=0.6)

    rules_left = [
        (r"Modus Ponens (15):", r"$p,\;\; p \rightarrow q \;\;\vdash\;\; \therefore q$"),
        (r"Modus Tollens (16):", r"$p \rightarrow q,\;\; q' \;\;\vdash\;\; \therefore p'$"),
        (r"Silogismo Hipotético (13):", r"$p \rightarrow q,\;\; q \rightarrow r \;\;\vdash\;\; \therefore p \rightarrow r$"),
        (r"Silogismo Disyuntivo (12):", r"$p \vee q,\;\; p' \;\;\vdash\;\; \therefore q$"),
    ]
    rules_right = [
        (r"Simplificación (11):", r"$p \wedge q \;\;\vdash\;\; \therefore p$"),
        (r"Adición (10):", r"$p \;\;\vdash\;\; \therefore p \vee q$"),
        (r"Conjunción (14):", r"$p,\;\; q \;\;\vdash\;\; \therefore p \wedge q$"),
        (r"Dilema Constructivo (9a):", r"$(p \rightarrow q) \wedge (r \rightarrow s),\; p \vee r \;\vdash\; \therefore q \vee s$"),
    ]

    for idx, (name, form) in enumerate(rules_left):
        ry = 5.75 - idx * 0.68
        ax.text(0.5, ry + 0.12, name, ha='left', va='center', fontsize=8.8, fontweight='bold', color='#1e3a8a')
        ax.text(0.5, ry - 0.14, form, ha='left', va='center', fontsize=9.1, color='#0f172a')

    ax.plot([3.95, 3.95], [3.5, 6.05], color='#93c5fd', linewidth=1.2, linestyle='--')

    for idx, (name, form) in enumerate(rules_right):
        ry = 5.75 - idx * 0.68
        ax.text(4.12, ry + 0.12, name, ha='left', va='center', fontsize=8.8, fontweight='bold', color='#1e3a8a')
        ax.text(4.12, ry - 0.14, form, ha='left', va='center', fontsize=9.1, color='#0f172a')

    # Top Right: Valid vs Fallacy
    rect_fal = patches.FancyBboxPatch(
        (8.1, 3.35), 5.0, 3.3,
        boxstyle="round,pad=0.06",
        facecolor='#fef2f2', edgecolor='#dc2626', linewidth=1.8
    )
    ax.add_patch(rect_fal)
    ax.text(10.6, 6.38, "Argumentos No Válidos (Falacias Comunes)",
            ha='center', va='center', fontsize=10.6, fontweight='bold', color='#b91c1c')
    ax.plot([8.28, 12.92], [6.14, 6.14], color='#dc2626', linewidth=1.1, alpha=0.6)

    ax.text(10.6, 5.78, r"Un argumento es INVÁLIDO si existe al menos un caso",
            ha='center', va='center', fontsize=8.9, color='#1e293b')
    ax.text(10.6, 5.48, r"con Hipótesis Verdaderas ($1$) y Conclusión Falsa ($0$):",
            ha='center', va='center', fontsize=8.9, fontweight='bold', color='#b91c1c')

    box_f1 = patches.FancyBboxPatch((8.32, 4.48), 4.56, 0.78, boxstyle="round,pad=0.04",
                                    facecolor='#ffffff', edgecolor='#f87171', linewidth=1.2)
    ax.add_patch(box_f1)
    ax.text(10.6, 5.02, r"1. Falacia de Afirmación del Consecuente:",
            ha='center', va='center', fontsize=8.9, fontweight='bold', color='#991b1b')
    ax.text(10.6, 4.68, r"$[(p \rightarrow q) \wedge q] \Rightarrow p$   (Falla si $p=0,\; q=1$)",
            ha='center', va='center', fontsize=9.0, color='#1e293b')

    box_f2 = patches.FancyBboxPatch((8.32, 3.52), 4.56, 0.78, boxstyle="round,pad=0.04",
                                    facecolor='#ffffff', edgecolor='#f87171', linewidth=1.2)
    ax.add_patch(box_f2)
    ax.text(10.6, 4.06, r"2. Falacia de Negación del Antecedente:",
            ha='center', va='center', fontsize=8.9, fontweight='bold', color='#991b1b')
    ax.text(10.6, 3.72, r"$[(p \rightarrow q) \wedge p'] \Rightarrow q'$   (Falla si $p=0,\; q=1$)",
            ha='center', va='center', fontsize=9.0, color='#1e293b')

    # Bottom Left: Direct Proof Method
    rect_dir = patches.FancyBboxPatch(
        (0.3, 0.3), 6.25, 2.78,
        boxstyle="round,pad=0.06",
        facecolor='#ecfdf5', edgecolor='#059669', linewidth=1.8
    )
    ax.add_patch(rect_dir)
    ax.text(3.42, 2.82, "Método 1: Demostración Formal por el Método Directo",
            ha='center', va='center', fontsize=10.5, fontweight='bold', color='#047857')
    ax.plot([0.48, 6.38], [2.58, 2.58], color='#059669', linewidth=1.1, alpha=0.6)

    dir_steps = [
        r"Paso 1 (Líneas $1$ a $n$): Listar las hipótesis $p_1, p_2, \dots, p_n$ como verdaderas.",
        r"Paso 2 (Líneas $n+1$ a $m-1$): Aplicar reglas de inferencia, equivalencias",
        r"       lógicas y tautologías indicando línea(s) y nombre/número de regla.",
        r"Paso 3 (Línea final $m$): Obtener explícitamente la conclusión $q$.   $\blacksquare$"
    ]
    for i, st in enumerate(dir_steps):
        ax.text(0.52, 2.25 - i * 0.48, st, ha='left', va='center', fontsize=8.9, color='#0f172a')

    # Bottom Right: Proof by Contradiction
    rect_con = patches.FancyBboxPatch(
        (6.85, 0.3), 6.25, 2.78,
        boxstyle="round,pad=0.06",
        facecolor='#fdf4ff', edgecolor='#9333ea', linewidth=1.8
    )
    ax.add_patch(rect_con)
    ax.text(9.97, 2.82, "Método 2: Demostración por Contradicción (Reducción al Absurdo)",
            ha='center', va='center', fontsize=10.5, fontweight='bold', color='#7e22ce')
    ax.plot([7.03, 12.92], [2.58, 2.58], color='#9333ea', linewidth=1.1, alpha=0.6)

    con_steps = [
        r"Paso 1 (Líneas $1$ a $n$): Listar las hipótesis $p_1, p_2, \dots, p_n$.",
        r"Paso 2 (Línea $n+1$): Incluir como premisa adicional la NEGACIÓN",
        r"       de la conclusión ($q'$), suponiendo que $q$ es falsa.",
        r"Paso 3: Deducir una contradicción $(r \wedge r') \equiv 0$, probando que $q$ es verdadera."
    ]
    for i, st in enumerate(con_steps):
        ax.text(7.08, 2.25 - i * 0.48, st, ha='left', va='center', fontsize=8.9, color='#0f172a')

    plt.tight_layout()
    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "reglas-inferencia-y-demostracion-formal.png")
    plt.savefig(out_path, dpi=180, bbox_inches='tight', facecolor='white')
    plt.close()


if __name__ == "__main__":
    main()
