import nbformat
from nbconvert import HTMLExporter

# Cargar el archivo notebook
nombre = input("Ingrese el nombre del archivo: ")
archivo = nombre + ".ipynb"
input("Presione Enter para convertir el archivo a HTML")

with open(archivo) as f:
    notebook_content = nbformat.read(f, as_version=4)

# Convertir a HTML
html_exporter = HTMLExporter()
body, _ = html_exporter.from_notebook_node(notebook_content)

# Guardar el archivo HTML
with open(f"{nombre}.html", "w", encoding="utf-8") as f:
    f.write(body)

print(f"Conversión completada: {nombre}.html")
