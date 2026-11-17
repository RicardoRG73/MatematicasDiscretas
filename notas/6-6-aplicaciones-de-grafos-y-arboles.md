# 6.6 Aplicaciones de Grafos y Árboles

La teoría de grafos y los árboles constituyen el núcleo algorítmico de un vasto espectro de sistemas informáticos del mundo real. Desde el reconocimiento de patrones y agrupamiento (*clustering*) de datos médicos o perfiles de usuarios en comercio electrónico, hasta el enrutamiento de paquetes en Internet, la asignación de registros en compiladores y la indexación logarítmica mediante árboles autobalanceados en motores de bases de datos, las estructuras estudiadas en esta unidad permiten resolver problemas de alta complejidad con eficiencia óptima.

---

## 1. Reconocimiento de Patrones y Agrupamiento mediante Grafos de Similaridad

En ciencia de datos, aprendizaje automático (*machine learning*), bioinformática y mercadotecnia digital, un problema recurrente consiste en **agrupar objetos en clases o clústeres homogéneos** sin supervisión previa (*clustering*), de modo que los elementos dentro de un mismo grupo sean muy parecidos entre sí y muy distintos de los elementos de otros grupos.

### Medida de Disimilaridad (Distancia de Manhattan / Norma $L_1$)
Supóngase que se tienen $n$ objetos o registros $P_1, P_2, \dots, P_n$, cada uno caracterizado por $m$ atributos cuantitativos:
$$P_x = (a_x, b_x, c_x, d_x, \dots)$$
Se define la **función de disimilaridad** $S(P_x - P_y)$ entre cualquier par de objetos $P_x$ y $P_y$ como la suma de las diferencias absolutas entre sus atributos correspondientes:
$$S(P_x - P_y) = |a_x - a_y| + |b_x - b_y| + |c_x - c_y| + |d_x - d_y| + \dots$$

Cuanto menor sea el valor de $S(P_x - P_y)$, **más similares** son los objetos $P_x$ y $P_y$ (en particular, $S(P_x - P_x) = 0$).

### Construcción del Grafo de Similaridad y Componentes Conexas
1. Se calcula la matriz triangular de disimilaridades $S(P_x - P_y)$ para todos los $\frac{n(n-1)}{2}$ pares de objetos.
2. Se fija un **umbral o cota de tolerancia $C > 0$**.
3. Se construye el **grafo de similaridad** $G_C = (V, L_C)$ donde los vértices son los objetos $V = \{P_1, P_2, \dots, P_n\}$ y se traza una arista entre $P_x$ y $P_y$ **si y sólo si** su disimilaridad es estrictamente menor que la cota $C$:
   $$(P_x, P_y) \in L_C \iff S(P_x - P_y) < C$$
4. **Clasificación automática por componentes conexas:** Si se requiere dividir la población en $k$ clases (por ejemplo, $3$ especies biológicas o $3$ segmentos de clientes), se ajusta el umbral $C$ de forma que el grafo $G_C$ quede dividido exactamente en **$k$ componentes conexas disjuntas**. Cada componente conexa constituye una clase o clúster natural de objetos similares.

---

## 2. Redes de Telecomunicaciones, Enrutamiento e Infraestructura

| Problema en Ingeniería de Redes | Modelo en Teoría de Grafos y Árboles | Algoritmo Estándar Empleado |
| :--- | :--- | :--- |
| **Enrutamiento de paquetes en Internet (Estado de Enlace)** | Grafo ponderado $G = (V, L, w)$ donde $w(e)$ es el costo inversamente proporcional al ancho de banda o latencia del enlace | **Algoritmo de Dijkstra** en protocolos **OSPF** (*Open Shortest Path First*) e **IS-IS** |
| **Prevención de tormentas de *broadcast* en redes LAN (Ethernet)** | Eliminación de ciclos físicos entre *switches* conservando la conectividad total de la red local | **Árbol Generador (Spanning Tree Protocol, IEEE 802.1D STP)** |
| **Diseño de cableado estructurado, fibra óptica y redes eléctricas** | Conectar $n$ edificios o nodos de distribución minimizando los metros totales de cable o costo de instalación | **Árbol Generador Mínimo (MST)** mediante **Prim** o **Kruskal** |
| **Ingeniería de tráfico y tolerancia a fallos en enlaces troncales** | Determinar el caudal máximo de datos entre dos centros de datos y detectar los enlaces cuello de botella | **Flujo Máximo / Corte Mínimo (Ford-Fulkerson / Edmonds-Karp)** |

---

## 3. Coloración de Grafos: Asignación de Frecuencias, Horarios y Registros de CPU

La **coloración de vértices** de un grafo $G = (V, L)$ (asignar un color a cada vértice de modo que ningún par de vértices adyacentes comparta el mismo color, utilizando el mínimo número posible de colores $\chi(G)$) resuelve problemas donde las aristas representan **incompatibilidades, interferencias o conflictos de simultaneidad**:

1. **Asignación de frecuencias en telefonía celular y redes Wi-Fi:**
   - **Vértices:** Antenas o estaciones base de transmisión.
   - **Aristas:** Par de antenas cuyas áreas geográficas de cobertura se traslapan y causarían interferencia co-canal.
   - **Número cromático $\chi(G)$:** Cantidad mínima de canales de frecuencia distintos requeridos para operar toda la red sin interferencias.
2. **Programación de horarios de exámenes universitarios:**
   - **Vértices:** Asignaturas del semestre.
   - **Aristas:** Dos asignaturas se conectan con una arista si existe al menos un alumno inscrito en ambas.
   - **Colores:** Franjas horarias de examen. $\chi(G)$ determina el número mínimo de periodos de examen necesarios para que ningún estudiante tenga dos exámenes a la misma hora.
3. **Asignación de registros de CPU en compiladores (*Register Allocation*):**
   - **Vértices:** Variables temporales de un programa.
   - **Aristas (Grafo de interferencia):** Dos variables están conectadas si sus tiempos de vida (*liveness*) se traslapan (ambas están activas simultáneamente).
   - **Colores:** Registros físicos de alta velocidad del procesador. Si el grafo es $k$-coloreable con $k$ igual al número de registros de la CPU, el código se ejecuta sin necesidad de volcar variables a la memoria RAM (*register spilling*).

---

## 4. Eliminación de Duplicados e Indexación en Bases de Datos mediante Árboles

Una de las aplicaciones más importantes de los árboles en la ingeniería de software es la **búsqueda rápida, el ordenamiento y la depuración de registros duplicados** en grandes bases de datos y sistemas de archivos.

### Comparación entre Búsqueda Secuencial y Árboles Binarios de Búsqueda (ABB)
Supóngase que se tiene una lista o archivo con $N$ registros y se desea detectar y eliminar todas las claves repetidas:
- **Con una lista lineal o arreglo secuencial desordenado:** Cada nuevo registro $k$ debe compararse contra todos los registros previos ya aceptados. En el peor caso, esto requiere:
  $$\sum_{k=1}^{N-1} k = \frac{N(N-1)}{2} = O(N^2) \text{ comparaciones}$$
  Para $N = 1{,}000{,}000$ de registros, una búsqueda secuencial requeriría cerca de $5 \times 10^{11}$ comparaciones (minutos u horas de procesamiento).
- **Con un Árbol Binario de Búsqueda (ABB):** Al insertar cada registro en el ABB, en cada nivel se descarta la mitad del árbol (descendiendo a la izquierda si es menor o a la derecha si es mayor; si se encuentra un nodo con el mismo valor, se detecta inmediatamente como **duplicado** y se descarta).

### El problema del desbalanceo y los Árboles Autobalanceados (AVL y Árboles B)
Si los datos llegan en orden aleatorio, un ABB tiene una altura cercana a $\log_2(N)$. Sin embargo, si los datos llegan **previamente ordenados** (por ejemplo, $10, 20, 30, 40, 50$), un ABB simple degenera en una lista lineal sesgada de altura $h = N - 1$, degradando su rendimiento nuevamente a $O(N)$ por búsqueda.

Para garantizar matemáticamente un tiempo logarítmico en todos los casos, los sistemas gestores de bases de datos emplean **árboles balanceados**:

1. **Árboles AVL (Adelson-Velskii y Landis, 1962):**
   - Son Árboles Binarios de Búsqueda que mantienen en cada nodo $u$ un **factor de equilibrio** $\text{FE}(u) = h_{\text{der}}(u) - h_{\text{izq}}(u) \in \{-1, 0, +1\}$.
   - Si tras insertar o eliminar una clave algún nodo alcanza $|\text{FE}(u)| = 2$, el árbol aplica automáticamente una **rotación simple** (Izquierda o Derecha) o una **rotación doble** (Izquierda-Derecha o Derecha-Izquierda) en tiempo constante $O(1)$, restaurando el balanceo y garantizando que la búsqueda de un registro entre $N$ datos tome a lo sumo $\approx 1.44 \log_2(N)$ comparaciones (para $N = 1{,}000{,}000$, ¡a lo sumo $20$ a $28$ comparaciones!).
2. **Árboles B y Árboles B+ (Índices en Sistemas de Bases de Datos SQL y Sistemas de Archivos):**
   - Son árboles **$m$-arios balanceados** (con $m$ del orden de cientos de hijos por nodo, ajustado al tamaño de un bloque de disco o página SSD de $4\text{ KB}$ o $16\text{ KB}$).
   - Todas las hojas se mantienen exactamente al mismo nivel $h$, permitiendo localizar cualquier registro entre cientos de millones de filas en tan solo $3$ o $4$ accesos a disco.

---

## Ejemplos de Práctica (Resueltos Paso a Paso)

### Ejemplo 1: Clasificación de muestras mediante un Grafo de Similaridad

**Problema:**  
En un laboratorio clínico se analizaron $7$ muestras de tejido $P_1, P_2, \dots, P_7$, midiendo en cada una $4$ biomarcadores $(a, b, c, d)$ cuyos valores se muestran en la tabla:

| Muestra | Biomarcador $a$ | Biomarcador $b$ | Biomarcador $c$ | Biomarcador $d$ |
| :---: | :---: | :---: | :---: | :---: |
| **$P_1$** | $5$ | $2$ | $3$ | $3$ |
| **$P_2$** | $5$ | $1$ | $3$ | $2$ |
| **$P_3$** | $6$ | $2$ | $3$ | $2$ |
| **$P_4$** | $6$ | $8$ | $2$ | $8$ |
| **$P_5$** | $5$ | $2$ | $8$ | $2$ |
| **$P_6$** | $6$ | $2$ | $9$ | $3$ |
| **$P_7$** | $5$ | $9$ | $3$ | $8$ |

Utilizando la medida de disimilaridad $S(P_x - P_y) = |a_x - a_y| + |b_x - b_y| + |c_x - c_y| + |d_x - d_y|$:
1. Calcule la matriz de disimilaridades entre todos los pares de muestras.
2. Elija una cota $C$ adecuada para construir el grafo de similaridad $G_C$ de modo que las $7$ muestras queden agrupadas exactamente en **$3$ clases (componentes conexas)** e indique qué muestras integran cada clase.

**Solución paso a paso:**

1. **Cálculo de las disimilaridades $S(P_x - P_y)$:**
   - Entre $P_1(5,2,3,3)$, $P_2(5,1,3,2)$ y $P_3(6,2,3,2)$:
     - $S(P_1 - P_2) = |5-5| + |2-1| + |3-3| + |3-2| = 0 + 1 + 0 + 1 = \mathbf{2}$
     - $S(P_1 - P_3) = |5-6| + |2-2| + |3-3| + |3-2| = 1 + 0 + 0 + 1 = \mathbf{2}$
     - $S(P_2 - P_3) = |5-6| + |1-2| + |3-3| + |2-2| = 1 + 1 + 0 + 0 = \mathbf{2}$
   - Entre $P_4(6,8,2,8)$ y $P_7(5,9,3,8)$:
     - $S(P_4 - P_7) = |6-5| + |8-9| + |2-3| + |8-8| = 1 + 1 + 1 + 0 = \mathbf{3}$
   - Entre $P_5(5,2,8,2)$ y $P_6(6,2,9,3)$:
     - $S(P_5 - P_6) = |5-6| + |2-2| + |8-9| + |2-3| = 1 + 0 + 1 + 1 = \mathbf{3}$
   - Cualquier otra combinación entre elementos de distintos grupos arroja valores $\ge 6$ (por ejemplo, $S(P_1 - P_5) = 0 + 0 + 5 + 1 = 6$, $S(P_3 - P_6) = 0 + 0 + 6 + 1 = 7$, $S(P_1 - P_4) = 1 + 6 + 1 + 5 = 13$).

   | $S(P_x - P_y)$ | $P_1$ | $P_2$ | $P_3$ | $P_4$ | $P_5$ | $P_6$ | $P_7$ |
   | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
   | **$P_1$** | $0$ | **$2$** | **$2$** | $13$ | $6$ | $7$ | $12$ |
   | **$P_2$** | **$2$** | $0$ | **$2$** | $15$ | $6$ | $9$ | $14$ |
   | **$P_3$** | **$2$** | **$2$** | $0$ | $13$ | $6$ | $7$ | $14$ |
   | **$P_4$** | $13$ | $15$ | $13$ | $0$ | $19$ | $18$ | **$3$** |
   | **$P_5$** | $6$ | $6$ | $6$ | $19$ | $0$ | **$3$** | $18$ |
   | **$P_6$** | $7$ | $9$ | $7$ | $18$ | **$3$** | $0$ | $19$ |
   | **$P_7$** | $12$ | $14$ | $14$ | **$3$** | $18$ | $19$ | $0$ |

2. **Selección del umbral $C$ y formación de las $3$ clases:**
   - Si fijamos la cota en **$C = 4$** (o cualquier valor $3 < C \le 6$), sólo se conectan mediante aristas los pares con $S(P_x - P_y) < 4$:
     $$L_{C=4} = \{(P_1, P_2), (P_1, P_3), (P_2, P_3), (P_4, P_7), (P_5, P_6)\}$$
   - El grafo de similaridad $G_{C=4}$ se divide exactamente en **$3$ componentes conexas**, que corresponden a las $3$ clases buscadas:
     - **Clase 1:** $\{P_1, P_2, P_3\}$ (triángulo conexo con $S = 2$).
     - **Clase 2:** $\{P_4, P_7\}$ (unidos por una arista con $S = 3$).
     - **Clase 3:** $\{P_5, P_6\}$ (unidos por una arista con $S = 3$).

---

### Ejemplo 2: Detección de duplicados y conteo de comparaciones con un ABB

**Problema:**  
Se recibe el siguiente flujo de $10$ claves de productos en una base de datos:
$$45, \; 20, \; 70, \; 10, \; 30, \; 20, \; 60, \; 85, \; 70, \; 25$$
1. Construya el **Árbol Binario de Búsqueda (ABB)** descartando las claves duplicadas a medida que llegan e indique cuántas comparaciones contra nodos del árbol se realizan en cada inserción o detección de duplicado.
2. Obtenga la lista depurada y ordenada ascendentemente mediante el recorrido **Inorden** del ABB.

**Solución paso a paso:**

1. **Traza de inserción y detección de duplicados en el ABB:**
   - **`45`:** Árbol vacío $\to$ se inserta como **raíz** ($0$ comparaciones).
   - **`20`:** Se compara con $45$ ($20 < 45$) $\to$ se inserta como hijo izquierdo de $45$ ($1$ comparación).
   - **`70`:** Se compara con $45$ ($70 > 45$) $\to$ se inserta como hijo derecho de $45$ ($1$ comparación).
   - **`10`:** Compara con $45$ ($<$) y con $20$ ($<$) $\to$ se inserta como hijo izquierdo de $20$ ($2$ comparaciones).
   - **`30`:** Compara con $45$ ($<$) y con $20$ ($>$) $\to$ se inserta como hijo derecho de $20$ ($2$ comparaciones).
   - **`20` (Duplicado):** Compara con $45$ ($<$) y con $20$ ($=$) $\to$ **¡Duplicado detectado y descartado!** ($2$ comparaciones).
   - **`60`:** Compara con $45$ ($>$) y con $70$ ($<$) $\to$ se inserta como hijo izquierdo de $70$ ($2$ comparaciones).
   - **`85`:** Compara con $45$ ($>$) y con $70$ ($>$) $\to$ se inserta como hijo derecho de $70$ ($2$ comparaciones).
   - **`70` (Duplicado):** Compara con $45$ ($>$) y con $70$ ($=$) $\to$ **¡Duplicado detectado y descartado!** ($2$ comparaciones).
   - **`25`:** Compara con $45$ ($<$), con $20$ ($>$) y con $30$ ($<$) $\to$ se inserta como hijo izquierdo de $30$ ($3$ comparaciones).
   - **Total de comparaciones realizadas en el ABB:** $0 + 1 + 1 + 2 + 2 + 2 + 2 + 2 + 2 + 3 = \mathbf{17 \text{ comparaciones}}$.

2. **Lista depurada y ordenada (Recorrido Inorden $I \to R \to D$):**
   $$10, \; 20, \; 25, \; 30, \; 45, \; 60, \; 70, \; 85 \quad (8 \text{ registros únicos})$$

---

### Ejemplo 3: Asignación de frecuencias libres de interferencia mediante Coloración

**Problema:**  
Seis estaciones transmisoras de radio $V = \{E_1, E_2, E_3, E_4, E_5, E_6\}$ están ubicadas de tal forma que existen interferencias mutuas entre los siguientes pares de estaciones cercanas:
$$(E_1, E_2),\; (E_1, E_3),\; (E_1, E_4),\; (E_2, E_3),\; (E_2, E_5),\; (E_3, E_4),\; (E_3, E_5),\; (E_4, E_5),\; (E_4, E_6),\; (E_5, E_6)$$
Determine el **número mínimo de frecuencias distintas** $\chi(G)$ necesarias para operar las $6$ estaciones sin interferencia y asigne una frecuencia explícita $f_1, f_2, \dots$ a cada estación.

**Solución paso a paso:**

1. **Análisis de subgrafos completos (cliques):**
   - Observemos que las estaciones $\{E_1, E_2, E_3\}$ son mutuamente adyacentes entre sí (forman un triángulo $K_3$), al igual que $\{E_1, E_3, E_4\}$, $\{E_2, E_3, E_5\}$, $\{E_3, E_4, E_5\}$ y $\{E_4, E_5, E_6\}$.
   - Por lo tanto, se requieren **al menos $3$ frecuencias distintas** ($\chi(G) \ge 3$).

2. **Asignación voraz de frecuencias (coloración de vértices):**
   - Asignamos a $E_3$ (el nodo de mayor grado, $\text{grado}(E_3) = 4$) la frecuencia **$f_1$**.
   - $E_1$ es adyacente a $E_3 \to$ recibe **$f_2$**.
   - $E_2$ es adyacente a $E_1(f_2)$ y a $E_3(f_1) \to$ recibe **$f_3$**.
   - $E_4$ es adyacente a $E_1(f_2)$ y a $E_3(f_1)$, pero **no** es adyacente a $E_2(f_3) \to$ puede reutilizar **$f_3$**.
   - $E_5$ es adyacente a $E_2(f_3)$, $E_3(f_1)$ y $E_4(f_3)$, pero **no** es adyacente a $E_1(f_2) \to$ puede reutilizar **$f_2$**.
   - $E_6$ es adyacente únicamente a $E_4(f_3)$ y $E_5(f_2) \to$ puede reutilizar **$f_1$**.

3. **Resultado final ($\chi(G) = \mathbf{3}$ frecuencias):**
   - **Frecuencia $f_1$:** $\{E_3, E_6\}$
   - **Frecuencia $f_2$:** $\{E_1, E_5\}$
   - **Frecuencia $f_3$:** $\{E_2, E_4\}$

---

## Ejercicios de Tarea (Práctica en Casa)

### Ejercicio 1: Segmentación de usuarios de Internet mediante Grafo de Similaridad
Un portal de comercio electrónico registra los hábitos de navegación de $8$ usuarios $P_1, P_2, \dots, P_8$ a través de $4$ indicadores $(a, b, c, d)$ de tiempo semanal en distintas secciones del sitio:

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

1. Calcule la disimilaridad $S(P_x - P_y) = |a_x - a_y| + |b_x - b_y| + |c_x - c_y| + |d_x - d_y|$ entre los usuarios.
2. Construya el grafo de similaridad con cota **$C = 5$** ($S(P_x - P_y) < 5$) y determine las **$3$ clases (perfiles de usuario)** en las que se divide la población.

<!--
SOLUCIÓN DEL EJERCICIO 1:

1. Cálculo de las disimilaridades dentro de cada perfil afin:
   - Grupo de alta actividad (P_1, P_4, P_7):
     * S(P_1 - P_4) = |10-10| + |7-8| + |10-9| + |6-7| = 0 + 1 + 1 + 1 = 3 < 5
     * S(P_1 - P_7) = |10-9| + |7-8| + |10-10| + |6-7| = 1 + 1 + 0 + 1 = 3 < 5
     * S(P_4 - P_7) = |10-9| + |8-8| + |9-10| + |7-7| = 1 + 0 + 1 + 0 = 2 < 5
   - Grupo de actividad media (P_3, P_6):
     * S(P_3 - P_6) = |5-5| + |5-6| + |4-5| + |6-5| = 0 + 1 + 1 + 1 = 3 < 5
   - Grupo de baja actividad (P_2, P_5, P_8):
     * S(P_2 - P_5) = |1-0| + |2-2| + |0-1| + |1-1| = 1 + 0 + 1 + 0 = 2 < 5
     * S(P_2 - P_8) = |1-1| + |2-1| + |0-1| + |1-2| = 0 + 1 + 1 + 1 = 3 < 5
     * S(P_5 - P_8) = |0-1| + |2-1| + |1-1| + |1-2| = 1 + 1 + 0 + 1 = 3 < 5
   - Cualquier par de usuarios de grupos distintos tiene S >= 13 (por ejemplo, S(P_3 - P_1) = 5+2+6+0 = 13; S(P_3 - P_2) = 4+3+4+5 = 16).

2. Clases resultantes para C = 5 (3 componentes conexas):
   - Clase 1 (Usuarios intensivos): {P_1, P_4, P_7}
   - Clase 2 (Usuarios moderados): {P_3, P_6}
   - Clase 3 (Usuarios ocasionales): {P_2, P_5, P_8}
-->

---

### Ejercicio 2: Diseño de Red de Fibra Óptica con Costo Mínimo (MST)
Una universidad desea interconectar mediante cableado de fibra óptica subterránea sus $6$ edificios principales: Rectoría ($R$), Ingeniería ($I$), Ciencias ($C$), Biblioteca ($B$), Laboratorios ($L$) y Auditorio ($A$). Los costos de excavación y tendido (en miles de dólares) entre los pares de edificios factibles son:
$$(R, I)=12,\; (R, B)=8,\; (R, A)=15,\; (I, C)=7,\; (I, B)=9,\; (I, L)=6,\; (C, L)=5,\; (B, L)=11,\; (B, A)=10,\; (L, A)=14$$
1. Aplique el algoritmo de **Kruskal** (o **Prim**) para determinar qué enlaces de fibra óptica deben construirse de modo que todos los edificios queden comunicados con la **mínima inversión total**.
2. Calcule el costo total en dólares de la red óptima y verifique que la topología resultante es un árbol.

<!--
SOLUCIÓN DEL EJERCICIO 2:

1. Aplicación del Método de Kruskal (ordenando los 10 enlaces de menor a mayor costo):
   - (C, L) = 5  -> Se acepta (Enlace 1).
   - (I, L) = 6  -> Se acepta (Enlace 2).
   - (I, C) = 7  -> Se rechaza (formaría el ciclo I - L - C - I).
   - (R, B) = 8  -> Se acepta (Enlace 3).
   - (I, B) = 9  -> Se acepta (Enlace 4; une {R, B} con {I, L, C}).
   - (B, A) = 10 -> Se acepta (Enlace 5; conecta el edificio A).
   Se han seleccionado |V| - 1 = 6 - 1 = 5 enlaces sin ciclos.

2. Costo total y verificación:
   - Enlaces seleccionados: (C, L), (I, L), (R, B), (I, B), (B, A).
   - Costo total mínimo: 5 + 6 + 8 + 9 + 10 = 38 mil dólares ($38,000 USD).
   - Es un árbol porque conecta los 6 edificios (conexo) con exactamente 5 aristas y sin ningún ciclo.
-->

---

### Ejercicio 3: Comparación de Eficiencia entre ABB Desbalanceado y Árbol Balanceado
Se tienen las $7$ claves numéricas $\{10, 20, 30, 40, 50, 60, 70\}$.
1. Si se insertan exactamente en ese orden ascendente ($10, 20, 30, 40, 50, 60, 70$) en un ABB simple sin balanceo, ¿cuál es la altura $h$ del árbol resultante y cuántas comparaciones se requieren para buscar el número $70$?
2. Reordene la secuencia de inserción para que el ABB resultante quede **perfectamente balanceado** (altura mínima), indique qué clave queda en la raíz, cuál es la nueva altura $h$ y cuántas comparaciones como máximo requiere buscar cualquier elemento del árbol.

<!--
SOLUCIÓN DEL EJERCICIO 3:

1. Inserción en orden ascendente (10, 20, 30, 40, 50, 60, 70):
   - Cada nodo se inserta como hijo derecho del anterior, formando una cadena degenerada (sesgada a la derecha) con raíz en 10 y única hoja en 70.
   - Su altura es h = 6 (niveles 0 al 6).
   - Para buscar el 70 se debe comparar contra los 7 nodos del árbol (7 comparaciones, complejidad lineal O(N)).

2. Árbol Binario de Búsqueda perfectamente balanceado:
   - Se elige la mediana como raíz (40), luego las medianas de cada mitad (20 y 60), y finalmente las hojas (10, 30, 50, 70).
   - Orden de inserción balanceado: 40, 20, 60, 10, 30, 50, 70.
   - Estructura:
     * Nivel 0 (Raíz): 40
     * Nivel 1: 20 (izq.), 60 (der.)
     * Nivel 2 (Hojas): 10 y 30 (hijos de 20); 50 y 70 (hijos de 60).
   - Nueva altura: h = 2 (todas las hojas están en el nivel 2).
   - Número máximo de comparaciones para buscar cualquier elemento (incluyendo el 70): a lo sumo 3 comparaciones (40 -> 60 -> 70), reduciendo el costo a O(log_2 N).
-->
