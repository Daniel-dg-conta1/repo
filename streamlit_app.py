import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
import streamlit as st
import datetime


#ticker search feature in sidebar
st.sidebar.subheader("""Aplicativo QuantRock""")
selected_stock = st.sidebar.text_input("Enter a valid stock ticker...", "PETR4")
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
    st.line_chart(stock_df.Close)

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
 

if __name__ == "__main__":
    main()
