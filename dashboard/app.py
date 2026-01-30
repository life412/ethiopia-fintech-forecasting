
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Ethiopia Financial Inclusion Forecast")

# Load forecasts
access_forecast = pd.read_csv('../data/processed/access_forecast.csv')
usage_forecast = pd.read_csv('../data/processed/usage_forecast.csv')

st.header("Forecasted Account Ownership (Access)")
st.line_chart(access_forecast.set_index('year')['value_numeric'])

st.header("Forecasted Digital Payment Usage")
st.line_chart(usage_forecast.set_index('year')['value_numeric'])
