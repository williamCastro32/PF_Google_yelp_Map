import streamlit as st
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np

def get_recommendations(user_id, categoria, df):
    # Filtrar el DataFrame para obtener solo las filas con la categoría especificada
    df_categoria = df[(df[categoria] == 1)]

    if len(df_categoria) == 0:
        # Si no hay negocios en la categoría especificada, devolver una lista de recomendaciones alternativas
        recomendaciones_alternativas = df[df['stars'] >= 4]['name'].tolist()  # Por ejemplo, negocios con 4 estrellas o más
        return recomendaciones_alternativas

    # Convertir el DataFrame a una matriz de calificaciones de usuarios y negocios
    matriz_calificaciones = df_categoria.pivot_table(index='user_id', columns='name', values='stars', fill_value=0)

    # Escalar las calificaciones para que tengan media 0 y desviación estándar 1
    scaler = StandardScaler()
    matriz_calificaciones_escaladas = scaler.fit_transform(matriz_calificaciones)

    # Calcular la similitud de coseno entre usuarios
    similitud_usuarios = cosine_similarity(matriz_calificaciones_escaladas)

    # Obtener el índice del usuario dado en la matriz de similitud
    indice_usuario = matriz_calificaciones.index.get_loc(user_id)

    # Obtener los usuarios más similares al usuario dado
    usuarios_similares = np.argsort(similitud_usuarios[indice_usuario])[::-1][1:]  # Excluimos al propio usuario

    # Obtener las calificaciones de los usuarios similares
    calificaciones_similares = matriz_calificaciones.iloc[usuarios_similares]

    # Calcular la calificación promedio para cada negocio
    calificaciones_promedio = calificaciones_similares.mean(axis=0)

    # Obtener los nombres de los negocios recomendados, ordenados por calificación promedio
    negocios_recomendados = calificaciones_promedio.sort_values(ascending=False).index.tolist()

    return negocios_recomendados[:3]  # Devolver las 3 mejores recomendaciones

# Importar dataset
df_recomendaciones = pd.read_csv('./docs/data_modelo/df_recomendaciones.csv.gz')

# Configuración de la aplicación Streamlit
st.title('Sistema de Recomendaciones')

# Entrada de usuario
user_id = st.text_input('Usuario ID', 'user1')
categoria = st.text_input('Categoría', 'Acai Bowls')

# Obtener recomendaciones
sugerencias = get_recommendations(user_id, categoria, df_recomendaciones)

# Mostrar resultados
if sugerencias:
    st.write("Sugerencias basadas en la categoría '{}' para el usuario '{}':".format(categoria, user_id))
    for i, sugerencia in enumerate(sugerencias):
        st.write(f"{i+1}. {sugerencia}")
else:
    st.write("No hay negocios recomendados para la categoría '{}' para el usuario '{}'.".format(categoria, user_id))
