# 1. Sistemas Numéricos

## Información General de la Unidad

| Campo | Detalle |
| :--- | :--- |
| **Unidad** | 1. Sistemas Numéricos |
| **Duración** | 14 horas |
| **Competencia a desarrollar** | Sistematiza la conversión entre sistemas numéricos posicionales, mediante el uso de operaciones básicas como suma, resta, multiplicación y división, para aplicarlo en la solución de problemas en computación. |

---

## Introducción a la Unidad

Los sistemas numéricos constituyen el fundamento matemático de la representación de datos en las ciencias de la computación. Aunque en la vida cotidiana utilizamos el **sistema decimal** (base $10$), los circuitos digitales de una computadora operan mediante estados biestables (presencia o ausencia de voltaje, interruptor cerrado o abierto), por lo que su lenguaje nativo es el **sistema binario** (base $2$). A su vez, los sistemas **octal** (base $8$) y **hexadecimal** (base $16$) permiten compactar grandes cadenas de bits de manera exacta y directa, facilitando la lectura, el direccionamiento de memoria y la depuración de programas.

---

## Subtemas de la Unidad

- **[1.1 Sistemas numéricos (Binario, Octal, Decimal, Hexadecimal)](1-1-sistemas-numericos.md)**
   - Sistemas aditivos frente a sistemas posicionales.
   - Expresión general y notación expandida en base $b$.
   - Estudio detallado de los sistemas Decimal ($b = 10$), Binario ($b = 2$), Octal ($b = 8$) y Hexadecimal ($b = 16$).
- **[1.2 Conversiones entre sistemas numéricos](1-2-conversiones-entre-sistemas-numericos.md)**
   - Conversión de cualquier base $b$ a decimal (notación exponencial y método de Horner).
   - Conversión de decimal a cualquier base $b$ (divisiones sucesivas para enteros y multiplicaciones sucesivas para fracciones).
   - Conversión directa entre binario, octal y hexadecimal por agrupación de bits ($3$ y $4$ bits).
   - Conversión general entre una base arbitraria $X$ y otra base $W$.
- **[1.3 Operaciones básicas (Suma, Resta, Multiplicación, División)](1-3-operaciones-basicas.md)**
   - Suma, resta (método de préstamo y suma al sustraendo), multiplicación y división desarrollada en binario, octal, hexadecimal y otras bases.
   - Representación de números con signo: magnitud y signo, complemento a $1$ y complemento a $2$.
   - Aritmética en complemento a $2$ y detección de desbordamiento (*overflow*).
- **[1.4 Algoritmos de Booth para la multiplicación y división en binario](1-4-algoritmos-de-booth-para-la-multiplicacion-y-division-en-binario.md)**
   - Algoritmo de Booth para multiplicación binaria con signo en complemento a $2$ (registros $A$, $Q$, $Q_{-1}$ y $M$).
   - Algoritmos de división binaria mediante registros: división con restauración y división sin restauración (estilo Booth).
- **[1.5 Aplicación de los sistemas numéricos en la computación](1-5-aplicacion-de-los-sistemas-numericos-en-la-computacion.md)**
   - Unidades de información digital y direccionamiento de memoria.
   - Representación de enteros y de números reales en punto flotante (estándar IEEE 754).
   - Códigos binarios y alfanuméricos: BCD ($8\text{-}4\text{-}2\text{-}1$, Exceso-$3$), Gray, ASCII, UTF-8, colores RGB y redes (IPv4, IPv6, MAC).
   - Errores numéricos en computación: redondeo, truncamiento, desbordamiento y cancelación sustractiva.

---

## Bibliografía de Referencia

- **Jiménez Murillo, J. A.** (2012). *Matemáticas para la computación* (2.ª ed., Cap. 1: Sistemas numéricos, pp. 2–37). Alfaomega.
- **Lipschutz, S.** (1992). *Matemáticas para computación* (Serie Schaum, Caps. 1–3, pp. 1–75). McGraw-Hill.
- **Epp, S. S.** (2012). *Matemáticas discretas con aplicaciones* (4.ª ed., Cap. 2.5: Aplicación: Sistemas de numeración y circuitos para suma). Cengage Learning.
- **Johnsonbaugh, R.** (2005). *Matemáticas discretas* (6.ª ed.). Pearson Educación.
- **Rosen, K. H.** (2004). *Matemática discreta y sus aplicaciones* (5.ª ed., Cap. 2.4: Los enteros y la división; representaciones de enteros). McGraw-Hill.
