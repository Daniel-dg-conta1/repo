import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
import streamlit as st


local_css("style.css")

#ticker search feature in sidebar
st.sidebar.subheader("""Stock Search Web App""")
selected_stock = st.sidebar.text_input("Enter a valid stock ticker...", "GOOG")
button_clicked = st.sidebar.button("GO")
if button_clicked == "GO":
  
  
ticker="CCRO3.SA"
df=yf.download(ticker, period="10y", auto_adjust= True)


#arr = np.random.normal(1, 1, size=1000)
fig = plt.figure()
plt.plot(df['Close'])

st.pyplot(fig)
