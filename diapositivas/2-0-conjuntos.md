---
marp: true
theme: discretas
size: 16:9
paginate: true
math: mathjax
header: "Matemáticas Discretas · Unidad 2"
footer: "Unidad 2 · Panorama general de Conjuntos"
---
<!-- _class: portada -->
<!-- _paginate: false -->
<!-- _header: "" -->
<!-- _footer: "" -->

# Unidad 2. Conjuntos
## Panorama general, competencias y mapa temático

- **Asignatura:** Matemáticas Discretas (`LISSI0211` · Segundo Semestre)
- **Duración:** 10 horas
- **Competencia:** Resuelve problemas con operaciones y propiedades de conjuntos, usando leyes y diagramas, para facilitar la representación de datos en computación.

---

## Introducción a la Teoría de Conjuntos

- Desarrollada formalmente a finales del siglo XIX por **Georg Cantor** ($1845\text{–}1918$).
- Constituye el lenguaje universal de las matemáticas modernas y la base de las ciencias de la computación.
- Sustenta estructuras clave: tipos de datos, bases de datos relacionales (SQL), redes, grafos, lenguajes formales, compiladores y circuitos digitales.
- Presenta un **isomorfismo estructural directo** con la **lógica proposicional** (Unidad 3) y el **álgebra booleana** (Unidad 4).
- Permite traducir condiciones complejas y consultas en expresiones simplificables y verificables mediante diagramas de Venn.

---

## Subtema 2.1: Características de los Conjuntos

- Concepto de conjunto, pertenencia ($\in, \notin$), especificación por extensión/comprensión y cardinalidad ($|A|$).
- **2.1.1 Universo y vacío:** conjunto referencial $U$, vacío $\emptyset$, unitarios y diagramas de Venn.
- **2.1.2 Conjuntos numéricos:** $\mathbb{N}, \mathbb{Z}^+, \mathbb{Z}, \mathbb{Q}, \mathbb{I}, \mathbb{R}$, imaginarios puros y complejos $\mathbb{C}$.
- **2.1.3 Subconjuntos:** inclusión ($A \subseteq B$), subconjunto propio ($A \subset B$), igualdad y disjuntos.
- **2.1.4 Conjunto potencia:** $\mathcal{P}(A)$, $|\mathcal{P}(A)| = 2^{|A|}$, cadenas binarias, familias y particiones.

---

## Subtemas 2.2 y 2.3: Operaciones y Propiedades

- **2.2 Operaciones con conjuntos:**
  - Unión ($A \cup B$), intersección ($A \cap B$), complemento ($A'$), diferencia ($A - B$) y diferencia simétrica ($A \oplus B$).
  - Universos finitos, infinitos, intervalos reales y operaciones generalizadas ($\bigcup_{i=1}^m A_i$, $\bigcap_{i=1}^m A_i$).
- **2.3 Propiedades de los conjuntos:**
  - Leyes del álgebra de conjuntos (idempotencia, distributiva, absorción, equivalencia y **Leyes de De Morgan**).
  - Principio de dualidad, $2^n$ productos fundamentales y equivalencia con Lógica y Álgebra Booleana.
  - Verificación y demostración: Venn, tablas de pertenencia, método del elemento y simplificación algebraica.

---

## Subtema 2.4: Aplicaciones de Conjuntos

- **Conteo finito y Principio de Inclusión-Exclusión:** fórmulas para $2, 3$ y $n$ conjuntos (encuestas y auditorías).
- **Representación en memoria:** cadenas o vectores de bits (*bitmasks*) y operaciones bit a bit en $O(1)$.
- **Bases de datos relacionales (SQL):** traducción a `UNION`, `INTERSECT`, `EXCEPT` y `JOIN`.
- **Lenguajes formales, redes y lógica:** alfabetos, gramáticas, grafos y validez de silogismos (Lewis Carroll) con diagramas de Venn.

---

<!-- _class: compacta -->

## Bibliografía de Referencia

- **Jiménez Murillo, J. A.** (2012). *Matemáticas para la computación* (2.ª ed., Cap. 3: Conjuntos, pp. 72–113). Alfaomega.
- **Lipschutz, S., & Lipson, M.** (2009). *Matemáticas discretas* (3.ª ed., Serie Schaum, Cap. 1: Teoría de conjuntos, pp. 1–22). McGraw-Hill.
- **Epp, S. S.** (2012). *Matemáticas discretas con aplicaciones* (4.ª ed., Cap. 1.2 y Cap. 6, pp. 6–13, 336–382). Cengage Learning.
- **Rosen, K. H.** (2004). *Matemática discreta y sus aplicaciones* (5.ª ed., Cap. 1.6 y 1.7). McGraw-Hill.
- **Johnsonbaugh, R.** (2005). *Matemáticas discretas* (6.ª ed., Cap. 1.1: Conjuntos). Pearson Educación.
