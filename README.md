# Python Principia

Este repositorio empezó como un espacio de experimentación personal. Mi objetivo es aprender a programar, calcular y visualizar fenómenos científicos, y de paso, generar material de estudio que pueda servirle a otros estudiantes. Aunque actualmente está enfocado en Python, la visión a largo plazo es integrar otras herramientas y lenguajes de programación a medida que el proyecto escale.

*This repository started as a personal space for experimentation. My goal is to learn programming, computation, and scientific visualization, while generating study material that can be useful to other students. Although currently focused on Python, the long-term vision is to integrate other tools and programming languages as the project scales.*

Las bases, la estructura de aprendizaje y la lógica de programación las he construido siguiendo a creadores como Nikorasu Def y Bro Code. Mi aspiración a largo plazo es alcanzar el nivel de divulgación visual de Mates Mike y Grant Sanderson (3Blue1Brown), y PixelCuántico, adaptando ese estilo a mi propio contexto: la química, la física y las matemáticas con rigor.

*The foundations, learning structure, and programming logic have been built following creators like Nikorasu Def and Bro Code. My long-term aspiration is to reach the visual communication level of Mates Mike, Grant Sanderson (3Blue1Brown), and PixelCuántico, adapting that style to my own context: chemistry, physics, and mathematics with rigor.*

A diferencia de un canal de divulgación tradicional, aquí documento mi proceso de aprendizaje a través del código. A futuro, cuando tenga los conceptos dominados, la idea es complementar con videos o material explicativo que muestre cómo aprender paso a paso, de dónde salieron los recursos y cómo se aplican. Es un registro en constante construcción.

*Unlike a traditional educational channel, here I document my learning process through code. In the future, once I have mastered the concepts, the idea is to complement this with videos or explanatory material showing how to learn step-by-step, where the resources came from, and how they are applied. It is a record in constant construction.*

## Fases del Proyecto / Project Phases

El desarrollo está estructurado en cuatro fases progresivas:
*(The development is structured in four progressive phases):*

*   **Fase 1: Fundamentos Python Científico (Completada) / Phase 1: Scientific Python Fundamentals (Completed)**
    Dominio de la sintaxis base, estructuras de datos, funciones, clases, manejo de excepciones y módulos.
    *(Mastery of base syntax, data structures, functions, classes, exception handling, and modules.)*
*   **Fase 2: Nivel Intermedio y Librerías (En progreso) / Phase 2: Intermediate Level and Libraries (In progress)**
    Comprensión de listas, lambdas, y uso de NumPy, Matplotlib, Pandas y SciPy para resolver y visualizar problemas matemáticos.
    *(List comprehensions, lambdas, and use of NumPy, Matplotlib, Pandas, and SciPy to solve and visualize mathematical problems.)*
*   **Fase 3: Simulación y Animación Científica (Planificada) / Phase 3: Scientific Simulation and Animation (Planned)**
    Uso de SciPy (solve_ivp), SymPy y Manim (animaciones matemáticas).
    *(Use of SciPy (solve_ivp), SymPy, and Manim (mathematical animations).)*
*   **Fase 4: Dashboards Interactivos (Pendiente) / Phase 4: Interactive Dashboards (Pending)**
    Desarrollo de aplicaciones web interactivas para la exploración de datos y conceptos científicos con Streamlit y Plotly Dash.
    *(Development of interactive web applications for exploring data and scientific concepts with Streamlit and Plotly Dash.)*

## Stack Tecnológico / Tech Stack

*   **Lenguaje / Language:** Python 3.13+
*   **Cálculo y Datos / Computing and Data:** NumPy, SciPy, SymPy, Pandas
*   **Visualización Estática / Static Visualization:** Matplotlib
*   **Animación / Animation:** Manim (Planificado / Planned)
*   **Documentación / Documentation:** LaTeX
*   **Control de Versiones / Version Control:** Git y GitHub
*   **Planificado / Planned:** SQL, Streamlit, Plotly Dash, HTML/CSS

## Estructura del Repositorio / Repository Structure

La organización del código sigue una secuencia de aprendizaje y desarrollo de proyectos:
*(The code organization follows a sequence of learning and project development):*

```text
Python-Principia/
├── Basico-Py/
│   ├── Mini_Proyectos/
│   ├── 01_Fundamentos.py
│   ├── 02_Sets_Diccionarios.py
│   ├── 03_Condiciones_Bucles.py
│   ├── 04_Funciones_clases.py
│   ├── 05_Excepciones.py
│   ├── 06_Modulos.py
│   └── Funciones.py
├── Intermedio-Py/
│   ├── 01_Dates.py
│   ├── 02_Comprehension_llst.py
│   ├── 02.1_lambdas.py
│   ├── 03_Funciones_Avanzadas.py
│   ├── 04_Tipos_de_Errores.py
│   └── 05_Imputs.py
├── Principia_Librerias-Py/
│   ├── 01_Numpy.py
│   ├── 02_Matplotlib.py
│   ├── 03_Pandas.py
│   └── 04_SciPy.py
├── Tareas_Prueba-Py/
└── README.md
```

## Requisitos e Instalación / Requirements and Installation

Este proyecto ha sido desarrollado y probado principalmente en **Arch Linux**, pero al estar construido en Python puro, es totalmente multiplataforma (funciona en Windows, macOS y otras distribuciones de Linux).

*(This project has been developed and tested primarily on **Arch Linux**, but since it is built in pure Python, it is fully cross-platform (works on Windows, macOS, and other Linux distributions).)*

Para ejecutar los scripts, se recomienda tener instalado Python 3.13 o superior.
*(To run the scripts, it is recommended to have Python 3.13 or higher installed.)*

1. Clonar el repositorio (vía HTTPS) / Clone the repository (via HTTPS):
   ```bash
   git clone https://github.com/azquepchup/Python-Principia.git
   cd Python-Principia
   ```

2. Crear el entorno virtual / Create the virtual environment:
   ```bash
   python -m venv venv
   ```

3. Activar el entorno virtual / Activate the virtual environment:
   *   **Linux / macOS:**
       ```bash
       source venv/bin/activate
       ```
   *   **Windows:**
       ```bash
       .\venv\Scripts\activate
       ```

4. Instalar las dependencias principales / Install main dependencies:
   ```bash
   pip install numpy matplotlib scipy sympy pandas
   ```
   *(Nota: para la Fase 3, será necesario instalar Manim. En Windows, la instalación de Manim suele requerir herramientas adicionales o el uso de WSL).*
   *(Note: for Phase 3, Manim must be installed. On Windows, installing Manim usually requires additional tools or the use of WSL according to the official documentation.)*

## Entorno de Desarrollo / Development Environment

Este repositorio es escrito y mantenido utilizando las siguientes herramientas:
*(For the curious, this repository is written and maintained using the following tools):*

*   **Sistema Operativo / OS:** Arch Linux (con el gestor de ventanas Hyprland / with Hyprland window manager).
*   **Editor de Código / Code Editor:** Code - OSS (la base de código abierto de VS Code / the open-source base of VS Code).
*   **Terminal:** Kitty + Zsh con Starship.

## Autor / Author

**Uriel Sánchez Méndez** (azquepchup)
Estudiante de Química e Ingeniería en Materiales (UNAM) y Matemáticas (UnADM).
*(Student of Materials Chemistry and Engineering at UNAM and Mathematics at UnADM).*
Enfoque profesional: Análisis científico, programación y manejo de datos.
*(Professional focus: Scientific analysis, programming, and data handling).*