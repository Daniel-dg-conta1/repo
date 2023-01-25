import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
import streamlit as st

ticker="CCRO3.SA"
df=yf.download(ticker, period="10y", auto_adjust= True)


st.pyplot(df["Close"].plot(figsize=(22,8)))
