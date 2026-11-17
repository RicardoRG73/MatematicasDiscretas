# 4. Álgebra Booleana

## Información General de la Unidad

| Campo | Detalle |
| :--- | :--- |
| **Unidad** | 4. Álgebra Booleana |
| **Duración** | 10 horas |
| **Competencia a desarrollar** | Aplica los conceptos del álgebra booleana, optimizando expresiones y diseñando circuitos lógicos para la construcción de sistemas digitales eficientes. |

---

## Introducción a la Unidad

El **álgebra booleana** (o **álgebra de Boole**) es un sistema matemático deductivo que formaliza mediante operaciones algebraicas el comportamiento de variables lógicas y señales binarias. Fue introducida en $1854$ por el matemático autodidacta británico **George Boole** ($1815\text{–}1864$) en su obra clásica *An Investigation of the Laws of Thought* (*Las leyes del pensamiento*), con el propósito de dotar a la lógica proposicional y al álgebra de clases de un cálculo simbólico riguroso. Posteriormente, en $1904$, el matemático estadounidense **Edward Vermilye Huntington** ($1874\text{–}1952$) estableció el conjunto formal de axiomas independientes (conocidos como **postulados de Huntington**) que definen toda estructura de álgebra booleana abstracta $\langle B, +, \cdot, ', 0, 1 \rangle$ (Jiménez Murillo, 2012; Lipschutz & Lipson, 2009; Johnsonbaugh, 2005).

Durante más de ocho décadas, el álgebra de Boole permaneció como una rama puramente teórica de la matemática hasta que en $1938$ **Claude Elwood Shannon** ($1916\text{–}2001$), en su célebre tesis de maestría en el MIT (*A Symbolic Analysis of Relay and Switching Circuits*) y en los Laboratorios Bell, demostró que el álgebra booleana bivalente ($B = \{0, 1\}$) modela de forma exacta el análisis y la síntesis de **circuitos eléctricos de conmutación biestables** basados en relevadores e interruptores. En la década de $1950$, **Edward W. Veitch** ($1952$) y **Maurice Karnaugh** ($1953$), junto con **Willard Van Orman Quine** y **Edward J. McCluskey**, desarrollaron métodos gráficos y algorítmicos sistemáticos para **minimizar funciones booleanas**, sentando las bases directas de la arquitectura de computadoras modernas ideada por **John von Neumann** ($1903\text{–}1957$) (Jiménez Murillo, 2012, Cap. 5).

En la ingeniería en sistemas computacionales, electrónica digital y ciencias de la computación, el álgebra booleana constituye la herramienta esencial para:
- **Diseño y síntesis de circuitos digitales combinatorios:** Modelado de señales binarias provenientes de sensores (ópticos, magnéticos, térmicos, de presión o nivel) y actuadores mediante funciones booleanas.
- **Optimización de hardware y reducción de costos:** Simplificación algebraica y por mapas de Karnaugh para reducir el número de compuertas lógicas, entradas (literales), consumo de energía, área en silicio (VLSI) y retardo de propagación de señales.
- **Arquitectura de microprocesadores y memorias:** Construcción de la Unidad Lógico-Aritmética (ALU), semisumadores (*half adders*), sumadores completos (*full adders*), decodificadores, multiplexores y celdas de memoria (`ROM`, `EEPROM`, `SRAM`, `DRAM`) utilizando compuertas universales `NAND` y `NOR`.
- **Optimización de código y consultas:** Simplificación de expresiones condicionales complejas en compiladores y motores de búsqueda o bases de datos.

---

## Subtemas de la Unidad

- **[4.1 Teoremas y postulados](4-1-teoremas-y-postulados.md)**
  - Definición axiomática de un álgebra booleana $\langle B, +, \cdot, ', 0, 1 \rangle$ y los **Postulados de Huntington** (identidad/neutros, conmutatividad, distributividad mutua, complementos y asociatividad).
  - Álgebra booleana bivalente ($B = \{0, 1\}$), señales analógicas frente a señales digitales binarias, operaciones básicas OR ($+$), AND ($\cdot$) y NOT ($'$), y jerarquía de precedencia de operadores.
  - Ejemplos de estructuras booleanas: álgebra de cadenas de bits $B^n$, álgebra de conjuntos $\mathcal{P}(U)$ y álgebra de divisores libres de cuadrados $D_m$ (Teorema de representación de Stone y corolario $|B| = 2^n$).
  - **Principio de Dualidad** y catálogo completo de **Teoremas del Álgebra de Boole** (Tabla 5.1 de Jiménez Murillo y Teoremas 15.1–15.5 de Lipschutz: acotamiento, idempotencia, involución, unicidad del complemento, Leyes de De Morgan generalizadas, adyacencia/combinación, absorción, eliminación de redundancia y teorema del consenso), con sus demostraciones deductivas paso a paso y tablas de verdad.
- **[4.2 Optimización de expresiones booleanas](4-2-optimizacion-de-expresiones-booleanas.md)**
  - Criterios de optimalidad de una expresión booleana (conteo de literales $E_L$ y de términos/sumandos $E_S$, implicantes primos y formas minimales).
  - **Simplificación algebraica paso a paso** mediante teoremas y postulados del álgebra de Boole, y el **Método del Consenso de Quine** (Algoritmos 15.3 y 15.4 de Lipschutz).
  - **Simplificación mediante Mapas de Karnaugh (K-Mapas):** código reflejado (**Código Gray**), adyacencia física y topología cilíndrica/toroidal (bordes opuestos y las $4$ esquinas) en mapas de $2, 3$ y $4$ variables, y extensión mediante simetría de espejo a mapas de $5$ y $6$ variables.
  - Obtención de expresiones óptimas tanto en **Suma de Productos (SOP)** (agrupando $1\text{s}$) como en **Producto de Sumas (POS)** (agrupando $0\text{s}$ para hallar $F'$ y aplicando Leyes de De Morgan), así como el aprovechamiento de condiciones de indiferencia (**«No importa» / *Don't Care***, $X$ o $d$).
- **[4.3 Aplicación del álgebra booleana (Compuertas lógicas)](4-3-aplicacion-del-algebra-booleana.md)**
  - **4.3.1 Mini y maxi términos:** Literales, productos y sumas fundamentales, **minitérminos ($m_i$)** y Forma Canónica Disyuntiva (Suma de Minitérminos, $\sum m$), **maxitérminos ($M_i$)** y Forma Canónica Conjuntiva (Producto de Maxitérminos, $\prod M$), algoritmos de expansión algebraica de términos incompletos y conversión directa entre ambas formas canónicas.
  - **4.3.2 Representación de expresiones:** Símbolos estándar ANSI/IEEE, ecuaciones y tablas de verdad de las compuertas básicas (`AND`, `OR`, `NOT`, `XOR`) y compuestas (`NAND`, `NOR`, `XNOR`), **completitud funcional y universalidad de `NAND` y `NOR`**, análisis y síntesis de circuitos combinatorios en tres arquitecturas (`AND-OR-NOT`, sólo `NAND` y sólo `NOR`), y diseño de sistemas digitales prácticos (sensores industriales, **Semisumador** y **Sumador Completo** en la ALU).

---

## Bibliografía de Referencia

- **Jiménez Murillo, J. A.** (2012). *Matemáticas para la computación* (2.ª ed., Cap. 5: Álgebra booleana, pp. 176–216). Alfaomega.
- **Lipschutz, S., & Lipson, M.** (2009). *Matemáticas discretas* (3.ª ed., Serie Schaum, Cap. 15: Álgebra booleana, pp. 368–404). McGraw-Hill.
- **Johnsonbaugh, R.** (2005). *Matemáticas discretas* (6.ª ed., Cap. 11: Álgebras booleanas y circuitos combinatorios, pp. 470–504). Pearson Educación.
- **Epp, S. S.** (2012). *Matemáticas discretas con aplicaciones* (4.ª ed., Secc. 2.4: Aplicación: circuitos lógicos digitales, pp. 64–78; Secc. 2.5: Circuitos para suma; Secc. 6.4: Álgebra booleana, pp. 374–392). Cengage Learning.
- **Rosen, K. H.** (2004). *Matemática discreta y sus aplicaciones* (5.ª ed., Cap. 10: Álgebra de Boole). McGraw-Hill.
