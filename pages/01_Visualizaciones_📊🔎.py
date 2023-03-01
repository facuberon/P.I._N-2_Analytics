import yfinance as yf
from fredapi import Fred
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import requests
import streamlit as st 
import plotly.express as px

st.title('Visualizaciones 📊🔎')
st.markdown('*****')
st.subheader('Valor total del S&P500 desde el año 2000')

sp500_history = pd.read_csv('sp500_history.csv',index_col=0 )
total_historico_valor = pd.read_csv('total_historical_value.csv', index_col=0, parse_dates=True)

# Creo gráfico interactivo con Plotly Express
fig = px.line(total_historico_valor, x=total_historico_valor.index, y='Total Value')
fig.update_xaxes(title_text="Fecha")
fig.update_yaxes(title_text="Valor total en millones de dólares")
# Muestro gráfico en Streamlit
st.plotly_chart(fig)

st.markdown('*****')
st.subheader('Empresas del S&P500 con mejor rendimiento desde el año 2000')
# Calculo la diferencia porcentual para cada columna
porcentaje_aumento = (sp500_history.iloc[-1] / sp500_history.iloc[0] - 1) * 100

# Ordeno por el porcentaje de aumento de forma descendente
porcentaje_aumento = porcentaje_aumento.sort_values(ascending=False)
porcentaje_aumento_df = pd.DataFrame(porcentaje_aumento)
porcentaje_aumento_df = porcentaje_aumento_df.rename(columns={0: 'Porcentaje de aumento'})
porcentaje_aumento_df = porcentaje_aumento_df.rename_axis('Ticker')
porcentaje_aumento_df['Porcentaje de aumento'] = porcentaje_aumento_df['Porcentaje de aumento'].apply(lambda x: '{:.2f}%'.format(x*1))
# Muestro el porcentaje de aumento de cada empresa
st.dataframe(porcentaje_aumento_df.head(30))

st.markdown('*****')

st.subheader('Sectores de Top 20 empresas del S&P500')

tickers = ['MNST','ODFL','TSCO','NVDA','AAPL','IDXX','NVR','ANSS','POOL','UNH','AZO','ORLY','HUM','JBHT','BLK','ATVI','ROST','REGN','KMX','GILD']
sp500_data = yf.download(tickers, start='2000-01-01', end='2022-02-13', group_by='ticker')

sectors = {'MNST':'Productos consumibles','ODFL':'Industrial','TSCO':'Consumo minorista','NVDA':'Tecnológico','AAPL':'Tecnológico','IDXX':'Atención sanitaria','NVR':'Consumo minorista','ANSS':'Tecnológico','POOL':'Industrial','UNH':'Atención sanitaria','AZO':'Consumo minorista','ORLY':'Consumo minorista','HUM':'Atención sanitaria','JBHT':'Industrial','BLK':'Servicios Financieros','ATVI':'Servicios de comunicación','ROST':'Consumo minorista','REGN':'Atención sanitaria','KMX':'Consumo minorista','GILD':'Atención sanitaria'}

top_companies = ['MNST','ODFL','TSCO','NVDA','AAPL','IDXX','NVR','ANSS','POOL','UNH','AZO','ORLY','HUM','JBHT','BLK','ATVI','ROST','REGN','KMX','GILD']

sectors_count = {}
for company in top_companies:
    sector = sectors[company]
    if sector in sectors_count:
        sectors_count[sector] += 1
    else:
        sectors_count[sector] = 1

labels = list(sectors_count.keys())
sizes = list(sectors_count.values())

fig1, ax1 = plt.subplots(figsize=(5.5,5.5))
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=45)
ax1.axis('equal')
for text in ax1.texts:
    text.set_color('black')

st.pyplot(fig1, ax1)

st.markdown('*****')
st.subheader('La política monetaria de la FED')

st.text('Base monetaria: suma total de emisión de moneda')

# Inicializar objeto Fred con API key
fred = Fred(api_key='a3c4e4a7fb46b9719f54facd9fd9aded')
# Descargar los datos de la serie "Base Monetaria"
base_monetaria = fred.get_series('BOGMBASE', observation_start='2000-01-01')
#st.line_chart(base_monetaria)
base_monetaria_df = pd.DataFrame(base_monetaria)
base_monetaria_df = base_monetaria_df.rename_axis('Fecha')
base_monetaria_df = base_monetaria_df.rename(columns={0: 'Dólares'})
#st.dataframe(base_monetaria_df)
# Creo gráfico interactivo con Plotly Express
fig2 = px.line(base_monetaria_df, x=base_monetaria_df.index, y=['Dólares'])
fig2.update_xaxes(title_text="Fecha")
fig2.update_yaxes(title_text="M = mil millones de dólares")
# Muestro gráfico en Streamlit
st.plotly_chart(fig2)

st.text('Tasas de interés: costo del crédito')
# Obtener datos de la tasa federal de fondos federales (Federal Funds Rate) desde 2000
fedfunds_data = fred.get_series('FEDFUNDS', observation_start='2000-01-01')

# Graficar datos
fedfunds_data_df = pd.DataFrame(fedfunds_data)
fedfunds_data_df = fedfunds_data_df.rename_axis('Fecha')
fedfunds_data_df = fedfunds_data_df.rename(columns={0:'Tasa'})
fig3 = px.line(fedfunds_data_df, x=fedfunds_data_df.index, y=['Tasa'])
fig3.update_xaxes(title_text='Fecha')
fig3.update_yaxes(title_text='Puntos porcentuales')
st.plotly_chart(fig3)

st.markdown('*****')

st.subheader('Correlación entre el S&P500 y la base monetaria')

df2 = pd.concat([total_historico_valor, base_monetaria_df], axis=1)

# Calcular la matriz de correlación
corr_matrix = df2.corr()

# Mostrar la matriz de correlación
st.write(corr_matrix)

# Crear un gráfico de correlación utilizando seaborn
# Calcular la media y la desviación estándar de la serie "fed_data"
fed_mean = np.mean(base_monetaria)
fed_std = np.std(base_monetaria)

# Estandarizar la serie "fed_data"
fed_data_std = (base_monetaria - fed_mean) / fed_std

# Calcular la media y la desviación estándar de la serie "sp500_data"
sp500_mean = np.mean(total_historico_valor)
sp500_std = np.std(total_historico_valor)

# Estandarizar la serie "sp500_data"
sp500_data_std = (total_historico_valor - sp500_mean) / sp500_std

fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(fed_data_std.index, fed_data_std, label='Base Monetaria de la FED')
ax.plot(sp500_data_std.index, sp500_data_std, label='Valor Total del S&P500')

ax.set_xlabel('Año')
ax.set_ylabel('Valor')
ax.set_title('Comparación entre la Base Monetaria de la FED y el Valor Total del S&P500')

ax.legend()
st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot()

st.markdown(''' El índice de correlación entre el S&P500 y la base monetaria es muy alto (`0.91`). Ambos estan fuertemente relacionados, como podemos ver en el gráfico de comparación, cuando la FED expande la base monetaria las acciones tienden a subir y cuando la FED contrae, tienden a bajar.
Esto nos indica que deveríamos diversificar nuestra cartera de inversiones para no tener demasiada exposición a las políticas monetarias de la FED.
 
''')