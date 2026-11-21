---
marp: true
theme: discretas
size: 16:9
paginate: true
math: mathjax
header: "Matemáticas Discretas · Unidad 1"
footer: "Unidad 1 · Sistemas Numéricos"
---
<!-- _class: portada -->
<!-- _paginate: false -->
<!-- _header: "" -->
<!-- _footer: "" -->

# Unidad 1: Sistemas Numéricos
## Fundamentos de Representación y Aritmética Computacional

- **Asignatura:** Matemáticas Discretas (`LISSI0211`) · Segundo Semestre
- **Duración:** 14 horas
- **Competencia:** Sistematiza la conversión entre sistemas posicionales mediante operaciones básicas para resolver problemas en computación.

---

## Información General de la Unidad

| Campo | Detalle |
| :--- | :--- |
| **Unidad** | 1. Sistemas Numéricos |
| **Duración** | 14 horas |
| **Competencia a desarrollar** | Sistematiza la conversión entre sistemas numéricos posicionales, mediante el uso de operaciones básicas como suma, resta, multiplicación y división, para aplicarlo en la solución de problemas en computación. |

---

## Introducción a la Unidad

- Los sistemas numéricos fundamentan la representación de datos en computación.
- **Sistema decimal ($b = 10$):** utilizado en la vida cotidiana.
- **Sistema binario ($b = 2$):** lenguaje nativo de los circuitos digitales biestables (presencia/ausencia de voltaje, encendido/apagado).
- **Sistemas octal ($b = 8$) y hexadecimal ($b = 16$):** compactan cadenas largas de bits de forma exacta para facilitar lectura, direccionamiento de memoria y depuración.

---

## Subtemas de la Unidad (1/2)

- **[1.1 Sistemas numéricos (Binario, Octal, Decimal, Hexadecimal)](1-1-sistemas-numericos.md)**
  - Sistemas aditivos frente a sistemas posicionales.
  - Expresión general y notación expandida en base $b$.
  - Estudio detallado de Decimal ($b = 10$), Binario ($b = 2$), Octal ($b = 8$) y Hexadecimal ($b = 16$).
- **[1.2 Conversiones entre sistemas numéricos](1-2-conversiones-entre-sistemas-numericos.md)**
  - Base $b \to$ decimal (notación exponencial y método de Horner).
  - Decimal $\to$ base $b$ (divisiones y multiplicaciones sucesivas).
  - Conversión directa ($2 \leftrightarrow 8 \leftrightarrow 16$) y método general ($X \to W$).

---

## Subtemas de la Unidad (2/2)

- **[1.3 Operaciones básicas (Suma, Resta, Multiplicación, División)](1-3-operaciones-basicas.md)**
  - Operaciones desarrolladas en binario, octal, hexadecimal y otras bases.
  - Signo y magnitud, complemento a $1$ y a $2$, y detección de desbordamiento (*overflow*).
- **[1.4 Algoritmos de Booth para multiplicación y división en binario](1-4-algoritmos-de-booth-para-la-multiplicacion-y-division-en-binario.md)**
  - Multiplicación con signo en $C_2$ (registros $A$, $Q$, $Q_{-1}$ y $M$).
  - División binaria en registros: con restauración y sin restauración.
- **[1.5 Aplicación de los sistemas numéricos en la computación](1-5-aplicacion-de-los-sistemas-numericos-en-la-computacion.md)**
  - Memoria, punto flotante IEEE 754, códigos (BCD, Gray, ASCII, UTF-8), RGB, redes y errores numéricos.

---

## Bibliografía de Referencia

- **Jiménez Murillo, J. A.** (2012). *Matemáticas para la computación* (2.ª ed., Cap. 1: Sistemas numéricos, pp. 2–37). Alfaomega.
- **Lipschutz, S.** (1992). *Matemáticas para computación* (Serie Schaum, Caps. 1–3, pp. 1–75). McGraw-Hill.
- **Epp, S. S.** (2012). *Matemáticas discretas con aplicaciones* (4.ª ed., Cap. 2.5: Sistemas de numeración y circuitos para suma). Cengage Learning.
- **Johnsonbaugh, R.** (2005). *Matemáticas discretas* (6.ª ed.). Pearson Educación.
- **Rosen, K. H.** (2004). *Matemática discreta y sus aplicaciones* (5.ª ed., Cap. 2.4: Los enteros y la división). McGraw-Hill.
