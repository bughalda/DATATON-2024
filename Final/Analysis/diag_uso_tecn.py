# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 05:19:29 2024

@author: liera
"""

import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos desde el archivo CSV
data = pd.read_csv('C:\\Users\\liera\\Downloads\\Endutih 2023 dataset\\conjunto_de_datos\\tr_endutih_usuarios2_anual_2023.csv')

#---------EDAD----------#
# Definir los rangos de edad
bins = [0, 19, 39, 59, 79, 99]
labels = ['0-19', '20-39', '40-59', '60-79', '80-99']

# Crear una nueva columna con los rangos de edad
data['Rango de Edad'] = pd.cut(data['EDAD'], bins=bins, labels=labels, right=False)

# Contar la cantidad de personas en cada rango de edad
age_range_counts = data['Rango de Edad'].value_counts().sort_index()

# Graficar los datos
plt.figure(figsize=(10, 6))
age_range_counts.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Distribución de Rangos de Edad')
plt.xlabel('Rangos de Edad')
plt.ylabel('Cantidad de Personas')
plt.xticks(rotation=45)
plt.show()

#------------SEXO------------#
# Contar la cantidad de personas en cada categoría de sexo
data['SEXO'] = data['SEXO'].map({1: 'Hombre', 2: 'Mujer'})
sex_counts = data['SEXO'].value_counts()


# Graficar los datos
plt.figure(figsize=(8, 5))
sex_counts.plot(kind='bar', color='lightblue', edgecolor='black')
plt.title('Distribución por Sexo')
plt.xlabel('Sexo')
plt.ylabel('Cantidad de Personas')
plt.xticks(rotation=0)
plt.show()