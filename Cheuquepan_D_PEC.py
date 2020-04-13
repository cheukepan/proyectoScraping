# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 17:52:59 2020

@author: Diego Cheuquepán
"""

# Librerías
from urllib.request import urlopen
from bs4 import BeautifulSoup

# Definimos la URL del proyecto
url = 'http://www.fegosa.cl/preciososorno/precioosorno.html'

# Identificamos la tecnología del sitio web
import builtwith
print("")
print("Información de la tecnología del sitio web FEGOSA")
print(builtwith.parse(url))
print("===================================================")

# Identificamos al dueño del sitio web
import whois
print("")
print("Información del dueño del sitio web FEGOSA")
print(whois.whois(url))
print("===================================================")

# Análisis de robot.txt
import requests
response = requests.get("http://www.fegosa.cl/sitemap.xml")
test = response.text
print("")
print(response.status_code)
print("robots.txt del sitio web FEGOSA")
print(test)
print("===================================================")

# Definimos las matrices

especie = []
cabezas = []
pesoProm = []
primer = []
segundo = []
tercero = []
cuarto = []
quinto = []
promedio = []
general = []
date = []
ciudad = []

fecha = ""

# Definimos la lista de páginas HTML que recorreremos para obtener los datos
urlosorno = "http://www.fegosa.cl/preciosciudades/Tosorno.html"
urlpaillaco = "http://www.fegosa.cl/preciosciudades/Tpaillaco.html"
urlptomontt = "http://www.fegosa.cl/preciosciudades/Tptomontt.html"
urlptovaras = "http://www.fegosa.cl/preciosciudades/Tptovaras.html"

newurl = [urlosorno, urlpaillaco, urlptomontt, urlptovaras]

for i in range(4):
    x = newurl[i]
    # Análisis the HTML
    html = urlopen(x)
    soup = BeautifulSoup(html.read(),"html5lib")
    table = soup.find('table')
    rows = table.findAll('tr')
    divs = soup.findAll("table")

    for div in divs:
        rows = div.findAll('tr')
        for row in rows[0:1]:
            column = str(row.findAll('td')[0].text)
            column = column.replace("PRECIOS FEGOSA ", "")
            osorno = column.find("OSORNO")
            paillaco = column.find("PAILLACO")
            montt = column.find("NTT")
            varas = column.find("VARAS")
            if osorno == 4:
                fecha = column.replace("OSORNO", "")
            if paillaco == 4:
                fecha = column.replace("PAILLACO", "")
            if montt == 13:
                fecha = column.replace("PUERTO MONTT", "")
            if varas == 11:
                fecha = column.replace("PUERTO VARAS", "")
        for row in rows[2:]:
            column = str(row.findAll('font')[0].contents)
            column = column.replace("[' ", "")
            column = column.replace("['", "")
            column = column.replace(" ']", "")
            column = column.replace("']", "")
            especie.append(column)
            date.append(fecha.strip())
            if osorno == 4:
                ciudad.append('Osorno')
            if paillaco == 4:
                ciudad.append('Paillaco')
            if montt == 13:
                ciudad.append('Puerto Montt')
            if varas == 11:
                ciudad.append('Puerto Varas')
        for row in rows[2:]:
            column = str(row.findAll('font')[1].contents)
            column = column.replace("[' ", "")
            column = column.replace("['", "")
            column = column.replace(" ", "")
            column = column.replace(" ']", "")
            column = column.replace("']", "")  
            cabezas.append(column)
        for row in rows[2:]:
            column = str(row.findAll('font')[2].contents)
            column = column.replace("[' ", "")
            column = column.replace("['", "")
            column = column.replace(" ", "")
            column = column.replace(" ']", "")
            column = column.replace("']", "")
            pesoProm.append(column)
        for row in rows[2:]:
            column = str(row.findAll('font')[3].contents)
            column = column.replace("[' ", "")
            column = column.replace("['", "")
            column = column.replace(" ", "")
            column = column.replace(" ']", "")
            column = column.replace("']", "")
            primer.append(column)
        for row in rows[2:]:
            column = str(row.findAll('font')[4].contents)
            column = column.replace("[' ", "")
            column = column.replace("['", "")
            column = column.replace(" ", "")
            column = column.replace(" ']", "")
            column = column.replace("']", "")
            segundo.append(column)
        for row in rows[2:]:
            column = str(row.findAll('font')[5].contents)
            column = column.replace("[' ", "")
            column = column.replace("['", "")
            column = column.replace(" ", "")
            column = column.replace(" ']", "")
            column = column.replace("']", "")
            tercero.append(column)
        for row in rows[2:]:
            column = str(row.findAll('font')[6].contents)
            column = column.replace("[' ", "")
            column = column.replace("['", "")
            column = column.replace(" ", "")
            column = column.replace(" ']", "")
            column = column.replace("']", "")
            cuarto.append(column)
        for row in rows[2:]:
            column = str(row.findAll('font')[7].contents)
            column = column.replace("[' ", "")
            column = column.replace("['", "")
            column = column.replace(" ", "")
            column = column.replace(" ']", "")
            column = column.replace("']", "")
            quinto.append(column)
        for row in rows[2:]:
            column = str(row.findAll('font')[8].contents)
            column = column.replace("[' ", "")
            column = column.replace("['", "")
            column = column.replace(" ", "")
            column = column.replace(" ']", "")
            column = column.replace("']", "")
            promedio.append(column)
        for row in rows[2:]:
            column = str(row.findAll('font')[9].contents)
            column = column.replace("[' ", "")
            column = column.replace("['", "")
            column = column.replace(" ", "")
            column = column.replace(" ']", "")
            column = column.replace("']", "")
            general.append(column)

import pandas as pd

# Definición archivo:
archivo = {'Feria': ciudad, 'Fecha': date, 'Especie': especie, 'Cabezas': cabezas, 'Peso Promedio': pesoProm, '1 er': primer, '2 do': segundo, '3 er': tercero, '4 to': cuarto, '5 to': quinto, 'Promedio 5PP': promedio, 'Promedio General': general}

# Creación DataFrame:
df_numeros = pd.DataFrame(archivo)

# Guarda datos en CSV:
df_numeros.to_csv('fegosa.csv', header=True, index=False)
