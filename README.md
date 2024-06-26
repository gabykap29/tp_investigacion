# Algoritmos y Complejidad Computacional

Este repositorio contiene implementaciones en Python de varios algoritmos con diferentes complejidades temporales, desde O(1) hasta O(2^n). También se incluye un script para medir y graficar los tiempos de ejecución utilizando `matplotlib` y `time`.

## Tabla de Contenidos

- [Descripción](#descripción)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Uso](#uso)
- [Solución de Problemas](#solución-de-problemas)
- [Contribuciones](#contribuciones)
- [Licencia](#licencia)

## Descripción

Este proyecto implementa y grafica la complejidad de los siguientes algoritmos:

- **O(1)**: Acceso constante a un elemento de una lista.
- **O(log n)**: Búsqueda binaria.
- **O(n)**: Suma de elementos en una lista.
- **O(n log n)**: Merge Sort.
- **O(n^2)**: Bubble Sort.
- **O(2^n)**: Fibonacci recursivo sin optimización.

## Requisitos

- Python 3.6 o superior
- `pip` (administrador de paquetes de Python)
- `matplotlib` para la visualización de datos
- `time` para la medición de tiempos de ejecución

## Instalación

1. **Clona este repositorio**:

    ```bash
    git clone https://github.com/tu-usuario/tu-repositorio.git
    cd tu-repositorio
    ```

2. **Crea y activa un entorno virtual**:

    En Windows:
    ```bash
    python -m venv nv
    nv\Scripts\activate
    ```

    En Linux/Mac:
    ```bash
    python3 -m venv nv
    source nv/bin/activate
    ```

3. **Instala las dependencias**:

    ```bash
    pip install -r requirements.txt
    ```

    Asegúrate de que el archivo `requirements.txt` contenga las siguientes líneas:
    ```plaintext
    matplotlib
    ```

## Uso

1. **Ejecuta el script principal**:

    ```bash
    python main.py
    ```

    Este script ejecutará los algoritmos, medirá los tiempos de ejecución y generará una gráfica comparativa.

2. **Visualiza la gráfica**:

    La gráfica se generará y mostrará en una ventana de `matplotlib`. Puedes cerrar la ventana para terminar la ejecución.

## Solución de Problemas

### Error: `ImportError: DLL load failed while importing _cext`

Si encuentras este error, intenta lo siguiente:

1. **Reinstala `kiwisolver` y `matplotlib`**:

    ```bash
    pip uninstall kiwisolver matplotlib
    pip install kiwisolver matplotlib
    ```

2. **Asegúrate de tener instaladas las Redistribuibles de Visual C++** en Windows:

    [Descargar Redistribuibles de Visual C++](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170)

3. **Verifica los permisos de archivos DLL** y asegúrate de que no estén bloqueados por otro proceso.

### Error: `ModuleNotFoundError`

Asegúrate de que el entorno virtual esté activado y que las bibliotecas necesarias estén instaladas.

```bash
nv\Scripts\activate  # Windows
source nv/bin/activate  # Linux/Mac
pip install -r requirements.txt
