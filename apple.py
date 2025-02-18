import streamlit as st
import yfinance as yf
import warnings
import pandas as pd
import matplotlib.pyplot as plt
warnings.filterwarnings('ignore')

st.title('Все и ничего о компании ***APPLE***')
tickerSymbol = 'AAPL'
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period='1d', start='2010-1-31', end='2025-1-31')


st.sidebar.title("Выберите график")
option = st.sidebar.selectbox(
    "Какой график вы хотите увидеть?",
    ("Стоимость акций", "Объем торгов", "Размер дивидендов")
)


if option == "Стоимость акций":
    st.write('### Стоимость акций на момент закрытия')
    st.line_chart(tickerDf.Close)
elif option == "Объем торгов":
    st.write('### Объем торгов')
    st.line_chart(tickerDf.Volume)
elif option == "Размер дивидендов":
    st.write('### Размер дивидендов')
    st.line_chart(tickerDf.Dividends)


st.write('### Данные о котировках компании Apple')
st.dataframe(tickerDf.head(10))

