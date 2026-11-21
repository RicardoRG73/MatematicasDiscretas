---
marp: true
theme: discretas
size: 16:9
paginate: true
math: mathjax
header: "Matemáticas Discretas · Unidad 5"
footer: "Subtema 5.5 · Aplicaciones en computación"
---
<!-- _class: portada -->
<!-- _paginate: false -->
<!-- _header: "" -->
<!-- _footer: "" -->

# 5.5 Aplicaciones en la computación
## Listas enlazadas, bases de datos relacionales, subrutinas y tablas hash

- **Unidad:** 5. Relaciones | **Subtema:** 5.5
- **Objetivo:** Aplicar relaciones binarias, relaciones $n$-arias y funciones en estructuras de datos, consultas relacionales, programación, *hashing* y criptografía modular.

---

## 1.1 Listas Simplemente Enlazadas como Relaciones

Para recorrer datos en orden lógico sin desplazar elementos al insertar o borrar, se emplean arreglos paralelos:

- **Vector de datos $A[1..N]$:** almacena cada nodo en orden cronológico de llegada.
- **Vector de apuntadores $P[1..N]$:** guarda el índice del siguiente elemento lógico (`*` o `NULL` / `0` / `-1` indica fin).
- **Cabecera de inicio $X$:** posición del primer elemento ordenado ($X = *$ si está vacía).
- **Grafo dirigido:** cada $P[i] = j$ define $(A[i], A[j]) \in R$, formando una cadena lineal:
  $$X \longrightarrow \text{Nodo}_1 \longrightarrow \text{Nodo}_2 \longrightarrow \dots \longrightarrow \text{Nodo}_k \longrightarrow *$$

---

## 1.1 Altas, Bajas y 1.2 Listas Múltiplemente Enlazadas

- **Alta (inserción) en $O(1)$ movimientos físicos:** el nuevo registro se escribe en la primera celda libre al final de $A$ y sólo se ajustan dos apuntadores en $P$ (o $X$).
- **Baja (eliminación):** no se borra físicamente de $A$; se desconecta haciendo $P[\text{anterior}] \leftarrow P[\text{eliminado}]$ *(su espacio queda disponible para reutilizarse)*.
- **Listas múltiplemente enlazadas:** para ordenar un mismo arreglo $A[1..N]$ bajo **dos o más criterios** sin duplicar datos (p. ej. nombre y edad):
  - Se usan **dos cabeceras** ($X$ para nombre, $Y$ para edad) y **dos columnas de apuntadores** ($P_{\text{nombre}}, P_{\text{edad}}$), es decir, dos relaciones binarias sobre $A$.

---

## 2. Bases de Datos Relacionales y Álgebra Relacional

En el modelo de **E. F. Codd (1970)**, cada tabla con $n$ columnas (atributos) y $m$ filas (tuplas) es una **relación $n$-aria**:
$$R \subseteq D_1 \times D_2 \times \dots \times D_n$$

- **1. Selección booleana ($\sigma$):** evalúa condiciones lógicas sobre los campos asignando $1$ si cumple y $0$ si no cumple.
- **2. Unión ($\cup$) e Intersección ($\cap$):** combina tablas o máscaras booleanas aplicando suma lógica ($\cup$) o producto lógico ($\cap$) registro por registro.
- **3. Proyección ($\pi$):** extrae y reordena las columnas solicitadas de los registros con $1$, renumerando las filas resultantes.

---

## 3.1 Funciones en Lenguajes de Programación

Además de funciones integradas (`sin`, `cos`, `abs`, `sqrt`, `mod`), en `Java`, `C++`, `Python` o `Pascal` el programador define funciones con:

- **Nombre y parámetros formales con sus tipos de datos:** representan el dominio $A_1 \times A_2 \times \dots \times A_k$.
- **Tipo de dato de retorno:** representa el codominio $B$.
- **Cuerpo algorítmico determinista:** ante iguales entradas devuelve un único resultado (cumple la definición matemática de función).
- **Composición en código:** `w := abs(sqrt(cos(x - 3 * y)))` evalúa $(h \circ g \circ f)(x, y)$ de adentro hacia afuera.

---

## 3.2 Funciones de Dispersión (*Hashing*) en $O(1)$

Para localizar claves grandes $k \in U$ en una tabla de $m$ celdas ($0$ a $m - 1$) sin recorrido lineal, se usa $h: U \to \{0, 1, \dots, m - 1\}$:
$$\boxed{h(k) = k \bmod m} \qquad (m\text{ suele ser primo para distribuir mejor})$$

- **Colisión (falta de inyectividad):** como $|U| \gg m$, pueden existir $k_1 \neq k_2$ con $h(k_1) = h(k_2)$.
- **Resolución de colisiones:**
  1. **Encadenamiento separado (*Chaining*):** cada celda $j$ apunta a una lista enlazada con las claves de esa clase módulo $m$.
  2. **Sondeo lineal (*Linear Probing*):** prueba secuencialmente la siguiente celda libre:
     $$h_i(k) = \big(h(k) + i\big) \bmod m \qquad (i = 1, 2, 3, \dots)$$

---
<!-- _class: seccion -->
<!-- _header: "" -->
<!-- _footer: "" -->

## Ejemplos de Práctica

Listas enlazadas simples y dobles, consultas en bases de datos y tablas *hash*.

---
<!-- _class: compacta -->

## Ejemplo 5.5.1: Lista enlazada simple inicial (1/2)

Llegan en orden: **María (1), Juan (2), Ana (3), Pedro (4), Jaime (5)**. El recorrido alfabético inicia en **$X = 3$**:
$$\text{Ana (3)} \longrightarrow \text{Jaime (5)} \longrightarrow \text{Juan (2)} \longrightarrow \text{María (1)} \longrightarrow \text{Pedro (4)} \longrightarrow *$$

| Índice $i$ | Vector de Datos $A[i]$ | Apuntador $P[i]$ | Explicación $(A[i], A[P[i]])$ |
| :---: | :--- | :---: | :--- |
| **1** | María | `4` | Después de María sigue Pedro (pos. `4`) |
| **2** | Juan | `1` | Después de Juan sigue María (pos. `1`) |
| **3** | Ana | `5` | **Inicio ($X = 3$):** sigue Jaime (pos. `5`) |
| **4** | Pedro | `*` | Último alfabéticamente (fin de lista `*`) |
| **5** | Jaime | `2` | Después de Jaime sigue Juan (pos. `2`) |

---
<!-- _class: compacta -->

## Ejemplo 5.5.1: Altas y bajas en la lista (2/2)

Se da de **alta** a **Benito** (`6`) y **Luis** (`7`), y de **baja** a **Juan** (`2`). Se ajustan $P[3]=6$, $P[6]=5$, $P[5]=7$ y $P[7]=1$ ($X = 3$):

| $i$ | Datos $A[i]$ | $P[i]$ | Estado en el grafo dirigido |
| :---: | :--- | :---: | :--- |
| **1** | María | `4` | Conectado: María $\to$ Pedro (`4`) |
| **2** | *Juan (baja)* | `1` | **Desconectado:** ningún apuntador llega a `2` |
| **3** | Ana | `6` | **Inicio ($X=3$):** Ana $\to$ Benito (`6`) |
| **4** | Pedro | `*` | Fin de lista (`*`) |
| **5** | Jaime | `7` | Conectado: Jaime $\to$ Luis (`7`) *(saltó a Juan)* |
| **6** | Benito | `5` | Conectado: Benito $\to$ Jaime (`5`) |
| **7** | Luis | `1` | Conectado: Luis $\to$ María (`1`) |

$$\text{Recorrido: } X=3 \implies \text{Ana(3)} \to \text{Benito(6)} \to \text{Jaime(5)} \to \text{Luis(7)} \to \text{María(1)} \to \text{Pedro(4)} \to *$$

---
<!-- _class: compacta -->

## Ejemplo 5.5.2: Lista doblemente enlazada (Nombre y Edad)

Llegan: **Mario (50), Alfonso (25), Paola (17), Carlos (20), Francisco (18), Carmen (14)**.  
- **Nombre ($X = 2$):** $\text{Alfonso(2)} \to \text{Carlos(4)} \to \text{Carmen(6)} \to \text{Francisco(5)} \to \text{Mario(1)} \to \text{Paola(3)} \to *$  
- **Edad ($Y = 6$):** $\text{Carmen(6)} \to \text{Paola(3)} \to \text{Francisco(5)} \to \text{Carlos(4)} \to \text{Alfonso(2)} \to \text{Mario(1)} \to *$

| Pos. $i$ | Nombre $A[i]$ | Edad | $P_{\text{nom}}[i]$ ($X = 2$) | $P_{\text{edad}}[i]$ ($Y = 6$) |
| :---: | :--- | :---: | :---: | :---: |
| **1** | Mario | $50$ | `3` *(sigue Paola)* | `*` *(mayor edad, fin)* |
| **2** | Alfonso | $25$ | `4` *(inicio $X=2$, Carlos)* | `1` *(sigue Mario, 50)* |
| **3** | Paola | $17$ | `*` *(último nombre, fin)* | `5` *(sigue Francisco, 18)* |
| **4** | Carlos | $20$ | `6` *(sigue Carmen)* | `2` *(sigue Alfonso, 25)* |
| **5** | Francisco | $18$ | `1` *(sigue Mario)* | `4` *(sigue Carlos, 20)* |
| **6** | Carmen | $14$ | `5` *(sigue Francisco)* | `3` *(inicio $Y=6$, Paola)* |

---
<!-- _class: tabla-ancha -->

## Ejemplo 5.5.3: Relaciones en Bases de Datos (1/3)

Archivos `Archivo A` y `Archivo B` de los empleados de una empresa:

| Reg. | Nombre | Puesto | H. Semanales (`Archivo A`) | H. Extras (`Archivo A`) | Salario (`Archivo B`) | Antigüedad (`Archivo B`) |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: |
| **1** | Juan | Supervisor | $40$ | $0$ | &#36;4,000 | $5$ |
| **2** | Lorena | Secretaria | $40$ | $0$ | &#36;3,000 | $2$ |
| **3** | Jaime | Obrero | $40$ | $12$ | &#36;1,800 | $7$ |
| **4** | Alicia | Gerente | $40$ | $0$ | &#36;8,000 | $3$ |
| **5** | Alfredo | Obrero | $40$ | $8$ | &#36;2,100 | $9$ |
| **6** | Carlos | Supervisor | $40$ | $6$ | &#36;4,800 | $6$ |
| **7** | Alberto | Supervisor | $40$ | $4$ | &#36;2,400 | $2$ |

---

## Ejemplo 5.5.3: Consulta con intersección (2/3)

- **a) `Archivo C`:** Campos `Nombre, Puesto, H. Extras, Antigüedad` (en ese orden) para **Puesto = «Supervisor» Y Antigüedad $\ge 5$**:
  - `Puesto = Supervisor`: registros $\{1, 6, 7\}$.
  - `Antigüedad >= 5`: registros $\{1, 3, 5, 6\}$.
  - **Intersección:** $\{1, 6, 7\} \cap \{1, 3, 5, 6\} = \mathbf{\{1, 6\}}$ (Juan y Carlos).

| Reg. | Nombre | Puesto | H. Extras | Antigüedad |
| :---: | :--- | :--- | :---: | :---: |
| **1** | Juan | Supervisor | $0$ | $5$ |
| **2** | Carlos | Supervisor | $6$ | $6$ |

---
<!-- _class: compacta -->

## Ejemplo 5.5.3: Consulta con unión (3/3)

- **b) `Archivo D`:** Campos `Puesto, H. Extras, Nombre` (en ese orden) para **H. Extras $> 0$ O BIEN Puesto = «Gerente»**:
  - `H. Extras > 0`: registros $\{3, 5, 6, 7\}$.
  - `Puesto = Gerente`: registro $\{4\}$.
  - **Unión:** $\{3, 5, 6, 7\} \cup \{4\} = \mathbf{\{3, 4, 5, 6, 7\}}$.

| Reg. | Puesto | H. Extras | Nombre |
| :---: | :--- | :---: | :--- |
| **1** | Obrero | $12$ | Jaime |
| **2** | Gerente | $0$ | Alicia |
| **3** | Obrero | $8$ | Alfredo |
| **4** | Supervisor | $6$ | Carlos |
| **5** | Supervisor | $4$ | Alberto |

---
<!-- _class: compacta -->

## Ejemplo 5.5.4: Hashing con sondeo lineal (1/2)

Insertar $K = \{104, 215, 322, 145, 287, 309\}$ en $m = 7$ celdas ($0$ a $6$) con $h(k) = k \bmod 7$ y $h_i(k) = (h(k) + i) \bmod 7$:

1. **$k = 104$:** $104 = 14 \times 7 + 6 \implies h(104) = \mathbf{6} \to T[6] = 104$.
2. **$k = 215$:** $215 = 30 \times 7 + 5 \implies h(215) = \mathbf{5} \to T[5] = 215$.
3. **$k = 322$:** $322 = 46 \times 7 + 0 \implies h(322) = \mathbf{0} \to T[0] = 322$.
4. **$k = 145$:** $h(145) = 5$ *(colisión)*: $i=1 \to 6$ (oc.), $i=2 \to 0$ (oc.), $i=3 \to \mathbf{1} \to T[1] = 145$.
5. **$k = 287$:** $h(287) = 0$ *(colisión)*: $i=1 \to 1$ (oc.), $i=2 \to \mathbf{2} \to T[2] = 287$.
6. **$k = 309$:** $h(309) = 1$ *(colisión)*: $i=1 \to 2$ (oc.), $i=2 \to \mathbf{3} \to T[3] = 309$.

---
<!-- _class: tabla-ancha -->

## Ejemplo 5.5.4: Estado final de la Tabla Hash (2/2)

Tras resolver las colisiones por sondeo lineal en la tabla de tamaño $m = 7$, las seis claves quedan distribuidas así:

| Índice de celda | `0` | `1` | `2` | `3` | `4` | `5` | `6` |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Clave almacenada** | `322` | `145` | `287` | `309` | *(vacía)* | `215` | `104` |

- Tres claves ($104, 215, 322$) se ubicaron en su dirección inicial y tres ($145, 287, 309$) requirieron sondeo lineal; la celda `4` permanece disponible.

---
<!-- _class: seccion -->
<!-- _header: "" -->
<!-- _footer: "" -->

## Ejercicios de Tarea (Práctica en Casa)

Muestre las tablas de arreglos, apuntadores, relaciones resultantes y cálculos paso a paso.

---

## Tarea 1: Altas y bajas en lista enlazada simple

*(Jiménez Murillo, Prob. 6.9, p. 275)* Llegan en orden los nombres: **«Roberto», «Lucía», «Fernando», «Diana», «Alejandro», «Sofía»**.

- **a)** Determine el valor de inicio $X$ y el contenido de los arreglos $A$ (nombres) y $P$ (apuntadores) para recorrer la lista en **orden alfabético ascendente**, así como su grafo dirigido.
- **b)** Actualice $X$, $A$ y $P$ si posteriormente se dan de **alta** **«Beatriz»** y **«Miguel»**, y se dan de **baja** **«Alejandro»** y **«Fernando»**.

---

## Tarea 2: Lista doblemente enlazada por atributos

*(Jiménez Murillo, Prob. 6.10, p. 276)* A un archivo llegan en orden los datos de $5$ productos con su `Nombre` y `Precio`:

1. `Monitor`, &#36;3200
2. `Teclado`, &#36;450
3. `Ratón`, &#36;280
4. `Impresora`, &#36;2600
5. `Escáner`, &#36;1900

Diseñe la tabla de arreglos $A$ y $P$ junto con las variables de inicio $X$ (**orden alfabético por nombre**) e $Y$ (**orden ascendente por precio**).

---

## Tarea 3: Consultas relacionales booleanas

*(Jiménez Murillo, Prob. 6.11, p. 276)* Utilizando los mismos archivos `Archivo A` y `Archivo B` del Ejemplo 5.5.3:

- **a)** Obtenga la relación con los campos `Antigüedad, Salario, Nombre, Puesto` (en ese orden) para los empleados que tengan **Salario $>$ &#36;2,000 Y hayan trabajado Horas Extras ($> 0$)**.
- **b)** Obtenga la relación con los campos `Nombre, Salario, H. Semanales` para los empleados cuya **Antigüedad sea $\le 3$ años O BIEN su puesto sea «Obrero»**.

---

## Tarea 4: Tabla Hash y Cifrado Biyectivo Modular

- **a)** Inserte las $7$ claves $K = \{54, 76, 98, 120, 43, 65, 87\}$ en una tabla *hash* de $m = 11$ celdas ($0$ a $10$) usando $h(k) = k \bmod 11$ y sondeo lineal $h_i(k) = (h(k) + i) \bmod 11$.
- **b)** En el Cifrado Afín sobre $\mathbb{Z}_{27} = \{0, 1, \dots, 26\}$, se define $E(x) = (5x + 3) \bmod 27$. Compruebe que es biyectiva verificando que su inversa es $D(y) = 11(y - 3) \bmod 27$ (ya que $5 \times 11 = 55 \equiv 1 \pmod{27}$), y cifre y descifre $x = 4$.
