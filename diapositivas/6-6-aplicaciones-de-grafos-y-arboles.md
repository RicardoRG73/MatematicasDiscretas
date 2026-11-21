---
marp: true
theme: discretas
size: 16:9
paginate: true
math: mathjax
header: "Matemáticas Discretas · Unidad 6"
footer: "Subtema 6.6 · Aplicaciones de grafos y árboles"
---
<!-- _class: portada -->
<!-- _paginate: false -->
<!-- _header: "" -->
<!-- _footer: "" -->

# 6.6 Aplicaciones de grafos y árboles

## Agrupamiento por similaridad, telecomunicaciones, coloración e indexación en BD

- **Unidad 6:** Teoría de Grafos · **Asignatura:** Matemáticas Discretas (`LISSI0211`)
- **Objetivos:** aplicar grafos de similaridad al agrupamiento de datos; modelar redes, frecuencias y horarios mediante grafos y coloración; y utilizar árboles ABB, AVL y Árboles B para deduplicación e indexación eficiente.

---

## 1. Agrupamiento mediante Grafos de Similaridad

En ciencia de datos, bioinformática y *machine learning*, se busca agrupar $n$ objetos $P_1, \dots, P_n$ en clústeres homogéneos sin supervisión previa:

- **Atributos cuantitativos:** $P_x = (a_x, b_x, c_x, d_x, \dots)$.
- **Función de disimilaridad (Distancia de Manhattan / Norma $L_1$):**
  $$S(P_x - P_y) = |a_x - a_y| + |b_x - b_y| + |c_x - c_y| + |d_x - d_y| + \dots$$
- A menor valor de $S(P_x - P_y)$, **más similares** son los objetos ($S(P_x - P_x) = 0$).

---

## Construcción del Grafo de Similaridad $G_C$

1. Calcular la matriz triangular de disimilaridades para los $\frac{n(n - 1)}{2}$ pares de objetos.
2. Fijar un **umbral o cota de tolerancia $C > 0$**.
3. Construir $G_C = (V, L_C)$ con vértices $V = \{P_1, \dots, P_n\}$ y aristas:
   $$(P_x, P_y) \in L_C \iff S(P_x - P_y) < C$$
4. **Clasificación por componentes conexas:** ajustar $C$ para particionar $G_C$ en **$k$ componentes conexas disjuntas** (cada una define una clase natural).

---

<!-- _class: compacta -->

## 2. Redes de Telecomunicaciones e Infraestructura

| Problema en Ingeniería de Redes | Modelo en Grafos y Árboles | Algoritmo / Protocolo |
| :--- | :--- | :--- |
| **Enrutamiento en Internet (Estado de Enlace)** | Grafo ponderado $G = (V, L, w)$ con costo según ancho de banda o latencia | **Dijkstra** en **OSPF** e **IS-IS** |
| **Prevención de tormentas de *broadcast* LAN** | Eliminar ciclos entre *switches* conservando conectividad | **Árbol Generador (IEEE 802.1D STP)** |
| **Diseño de fibra óptica y redes eléctricas** | Conectar $n$ nodos minimizando cable o costo de instalación | **MST** mediante **Prim** o **Kruskal** |
| **Ingeniería de tráfico y cuellos de botella** | Caudal máximo entre centros de datos y enlaces críticos | **Flujo Máximo / Corte Mínimo** (Ford-Fulkerson / Edmonds-Karp) |

---

## 3. Coloración de Grafos en Ingeniería

La **coloración propia** con número cromático $\chi(G)$ modela incompatibilidades y conflictos de simultaneidad:

- **Frecuencias en telefonía celular y Wi-Fi:** vértices = antenas; aristas = áreas con interferencia co-canal; $\chi(G)$ = mínimo de canales requeridos.
- **Horarios de exámenes universitarios:** vértices = asignaturas; aristas = alumnos inscritos en ambas; colores = franjas horarias sin traslapes.
- **Registros de CPU en compiladores:** vértices = variables temporales; aristas = traslape de vida (*liveness*); colores = registros físicos para evitar *register spilling*.

---

## 4. Eliminación de Duplicados: Secuencial vs. ABB

Al depurar registros repetidos en un conjunto de $N$ claves:

- **Lista o arreglo secuencial desordenado:** cada registro $k$ se compara contra los anteriores $\implies \sum_{k=1}^{N-1} k = \frac{N(N-1)}{2} = O(N^2)$ *(para $N = 10^6$, $\approx 5 \times 10^{11}$ comparaciones)*.
- **Árbol Binario de Búsqueda (ABB):** descarta la mitad del árbol en cada nivel; si halla coincidencia, detecta el **duplicado** al instante y lo descarta.
- *Limitación:* si los datos llegan ordenados ($10, 20, 30 \dots$), el ABB degenera en una cadena de altura $h = N - 1$ ($O(N)$ por búsqueda).

---

## Árboles Autobalanceados: AVL y Árboles B / B+

1. **Árboles AVL (Adelson-Velskii y Landis, 1962):**
   - Mantienen en cada nodo un **factor de equilibrio** $\text{FE}(u) = h_{\text{der}}(u) - h_{\text{izq}}(u) \in \{-1, 0, +1\}$.
   - Si $|\text{FE}(u)| = 2$, aplican **rotación simple o doble** en $O(1)$, acotando la búsqueda a $\approx 1.44 \log_2(N)$ comparaciones ($\le 28$ para $N = 10^6$).
2. **Árboles B y B+ (Motores SQL y Sistemas de Archivos):**
   - Árboles **$m$-arios balanceados** ajustados al tamaño de bloque en disco/SSD ($4\text{ KB}$ o $16\text{ KB}$); todas las hojas quedan al mismo nivel ($3$–$4$ accesos entre cientos de millones de filas).

---

<!-- _class: seccion -->
<!-- _header: "" -->
<!-- _footer: "" -->

## Ejemplos de Práctica

Grafo de similaridad, detección de duplicados con ABB y coloración de frecuencias

---

<!-- _class: compacta -->

## Ejemplo 1: Grafo de Similaridad — Planteamiento (1/3)

**Problema:** Se analizaron $7$ muestras de tejido $P_1, \dots, P_7$ midiendo $4$ biomarcadores $(a, b, c, d)$:

| Muestra | Biomarcador $a$ | Biomarcador $b$ | Biomarcador $c$ | Biomarcador $d$ |
| :---: | :---: | :---: | :---: | :---: |
| **$P_1$** | $5$ | $2$ | $3$ | $3$ |
| **$P_2$** | $5$ | $1$ | $3$ | $2$ |
| **$P_3$** | $6$ | $2$ | $3$ | $2$ |
| **$P_4$** | $6$ | $8$ | $2$ | $8$ |
| **$P_5$** | $5$ | $2$ | $8$ | $2$ |
| **$P_6$** | $6$ | $2$ | $9$ | $3$ |
| **$P_7$** | $5$ | $9$ | $3$ | $8$ |

1. Calcule la matriz de disimilaridades $S(P_x - P_y)$.  2. Elija una cota $C$ para obtener **$3$ clases**.

---

## Ejemplo 1: Cálculo de Disimilaridades $S(P_x - P_y)$ (2/3)

- **Entre $P_1(5,2,3,3)$, $P_2(5,1,3,2)$ y $P_3(6,2,3,2)$:**
  - $S(P_1 - P_2) = |5-5| + |2-1| + |3-3| + |3-2| = \mathbf{2}$
  - $S(P_1 - P_3) = |5-6| + |2-2| + |3-3| + |3-2| = \mathbf{2}$
  - $S(P_2 - P_3) = |5-6| + |1-2| + |3-3| + |2-2| = \mathbf{2}$
- **Entre $P_4(6,8,2,8)$ y $P_7(5,9,3,8)$:**
  - $S(P_4 - P_7) = |6-5| + |8-9| + |2-3| + |8-8| = \mathbf{3}$
- **Entre $P_5(5,2,8,2)$ y $P_6(6,2,9,3)$:**
  - $S(P_5 - P_6) = |5-6| + |2-2| + |8-9| + |2-3| = \mathbf{3}$
- Pares de grupos distintos arrojan valores $\ge 6$ (p. ej., $S(P_1-P_5)=6$, $S(P_3-P_6)=7$, $S(P_1-P_4)=13$).

---

<!-- _class: tabla-ancha -->

## Ejemplo 1: Matriz de Distancias y 3 Clases (3/3)

| $S(P_x - P_y)$ | $P_1$ | $P_2$ | $P_3$ | $P_4$ | $P_5$ | $P_6$ | $P_7$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **$P_1$** | $0$ | **$2$** | **$2$** | $13$ | $6$ | $7$ | $12$ |
| **$P_2$** | **$2$** | $0$ | **$2$** | $15$ | $6$ | $9$ | $14$ |
| **$P_3$** | **$2$** | **$2$** | $0$ | $13$ | $6$ | $7$ | $14$ |
| **$P_4$** | $13$ | $15$ | $13$ | $0$ | $19$ | $18$ | **$3$** |
| **$P_5$** | $6$ | $6$ | $6$ | $19$ | $0$ | **$3$** | $18$ |
| **$P_6$** | $7$ | $9$ | $7$ | $18$ | **$3$** | $0$ | $19$ |
| **$P_7$** | $12$ | $14$ | $14$ | **$3$** | $18$ | $19$ | $0$ |

Con cota **$C = 4$** ($3 < C \le 6$), $L_{C=4} = \{(P_1, P_2), (P_1, P_3), (P_2, P_3), (P_4, P_7), (P_5, P_6)\}$:
**Clase 1:** $\{P_1, P_2, P_3\}$ · **Clase 2:** $\{P_4, P_7\}$ · **Clase 3:** $\{P_5, P_6\}$.

---

## Ejemplo 2: Deduplicación con un ABB (1/2)

**Problema:** Para el flujo $45, 20, 70, 10, 30, 20, 60, 85, 70, 25$, construya el ABB descartando duplicados, cuente las comparaciones y obtenga el recorrido Inorden.

**1. Traza de inserción (primeros 5 elementos):**
- **`45`:** árbol vacío $\to$ se inserta como **raíz** ($0$ comparaciones).
- **`20`:** $20 < 45 \to$ hijo izquierdo de $45$ ($1$ comp.).
- **`70`:** $70 > 45 \to$ hijo derecho de $45$ ($1$ comp.).
- **`10`:** $< 45$, $< 20 \to$ hijo izquierdo de $20$ ($2$ comp.).
- **`30`:** $< 45$, $> 20 \to$ hijo derecho de $20$ ($2$ comp.).

---

<!-- _class: compacta -->

## Ejemplo 2: Traza Final, Comparaciones e Inorden (2/2)

**Continuación de la traza:**
- **`20` (Duplicado):** $< 45$, $= 20 \to$ **¡Duplicado descartado!** ($2$ comp.).
- **`60`:** $> 45$, $< 70 \to$ hijo izquierdo de $70$ ($2$ comp.).
- **`85`:** $> 45$, $> 70 \to$ hijo derecho de $70$ ($2$ comp.).
- **`70` (Duplicado):** $> 45$, $= 70 \to$ **¡Duplicado descartado!** ($2$ comp.).
- **`25`:** $< 45$, $> 20$, $< 30 \to$ hijo izquierdo de $30$ ($3$ comp.).

- **Total de comparaciones:** $0 + 1 + 1 + 2 + 2 + 2 + 2 + 2 + 2 + 3 = \mathbf{17\text{ comparaciones}}$.
- **2. Lista depurada (Inorden $I \to R \to D$):** $10,\; 20,\; 25,\; 30,\; 45,\; 60,\; 70,\; 85$ ($8$ registros únicos).

---

## Ejemplo 3: Asignación de Frecuencias por Coloración (1/2)

**Problema:** Seis estaciones de radio $V = \{E_1, E_2, E_3, E_4, E_5, E_6\}$ presentan interferencia entre:
$$(E_1, E_2),\; (E_1, E_3),\; (E_1, E_4),\; (E_2, E_3),\; (E_2, E_5),\; (E_3, E_4),\; (E_3, E_5),\; (E_4, E_5),\; (E_4, E_6),\; (E_5, E_6)$$

Determine $\chi(G)$ y asigne una frecuencia a cada estación.

**1. Análisis de subgrafos completos (cliques):**
- Las estaciones $\{E_1, E_2, E_3\}$ son mutuamente adyacentes (triángulo $K_3$), al igual que $\{E_1, E_3, E_4\}$, $\{E_2, E_3, E_5\}$, $\{E_3, E_4, E_5\}$ y $\{E_4, E_5, E_6\}$.
- Por lo tanto, se necesitan **al menos $3$ frecuencias distintas** ($\chi(G) \ge 3$).

---

## Ejemplo 3: Coloración Voraz y Resultado (2/2)

**2. Asignación voraz de frecuencias:**
- $E_3$ (mayor grado, $\delta(E_3) = 4$) $\to$ **$f_1$**.
- $E_1$ (adyacente a $E_3$) $\to$ **$f_2$**.
- $E_2$ (adyacente a $E_1, E_3$) $\to$ **$f_3$**.
- $E_4$ (adyacente a $E_1, E_3$; no a $E_2$) $\to$ reutiliza **$f_3$**.
- $E_5$ (adyacente a $E_2, E_3, E_4$; no a $E_1$) $\to$ reutiliza **$f_2$**.
- $E_6$ (adyacente a $E_4, E_5$; no a $E_3$) $\to$ reutiliza **$f_1$**.

**3. Resultado ($\chi(G) = \mathbf{3}$):** **$f_1$:** $\{E_3, E_6\}$ · **$f_2$:** $\{E_1, E_5\}$ · **$f_3$:** $\{E_2, E_4\}$.

---

<!-- _class: seccion -->
<!-- _header: "" -->
<!-- _footer: "" -->

## Ejercicios de Tarea

Práctica con grafos de similaridad, diseño de fibra óptica (MST) y balanceo de ABB

---

<!-- _class: compacta -->

## Ejercicio 1: Segmentación de Usuarios por Similaridad

Un portal registra $8$ usuarios $P_1, \dots, P_8$ según $4$ indicadores de tiempo semanal $(a, b, c, d)$:

| Usuario | Sección $a$ | Sección $b$ | Sección $c$ | Sección $d$ |
| :---: | :---: | :---: | :---: | :---: |
| **$P_1$** | $10$ | $7$ | $10$ | $6$ |
| **$P_2$** | $1$ | $2$ | $0$ | $1$ |
| **$P_3$** | $5$ | $5$ | $4$ | $6$ |
| **$P_4$** | $10$ | $8$ | $9$ | $7$ |
| **$P_5$** | $0$ | $2$ | $1$ | $1$ |
| **$P_6$** | $5$ | $6$ | $5$ | $5$ |
| **$P_7$** | $9$ | $8$ | $10$ | $7$ |
| **$P_8$** | $1$ | $1$ | $1$ | $2$ |

1. Calcule $S(P_x - P_y) = |a_x - a_y| + |b_x - b_y| + |c_x - c_y| + |d_x - d_y|$ entre los usuarios.
2. Construya el grafo de similaridad con cota **$C = 5$** ($S(P_x - P_y) < 5$) y halle las **$3$ clases**.

---

## Ejercicio 2: Red de Fibra Óptica al Costo Mínimo (MST)

Una universidad conectará $6$ edificios: Rectoría ($R$), Ingeniería ($I$), Ciencias ($C$), Biblioteca ($B$), Laboratorios ($L$) y Auditorio ($A$). Costos factibles (en miles de dólares):
$$(R, I)=12,\; (R, B)=8,\; (R, A)=15,\; (I, C)=7,\; (I, B)=9,\; (I, L)=6,\; (C, L)=5,\; (B, L)=11,\; (B, A)=10,\; (L, A)=14$$

1. Aplique **Kruskal** (o **Prim**) para determinar los enlaces de fibra óptica que conectan todos los edificios con la **mínima inversión total**.
2. Calcule el costo total en dólares y verifique que la topología resultante es un árbol.

---

## Ejercicio 3: ABB Desbalanceado vs. Árbol Balanceado

Se tienen las $7$ claves numéricas $\{10, 20, 30, 40, 50, 60, 70\}$:

1. Si se insertan exactamente en ese orden ascendente ($10, 20, 30, 40, 50, 60, 70$) en un ABB simple sin balanceo, ¿cuál es la altura $h$ resultante y cuántas comparaciones requiere buscar el $70$?
2. Reordene la secuencia de inserción para que el ABB quede **perfectamente balanceado** (altura mínima), indique qué clave queda en la raíz, la nueva altura $h$ y el máximo de comparaciones para cualquier búsqueda.
