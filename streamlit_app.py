!pip install streamlit
!pip install matplotlib
!pip install pandas_datareader
!pip install yfinance

import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader.data as web
import yfinance as yf
yf.pdr_override()




st.sidebar.title('menu')
paginaSelecionada=st.sidebar.selectbox('Selecione a página',['Página 1', 'Página 2'])

if paginaSelecionada== 'Página 1':
    st.title('Video Exemplo')
    st.selectbox('Selecione uma opção',['opção 1', 'opção 2'])
elif paginaSelecionada== 'Página 2':
    st.title('Você selecionou a página 2')
    

papel=yf.download('PETR4.SA', period="10y", auto_adjust= True)
st.pyplot(papel["Close"].plot(figsize=(22,8)))
