import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import datetime

# Importamos el archivo
alumnos = pd.read_csv('E:/UNASAM/IA/Proyecto de Investigación/kmeans/reportes_base/calificacionesMaster.csv', engine='python')

# Mostramos las caracteristicas
print(alumnos.info())

# Mostrar primeras filas
print(alumnos.head())

# Eliminamos la columna de numeración
alumnos_bimestres = alumnos.drop(['Alumno'], axis=1)

# Mostramos los variables
print(alumnos_bimestres.describe())

# Normalizamos los valores
alumnos_norm = (alumnos_bimestres - alumnos_bimestres.min()) /\
               (alumnos_bimestres.max() - alumnos_bimestres.min())
print(alumnos_norm)

## GRAFICOS Y ANALISIS ##

# Creacion de los clusters
clustering = KMeans(n_clusters=4, max_iter=1000, n_init=10)
clustering.fit(alumnos_norm)

# Agregamos el resultdo al archivo original
alumnos['KMeans_Clusters'] = clustering.labels_
print(alumnos.head())

# Aplicamos analisis de componentes para reducir las varaibles a valores significativos
pca = PCA(n_components=2)
pca_alumnos = pca.fit_transform(alumnos_norm)
pca_alumnos_df = pd.DataFrame(data=pca_alumnos, columns=['Component_1', 'Component_2'])
pca_codigo_alumnos = pd.concat([pca_alumnos_df, alumnos[['KMeans_Clusters']]], axis=1)

print(pca_codigo_alumnos)

# Grafico
fig = plt.figure(figsize=(8, 8))

ax = fig.add_subplot(1, 1, 1)
ax.set_xlabel('Campo 1', fontsize=15)
ax.set_ylabel('Campo 2', fontsize=15)
ax.set_title('Componentes', fontsize=25)

color_theme = np.array(["blue", "green", "orange", "red"])
ax.scatter(x=pca_codigo_alumnos.Component_1, y=pca_codigo_alumnos.Component_2,
           c=color_theme[pca_codigo_alumnos.KMeans_Clusters], s=80)

# Capturamos la hora y fecha para crear la imagen de reporte
hora_actual = datetime.datetime.now()
print(hora_actual)

# Guardamos la imagen
plt.savefig("veinteava_iteracion.jpg", bbox_inches='tight')
plt.show()

# Guardamos el archivo con la nueva columna
alumnos.to_csv('E:/UNASAM/IA/Proyecto de Investigación/kmeans/alumnos_kmeans.csv')
