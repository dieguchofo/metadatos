# Esto va a hacer una BeautifulSoup de las páginas de resultados de TESIUNAM
# Se tiene que ha cer la búsqueda de "licenciatura en lengua y literaturas modernas inglesas",
# del 2006 al 2023 y luego copiar y pegar cada uno de los urls como una nueva línea
# en "urls_manuales.txt"

# el output es "sopa.txt" que es todo el html de todas las páginas de resultados

import requests
import os
import certifi
from bs4 import BeautifulSoup

# Read in the URLs from the text file
with open('urls_manuales.txt', 'r') as f:
    urls = f.readlines()

soup_l = []   # una lista vacía para appendear las sopas del loop que viene

# Loop over each URL
for url in urls:
    # Make a GET request to the page and get the HTML content
    response = requests.get(url.strip(), verify=False)  # verify=false es que ignora ssl porque por alguna razon no puedo hacer que funcione
    html_content = response.content

    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(html_content, "html.parser")
    soup_l.append(soup)     # juntar todo en una lista

soup_s = str(soup_l)        # hacer la lista un string

# Escribir sopa.txt
if not os.path.exists('sopa.txt'):  # Crea sopa.txt si no existe
    os.mknod('sopa.txt')

open("sopa.txt", "w").close()       # borra el contenido de sopa.txt

with open("sopa.txt", "w") as f:    # llenar "sopa.txt" con la sopa
    f.write(soup_s)