# 3. Lógica Matemática

## Información General de la Unidad

| Campo | Detalle |
| :--- | :--- |
| **Unidad** | 3. Lógica Matemática |
| **Duración** | 10 horas |
| **Competencia a desarrollar** | Analiza y resuelve problemas computacionales, aplicando técnicas de lógica e inducción matemática, para mejorar el razonamiento lógico en programación y algoritmos. |

---

## Introducción a la Unidad

La **lógica matemática** es la disciplina formal que estudia las leyes, estructuras y métodos que determinan la validez del razonamiento deductivo e inductivo. Sus raíces históricas se remontan a la *teoría silogística* de **Aristóteles** ($384\text{–}322\text{ a. C.}$) y a la lógica proposicional estoica de **Crisipo de Solos** ($281\text{–}206\text{ a. C.}$). Posteriormente, en el siglo XVII, **Gottfried Wilhelm Leibniz** concibió la idea de un lenguaje simbólico universal (*characteristica universalis*) para mecanizar el cálculo del pensamiento, proyecto que culminó en los siglos XIX y XX con el álgebra de la lógica de **George Boole** y **Augustus De Morgan**, el cálculo de predicados de **Gottlob Frege** y **Giuseppe Peano**, las tablas de verdad de **Charles Sanders Peirce** y **Ludwig Wittgenstein**, y los *Principia Mathematica* de **Alfred North Whitehead** y **Bertrand Russell** (Jiménez Murillo, 2012).

En la ingeniería en sistemas computacionales y ciencias de la computación, la lógica matemática constituye el fundamento teórico directo de:
- **Diseño y verificación de programas:** Construcción y simplificación de condiciones booleanas en estructuras de control (`if-else`, `while`, `for`), aserciones e invariantes de ciclo.
- **Sistemas digitales y arquitectura de computadoras:** Diseño de circuitos combinatorios y unidades lógico-aritméticas (ALU) mediante compuertas lógicas (Unidad 4).
- **Inteligencia artificial y sistemas expertos:** Representación del conocimiento, motores de inferencia automática, resolución lógica (Prolog) y verificación formal de sistemas (*model checking*).
- **Bases de datos y lenguajes formales:** Consultas declarativas en cálculo relacional (SQL) y especificación sintáctica/semántica en compiladores.

---

## Subtemas de la Unidad

- **[3.1 Lógica proposicional](3-1-logica-proposicional.md)**
  - **3.1.1 Concepto de proposición:** Enunciados declarativos, valor de verdad ($1$/$V$ o $0$/$F$), principio del tercero excluido y de no contradicción, proposiciones simples (atómicas) frente a expresiones que no son proposiciones, y oraciones abiertas.
  - **3.1.2 Proposiciones compuestas (Disyunción, Conjunción, Negación, Condicional, Bicondicional):** Sintaxis, semántica y traducción entre lenguaje natural y simbólico de la conjunción ($\land$), disyunción inclusiva ($\lor$), disyunción exclusiva ($\oplus$), negación ($'$ o $\neg$), condicional o implicación material ($\to$, junto con su recíproca, inversa y contrapositiva) y bicondicional ($\leftrightarrow$).
  - **3.1.3 Tablas de verdad:** Construcción sistemática para $n$ variables ($2^n$ filas en orden binario ascendente), jerarquía de precedencia de operadores lógicos y evaluación paso a paso.
  - **3.1.4 Tautologías, contradicción y contingencia:** Clasificación semántica de proposiciones compuestas e implicación tautológica ($P \Rightarrow Q$).
  - **3.1.5 Equivalencias Lógicas:** Concepto de equivalencia ($P \equiv Q$ o $P \Leftrightarrow Q$), catálogo completo de leyes del álgebra proposicional (Tabla 4.3 de Jiménez Murillo y Tabla 4-1 de Lipschutz) y simplificación o demostración algebraica de equivalencias.
  - **3.1.6 Reglas de inferencia:** Esquemas deductivos válidos (*Modus Ponens*, *Modus Tollens*, *Silogismo Hipotético*, *Silogismo Disyuntivo*, *Dilemas Constructivos*, *Adición*, *Simplificación*, *Conjunción*).
  - **3.1.7 Argumentos válidos y no válidos:** Estructura de un argumento o teorema $(p_1 \land p_2 \land \dots \land p_n) \Rightarrow q$, prueba de validez mediante tablas de verdad, falacias lógicas clásicas (*afirmación del consecuente* y *negación del antecedente*), y razonamiento deductivo frente a inductivo.
  - **3.1.8 Demostración formal (Directa, Por contradicción):** Traducción de problemas verbales a teoremas formales y demostración rigurosa línea por línea mediante el **método directo** y el **método por contradicción (reducción al absurdo)**.
- **[3.2 Lógica de predicados](3-2-logica-de-predicados.md)**
  - **3.2.1 Cuantificadores:** Limitaciones de la lógica proposicional, concepto de predicado o función proposicional $p(x)$, universo del discurso ($U$), conjunto de verdad ($T_p$), cuantificador universal ($\forall$), cuantificador existencial ($\exists$) y de unicidad ($\exists!$), y refutación mediante contraejemplo.
  - **3.2.2 Representación y evaluación de predicados:** Simbolización de enunciados categóricos, evaluación de verdad sobre dominios finitos e infinitos, **Leyes de De Morgan para cuantificadores** (negación de proposiciones cuantificadas), predicados multivariables $p(x, y)$ con cuantificadores anidados, variables libres y ligadas, y el **Principio de Inducción Matemática** sobre predicados $P(n)$ aplicado a sumatorias y verificación de algoritmos.

---

## Bibliografía de Referencia

- **Jiménez Murillo, J. A.** (2012). *Matemáticas para la computación* (2.ª ed., Cap. 4: Lógica matemática, pp. 114–175). Alfaomega.
- **Lipschutz, S., & Lipson, M.** (2009). *Matemáticas discretas* (3.ª ed., Serie Schaum, Cap. 4: Lógica y cálculo de proposiciones, pp. 70–87). McGraw-Hill.
- **Rosen, K. H.** (2004). *Matemática discreta y sus aplicaciones* (5.ª ed., Cap. 1: Los fundamentos: lógica y demostración, conjuntos y funciones, pp. 1–78; Cap. 3: Razonamiento matemático, inducción y recursividad). McGraw-Hill.
- **Epp, S. S.** (2012). *Matemáticas discretas con aplicaciones* (4.ª ed., Cap. 2: La lógica de los enunciados compuestos, pp. 23–94; Cap. 3: La lógica de enunciados cuantificados, pp. 95–144). Cengage Learning.
- **Johnsonbaugh, R.** (2005). *Matemáticas discretas* (6.ª ed., Cap. 1: Lógica y demostraciones, pp. 1–75). Pearson Educación.
