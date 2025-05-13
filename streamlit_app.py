import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import joblib
from PIL import Image
from datetime import datetime, date
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px



# Setting page configuration
st.set_page_config(page_title="Aviation flights fare", page_icon="✈️", layout='wide')

# Loading data
df = pd.read_csv('cleaned_df.csv')

with st.sidebar:

    st.sidebar.image('R.jpg')
    st.sidebar.subheader("This dashboard for Indian Aviation Flights Fare aimed at predicting the prices of flight tickets")
    st.sidebar.write("")
    
    data = df.copy()
    source = st.sidebar.selectbox("Departure City", ['All'] + list(data['Source'].unique()))
    # data after Source selection
    if source != 'All':
        data = data[data['Source'] == source]
    
    destination = st.sidebar.selectbox("Arrival City", ['All'] + list(data['Destination'].unique()))
    # data after Source and Destination selection
    if destination != 'All':
        data = data[data['Destination'] == destination]

    duration = data[(data['Source'] == source) & (data['Destination'] == destination)]
    
    airline = st.sidebar.selectbox("Airline Carrier", ['All'] + list(data['Airline'].unique()))
    # data after Source and Destination and Month and Day selection and departure hour selection and airline selection
    if airline != 'All':
        data = data[data['Airline'] == airline]

    add_info = st.sidebar.selectbox("Additional Services", ['All'] + list(data['Additional_Info'].unique()))

    filter_box = st.sidebar.selectbox("Filter Prices on", [None, 'Day', 'Month', 'Dep_Hour'])



    st.sidebar.write("")
    st.sidebar.markdown("Made by [Hussein zayed](https://github.com/HusseinZayed)")

    # filtering Function
def filter(airline, source, destination, add_info):
    if airline=='All' and source=='All' and destination=='All' and add_info=='All':
        filtered_data = data.copy()
    else:
        filtered_data = data

        if source != 'All':
            filtered_data = filtered_data[filtered_data['Source'] == source]

        if destination != 'All':
            filtered_data = filtered_data[filtered_data['Destination'] == destination]

        if airline != 'All':
            filtered_data = filtered_data[filtered_data['Airline'] == airline]

        if add_info != 'All':
            filtered_data = filtered_data[filtered_data['Additional_Info'] == add_info]

    return filtered_data

