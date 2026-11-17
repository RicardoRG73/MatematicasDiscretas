# 2. Conjuntos

## Información General de la Unidad

| Campo | Detalle |
| :--- | :--- |
| **Unidad** | 2. Conjuntos |
| **Duración** | 10 horas |
| **Competencia a desarrollar** | Resuelve problemas que involucren operaciones y propiedades de conjuntos, usando leyes y diagramas, para facilitar la representación de datos en computación. |

---

## Introducción a la Unidad

La **teoría de conjuntos**, desarrollada formalmente a finales del siglo XIX por el matemático alemán **Georg Cantor** ($1845\text{–}1918$), constituye el lenguaje universal de las matemáticas modernas y la piedra angular de las ciencias de la computación. Prácticamente todas las estructuras computacionales discretas —desde los tipos de datos, las bases de datos relacionales (SQL), las redes y los grafos, hasta los lenguajes formales, los compiladores y los circuitos digitales— se definen, modelan y manipulan mediante conjuntos y sus operaciones.

Asimismo, el estudio de los conjuntos guarda un **isomorfismo estructural directo** con la **lógica proposicional** (Unidad 3) y el **álgebra booleana** (Unidad 4), lo que permite traducir condiciones lógicas complejas y consultas de información en expresiones algebraicas simplificables y verificables mediante diagramas de Venn.

---

## Subtemas de la Unidad

- **[2.1 Características de los conjuntos](2-1-caracteristicas-de-los-conjuntos.md)**
  - Concepto de conjunto, elementos, pertenencia ($\in, \notin$), notación por extensión y por comprensión, y cardinalidad ($|A|$).
  - **2.1.1 Conjunto universo, vacío:** El conjunto referencial $U$, el conjunto vacío $\emptyset$, conjuntos unitarios y representación gráfica mediante diagramas de Venn.
  - **2.1.2 Números naturales, enteros, racionales, reales e imaginarios:** Caracterización formal y jerarquía de $\mathbb{N}, \mathbb{Z}^+, \mathbb{Z}, \mathbb{Q}, \mathbb{I}, \mathbb{R}$, números imaginarios puros y complejos $\mathbb{C}$.
  - **2.1.3 Subconjuntos:** Inclusión ($A \subseteq B$), subconjunto propio ($A \subset B$), igualdad de conjuntos, conjuntos disjuntos y propiedades fundamentales de la inclusión.
  - **2.1.4 Conjunto potencia:** Definición de $\mathcal{P}(A)$, cardinalidad $|\mathcal{P}(A)| = 2^{|A|}$, correspondencia con cadenas binarias, familias de conjuntos y particiones.
- **[2.2 Operaciones con conjuntos (Unión, Intersección, Complemento, Diferencia y diferencia simétrica)](2-2-operaciones-con-conjuntos.md)**
  - Definición formal, lectura lógica y representación con diagramas de Venn de la unión ($A \cup B$), intersección ($A \cap B$), complemento ($A'$ o $A^c$), diferencia ($A - B$) y diferencia simétrica ($A \oplus B$).
  - Operaciones combinadas sobre universos finitos, infinitos e intervalos reales.
  - Operaciones generalizadas ($\bigcup_{i=1}^m A_i$ y $\bigcap_{i=1}^m A_i$) y regiones en diagramas de Venn con condiciones de inclusión.
- **[2.3 Propiedades de los conjuntos](2-3-propiedades-de-los-conjuntos.md)**
  - Leyes del álgebra de conjuntos: idempotencia, conmutativa, asociativa, distributiva, identidad/dominación, involución (doble negación), complementos, absorción, equivalencia y **Leyes de De Morgan**.
  - Principio de dualidad en el álgebra de conjuntos y productos fundamentales ($2^n$ minitérminos o regiones disjuntas).
  - Métodos de demostración y verificación: diagramas de Venn, tablas de pertenencia, método del elemento y **simplificación algebraica paso a paso**.
  - Equivalencia estructural entre Teoría de Conjuntos, Lógica Matemática y Álgebra Booleana.
- **[2.4 Aplicaciones de conjuntos](2-4-aplicaciones-de-conjuntos.md)**
  - Cardinalidad de conjuntos finitos y el **Principio de Inclusión-Exclusión** para $2$, $3$ y $n$ conjuntos (análisis de encuestas y auditorías de sistemas).
  - Representación computacional de conjuntos en memoria mediante **cadenas o vectores de bits (*bitmasks*)** y operaciones bit a bit en $O(1)$.
  - Aplicaciones en **Bases de Datos Relacionales** (Álgebra Relacional y consultas SQL: `UNION`, `INTERSECT`, `EXCEPT`, `JOIN`), **Lenguajes Formales / Compiladores** y **Redes / Grafos**.
  - Validez de argumentos deductivos (silogismos de Lewis Carroll) mediante diagramas de Venn.

---

## Bibliografía de Referencia

- **Jiménez Murillo, J. A.** (2012). *Matemáticas para la computación* (2.ª ed., Cap. 3: Conjuntos, pp. 72–113). Alfaomega.
- **Lipschutz, S., & Lipson, M.** (2009). *Matemáticas discretas* (3.ª ed., Serie Schaum, Cap. 1: Teoría de conjuntos, pp. 1–22). McGraw-Hill.
- **Epp, S. S.** (2012). *Matemáticas discretas con aplicaciones* (4.ª ed., Cap. 1.2 y Cap. 6: Teoría de conjuntos, pp. 6–13, 336–382). Cengage Learning.
- **Rosen, K. H.** (2004). *Matemática discreta y sus aplicaciones* (5.ª ed., Cap. 1.6 y 1.7: Conjuntos y Operaciones con conjuntos). McGraw-Hill.
- **Johnsonbaugh, R.** (2005). *Matemáticas discretas* (6.ª ed., Cap. 1.1: Conjuntos). Pearson Educación.
