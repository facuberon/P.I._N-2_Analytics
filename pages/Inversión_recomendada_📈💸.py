import streamlit as st
import pandas as pd
import pandas_datareader as pdr
import seaborn as sns
import matplotlib.pyplot as plt
import yfinance as yf
from fredapi import Fred

st.title('Inversión recomendada 📈💸')
st.markdown('*****')
st.subheader('Una cartera diversificada: aumentamos ganancias y reducimos exposición a la FED')

col1, col2, col3 = st.columns(3)
col1.metric("S&P500","0.91 c.c.","1,026.32%")
col2.metric("Top 20 empresas S&P500", "0.89 c.c.", "17,307.56%")
col3.metric("Oro", "O.86 c.c.", "673.89%")
col1.metric("Plata","0.81 c.c.","448.11%")
col2.metric("Platino", "0.76 c.c.", "407.7%")
col3.metric("Bitcoin", "O.50 c.c.", "24,635.46%")
col1.metric("Cruede Oil","0.53 c.c.","229.02%")
col2.metric("Cobre", "0.78 c.c.", "577.7%")
col3.metric("Paladio", "O.84 c.c.", "668.23%")
col1.metric("Gas natural","0.47 c.c.","138.89%")
col2.metric("Litio", "0.80 c.c.", "896.48%")
col3.metric("Ganado", "O.59 c.c.", "289,54%")


st.text("c.c = Coeficiente de correlacion con base monetaria FED")

st.markdown('*****')

st.subheader('Resultados de cartera recomendada:')

col1, col2 = st.columns(2)
col1.metric("Retorno de inverción","3.941,57%","+383,04%")
col2.metric("Exposición FED","0.72 c.c","-20,9%")

st.markdown('Maximizamos retornos ✅✅✅✅✅✅✅✅✅ Minimizamos exposición')

st.markdown('*****')

st.image('https://querido-dinero.imgix.net/uploads/2020/01/khgjNnn3EbC0XQzS4QvqthC6k4QI713vl5OGnlOo.gif')


