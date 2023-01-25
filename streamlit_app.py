!pip install streamlit
!pip install yfinance --upgrade --no-cache-dir
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader.data as web
import yfinance as yf
yf.pdr_override()
papel=yf.download('PETR4.SA')
papel["Close"].plot(figsize=(22,8))
