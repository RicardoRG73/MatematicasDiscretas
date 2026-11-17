# 5.5 Aplicaciones de las relaciones y las funciones en la computación

## Introducción

Los conceptos de relaciones binarias, relaciones $n$-arias, matrices booleanas, grafos dirigidos y funciones no son abstracciones aisladas: constituyen el modelo matemático directo con el que se diseñan e implementan las **estructuras de datos**, los **sistemas manejadores de bases de datos (DBMS)**, los **lenguajes de programación** y las **tablas de dispersión (*hash tables*)** en la ingeniería en sistemas computacionales (Jiménez Murillo, 2012, Cap. 6.7 y 6.9, pp. 248–256, 267).

---

## 1. Aplicación en Estructuras de Datos: Listas Enlazadas Simples y Dobles como Relaciones

En programación, cuando los datos llegan en orden arbitrario pero se necesita recorrerlos de forma ordenada (por ejemplo, en orden alfabético por nombre o en orden ascendente por edad o salario) sin tener que mover físicamente todos los registros del arreglo cada vez que se inserta o elimina un elemento, se utiliza una estructura de datos llamada **lista enlazada** (*linked list*) (Jiménez Murillo, 2012, Cap. 6.7.1, pp. 248–253).

### 1.1 Una Lista Simplemente Enlazada es una Relación Binaria
Como demuestra Jiménez Murillo (2012, pp. 248–252), una lista simplemente enlazada almacenada en memoria mediante arreglos paralelos consta de:
1. **Un vector de datos $A[1..N]$:** Guarda la información de cada nodo (por ejemplo, nombres de personas o registros completos) en el orden cronológico en que van llegando (altas).
2. **Un vector de apuntadores $P[1..N]$:** Guarda en la posición $i$ el **índice (dirección)** del siguiente elemento en el orden lógico de recorrido. El símbolo **`*`** (o `NULL` / `0` / `-1`) indica el **fin de la lista**.
3. **Una variable cabecera de inicio $X$:** Guarda el índice de la posición en $A$ donde se encuentra el **primer elemento** del recorrido ordenado (cuando la lista está vacía, $X = *$).

- **Interpretación como relación matemática y grafo dirigido:**
  Cada apuntador $P[i] = j$ define el par ordenado $(A[i], A[j]) \in R$, lo que convierte a la lista enlazada en una **relación binaria cuyo grafo dirigido es una cadena lineal** que comienza en el nodo apuntado por $X$ y termina en el nodo cuyo apuntador es `*`:
  $$X \longrightarrow \text{Nodo}_1 \longrightarrow \text{Nodo}_2 \longrightarrow \dots \longrightarrow \text{Nodo}_k \longrightarrow *$$

- **Operaciones de Alta (Inserción) y Baja (Eliminación) en $O(1)$ movimientos físicos:**
  - **Alta (inserción de un nuevo registro):** El nuevo dato se escribe en la primera celda libre al final del arreglo $A$ (sin desplazar los datos existentes) y únicamente se ajustan dos apuntadores en $P$ (o la variable de inicio $X$) para intercalarlo en su posición alfabética correcta.
  - **Baja (eliminación de un registro):** Para dar de baja a una persona, **no se borra físicamente de $A$**; simplemente se **desconecta** haciendo que el apuntador del nodo anterior salte directamente al nodo siguiente ($P[\text{anterior}] \leftarrow P[\text{eliminado}]$). El nodo desconectado queda fuera del recorrido (y su celda puede marcarse en una lista de espacios disponibles para reutilizarse posteriormente) (Jiménez Murillo, 2012, pp. 251–252).

### 1.2 Listas Múltiplemente Enlazadas (Múltiples Criterios de Ordenamiento)
Cuando un mismo archivo de registros (por ejemplo, `Nombre` y `Edad`) debe poder recorrerse rápidamente bajo **dos o más criterios distintos** (por ejemplo, alfabéticamente por nombre y ascendentemente por edad) sin duplicar los datos en memoria:
- Se mantiene un solo arreglo de registros $A[1..N]$.
- Se definen **dos variables de inicio** ($X$ para el inicio alfabético por nombre, e $Y$ para el inicio ascendente por edad) y **dos columnas de apuntadores** ($P_{\text{nombre}}$ y $P_{\text{edad}}$), las cuales representan **dos relaciones binarias distintas sobre el mismo conjunto de nodos $A$** (Jiménez Murillo, 2012, Ej. 6.12, pp. 252–253).

---

## 2. Aplicación en Bases de Datos Relacionales y Álgebra Relacional

En los sistemas manejadores de bases de datos relacionales (como PostgreSQL, MySQL, Oracle o SQL Server), propuestos por **E. F. Codd** ($1970$), cada **archivo o tabla** con $n$ campos (columnas o atributos) y $m$ registros (filas o tuplas) es formalmente una **relación $n$-aria**:

$$R \subseteq D_1 \times D_2 \times \dots \times D_n$$

donde $D_k$ es el dominio del atributo $k$ (por ejemplo, `Registro`, `Nombre`, `Puesto`, `Salario`, `Antigüedad`, `Horas_Extras`).

### Operaciones Booleano-Relacionales entre Archivos (Jiménez Murillo, 2012, Cap. 6.7.2, pp. 253–256)
Como ilustra Jiménez Murillo en el Ejemplo 6.13, los manejadores de bases de datos responden consultas complejas combinando archivos mediante **álgebra relacional** y **matrices booleanas**:
1. **Evaluación de condiciones (Selección booleana $\sigma$):** Dada una condición lógica sobre los campos —por ejemplo, $(\text{Puesto} = \text{«Supervisor»}) \land (\text{Antigüedad} > 5)$, o bien $(\text{H. Extras} > 0) \lor (\text{Puesto} = \text{«Gerente»})$—, se evalúa cada celda o registro colocando un **$1$** donde se cumple la condición y un **$0$** donde no se cumple.
2. **Unión ($\cup$) e Intersección ($\cap$) de relaciones:** Se combinan las tablas o máscaras booleanas de los archivos $A$ y $B$ aplicando suma lógica ($\cup$) o producto lógico ($\cap$) registro por registro.
3. **Proyección y reordenamiento de campos ($\pi$):** Finalmente se seleccionan únicamente las columnas solicitadas en el orden requerido y los registros que cumplieron la condición booleana ($1$), renumerando los registros de la nueva relación resultante.

---

## 3. Aplicación de las Funciones en Lenguajes de Programación, Hashing y Criptografía

### 3.1 Funciones en Lenguajes de Programación (Subrutinas y Modularidad)
En los lenguajes de programación (`Java`, `C++`, `Python`, `Pascal`), además de las funciones matemáticas y de biblioteca integradas (`sin(x)`, `cos(x)`, `abs(x)`, `sqrt(x)`, `mod(a, b)`), el programador define sus propias funciones especificando (Jiménez Murillo, 2012, Cap. 6.8 y 6.9, pp. 258–259, 267):
- **Nombre de la función** y **lista de parámetros formales con sus tipos de datos** (el dominio $A_1 \times A_2 \times \dots \times A_k$).
- **Tipo de dato de retorno** (el codominio $B$).
- **Cuerpo algorítmico determinista:** Garantiza que para los mismos valores de entrada siempre se devuelva un único resultado, cumpliendo estrictamente la definición matemática de función.
- **Composición de funciones en código:** Permite anidar llamadas en una sola expresión, como `w := abs(sqrt(cos(x - 3 * y)))`, que evalúa la función compuesta $(h \circ g \circ f)(x, y)$ de adentro hacia afuera (Jiménez Murillo, 2012, p. 262).

### 3.2 Funciones de Dispersión (*Hashing*) para Búsqueda en Tiempo $O(1)$
Cuando se desea almacenar y localizar registros (identificados por una clave numérica grande $k$, como una matrícula, RFC o código de producto) dentro de una tabla en memoria de tamaño fijo $m$ (con índices $0, 1, \dots, m - 1$) sin tener que recorrer toda la tabla, se utiliza una **función de dispersión** (o **función *hash***) (Johnsonbaugh, 2005, Secc. 5.1; Epp, 2012, Secc. 8.4):

$$h: U \to \{0, 1, \dots, m - 1\}$$

La función *hash* más utilizada es el **método de la división (aritmética modular)**:

$$\boxed{h(k) = k \bmod m}$$

(donde habitualmente se elige $m$ como un número primo para distribuir uniformemente las claves).
- **Colisión (Falta de inyectividad):** Como el universo de claves posibles $|U|$ es mucho mayor que el número de celdas $m$ de la tabla, la función $h$ **no es inyectiva**: puede ocurrir que dos claves distintas $k_1 \neq k_2$ produzcan la misma dirección $h(k_1) = h(k_2)$. Este fenómeno se llama **colisión**.
- **Resolución de colisiones:**
  1. **Encadenamiento separado (*Chaining*):** Cada celda $j \in \{0, \dots, m-1\}$ de la tabla apunta a una **lista enlazada** que contiene todas las claves de la clase de equivalencia módulo $m$ cuya función hash dio $j$.
  2. **Direccionamiento abierto (*Sondeo lineal* / *Linear Probing*):** Si la celda $h(k)$ ya está ocupada, se prueba secuencialmente la siguiente celda disponible:
     $$h_i(k) = \big(h(k) + i\big) \bmod m \qquad (i = 1, 2, 3, \dots)$$

---

## Ejemplos de Práctica (Resueltos Paso a Paso)

### Ejemplo 5.5.1: Construcción, inserción (alta) y eliminación (baja) en una Lista Enlazada Simple
Sea $A$ un vector para guardar nombres de personas en el orden en que llegan, $P$ un vector de las mismas dimensiones para guardar el apuntador al siguiente nombre en **orden alfabético**, y $X$ la variable que indica la posición donde inicia la lista (con `*` como marca de fin de lista) (Jiménez Murillo, 2012, Secc. 6.7.1, pp. 248–252):
a) Si llegan en orden los $5$ nombres: **«María», «Juan», «Ana», «Pedro», «Jaime»**, determine el valor de $X$, el estado de los arreglos $A$ y $P$, y la secuencia de recorrido.  
b) Si posteriormente se dan de **alta** los nombres **«Benito»** y **«Luis»**, y se da de **baja** a **«Juan»**, muestre cómo quedan actualizados los arreglos $A$ y $P$ y su grafo dirigido.

**Solución:**
- **a) Estado tras llegar María (1), Juan (2), Ana (3), Pedro (4) y Jaime (5):**
  El orden alfabético correcto de los cinco nombres es:
  $$\text{Ana (pos. 3)} \longrightarrow \text{Jaime (pos. 5)} \longrightarrow \text{Juan (pos. 2)} \longrightarrow \text{María (pos. 1)} \longrightarrow \text{Pedro (pos. 4)} \longrightarrow *$$
  Por lo tanto, la variable de inicio vale **$X = 3$** (apunta a Ana), y los arreglos quedan:

  | Índice $i$ | Vector de Datos $A[i]$ | Vector de Apuntadores $P[i]$ | Explicación de la relación $(A[i], A[P[i]])$ |
  | :---: | :--- | :---: | :--- |
  | **1** | María | `4` | Después de María sigue Pedro (pos. `4`) |
  | **2** | Juan | `1` | Después de Juan sigue María (pos. `1`) |
  | **3** | Ana | `5` | **Inicio ($X=3$):** Después de Ana sigue Jaime (pos. `5`) |
  | **4** | Pedro | `*` | Pedro es el último alfabéticamente (fin de lista `*`) |
  | **5** | Jaime | `2` | Después de Jaime sigue Juan (pos. `2`) |

- **b) Estado tras dar de alta a «Benito» (pos. 6) y «Luis» (pos. 7), y dar de baja a «Juan» (pos. 2):**
  - «Benito» se coloca en $A[6]$ y se inserta alfabéticamente entre Ana (pos. `3`) y Jaime (pos. `5`): ahora $P[3] = 6$ y $P[6] = 5$.
  - «Luis» se coloca en $A[7]$. Como «Juan» (pos. `2`) se da de baja, se desconecta a Juan haciendo que Jaime (pos. `5`) apunte directamente a Luis ($P[5] = 7$) y Luis apunte a María ($P[7] = 1$).
  - La variable de inicio sigue siendo **$X = 3$**:

  | Índice $i$ | Vector de Datos $A[i]$ | Vector de Apuntadores $P[i]$ | Estado del nodo en el grafo dirigido |
  | :---: | :--- | :---: | :--- |
  | **1** | María | `4` | Conectado: María $\to$ Pedro (`4`) |
  | **2** | *Juan (baja)* | `1` | **Desconectado:** Ningún apuntador llega a la posición `2` |
  | **3** | Ana | `6` | **Inicio ($X=3$):** Ana $\to$ Benito (`6`) |
  | **4** | Pedro | `*` | Fin de lista (`*`) |
  | **5** | Jaime | `7` | Conectado: Jaime $\to$ Luis (`7`) *(saltó a Juan)* |
  | **6** | Benito | `5` | Conectado: Benito $\to$ Jaime (`5`) |
  | **7** | Luis | `1` | Conectado: Luis $\to$ María (`1`) |

  - **Nuevo grafo dirigido de recorrido:**
    $$X = 3 \implies \text{Ana (3)} \to \text{Benito (6)} \to \text{Jaime (5)} \to \text{Luis (7)} \to \text{María (1)} \to \text{Pedro (4)} \to *$$

---

### Ejemplo 5.5.2: Lista Doblemente Enlazada por dos atributos (Nombre y Edad)
Coloque en un arreglo $A$ los siguientes $6$ registros en el orden en que llegan: **Mario (50), Alfonso (25), Paola (17), Carlos (20), Francisco (18), Carmen (14)**, y construya el arreglo de apuntadores $P$ con dos columnas para recorrer la información tanto **alfabéticamente por nombre** (inicio $X$) como **ascendentemente por edad** (inicio $Y$) (Jiménez Murillo, 2012, Ej. 6.12, p. 252).

**Solución:**
1. **Orden alfabético por Nombre:**
   $$\text{Alfonso (2)} \to \text{Carlos (4)} \to \text{Carmen (6)} \to \text{Francisco (5)} \to \text{Mario (1)} \to \text{Paola (3)} \to * \qquad \implies \mathbf{X = 2}$$
2. **Orden ascendente por Edad:**
   $$\text{Carmen (14, pos. 6)} \to \text{Paola (17, pos. 3)} \to \text{Francisco (18, pos. 5)} \to \text{Carlos (20, pos. 4)} \to \text{Alfonso (25, pos. 2)} \to \text{Mario (50, pos. 1)} \to * \implies \mathbf{Y = 6}$$

| Posición $i$ | Nombre en $A[i]$ | Edad en $A[i]$ | Apuntador Nombre $P_{\text{nom}}[i]$ ($X = 2$) | Apuntador Edad $P_{\text{edad}}[i]$ ($Y = 6$) |
| :---: | :--- | :---: | :---: | :---: |
| **1** | Mario | $50$ | `3` *(sigue Paola)* | `*` *(mayor edad, fin)* |
| **2** | Alfonso | $25$ | `4` *(inicio $X=2$, sigue Carlos)* | `1` *(sigue Mario, 50)* |
| **3** | Paola | $17$ | `*` *(último nombre, fin)* | `5` *(sigue Francisco, 18)* |
| **4** | Carlos | $20$ | `6` *(sigue Carmen)* | `2` *(sigue Alfonso, 25)* |
| **5** | Francisco | $18$ | `1` *(sigue Mario)* | `4` *(sigue Carlos, 20)* |
| **6** | Carmen | $14$ | `5` *(sigue Francisco)* | `3` *(inicio $Y=6$, sigue Paola, 17)* |

---

### Ejemplo 5.5.3: Operaciones entre relaciones en Bases de Datos
Considere los archivos (relaciones) `Archivo A` y `Archivo B` de los empleados de una empresa (Jiménez Murillo, 2012, Ej. 6.13, pp. 253–256):

| Reg. | Nombre | Puesto | H. Semanales (`Archivo A`) | H. Extras (`Archivo A`) | Salario (`Archivo B`) | Antigüedad (`Archivo B`) |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: |
| **1** | Juan | Supervisor | $40$ | $0$ | $\$4\,000$ | $5$ |
| **2** | Lorena | Secretaria | $40$ | $0$ | $\$3\,000$ | $2$ |
| **3** | Jaime | Obrero | $40$ | $12$ | $\$1\,800$ | $7$ |
| **4** | Alicia | Gerente | $40$ | $0$ | $\$8\,000$ | $3$ |
| **5** | Alfredo | Obrero | $40$ | $8$ | $\$2\,100$ | $9$ |
| **6** | Carlos | Supervisor | $40$ | $6$ | $\$4\,800$ | $6$ |
| **7** | Alberto | Supervisor | $40$ | $4$ | $\$2\,400$ | $2$ |

Determine:
a) Una relación `Archivo C` que contenga los campos `Nombre, Puesto, H. Extras, Antigüedad` (en ese orden) para los trabajadores cuyo puesto sea **«Supervisor» Y tengan una antigüedad $\ge 5$ años**.  
b) Una relación `Archivo D` que contenga los campos `Puesto, H. Extras, Nombre` (en ese orden) para los trabajadores que **hayan trabajado horas extras ($> 0$) O BIEN su puesto sea «Gerente»**.

**Solución:**
- **a) Intersección booleana $(\text{Puesto} = \text{«Supervisor»}) \cap (\text{Antigüedad} \ge 5)$:**
  - Cumplen `Puesto = Supervisor`: registros `{1, 6, 7}`.
  - Cumplen `Antigüedad >= 5`: registros `{1, 3, 5, 6}`.
  - Su intersección es `{1, 6, 7} ∩ {1, 3, 5, 6} = {1, 6}` (Juan y Carlos). Proyectando los campos en el orden pedido y renumerando los registros:

    | Reg. | Nombre | Puesto | H. Extras | Antigüedad |
    | :---: | :--- | :--- | :---: | :---: |
    | **1** | Juan | Supervisor | $0$ | $5$ |
    | **2** | Carlos | Supervisor | $6$ | $6$ |

- **b) Unión booleana $(\text{H. Extras} > 0) \cup (\text{Puesto} = \text{«Gerente»})$:**
  - Cumplen `H. Extras > 0`: registros `{3, 5, 6, 7}`.
  - Cumplen `Puesto = Gerente`: registro `{4}`.
  - Su unión es `{3, 4, 5, 6, 7}`. Proyectando los campos `Puesto, H. Extras, Nombre` en ese orden:

    | Reg. | Puesto | H. Extras | Nombre |
    | :---: | :--- | :---: | :--- |
    | **1** | Obrero | $12$ | Jaime |
    | **2** | Gerente | $0$ | Alicia |
    | **3** | Obrero | $8$ | Alfredo |
    | **4** | Supervisor | $6$ | Carlos |
    | **5** | Supervisor | $4$ | Alberto |

---

### Ejemplo 5.5.4: Aplicación de Funciones de Dispersión (*Hashing*) con Sondeo Lineal
Se desea almacenar los $6$ números de control (claves) $K = \{104, 215, 322, 145, 287, 309\}$ en una tabla *hash* de $m = 7$ celdas (indexadas de $0$ a $6$) utilizando la función de dispersión:
$$h(k) = k \bmod 7$$
y resolviendo las colisiones mediante **sondeo lineal** $h_i(k) = (h(k) + i) \bmod 7$. Muestre paso a paso la asignación de cada clave y el estado final de la tabla.

**Solución:**
Evaluamos $h(k) = k \bmod 7$ en el orden de llegada:
1. **$k = 104$:** $104 = 14 \times 7 + 6 \implies h(104) = \mathbf{6}$. Celda `6` libre $\to T[6] = 104$.
2. **$k = 215$:** $215 = 30 \times 7 + 5 \implies h(215) = \mathbf{5}$. Celda `5` libre $\to T[5] = 215$.
3. **$k = 322$:** $322 = 46 \times 7 + 0 \implies h(322) = \mathbf{0}$. Celda `0` libre $\to T[0] = 322$.
4. **$k = 145$:** $145 = 20 \times 7 + 5 \implies h(145) = 5$. **¡Colisión en celda `5`!**
   - Probamos $i = 1$: $(5 + 1) \bmod 7 = 6$ *(ocupada por $104$)*.
   - Probamos $i = 2$: $(5 + 2) \bmod 7 = 0$ *(ocupada por $322$)*.
   - Probamos $i = 3$: $(5 + 3) \bmod 7 = \mathbf{1}$ *(libre)* $\to T[1] = 145$.
5. **$k = 287$:** $287 = 41 \times 7 + 0 \implies h(287) = 0$. **¡Colisión en celda `0`!**
   - Probamos $i = 1$: $(0 + 1) \bmod 7 = 1$ *(ocupada por $145$)*.
   - Probamos $i = 2$: $(0 + 2) \bmod 7 = \mathbf{2}$ *(libre)* $\to T[2] = 287$.
6. **$k = 309$:** $309 = 44 \times 7 + 1 \implies h(309) = 1$. **¡Colisión en celda `1`!**
   - Probamos $i = 1$: $(1 + 1) \bmod 7 = 2$ *(ocupada por $287$)*.
   - Probamos $i = 2$: $(1 + 2) \bmod 7 = \mathbf{3}$ *(libre)* $\to T[3] = 309$.

**Estado final de la Tabla Hash:**

| Índice de celda | `0` | `1` | `2` | `3` | `4` | `5` | `6` |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Clave almacenada** | `322` | `145` | `287` | `309` | *(vacía)* | `215` | `104` |

---

## Ejercicios de Tarea (Práctica en Casa)

> **Instrucciones:** Resuelva cada uno de los siguientes problemas prácticos mostrando las tablas de arreglos, apuntadores y relaciones resultantes.

1. **Gestión de altas y bajas en una lista simplemente enlazada (Jiménez Murillo, Prob. 6.9, p. 275):**  
   Supóngase que a una estructura de lista enlazada llegan en orden los siguientes nombres: **«Roberto», «Lucía», «Fernando», «Diana», «Alejandro», «Sofía»**.  
   a) Determine el valor de la variable de inicio $X$ y el contenido de los arreglos $A$ (nombres) y $P$ (apuntadores) para recorrer la lista en **orden alfabético ascendente**, así como su grafo dirigido.  
   b) Actualice el valor de $X$ y los arreglos $A$ y $P$ si posteriormente se dan de **alta** los nombres **«Beatriz»** y **«Miguel»**, y se dan de **baja** los nombres **«Alejandro»** y **«Fernando»**.
   <!--
   Solución del Ejercicio 1:
   - a) Estado inicial con los 6 nombres en orden de llegada:
        1: Roberto, 2: Lucía, 3: Fernando, 4: Diana, 5: Alejandro, 6: Sofía.
        Orden alfabético:
        Alejandro (5) -> Diana (4) -> Fernando (3) -> Lucía (2) -> Roberto (1) -> Sofía (6) -> *
        Por lo tanto, X = 5, y los arreglos quedan:
        - Pos 1: A[1] = Roberto,   P[1] = 6
        - Pos 2: A[2] = Lucía,     P[2] = 1
        - Pos 3: A[3] = Fernando,  P[3] = 2
        - Pos 4: A[4] = Diana,     P[4] = 3
        - Pos 5: A[5] = Alejandro, P[5] = 4   (Inicio X = 5)
        - Pos 6: A[6] = Sofía,     P[6] = *

   - b) Altas de Beatriz (pos. 7) y Miguel (pos. 8), y bajas de Alejandro (pos. 5) y Fernando (pos. 3):
        - Los nombres activos ahora son: Beatriz (7), Diana (4), Lucía (2), Miguel (8), Roberto (1), Sofía (6).
        - Nuevo orden alfabético:
          Beatriz (7) -> Diana (4) -> Lucía (2) -> Miguel (8) -> Roberto (1) -> Sofía (6) -> *
        - Como Alejandro (5) era el primero y se dio de baja, ahora la variable de inicio cambia a X = 7 (Beatriz).
        - Diana (4) que apuntaba a Fernando (3) ahora salta a Lucía (2): P[4] = 2.
        - Lucía (2) ahora apunta a Miguel (8): P[2] = 8, y Miguel (8) apunta a Roberto (1): P[8] = 1.
        Tabla final actualizada (X = 7):
        - Pos 1: A[1] = Roberto,    P[1] = 6
        - Pos 2: A[2] = Lucía,      P[2] = 8
        - Pos 3: A[3] = (Fernando), P[3] = 2 (desconectado)
        - Pos 4: A[4] = Diana,      P[4] = 2
        - Pos 5: A[5] = (Alejandro),P[5] = 4 (desconectado)
        - Pos 6: A[6] = Sofía,      P[6] = *
        - Pos 7: A[7] = Beatriz,    P[7] = 4 (Nuevo inicio X = 7)
        - Pos 8: A[8] = Miguel,     P[8] = 1
   -->

2. **Lista doblemente enlazada por tres atributos (Jiménez Murillo, Prob. 6.10, p. 276):**  
   A un archivo llegan en orden los datos de $5$ productos con su `Nombre` y su `Precio`:  
   1) `Monitor, $3200`; $\quad$ 2) `Teclado, $450`; $\quad$ 3) `Ratón, $280`; $\quad$ 4) `Impresora, $2600`; $\quad$ 5) `Escáner, $1900`.  
   Diseñe la tabla de arreglos $A$ y $P$ junto con las variables de inicio $X$ (para recorrer en **orden alfabético por nombre**) e $Y$ (para recorrer en **orden ascendente por precio**).
   <!--
   Solución del Ejercicio 2:
   - Recorrido alfabético por Nombre:
     Escáner (5) -> Impresora (4) -> Monitor (1) -> Ratón (3) -> Teclado (2) -> *
     Por lo tanto, X = 5.
   - Recorrido ascendente por Precio:
     Ratón ($280, pos 3) -> Teclado ($450, pos 2) -> Escáner ($1900, pos 5) -> Impresora ($2600, pos 4) -> Monitor ($3200, pos 1) -> *
     Por lo tanto, Y = 3.
   - Tabla de arreglos A y P (con X = 5, Y = 3):
     * Pos 1: Monitor   | $3200 | P_nom[1] = 3 | P_precio[1] = *
     * Pos 2: Teclado   | $450  | P_nom[2] = * | P_precio[2] = 5
     * Pos 3: Ratón     | $280  | P_nom[3] = 2 | P_precio[3] = 2 (Inicio Y = 3)
     * Pos 4: Impresora | $2600 | P_nom[4] = 1 | P_precio[4] = 1
     * Pos 5: Escáner   | $1900 | P_nom[5] = 4 | P_precio[5] = 4 (Inicio X = 5)
   -->

3. **Consultas relacionales booleanas sobre archivos de una base de datos (Jiménez Murillo, Prob. 6.11, p. 276):**  
   Utilizando los mismos archivos `Archivo A` y `Archivo B` del Ejemplo 5.5.3:  
   a) Obtenga la relación que contenga los campos `Antigüedad, Salario, Nombre, Puesto` (en ese orden) para los empleados que tengan un **Salario $> \$2\,000$ Y hayan trabajado Horas Extras ($> 0$)**.  
   b) Obtenga la relación que contenga los campos `Nombre, Salario, H. Semanales` para los empleados cuya **Antigüedad sea $\le 3$ años O BIEN su puesto sea «Obrero»**.
   <!--
   Solución del Ejercicio 3:
   - a) Condición booleana: (Salario > 2000) n (H. Extras > 0):
        - Cumplen Salario > 2000: registros {1 ($4000), 2 ($3000), 4 ($8000), 5 ($2100), 6 ($4800), 7 ($2400)}.
        - Cumplen H. Extras > 0: registros {3 (12), 5 (8), 6 (6), 7 (4)}.
        - Intersección: registros {5, 6, 7} (Alfredo, Carlos y Alberto).
        Relación resultante con campos (Antigüedad, Salario, Nombre, Puesto):
        * Reg 1 (orig 5): 9 | 2100 | Alfredo | Obrero
        * Reg 2 (orig 6): 6 | 4800 | Carlos  | Supervisor
        * Reg 3 (orig 7): 2 | 2400 | Alberto | Supervisor

   - b) Condición booleana: (Antigüedad <= 3) u (Puesto = "Obrero"):
        - Cumplen Antigüedad <= 3: registros {2 (2 años), 4 (3 años), 7 (2 años)}.
        - Cumplen Puesto = Obrero: registros {3, 5}.
        - Unión: registros {2, 3, 4, 5, 7}.
        Relación resultante con campos (Nombre, Salario, H. Semanales):
        * Reg 1 (orig 2): Lorena  | 3000 | 40
        * Reg 2 (orig 3): Jaime   | 1800 | 40
        * Reg 3 (orig 4): Alicia  | 8000 | 40
        * Reg 4 (orig 5): Alfredo | 2100 | 40
        * Reg 5 (orig 7): Alberto | 2400 | 40
   -->

4. **Diseño de una Tabla Hash y Función de Cifrado Biyectivo Modular:**  
   a) Inserte las $7$ claves $K = \{54, 76, 98, 120, 43, 65, 87\}$ en una tabla *hash* de $m = 11$ celdas ($0$ a $10$) usando $h(k) = k \bmod 11$ y sondeo lineal $h_i(k) = (h(k) + i) \bmod 11$.  
   b) En criptografía clásica (Cifrado Afín sobre un alfabeto de $27$ letras identificadas con $\mathbb{Z}_{27} = \{0, 1, \dots, 26\}$), se define la función de cifrado $E(x) = (5x + 3) \bmod 27$. Compruebe que $f(x)$ es biyectiva verificando que la función de descifrado es $D(y) = 11(y - 3) \bmod 27$ (ya que $5 \times 11 = 55 \equiv 1 \pmod{27}$), y cifre y descifre el valor $x = 4$.
   <!--
   Solución del Ejercicio 4:
   - a) Cálculo de h(k) = k mod 11:
        1) k = 54:  54 = 4*11 + 10 => h(54) = 10 -> T[10] = 54.
        2) k = 76:  76 = 6*11 + 10 => h(76) = 10 (colisión en 10) -> prueba (10+1) mod 11 = 0 -> T[0] = 76.
        3) k = 98:  98 = 8*11 + 10 => h(98) = 10 (colisión en 10 y 0) -> prueba 1 -> T[1] = 98.
        4) k = 120: 120 = 10*11 + 10 => h(120) = 10 (colisión en 10, 0, 1) -> T[2] = 120.
        5) k = 43:  43 = 3*11 + 10 => h(43) = 10 (colisión en 10, 0, 1, 2) -> T[3] = 43.
        6) k = 65:  65 = 5*11 + 10 => h(65) = 10 (colisión en 10..3) -> T[4] = 65.
        7) k = 87:  87 = 7*11 + 10 => h(87) = 10 (colisión en 10..4) -> T[5] = 87.
        (Nota: todas las claves eran congruentes a 10 mod 11, ilustrando el agrupamiento primario o clustering del sondeo lineal).

   - b) Cifrado y descifrado afín en Z_27:
        - Comprobación algebraica de que D(E(x)) = x mod 27:
          D(E(x)) = 11 * ( (5x + 3) - 3 ) mod 27 = 11 * (5x) mod 27 = (55 * x) mod 27.
          Como 55 = 2 * 27 + 1, se tiene 55 === 1 (mod 27), por lo que (55 * x) mod 27 = (1 * x) mod 27 = x.
          Así, D = E^-1 y E es biyectiva sobre Z_27.
        - Para x = 4:
          * Cifrado:   y = E(4) = (5(4) + 3) mod 27 = 23 mod 27 = 23.
          * Descifrado: D(23) = 11(23 - 3) mod 27 = 11(20) mod 27 = 220 mod 27 = 4 (pues 220 = 8*27 + 4).
   -->
