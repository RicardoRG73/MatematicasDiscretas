---
marp: true
theme: discretas
size: 16:9
paginate: true
math: mathjax
header: "Matemáticas Discretas · Unidad 6"
footer: "Unidad 6 · Teoría de Grafos"
---
<!-- _class: portada -->
<!-- _paginate: false -->
<!-- _header: "" -->
<!-- _footer: "" -->

# Unidad 6: Teoría de Grafos

## Panorama general, competencias y mapa de contenidos

- **Asignatura:** Matemáticas Discretas (`LISSI0211`) · Segundo Semestre
- **Duración de la unidad:** 10 horas
- **Competencia:** Aplica los conceptos de grafos, resolviendo problemas de recorrido y búsqueda, para implementar soluciones en redes y estructuras de datos.

---

## Origen Histórico: Los Puentes de Königsberg (1735)

- **El problema:** cruzar los $7$ puentes sobre el río Pregel recorriendo las $4$ zonas de tierra firme pasando por cada puente **exactamente una vez** y regresando al punto de partida.
- **Abstracción de Leonhard Euler (1735 / pub. 1736):**
  - Masas de tierra $\longrightarrow$ **vértices (nodos)**.
  - Puentes $\longrightarrow$ **aristas (lados)**.
- **Demostración:** un recorrido cerrado exige **valencia par** en todos los vértices; al tener los $4$ grado impar, el recorrido es **imposible**.
- Con este resultado, Euler fundó la **Teoría de Grafos** y la topología.

---

## Hitos Clave (Siglo XIX y Principios del XX)

- **Gustav Kirchhoff (1847):** introdujo los **árboles** para el análisis de redes eléctricas.
- **Arthur Cayley (1857):** aplicó los árboles para enumerar isómeros químicos.
- **Sir William Rowan Hamilton (1857):** planteó recorrer todos los vértices de un dodecaedro.
- **Kazimierz Kuratowski (1930):** caracterizó los **grafos planos** mediante $K_5$ y $K_{3,3}$.

---

## Hitos Clave en Algoritmos y Redes (Siglo XX)

- **David A. Huffman (1952):** diseñó los árboles de **compresión óptima** sin pérdida.
- **Kruskal (1956), Prim (1957) y Dijkstra (1959):** algoritmos voraces de **árbol generador mínimo** y **ruta más corta**.
- **L. R. Ford Jr. y D. R. Fulkerson (1956):** demostraron el teorema de **flujo máximo y corte mínimo**.
- **Carl Adam Petri (1962):** inventó las **redes de Petri** para modelar sistemas concurrentes y distribuidos.

---

## Aplicaciones en Ingeniería en Sistemas Computacionales

- **Redes e Internet:** enrutamiento óptimo (protocolo **OSPF** con Dijkstra) y topologías sin ciclos mediante árboles generadores mínimos.
- **Estructuras de datos y BD:** búsqueda en tiempo $O(\log n)$ con árboles **ABB**, **AVL** y **B/B+** en sistemas de archivos y motores SQL.
- **Compiladores y compresión:** evaluación de expresiones (preorden, inorden, postorden / pilas) y **códigos de Huffman**.
- **Investigación de operaciones y concurrencia:** flujo máximo, pareos bipartitos (**Teorema de Hall**) y sistemas libres de *deadlock* (**redes de Petri**).

---

<!-- _class: seccion -->
<!-- _header: "" -->
<!-- _footer: "" -->

## Mapa de Subtemas de la Unidad 6

Estructura temática completa de los subtemas `6.1` a `6.6`

---

## Subtemas 6.1 y 6.2: Fundamentos y Representación

- **6.1 Elementos y características de los grafos**
  - **6.1.1 Componentes:** vértices, aristas, lados paralelos, lazos, valencia $\delta(v)$ y Teorema de la suma de valencias ($\sum \delta(v) = 2|L|$).
  - **6.1.2 Tipos:** simples, completos ($K_n$), complemento ($G'$), bipartidos ($K_{n,m}$), conexos (Euler, Fleury, Hamilton), planos ($A = L - V + 2$, Kuratowski), ponderados y coloración ($\chi(G)$, cuatro colores).
- **6.2 Representación de los grafos**
  - **6.2.1 Matemática:** $G = (V, L)$, Matriz de Adyacencia ($M_a$ y $M_a^k$), Matriz de Incidencia ($M_i$) e isomorfismo ($G_1 \cong G_2$).
  - **6.2.2 Computacional:** listas de adyacencia, arreglos paralelos, lista de aristas y complejidad espacial/temporal.

---

## Subtemas 6.3 y 6.4: Algoritmos y Árboles

- **6.3 Algoritmos de recorrido y búsqueda**
  - **6.3.1 Camino más corto:** algoritmo de **Dijkstra** y tabla de iteraciones.
  - **6.3.2 A lo ancho (BFS):** búsqueda por niveles con cola (`FIFO`) y árbol generador.
  - **6.3.3 En profundidad (DFS):** búsqueda con retroceso (*backtracking*) usando pila (`LIFO`).
- **6.4 Árboles**
  - **6.4.1–6.4.3:** raíz, hojas, ancestros; $|L|=|V|-1$, bosques, binarios completos; clasificación $m$-aria, altura $h$ y balanceo.
  - **6.4.4–6.4.5:** **Huffman**, MST (**Prim** y **Kruskal**), recorridos (preorden, inorden, postorden), pilas y **ABB**.

---

## Subtemas 6.5 y 6.6: Redes y Aplicaciones

- **6.5 Redes**
  - Redes de transporte dirigidas (fuente $a$, sumidero $z$, $C_{ij}$, $F_{ij}$, conservación).
  - **Ford-Fulkerson**, Teorema Flujo Máximo–Corte Mínimo ($\max |F| = \min C(P, \bar{P})$) y flujo mínimo ($m_{ij} \le F_{ij} \le C_{ij}$).
  - **Pareos** bipartitos, **Teorema de Hall** ($|S| \le |R(S)|$) y **Redes de Petri** ($N = (P, T, A, M_0)$).
- **6.6 Aplicaciones de grafos y árboles**
  - *Clustering* con **grafos de similaridad** ($S(P_x - P_y) < C$), coloración (frecuencias/horarios), diseño de redes al menor costo, eliminación de duplicados e indexación con **ABB, AVL y Árboles B**.

---

<!-- _class: compacta -->

## Bibliografía de Referencia

- **Jiménez Murillo, J. A.** (2012). *Matemáticas para la computación* (2.ª ed., Cap. 7: Grafos, pp. 284–349; Cap. 8: Árboles, pp. 350–399). Alfaomega.
- **Johnsonbaugh, R.** (2005). *Matemáticas discretas* (6.ª ed., Cap. 8: Teoría de gráficas, pp. 318–378; Cap. 9: Árboles, pp. 379–443; Cap. 10: Modelos de redes, pp. 444–469). Pearson Educación.
- **Lipschutz, S., & Lipson, M.** (2009). *Matemáticas discretas* (3.ª ed., Cap. 8: Teoría de grafos; Cap. 9: Grafos dirigidos; Cap. 10: Árboles binarios). McGraw-Hill.
- **Epp, S. S.** (2012). *Matemáticas discretas con aplicaciones* (4.ª ed., Cap. 10: Grafos y árboles, pp. 625–716). Cengage Learning.
- **Rosen, K. H.** (2004). *Matemática discreta y sus aplicaciones* (5.ª ed., Cap. 8: Grafos; Cap. 9: Árboles). McGraw-Hill.
