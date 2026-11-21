---
marp: true
theme: discretas
size: 16:9
paginate: true
math: mathjax
header: "Matemáticas Discretas · Unidad 5"
footer: "Unidad 5 · Relaciones"
---
<!-- _class: portada -->
<!-- _paginate: false -->
<!-- _header: "" -->
<!-- _footer: "" -->

# Unidad 5: Relaciones
## Panorama general, subtemas y aplicaciones computacionales

- **Asignatura:** Matemáticas Discretas (`LISSI0211` · Segundo Semestre)
- **Duración de la unidad:** 10 horas
- **Competencia:** Comprender el uso de relaciones en el diseño de problemas computacionales mediante bases de datos, estructuras de datos y grafos para optimizar la gestión de la información.

---

## Introducción a la Unidad

- **Carl Friedrich Gauss ($1777\text{–}1855$):** *«Las matemáticas no se ocupan más que de la enumeración y comparación de relaciones»*.
- **Concepto formal:** Correspondencia matemática que vincula elementos de dos o más conjuntos según una regla o propiedad.
- **Fundamentos modernos:** Par ordenado $(a, b)$, producto cartesiano $A \times B$ y relación como conjunto de tuplas (Peirce, Schröder, Frege, Kuratowski y Wiener).
- **Edgar Frank Codd ($1970$):** Impulsó el **modelo relacional de bases de datos** y el álgebra relacional.

---

## Relevancia en Ciencias de la Computación

- **Bases de datos relacionales (RDBMS):** Tablas como relaciones $n$-arias $R \subseteq D_1 \times D_2 \times \dots \times D_n$, llaves y consultas SQL ($\cup, \cap, -, \sigma, \pi$, *join*).
- **Estructuras de datos dinámicas:** Listas enlazadas simples y dobles, pilas, colas, árboles y grafos mediante apuntadores.
- **Redes y sistemas distribuidos:** Conectividad bidireccional y transitiva con relaciones de equivalencia, cerraduras y particiones.
- **Programación, criptografía y compiladores:** Subrutinas, recursividad, composición, invertibilidad y funciones *hash* en $O(1)$.

---
<!-- _class: seccion -->
<!-- _header: "" -->
<!-- _footer: "" -->

## Mapa de Contenidos de la Unidad 5

Cinco subtemas que conectan la teoría de conjuntos con el diseño de software y datos.

---

## Subtema 5.1 · Conceptos básicos

- **5.1.1 Producto cartesiano:**
  - Pares ordenados $(a, b)$, definición de $A \times B$, no conmutatividad ($A \times B \neq B \times A$), cardinalidad $|A \times B| = |A| \cdot |B|$ y $n$-tuplas.
- **5.1.2 Relación binaria:**
  - Subconjunto $R \subseteq A \times B$ ($2^{|A|\cdot|B|}$ posibles), dominio $\operatorname{Dom}(R)$, codominio $\operatorname{Cod}(R)$ y operaciones ($\cup, \cap, ', ^{-1}, \circ$).
- **5.1.3 Representación de relaciones:**
  - Conjuntos (extensión y comprensión), tablas, diagramas de flechas, matriz booleana $M_R$ y grafo dirigido (dígrafo).

---

## Subtemas 5.2 y 5.3 · Propiedades y Equivalencia

- **5.2 Propiedades de las relaciones:**
  - Caracterización lógica, matricial y en dígrafos sobre $A$: **Reflexiva** ($I \subseteq R$), **Irreflexiva** ($R \cap I = \emptyset$), **Simétrica** ($R = R^{-1}$), **Asimétrica** ($R \cap R^{-1} = \emptyset$), **Antisimétrica** ($R \cap R^{-1} \subseteq I$) y **Transitiva** ($M_R = M_R + M_R^2$).
  - Leyes algebraicas y conjuntos parcialmente ordenados (*posets*).
- **5.3 Relaciones de equivalencia:**
  - **Cerraduras** ($R_r, R_s, R^*$ por $M_R \leftarrow M_R \cup M_R^2$ y Warshall).
  - **Clases de equivalencia** $[a]$, congruencia módulo $m$, **particiones** $X = \{A_1, \dots, A_k\}$ y subgrafos completos disjuntos.

---

## Subtemas 5.4 y 5.5 · Funciones y Aplicaciones

- **5.4 Funciones:**
  - Relación especial $f: A \to B$ con $\operatorname{Dom}(f) = A$ y unicidad; criterio de la recta vertical y conteo combinatorio.
  - Clasificación (**Inyectiva**, **Suprayectiva**, **Biyectiva**), composición $(g \circ f)$ y funciones invertibles ($f^{-1}$).
- **5.5 Aplicaciones en computación:**
  - Listas enlazadas simples y dobles ($A$ y apuntadores $P$) con altas y bajas.
  - Álgebra relacional en bases de datos (selección, unión, intersección y proyección).
  - Subrutinas, $\lfloor x \rfloor$, $\lceil x \rceil$, tablas *hash* ($h(k) = k \bmod m$) y cifrado biyectivo modular.

---
<!-- _class: compacta -->

## Bibliografía de Referencia

- **Jiménez Murillo, J. A.** (2012). *Matemáticas para la computación* (2.ª ed., Cap. 6: Relaciones, pp. 218–283). Alfaomega.
- **Lipschutz, S., & Lipson, M.** (2009). *Matemáticas discretas* (3.ª ed., Caps. 2, 3 y 14). McGraw-Hill.
- **Johnsonbaugh, R.** (2005). *Matemáticas discretas* (6.ª ed., Cap. 3: Relaciones, pp. 116–164). Pearson Educación.
- **Epp, S. S.** (2012). *Matemáticas discretas con aplicaciones* (4.ª ed., Caps. 7 y 8, pp. 383–515). Cengage Learning.
- **Rosen, K. H.** (2004). *Matemática discreta y sus aplicaciones* (5.ª ed., Cap. 7: Relaciones). McGraw-Hill.
