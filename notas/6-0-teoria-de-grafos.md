# 6. Teoría de Grafos

## Información General de la Unidad

| Campo | Detalle |
| :--- | :--- |
| **Unidad** | 6. Teoría de Grafos |
| **Duración** | 10 horas |
| **Competencia a desarrollar** | Aplica los conceptos de grafos, resolviendo problemas relacionados con recorrido y búsqueda, para implementar soluciones en redes y estructuras de datos. |

---

## Introducción a la Unidad

La **teoría de grafos** nació formalmente en el año $1735$ (publicado en $1736$) cuando el gran matemático suizo **Leonhard Euler** ($1707\text{–}1783$) resolvió el célebre **problema de los siete puentes de Königsberg** (actual Kaliningrado): determinar si era posible recorrer a pie las cuatro regiones de tierra firme conectadas por siete puentes sobre el río Pregel pasando por cada puente exactamente una sola vez y regresando al punto de partida. Al abstraer las masas de tierra como puntos (**vértices o nodos**) y los puentes como líneas de conexión (**aristas o lados**), Euler demostró que dicho recorrido cerrado es imposible porque los cuatro vértices tenían grado impar, fundando con ello tanto la teoría de grafos como la topología (Jiménez Murillo, 2012, Cap. 7.1, pp. 286–287).

Durante los siglos XIX y XX, la teoría de grafos y de árboles se enriqueció con aportaciones fundamentales: **Gustav Kirchhoff** ($1847$) introdujo los **árboles** para el análisis de redes eléctricas; **Arthur Cayley** ($1857$) los aplicó para enumerar isómeros químicos; **Sir William Rowan Hamilton** ($1857$) planteó el recorrido de todos los vértices de un dodecaedro; **Kazimierz Kuratowski** ($1930$) caracterizó los grafos planos; **Edsger W. Dijkstra** ($1959$), **Robert C. Prim** ($1957$) y **Joseph B. Kruskal** ($1956$) crearon los algoritmos voraces de ruta más corta y árbol generador mínimo; **David A. Huffman** ($1952$) diseñó los árboles de compresión óptima; **Lester R. Ford Jr.** y **Delbert R. Fulkerson** ($1956$) demostraron el teorema de flujo máximo y corte mínimo en redes; y **Carl Adam Petri** ($1962$) inventó las **redes de Petri** para modelar sistemas concurrentes y distribuidos (Jiménez Murillo, 2012, Cap. 7 y 8; Johnsonbaugh, 2005, Cap. 8, 9 y 10).

En la ingeniería en sistemas computacionales, los grafos, árboles y redes modelan de forma directa:
- **Redes de telecomunicaciones e Internet:** Enrutamiento óptimo de paquetes (protocolo OSPF basado en el algoritmo de Dijkstra) y diseño de topologías sin redundancia mediante árboles generadores mínimos.
- **Estructuras de datos jerárquicas y bases de datos:** Organización y búsqueda eficiente en tiempo $O(\log n)$ mediante árboles binarios de búsqueda (ABB), árboles autobalanceados AVL y árboles B/B+ en sistemas de archivos y motores SQL.
- **Compiladores y compresión de datos:** Evaluación de expresiones aritméticas mediante recorridos preorden, inorden y postorden (notación polaca inversa y pilas), y compresión sin pérdida mediante códigos de Huffman.
- **Investigación de operaciones y sistemas concurrentes:** Maximización de flujo en redes logísticas o de datos, asignación óptima de tareas mediante pareos bipartitos (Teorema de Hall) y verificación de protocolos libres de interbloqueo (*deadlock*) mediante redes de Petri.

---

## Subtemas de la Unidad

- **[6.1 Elementos y características de los grafos](6-1-elementos-y-caracteristicas-de-los-grafos.md)**
  - **6.1.1 Componentes de un grafo:** Vértices (nodos), aristas (lados o ramas), lados paralelos, lazos (bucles), valencia (grado) de un vértice $\delta(v)$ y el Teorema de la suma de valencias ($\sum \delta(v) = 2|L|$).
  - **6.1.2 Tipos de grafos:** Grafos simples, completos ($K_n$) y complemento de un grafo ($G'$), bipartidos y bipartidos completos ($K_{n,m}$), conexos (caminos, circuitos de Euler con el algoritmo de Fleury, y circuitos de Hamilton), planos (fórmula de Euler $A = L - V + 2$, desigualdad $L \le 3V - 6$ y Teorema de Kuratowski con $K_5$ y $K_{3,3}$), ponderados y coloración de grafos (número cromático $\chi(G)$ y Teorema de los cuatro colores).
- **[6.2 Representación de los grafos](6-2-representacion-de-los-grafos.md)**
  - **6.2.1 Matemática:** Representación conjuntista $G = (V, L)$, **Matriz de Adyacencia ($M_a$)** (propiedades y potencias $M_a^k$ para contar caminos), **Matriz de Incidencia ($M_i$)** (representación de lados paralelos, lazos y cálculo de valencias por suma de filas) e **isomorfismo de grafos** ($G_1 \cong G_2$ por invariantes estructurales y coincidencia matricial).
  - **6.2.2 Computacional:** Estructuras de datos en memoria: **Listas de Adyacencia** (arreglo de cabeceras y listas enlazadas), arreglos paralelos de punteros, lista de aristas y comparación de complejidad espacial y temporal entre representaciones para grafos densos y dispersos.
- **[6.3 Algoritmos de recorrido y búsqueda](6-3-algoritmos-de-recorrido-y-busqueda.md)**
  - **6.3.1 El camino más corto:** Algoritmo de **Dijkstra** sobre grafos ponderados y construcción paso a paso de la matriz de iteraciones (`Iteración`, columnas de nodos, `Actual` y `Seleccionados`).
  - **6.3.2 A lo ancho (BFS):** Búsqueda por niveles (*Breadth-First Search*) utilizando una cola (`FIFO`) y obtención de árboles generadores a lo ancho.
  - **6.3.3 En profundidad (DFS):** Búsqueda por ramas con retroceso (*backtracking*, *Depth-First Search*) utilizando una pila (`LIFO`) y obtención de árboles generadores en profundidad.
- **[6.4 Árboles](6-4-arboles.md)**
  - **6.4.1 Componentes:** Raíz, hoja (nodo terminal), vértices internos, padre, hijo, hermanos, descendientes, antecesores (ancestros), subárboles y nivel de un nodo.
  - **6.4.2 Propiedades:** Unicidad de caminos, relación fundamental $|L| = |V| - 1$, bosques (conjuntos de árboles) y teoremas de árboles binarios completos ($\text{Hojas} = i + 1$ y $\text{Total de vértices} = 2i + 1$).
  - **6.4.3 Clasificación (altura, número de nodos):** Árboles binarios, trinarios, $m$-arios y completos; altura $h$ de un árbol, árboles balanceados y desbalanceados, y procedimiento de balanceo.
  - **6.4.4 Árboles con peso:** Compresión y codificación mediante el **Código de Huffman** (construcción del árbol binario óptimo de pesos) y obtención del **Árbol Generador Mínimo (MST)** mediante el **Método de Prim** y el **Método de Kruskal**.
  - **6.4.5 Recorrido de un árbol (Preorden, Inorden, Postorden):** Recorridos en orden primero (preorden / prefijo), orden segundo (inorden / infijo) y orden final (postorden / postfijo), reconstrucción de árboles de expresiones y evaluación mediante pilas, así como **Árboles Binarios de Búsqueda (ABB)** (inserción, búsqueda y eliminación de nodos).
- **[6.5 Redes](6-5-redes.md)**
  - Redes de transporte dirigidas (fuente $a$, sumidero $z$, capacidades $C_{ij}$, flujo $F_{ij}$ y ley de conservación del flujo), **Algoritmo de Flujo Máximo de Ford-Fulkerson** (trayectorias de aumento y etiquetado), **Teorema de Flujo Máximo y Corte Mínimo** ($\max |F| = \min C(P, \bar{P})$), redes con requerimientos de **flujo mínimo** ($m_{ij} \le F_{ij} \le C_{ij}$), **Pareos (Acoplamientos)** en grafos bipartitos y el **Teorema del Matrimonio de Hall** ($|S| \le |R(S)|$), y **Redes de Petri** ($N = (P, T, A, M_0)$, lugares, transiciones, tokens y regla de disparo).
- **[6.6 Aplicaciones de grafos y árboles](6-6-aplicaciones-de-grafos-y-arboles.md)**
  - Reconocimiento de patrones y agrupamiento (*clustering*) mediante **grafos de similaridad** ($S(P_x - P_y) < C$, Jiménez Murillo Cap. 7.9.1), asignación de frecuencias y horarios mediante coloración de grafos, diseño de redes al menor costo, eliminación de registros duplicados e indexación en bases de datos mediante árboles ABB, **AVL** y **Árboles B** (Jiménez Murillo Cap. 8.9).

---

## Bibliografía de Referencia

- **Jiménez Murillo, J. A.** (2012). *Matemáticas para la computación* (2.ª ed., Cap. 7: Grafos, pp. 284–349; Cap. 8: Árboles, pp. 350–399). Alfaomega.
- **Johnsonbaugh, R.** (2005). *Matemáticas discretas* (6.ª ed., Cap. 8: Teoría de gráficas, pp. 318–378; Cap. 9: Árboles, pp. 379–443; Cap. 10: Modelos de redes, pp. 444–469). Pearson Educación.
- **Lipschutz, S., & Lipson, M.** (2009). *Matemáticas discretas* (3.ª ed., Serie Schaum, Cap. 8: Teoría de grafos, pp. 154–200; Cap. 9: Grafos dirigidos, pp. 201–234; Cap. 10: Árboles binarios, pp. 235–263). McGraw-Hill.
- **Epp, S. S.** (2012). *Matemáticas discretas con aplicaciones* (4.ª ed., Cap. 10: Grafos y árboles, pp. 625–716). Cengage Learning.
- **Rosen, K. H.** (2004). *Matemática discreta y sus aplicaciones* (5.ª ed., Cap. 8: Grafos; Cap. 9: Árboles). McGraw-Hill.
