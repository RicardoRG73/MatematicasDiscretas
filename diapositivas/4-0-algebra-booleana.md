---
marp: true
theme: discretas
size: 16:9
paginate: true
math: mathjax
header: "Matemáticas Discretas · Unidad 4"
footer: "Unidad 4 · Álgebra Booleana"
---
<!-- _class: portada -->
<!-- _paginate: false -->
<!-- _header: "" -->
<!-- _footer: "" -->

# 4. Álgebra Booleana
## Panorama General de la Unidad

**Asignatura:** Matemáticas Discretas (`LISSI0211`) · Segundo Semestre
**Duración:** 10 horas · **Objetivo:** Optimizar expresiones lógicas y diseñar circuitos digitales eficientes mediante el álgebra booleana.

---

## Información General de la Unidad

| Campo | Detalle |
| :--- | :--- |
| **Unidad** | 4. Álgebra Booleana |
| **Duración** | 10 horas |
| **Competencia a desarrollar** | Aplica los conceptos del álgebra booleana, optimizando expresiones y diseñando circuitos lógicos para la construcción de sistemas digitales eficientes. |

- Formaliza variables lógicas y señales binarias mediante la estructura axiomática $\langle B, +, \cdot, ', 0, 1 \rangle$.
- Conecta la teoría deductiva con la minimización de funciones y el diseño de hardware digital combinatorio.

---

## Reseña Histórica del Álgebra Booleana

- **George Boole (1854):** Publica *An Investigation of the Laws of Thought*, dotando a la lógica y al álgebra de clases de un cálculo simbólico.
- **Edward V. Huntington (1904):** Formula los axiomas independientes (**postulados de Huntington**) que definen toda estructura booleana abstracta.
- **Claude E. Shannon (1938):** Demuestra en el MIT y Bell Labs que el álgebra bivalente $B = \{0, 1\}$ modela exactamente circuitos de conmutación.
- **Veitch, Karnaugh y Quine-McCluskey (1950s):** Desarrollan métodos gráficos y algorítmicos de minimización, base de la arquitectura de von Neumann.

---

## Relevancia en Ingeniería y Computación

- **Diseño de circuitos digitales combinatorios:** Modela señales binarias de sensores (ópticos, térmicos, de presión o nivel) y actuadores.
- **Optimización de hardware:** Reduce compuertas lógicas, literales (entradas), consumo energético, área en silicio (VLSI) y retardo de propagación.
- **Arquitectura de procesadores y memorias:** Base de la ALU, sumadores, decodificadores, multiplexores y memorias (`ROM`, `EEPROM`, `SRAM`, `DRAM`).
- **Software y bases de datos:** Simplifica expresiones condicionales complejas en compiladores y motores de búsqueda.

---

## Subtemas de la Unidad (1/2)

- **4.1 Teoremas y postulados**
  - Definición axiomática $\langle B, +, \cdot, ', 0, 1 \rangle$ y postulados de Huntington.
  - Álgebra bivalente $B = \{0, 1\}$, señales analógicas vs. binarias, operadores `OR`, `AND`, `NOT` y jerarquía de precedencia.
  - Estructuras isomorfas ($B^n$, $\mathcal{P}(U)$, $D_m$), Teorema de Stone ($|B| = 2^n$), Principio de Dualidad y catálogo de teoremas (Tabla 5.1) con demostraciones.
- **4.2 Optimización de expresiones booleanas**
  - Métricas de costo ($E_L, E_S$), implicantes primos, simplificación algebraica y Método del Consenso de Quine.
  - Mapas de Karnaugh (Código Gray, topología toroidal) en $2\text{–}6$ variables para formas SOP, POS y condiciones *Don't Care* ($X$).

---

## Subtemas de la Unidad (2/2)

- **4.3 Aplicación del álgebra booleana (Compuertas lógicas)**
  - **4.3.1 Mini y maxi términos:**
    - Minitérminos ($m_i$) y Forma Canónica Disyuntiva ($\sum m$).
    - Maxitérminos ($M_i$) y Forma Canónica Conjuntiva ($\prod M$), expansión algebraica y conversión directa entre formas.
  - **4.3.2 Representación de expresiones:**
    - Compuertas básicas (`AND`, `OR`, `NOT`, `XOR`) y compuestas (`NAND`, `NOR`, `XNOR`); universalidad funcional de `NAND` y `NOR`.
    - Síntesis de circuitos (`AND-OR-NOT`, sólo `NAND`, sólo `NOR`), sensores, Semisumador y Sumador Completo en la ALU.

---

<!-- _class: compacta -->

## Bibliografía de Referencia

- **Jiménez Murillo, J. A.** (2012). *Matemáticas para la computación* (2.ª ed., Cap. 5: Álgebra booleana, pp. 176–216). Alfaomega.
- **Lipschutz, S., & Lipson, M.** (2009). *Matemáticas discretas* (3.ª ed., Serie Schaum, Cap. 15: Álgebra booleana, pp. 368–404). McGraw-Hill.
- **Johnsonbaugh, R.** (2005). *Matemáticas discretas* (6.ª ed., Cap. 11: Álgebras booleanas y circuitos combinatorios, pp. 470–504). Pearson Educación.
- **Epp, S. S.** (2012). *Matemáticas discretas con aplicaciones* (4.ª ed., Secc. 2.4–2.5 y 6.4). Cengage Learning.
- **Rosen, K. H.** (2004). *Matemática discreta y sus aplicaciones* (5.ª ed., Cap. 10: Álgebra de Boole). McGraw-Hill.
