import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
import streamlit as st

ticker="CCRO3.SA"
df=yf.download(ticker, period="10y", auto_adjust= True)


arr = np.random.normal(1, 1, size=1000)
fig, ax = plt.subplots()
ax.hist(arr, bins=30)

st.pyplot(fig)
