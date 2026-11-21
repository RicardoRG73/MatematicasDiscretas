---
marp: true
theme: discretas
size: 16:9
paginate: true
math: mathjax
header: "Matemáticas Discretas · Unidad 3"
footer: "Unidad 3 · Lógica Matemática"
---
<!-- _class: portada -->
<!-- _paginate: false -->
<!-- _header: "" -->
<!-- _footer: "" -->

# Unidad 3: Lógica Matemática
## Fundamentos del razonamiento formal, proposiciones, predicados e inducción

- **Asignatura:** Matemáticas Discretas (`LISSI0211`) · Segundo Semestre
- **Duración:** 10 horas
- **Competencia:** Analiza y resuelve problemas computacionales, aplicando técnicas de lógica e inducción matemática, para mejorar el razonamiento lógico en programación y algoritmos.

---

## Información General y Definición

| Campo | Detalle |
| :--- | :--- |
| **Unidad** | 3. Lógica Matemática |
| **Duración** | 10 horas |
| **Competencia** | Analiza y resuelve problemas computacionales, aplicando técnicas de lógica e inducción matemática, para mejorar el razonamiento lógico en programación y algoritmos. |

- **Lógica matemática:** Disciplina formal que estudia las leyes, estructuras y métodos que determinan la validez del **razonamiento deductivo e inductivo**.

---

## Evolución Histórica de la Lógica

- **Antigüedad:** **Aristóteles** ($384\text{–}322\text{ a. C.}$, *teoría silogística*) y **Crisipo de Solos** ($281\text{–}206\text{ a. C.}$, lógica proposicional estoica).
- **Siglo XVII:** **G. W. Leibniz** propuso un lenguaje simbólico universal (*characteristica universalis*) para mecanizar el pensamiento.
- **Siglo XIX:** **G. Boole** y **A. De Morgan** crearon el álgebra de la lógica; **G. Frege** y **G. Peano** fundaron el cálculo de predicados.
- **Siglos XIX–XX:** **C. S. Peirce** y **L. Wittgenstein** consolidaron las tablas de verdad; **Whitehead** y **Russell** publicaron *Principia Mathematica*.

---

## Importancia en Sistemas Computacionales

- **Diseño y verificación de programas:** Condiciones booleanas (`if-else`, `while`, `for`), aserciones e invariantes de ciclo.
- **Sistemas digitales y arquitectura:** Circuitos combinatorios y unidades lógico-aritméticas (ALU) mediante compuertas lógicas (Unidad 4).
- **Inteligencia artificial y sistemas expertos:** Representación del conocimiento, motores de inferencia, resolución (Prolog) y *model checking*.
- **Bases de datos y lenguajes formales:** Consultas declarativas en cálculo relacional (SQL) y especificación sintáctica/semántica en compiladores.

---

## Mapa Temático · 3.1 Lógica Proposicional (1/2)

- **3.1.1 Concepto de proposición:** Enunciados declarativos, valor de verdad ($1/V$ o $0/F$), principios lógicos, proposiciones simples y oraciones abiertas.
- **3.1.2 Proposiciones compuestas:** Sintaxis, semántica y traducción de $\land$, $\lor$, $\oplus$, $'$ ($\neg$), $\to$ (recíproca, inversa, contrapositiva) y $\leftrightarrow$.
- **3.1.3 Tablas de verdad:** Construcción para $n$ variables ($2^n$ filas en orden binario ascendente) y jerarquía de precedencia.
- **3.1.4 Tautologías, contradicción y contingencia:** Clasificación semántica e implicación tautológica ($P \Rightarrow Q$).

---

## Mapa Temático · 3.1 Lógica Proposicional (2/2)

- **3.1.5 Equivalencias lógicas:** Relación $P \equiv Q$ ($P \Leftrightarrow Q$), catálogo de leyes del álgebra proposicional y demostración algebraica.
- **3.1.6 Reglas de inferencia:** *Modus Ponens*, *Modus Tollens*, *Silogismo Hipotético*, *Silogismo Disyuntivo*, *Dilemas Constructivos*, *Adición*, *Simplificación* y *Conjunción*.
- **3.1.7 Argumentos válidos y no válidos:** Estructura $(p_1 \land \dots \land p_n) \Rightarrow q$, tablas de verdad, falacias clásicas y deducción frente a inducción.
- **3.1.8 Demostración formal:** Traducción a teoremas y prueba línea por línea mediante el **método directo** y **por contradicción**.

---

## Mapa Temático · 3.2 Lógica de Predicados

- **3.2.1 Cuantificadores:**
  - Predicados $p(x)$, universo del discurso ($U$) y conjunto de verdad ($T_p$).
  - Cuantificadores universal ($\forall$), existencial ($\exists$) y de unicidad ($\exists!$), y refutación por contraejemplo.
- **3.2.2 Representación y evaluación de predicados:**
  - Enunciados categóricos, evaluación sobre dominios finitos/infinitos y **Leyes de De Morgan** para cuantificadores.
  - Predicados multivariables $p(x, y)$, cuantificadores anidados, variables libres/ligadas e **Inducción Matemática** sobre $P(n)$.

---

## Bibliografía de Referencia

- **Jiménez Murillo, J. A.** (2012). *Matemáticas para la computación* (2.ª ed., Cap. 4, pp. 114–175). Alfaomega.
- **Lipschutz, S., & Lipson, M.** (2009). *Matemáticas discretas* (3.ª ed., Serie Schaum, Cap. 4, pp. 70–87). McGraw-Hill.
- **Rosen, K. H.** (2004). *Matemática discreta y sus aplicaciones* (5.ª ed., Caps. 1 y 3). McGraw-Hill.
- **Epp, S. S.** (2012). *Matemáticas discretas con aplicaciones* (4.ª ed., Caps. 2 y 3). Cengage Learning.
- **Johnsonbaugh, R.** (2005). *Matemáticas discretas* (6.ª ed., Cap. 1, pp. 1–75). Pearson Educación.
