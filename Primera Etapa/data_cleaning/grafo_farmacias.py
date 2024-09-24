import pandas as pd
import networkx as nx

df = pd.read_csv('/Users/aldahir/desktop/DATATON/bd_Directorio/farmacias_filtered.csv',low_memory=False)

G = nx.Graph()

for index, row in df.iterrows():
    G.add_node(index, 
               nom_estab=row['nom_estab'], 
               tipo_vial=row['tipo_vial'], 
               tipo_asentamiento=row['tipo_asent'], 
               per_ocu=row['per_ocu'],
               cod_postal=row['cod_postal'],
               entidad=row['entidad'],
               municipio=row['municipio'],
               latitud=row['latitud'],
               longitud=row['longitud'],
               tipoUniEco=row['tipoUniEco'],
               fecha_alta=row['fecha_alta'])


# (Opcional) Imprimir información sobre algunos nodos para verificar
for node in list(G.nodes(data=True))[:5]:
    print(node)  # Esto imprimirá los primeros 5 nodos con sus atributos

# Guardar el grafo para análisis posterior, por ejemplo, en formato GEXF
nx.write_gexf(G, 'grafo_farmacias.gexf')


