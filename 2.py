# esto pretende tener de output un .json con autor, título, año de publicación
# y nombre de pdf con el input de sopa.txt
# El .json resultante no es del todo human-readable pero no me importa

import re
import json
import os
from bs4 import BeautifulSoup

with open("sopa.txt", "r") as f:
    sopa = f.read()

sopas = re.split("<!DOCTYPE html>", sopa)

sopas = sopas[1:51] # quitar el primer item de la lista porque es irrelevante
                    # hay 50 items, que son las 50 páginas de resultados

nombres = []
titulos = []
anos = []
doc_nums = []

resultados = []

# loopear cada elemento de "sopas" en BeautifulSoup
for s in sopas:
    beautiful = BeautifulSoup(s, "html.parser")     # mete cada página de resultados
    table = beautiful.find("table")                 # encuentra la tabla
    rows = table.find_all("tr")[1:]                 # separa cada renglon (sin el primero)
    
    # sacar la información de cada celda
    for row in rows:
        cells = row.find_all("td")
        nombre_sucio = str(cells[2])
        titulo_sucio = str(cells[3])
        ano_sucio = str(cells[4])
        link_sucio = str(cells[5])

        # limpiar
        # nombres
        nombre1 = re.sub("<td width=\"20%\">", "", nombre_sucio)
        nombre = re.sub("</td>", "", nombre1)
        nombres.append(nombre)

        # titulos
        pattern = r"title\s*=\s*'([^']*)'"
        match = re.search(pattern, titulo_sucio)
        if match:
            titulo1 = match.group(1)
        titulo2 = re.sub(" /", "", titulo1)
        titulo = re.sub("&nbsp;", "", titulo2)
        titulos.append(titulo)

        # años
        ano1 = re.sub("<td width=\"10%\">", "", ano_sucio)
        ano = re.sub("</td>", "", ano1)
        anos.append(ano)

        # links
        pattern = r"doc_number=(\d+)"
        match = re.search(pattern, link_sucio)
        if match:
            doc_num = match.group(1)
        doc_num = doc_num[2:9]   # quita los "00" del inicio que sobran
        doc_nums.append(doc_num)

        resultados.append({"nombre": nombre, "titulo": titulo, "año": ano, "doc_num": doc_num})

# Crea metadatos.json si no existe
if not os.path.exists('metadatos.json'):
    os.mknod('metadatos.json')

open("metadatos.json", "w").close()     # borra el contenido de metadatos.json

with open('metadatos.json', 'a') as f:  # escribe el .json
        json.dump(resultados, f)
        f.write('\n')