import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
import streamlit as st
import datetime
import fundamentus
import plotly.graph_objects as go

df = fundamentus.get_resultado()

#ticker search feature in sidebar
st.sidebar.subheader("""Aplicativo QuantRock""")

selected_stock = st.sidebar.selectbox(
        'Escolha o ativo',
        ('','OUTRO',"ABEV3","ALPA4","ALSO3","ARZZ3","ASAI3","AZUL4","B3SA3","BBAS3"
         ,"BBDC3","BBDC4","BBSE3","BEEF3","BPAC11","BPAN4","BRAP4","BRFS3","BRKM5"
         ,"CASH3","CCRO3","CIEL3","CMIG4","CMIN3","COGN3","CPFE3","CPLE6","CRFB3"
         ,"CSAN3","CSNA3","CVCB3","CYRE3","DXCO3","ECOR3","EGIE3","ELET3","ELET6"
         ,"EMBR3","ENBR3","ENEV3","ENGI11","EQTL3","EZTC3","FLRY3","GGBR4","GOAU4"
         ,"GOLL4","HAPV3","HYPE3","IGTI11","ITSA4","ITUB4","JBSS3","KLBN11","LREN3"
         ,"LWSA3","MGLU3","MRFG3","MRVE3","MULT3","NTCO3","PCAR3","PETR3","PETR4"
         ,"PETZ3","PRIO3","QUAL3","RADL3","RAIL3","RAIZ4","RDOR3","RENT3","RRRP3"
         ,"SANB11","SBSP3","SLCE3","SMTO3","SOMA3","SUZB3","TAEE11","TIMS3","TOTS3"
         ,"UGPA3","USIM5","VALE3","VBBR3","VIIA3","VIVT3","WEGE3","YDUQ3"))

if selected_stock == '':
    selected_stock = st.sidebar.text_input("Ou escreva o ticker no campo abaixo")

if selected_stock == 'OUTRO':
    selected_stock = st.sidebar.text_input("Ou escreva o ticker no campo abaixo")
    
#Selecionar o período
dIni = st.date_input(
    "Início",
    datetime.date(2020, 1, 1))



button_clicked = st.sidebar.button("OK")
if button_clicked == "OK":
    main()
  
def main():
    st.subheader("Preço de frechamento de " + selected_stock)
    #get data on searched ticker
    stock_data = yf.Ticker(selected_stock + '.SA')
    #get historical data for searched ticker
    stock_df = stock_data.history(period='1d', start=dIni, end=None, auto_adjust = True)
    #print line chart with daily closing prices for searched ticker
    #st.line_chart(stock_df.Close) #Gráfico de fechamento simples, de linha
    
    fig = go.Figure(data=[go.Candlestick(
        x=stock_df.index,
        open=stock_df['Open'], high=stock_df['High'],
        low=stock_df['Low'], close=stock_df['Close'],
        increasing_line_color= 'green', decreasing_line_color= 'red'
    )])
    
    st.plotly_chart(fig, use_container_width=True)  


    if selected_stock != '':       
            st.subheader("""Úlitmo **preço de fechamento** de """ + selected_stock)
            #imprime o último fechamento com a data
            last_price = str(round(stock_df['Close'].iloc[-1],2))
            hoje=str(stock_df.index[-1].strftime('%d/%m/%y'))
            st.write('Data:' + hoje + ' Preço: ' + last_price)
    
     
    #get daily volume for searched ticker
    st.subheader("""Volume **diário** de """ + selected_stock)
    st.line_chart(stock_df.Volume)

    #additional information feature in sidebar
    st.sidebar.subheader("""Mostrar Informações Adicionais""")
    #checkbox to display stock actions for the searched ticker
    actions = st.sidebar.checkbox("Dividendos e Splits")
    if actions:
        st.subheader("Dividendos pagos de " + selected_stock)
        display_action = (stock_data.actions)
        if display_action.empty == True:
            st.write("Sem dados no momento")
        else:
            st.write(display_action)
        
    #indicadores fundamentalistas
    st.sidebar.subheader("""Mostrar Indicadores Fundamentalistas""")
    #checkbox to display stock actions for the searched ticker
    actions = st.sidebar.checkbox("Indicadores")
    if actions:
        st.subheader("Indicadores de " + selected_stock)
        display_action = df.loc[selected_stock]
        if display_action.empty == True:
            st.write("Sem dados no momento")
        else:
            st.write(display_action)      
        
    #Mostrar todos ativos
    st.sidebar.subheader("""Mostrar Todos os Ativos""")
    #checkbox to display stock actions for the searched ticker
    todosAtivos = st.sidebar.checkbox("Todos ativos - Indicadores")
    if todosAtivos:
        st.subheader("Indicadores Fundamentalistas - Todos ativos do IBOV")
        st.dataframe(df,use_container_width=True)  
 

if __name__ == "__main__":
    main()
