# Python Principia

Este repositorio nace como un espacio de experimentación personal. Mi objetivo es aprender a programar, calcular y visualizar fenómenos científicos, y de paso, generar material de estudio que pueda servirle a otros estudiantes.

Las bases, la estructura de aprendizaje y la lógica de programación las he construido siguiendo a creadores como Nikorasu Def y Bro Code. Mi aspiración a largo plazo es alcanzar el nivel de divulgación visual de Mates Mike y Grant Sanderson (3Blue1Brown), adaptando ese estilo a mi propio contexto: la química, la física y las matemáticas con rigor.

A diferencia de un canal de divulgación tradicional, aquí documento mi proceso de aprendizaje a través del código. A futuro, cuando tenga los conceptos dominados, la idea es complementar con videos o material explicativo que muestre cómo aprender paso a paso, de dónde salieron los recursos y cómo se aplican. Es un registro en constante construcción.

## Fases del Proyecto

El desarrollo está estructurado en cuatro fases progresivas:

*   **Fase 1: Fundamentos Python Científico (Completada)**
    Dominio de la sintaxis base, estructuras de datos, funciones, clases, manejo de excepciones y módulos.
*   **Fase 2: Visualización y Cálculo Científico (En progreso)**
    Uso avanzado de NumPy, Matplotlib, SciPy y SymPy para resolver y visualizar problemas matemáticos y físicos.
*   **Fase 3: Animación Científica (Iniciada)**
    Creación de animaciones matemáticas de alta calidad utilizando Manim. El primer proyecto es la simulación de un péndulo.
*   **Fase 4: Dashboards Interactivos (Pendiente)**
    Desarrollo de aplicaciones web interactivas para la exploración de datos y conceptos científicos con Streamlit y Plotly Dash.

## Stack Tecnológico

*   **Lenguaje:** Python 3.14.8
*   **Cálculo y Datos:** NumPy, SciPy, SymPy, Pandas
*   **Visualización Estática:** Matplotlib
*   **Animación:** Manim
*   **Documentación:** LaTeX
*   **Control de Versiones:** Git y GitHub
*   **Planificado:** SQL, Streamlit, Plotly Dash, HTML/CSS

## Estructura del Repositorio

La organización del código sigue una secuencia de aprendizaje y desarrollo de proyectos:

```text
Python-Principia/
├── 01_Fundamentos/
│   ├── 01_Fundamentos.py
│   ├── 02_Sets_Diccionarios.py
│   ├── 03_Condicionales_Bucles.py
│   ├── 04_Funciones_Clases.py
│   ├── 05_Excepciones.py
│   └── 06_Modulos.py
├── 02_Numpy/
│   └── 01_Numpy.py
├── Proyectos/
│   ├── Calculadora_Concentraciones/
│   ├── Zefe/
│   └── Pendulo_Manim/
└── README.md
```

## Requisitos e Instalación

Este proyecto ha sido desarrollado y probado principalmente en **Arch Linux**, pero al estar construido en Python puro, es totalmente multiplataforma (funciona en Windows, macOS y otras distribuciones de Linux).

Para ejecutar los scripts y animaciones, se recomienda tener instalado Python 3.14 o superior.

1. Clonar el repositorio (vía HTTPS):
   ```bash
   git clone https://github.com/azquepchup/Python-Principia.git
   cd Python-Principia
   ```

2. Crear el entorno virtual:
   ```bash
   python -m venv venv
   ```

3. Activar el entorno virtual (elige tu sistema operativo):
   *   **Linux / macOS:**
       ```bash
       source venv/bin/activate
       ```
   *   **Windows:**
       ```bash
       .\venv\Scripts\activate
       ```

4. Instalar las dependencias principales:
   ```bash
   pip install numpy matplotlib scipy sympy pandas
   ```
   *(Nota: para la Fase 3, es necesario instalar Manim. En Windows, la instalación de Manim suele requerir herramientas adicionales o el uso de WSL según la documentación oficial).*

## Entorno de Desarrollo del Autor

Para los curiosos, este repositorio es escrito y mantenido utilizando las siguientes herramientas:
*   **Sistema Operativo:** Arch Linux (con el gestor de ventanas Hyprland).
*   **Editor de Código:** Code - OSS (la base de código abierto de VS Code).
*   **Terminal:** Kitty + Zsh con Starship.

## Autor

**Uriel Sánchez Méndez**
Estudiante de Química e Ingeniería en Materiales (UNAM) y Matemáticas (UnADM).
Enfoque profesional: Análisis científico, programación y manejo de datos.