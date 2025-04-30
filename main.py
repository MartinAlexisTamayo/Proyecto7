import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')
# Casilla para mostrar histograma
show_hist = st.checkbox('Mostrar histograma del odómetro')

if show_hist:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Casilla para mostrar gráfico de dispersión
show_scatter = st.checkbox('Mostrar gráfico de dispersión (odómetro vs precio)')

if show_scatter:
    st.write('Creación de un gráfico de dispersión entre odometer y price')
    fig = px.scatter(car_data, x="odometer", y="price", title="Kilometraje vs Precio")
    st.plotly_chart(fig, use_container_width=True)