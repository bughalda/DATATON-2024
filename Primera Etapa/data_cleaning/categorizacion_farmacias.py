import pandas as pd

df = pd.read_csv('farmacias_filtered.csv')

# Contar las ocurrencias por razón social o nombre del establecimiento
razon_social_counts = df['raz_social'].replace('', None).fillna(df['nom_estab']).value_counts()

# Crear una función para categorizar las farmacias
def categorizar_farmacia(count):
    if count >= 100:
        return 'Big'
    elif 5 <= count < 100:
        return 'Medium'
    else:
        return 'Small'

# Aplicar la función a las razones sociales en el DataFrame
df['categoria'] = df['raz_social'].replace('', None).fillna(df['nom_estab']).map(razon_social_counts).apply(categorizar_farmacia)

# Guardar el DataFrame resultante con la nueva columna
df.to_csv('farmacias_categorizadas.csv', index=False)

print(df[['raz_social', 'categoria']].head())  # Muestra las primeras filas para verificar
