from controllers.grafo import Grafo
import json

# Abrir el archivo en modo lectura
with open('./assets/info.json', 'r') as archivo_json :
    # Leer el contenido del archivo
    contenido = archivo_json.read()
    # Cerrar el archivo
    archivo_json.close()

# Cargar el contenido en un objeto de Python
datos = json.loads(contenido)

grafo = Grafo()

def createPlanets(datos, i):
    if i == len(datos["planetas"]):
        return
    grafo.ingresarVertices(datos["planetas"][i]["nombre"])
    createPlanets(datos, i+1)
    
def createPaths(datos, i):
    if i == len(datos["caminos"]):
        return
    grafo.ingresarArista(datos["caminos"][i]["origen"], datos["caminos"][i]["destino"], datos["caminos"][i]["peso"])
    createPaths(datos, i+1)

createPlanets(datos, 0)
createPaths(datos, 0)

grafo.showVertices()
grafo.showAristas()

# git remote add origin https://github.com/juliandres13/ProyectoStarWars.git
# git branch -M main
# git push -u origin main

# echo "# ProyectoStarWars" >> README.md
# git init
# git add README.md
# git commit -m "first commit"
# git branch -M main
# git remote add origin https://github.com/juliandres13/ProyectoStarWars.git
# git push -u origin main
