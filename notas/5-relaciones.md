# 5. Relaciones

## Información General de la Unidad

| Campo | Detalle |
| :--- | :--- |
| **Unidad** | 5. Relaciones |
| **Duración** | 10 horas |
| **Competencia a desarrollar** | Comprende el uso de relaciones en el diseño de problemas computacionales, utilizando conceptos de base de datos, estructuras de datos y grafos, para optimizar la gestión de la información en sistemas. |

---

## Introducción a la Unidad

Como expresó el matemático alemán **Carl Friedrich Gauss** ($1777\text{–}1855$), *«las matemáticas no se ocupan más que de la enumeración y comparación de relaciones»* (Jiménez Murillo, 2012, p. 219). En términos formales, una **relación** es una correspondencia matemática que vincula elementos de dos o más conjuntos que satisfacen una determinada regla, condición o propiedad. El concepto moderno de par ordenado $(a, b)$, producto cartesiano $A \times B$ y relación como conjunto de tuplas fue desarrollado entre finales del siglo XIX y principios del siglo XX por matemáticos como **Charles Sanders Peirce**, **Ernst Schröder**, **Gottlob Frege**, **Kazimierz Kuratowski** y **Norbert Wiener**, y en $1970$ **Edgar Frank Codd** ($1923\text{–}2003$) revolucionó la informática al publicar el **modelo relacional de bases de datos**, demostrando que toda la información empresarial y científica puede organizarse y consultarse mediante relaciones y operaciones del álgebra relacional.

En la ingeniería en sistemas computacionales y ciencias de la computación, las relaciones y las funciones constituyen el pilar estructural de:
- **Sistemas manejadores de bases de datos relacionales (RDBMS):** Tablas como relaciones $n$-arias $R \subseteq D_1 \times D_2 \times \dots \times D_n$, llaves primarias y foráneas, y consultas SQL sustentadas en operaciones de relaciones (unión, intersección, diferencia, selección, proyección y reunión o *join*).
- **Estructuras de datos dinámicas:** Listas simplemente y doblemente enlazadas, pilas, colas, árboles y grafos donde los nodos se relacionan mediante apuntadores en memoria (Jiménez Murillo, 2012, Cap. 6.7).
- **Redes de comunicación y sistemas distribuidos:** Modelado de conectividad bidireccional y transitiva entre computadoras mediante relaciones de equivalencia, cerraduras y particiones.
- **Lenguajes de programación, criptografía y compiladores:** Diseño modular mediante funciones, recursividad, composición funcional, funciones invertibles (cifrado/descifrado) y funciones de dispersión (*hashing*) para acceso en tiempo constante $O(1)$.

---

## Subtemas de la Unidad

- **[5.1 Conceptos básicos](5-1-conceptos-basicos.md)**
  - **5.1.1 Producto cartesiano:** Pares ordenados $(a, b)$, definición formal de $A \times B$, no conmutatividad ($A \times B \neq B \times A$), cardinalidad $|A \times B| = |A| \cdot |B|$ y generalización a $n$-tuplas ($A_1 \times \dots \times A_n$).
  - **5.1.2 Relación binaria:** Definición formal ($R \subseteq A \times B$, número total de relaciones $2^{|A|\cdot|B|}$), dominio $\operatorname{Dom}(R)$, codominio o rango $\operatorname{Cod}(R)$, relaciones sobre un mismo conjunto ($R \subseteq A \times A$) y operaciones entre relaciones (unión $R \cup S$, intersección $R \cap S$, complemento $R'$, inversa $R^{-1}$ y composición $R \circ S$).
  - **5.1.3 Representación de relaciones (matrices, conjuntos, grafos, diagrama de flechas):** Notación por extensión y comprensión, tablas, diagramas sagitales de flechas, matriz booleana de una relación $M_R = [m_{ij}]$ (y operaciones matriciales booleanas $\cup, \cap, ', T, \odot$) y grafo dirigido (dígrafo).
- **[5.2 Propiedades de las relaciones](5-2-propiedades-de-las-relaciones.md)**
  - Análisis formal, criterios en la matriz booleana $M_R$ y caracterización en el dígrafo de las seis propiedades fundamentales sobre un conjunto $A$: **Reflexiva** ($I \subseteq R$), **Irreflexiva** ($R \cap I = \emptyset$), **Simétrica** ($R = R^{-1}$ o $M_R = M_R^T$), **Asimétrica** ($R \cap R^{-1} = \emptyset$), **Antisimétrica** ($R \cap R^{-1} \subseteq I$) y **Transitiva** ($R^2 \subseteq R$, verificada mediante multiplicación booleana de matrices $M_R = M_R + M_R^2$), así como las leyes algebraicas de las relaciones y órdenes parciales (conjuntos parcialmente ordenados o *posets*).
- **[5.3 Relaciones de equivalencia](5-3-relaciones-de-equivalencia.md)**
  - **Cerraduras:** Cerradura reflexiva ($R_r = R \cup I$), cerradura simétrica ($R_s = R \cup R^{-1}$) y cerradura transitiva ($R^* = \bigcup_{k=1}^n R^k$ mediante el algoritmo matricial iterativo $M_R \leftarrow M_R \cup M_R^2$ y el algoritmo de Warshall).
  - **Clases de equivalencia ($[a]$):** Definición, propiedades fundamentales ($a \in [a]$, $[a] = [b] \iff (a, b) \in R$, o bien $[a] \cap [b] = \emptyset$) y congruencia módulo $m$ en $\mathbb{Z}$.
  - **Particiones:** Definición axiomática de partición $X = \{A_1, A_2, \dots, A_k\}$, Teorema Fundamental de las Relaciones de Equivalencia y representación gráfica mediante **subgrafos completos disjuntos**.
- **[5.4 Funciones](5-4-funciones.md)**
  - Definición formal de función $f: A \to B$ como relación especial ($\operatorname{Dom}(f) = A$ y unicidad de imagen), argumento, imagen $b = f(a)$ y criterio geométrico de la recta vertical.
  - Clasificación de funciones: **Inyectiva (uno a uno)**, **Suprayectiva (sobre)** y **Biyectiva (correspondencia biunívoca)**, conteo combinatorio de funciones, **composición de funciones** $(g \circ f)(a) = g(f(a))$ y **funciones invertibles** ($f^{-1}: B \to A$).
- **[5.5 Aplicaciones de las relaciones y las funciones en la computación](5-5-aplicaciones-de-las-relaciones-y-las-funciones-en-la-computacion.md)**
  - **Estructuras de datos (Listas simplemente y doblemente enlazadas):** Representación en arreglos de datos ($A$) y apuntadores ($P$), recorrido ordenado, inserción (alta) y eliminación (baja) lógica de registros (Jiménez Murillo, Cap. 6.7.1).
  - **Bases de datos relacionales y Álgebra Relacional:** Archivos/tablas como relaciones, consultas compuestas mediante máscaras booleanas de selección, unión, intersección y proyección (Jiménez Murillo, Cap. 6.7.2).
  - **Funciones en programación, tablas Hash y Criptografía:** Subrutinas parametrizadas, funciones de piso $\lfloor x \rfloor$, techo $\lceil x \rceil$ y módulo, **funciones de dispersión (*hashing*)** $h(k) = k \bmod m$ con resolución de colisiones, y cifrado biyectivo modular.

---

## Bibliografía de Referencia

- **Jiménez Murillo, J. A.** (2012). *Matemáticas para la computación* (2.ª ed., Cap. 6: Relaciones, pp. 218–283). Alfaomega.
- **Lipschutz, S., & Lipson, M.** (2009). *Matemáticas discretas* (3.ª ed., Serie Schaum, Cap. 2: Relaciones, pp. 23–42; Cap. 3: Funciones y algoritmos, pp. 43–69; Cap. 14: Conjuntos ordenados y retículos). McGraw-Hill.
- **Johnsonbaugh, R.** (2005). *Matemáticas discretas* (6.ª ed., Cap. 3: Relaciones, pp. 116–164). Pearson Educación.
- **Epp, S. S.** (2012). *Matemáticas discretas con aplicaciones* (4.ª ed., Cap. 7: Funciones, pp. 383–441; Cap. 8: Relaciones, pp. 442–515). Cengage Learning.
- **Rosen, K. H.** (2004). *Matemática discreta y sus aplicaciones* (5.ª ed., Cap. 7: Relaciones). McGraw-Hill.
