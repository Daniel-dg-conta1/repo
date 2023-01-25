
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

ticker="CCRO3.SA"
df=yf.download(ticker, period="10y", auto_adjust= True)
