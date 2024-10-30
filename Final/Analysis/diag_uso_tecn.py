# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 05:19:29 2024

@author: liera
"""

import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd

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

#------------ESCOLARIDAD----------#
# Definir el diccionario de mapeo para el grado de escolaridad
escolaridad_map = {
    0: 'Ninguno', 1: 'Preescolar o kínder', 2: 'Primaria', 3: 'Secundaria', 4: 'Normal básica',
    5: 'Estudio técnico terminal con secundaria', 6: 'Preparatoria o bachillerato',
    7: 'Estudio técnico superior con preparatoria terminada', 8: 'Licenciatura o ingeniería',
    9: 'Especialidad', 10: 'Maestría', 11: 'Doctorado', 99: 'No sabe'
}

# Mapear los códigos de escolaridad a sus nombres correspondientes
data['NIVEL'] = data['NIVEL'].map(escolaridad_map)

# Contar la cantidad de personas en cada nivel de escolaridad
escolaridad_counts = data['NIVEL'].value_counts()

# Graficar los datos
plt.figure(figsize=(12, 8))
escolaridad_counts.plot(kind='bar', color='lightgreen', edgecolor='black')
plt.title('Distribución por Grado de Escolaridad')
plt.xlabel('Grado de Escolaridad')
plt.ylabel('Cantidad de Personas')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
'''
#-----------entidad federativa--------------#
# Diccionario de mapeo de códigos de entidad a nombres de estados
entidad_map = {
    1: 'Aguascalientes', 2: 'Baja California', 3: 'Baja California Sur', 4: 'Campeche',
    5: 'Coahuila', 6: 'Colima', 7: 'Chiapas', 8: 'Chihuahua', 9: 'Ciudad de México',
    10: 'Durango', 11: 'Guanajuato', 12: 'Guerrero', 13: 'Hidalgo', 14: 'Jalisco',
    15: 'México', 16: 'Michoacán', 17: 'Morelos', 18: 'Nayarit', 19: 'Nuevo León',
    20: 'Oaxaca', 21: 'Puebla', 22: 'Querétaro', 23: 'Quintana Roo', 24: 'San Luis Potosí',
    25: 'Sinaloa', 26: 'Sonora', 27: 'Tabasco', 28: 'Tamaulipas', 29: 'Tlaxcala',
    30: 'Veracruz', 31: 'Yucatán', 32: 'Zacatecas', 0: 'No especificado'
}

# Mapear los códigos de entidad a nombres de estados
data['ENT'] = data['ENT'].map(entidad_map)

# Contar la cantidad de personas por estado
estado_counts = data['ENT'].value_counts()

# Cargar un shapefile de los estados de México 
mexico_geo = gpd.read_file('C:\\Users\\liera\\Downloads\\Endutih 2023 dataset\\conjunto_de_datos\\dest_2010gw.shp')

# Unir los datos de conteo al geodataframe de los estados de México
mexico_geo['nombre_estado'] = mexico_geo['nombre_estado_column_shapefile'] # Cambia a la columna adecuada del shapefile
mexico_geo['conteo'] = mexico_geo['nombre_estado'].map(estado_counts).fillna(0)

# Graficar el mapa de calor
plt.figure(figsize=(10, 10))
mexico_geo.plot(column='conteo', cmap='OrRd', linewidth=0.8, edgecolor='black', legend=True)
plt.title('Mapa de Calor de Entidades por Cantidad de Personas')
plt.axis('off')
plt.show()
'''
#---------ESTRATO SOCIOECONOMICO----------------#
# Definir el diccionario de mapeo para el estrato
estrato_map = {
    1: 'Bajo', 2: 'Medio bajo', 3: 'Medio alto', 4: 'Alto'
}

# Mapear los valores de estrato a sus nombres correspondientes
data['ESTRATO'] = data['ESTRATO'].map(estrato_map)

# Contar la cantidad de personas en cada nivel de estrato
estrato_counts = data['ESTRATO'].value_counts().sort_index()

# Graficar los datos
plt.figure(figsize=(8, 5))
estrato_counts.plot(kind='bar', color='lightcoral', edgecolor='black')
plt.title('Distribución por Estrato Socioeconómico')
plt.xlabel('Estrato')
plt.ylabel('Cantidad de Personas')
plt.xticks(rotation=0)
plt.show()
#-----------USO DE LAS TECNOLOGIAS------------#
# Definir el diccionario de mapeo para respuestas de Sí y No
yes_no_map = {1: 'Sí', 2: 'No'}

# Aplicar el mapeo a cada columna de interés
columns_to_map = {
    'P8_13_1': 'Mensajería instantánea',
    'P8_13_2': 'Contenidos de audio y video',
    'P8_13_3': 'Adquirir bienes o servicios',
    'P8_13_4': 'Tránsito o navegación asistida',
    'P8_13_5': 'Juegos',
    'P8_13_6': 'Redes sociales',
    'P8_13_7': 'Banca móvil',
    'P8_13_8': 'Editar fotos o videos'
}

# Crear un diccionario para almacenar los conteos de "Sí"
yes_counts = {}

for col, label in columns_to_map.items():
    # Mapear los valores de la columna actual
    data[col] = data[col].map(yes_no_map)
    # Contar las respuestas "Sí" y almacenar el resultado
    yes_counts[label] = data[col].value_counts().get('Sí', 0)

# Convertir el diccionario a un DataFrame para graficar
yes_counts_df = pd.DataFrame(list(yes_counts.items()), columns=['Actividad', 'Cantidad de Sí'])

# Graficar los datos
plt.figure(figsize=(10, 6))
yes_counts_df.set_index('Actividad').plot(kind='bar', legend=False, color='lightblue', edgecolor='black')
plt.title('Cantidad de Respuestas "Sí" por Actividad')
plt.xlabel('Actividad')
plt.ylabel('Cantidad de Respuestas "Sí"')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
