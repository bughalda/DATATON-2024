import pandas as pd
import glob

csv_files = glob.glob("/Users/aldahir/desktop/DATATON/bd_Directorio/*.csv")  # Reemplaza "ruta_a_los_archivos" por la ubicación de tus archivos

# Inicializar una lista para almacenar los dataframes filtrados
filtered_data = []

# Filtrar los archivos por la palabra "farm" en la columna 'nom_estab'
for file in csv_files:
    # Leer el archivo CSV
    df = pd.read_csv(file, delimiter=",", encoding='iso-8859-1', low_memory=False)

    # Filtrar las filas que contengan "farm" en la columna 'nom_estab'
    df_filtered = df[df['nom_estab'].str.contains('farma', case=False, na=False)]

    # Imprimir cuántas farmacias se encontraron en este archivo
    print(f"Archivo {file}: {len(df_filtered)} farmacias encontradas")
    
    # Añadir el dataframe filtrado a la lista
    filtered_data.append(df_filtered)

# Concatenar todos los dataframes filtrados en uno solo
final_df = pd.concat(filtered_data, ignore_index=True)

# Guardar el dataframe resultante en un nuevo archivo CSV
final_df.to_csv("/Users/aldahir/desktop/DATATON/bd_Directorio/farmacias_filtered.csv", index=False)

print("Archivo filtrado guardado con éxito.")
