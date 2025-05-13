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
    destination = st.sidebar.selectbox("Arrival City", ['All'] + list(data['Destination'].unique()))
    duration = data[(data['Source'] == source) & (data['Destination'] == destination)]
    airline = st.sidebar.selectbox("Airline Carrier", ['All'] + list(data['Airline'].unique()))
    add_info = st.sidebar.selectbox("Additional Services", ['All'] + list(data['Additional_Info'].unique()))

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

#------------------------------


# Filtered DataFrame
filtered_data = filter(airline, source, destination, add_info)

# Information Cards
card1, card2, card3, card4 = st.columns((2,2,2,4))

# Cards Values
flight_count = filtered_data['Airline'].count()
highest_Price = filtered_data['Price'].max()
lowest_Price = filtered_data['Price'].min()
top_airline = filtered_data['Airline'].value_counts().idxmax()

# Show The Cards
card1.metric("Flight Count", f"{flight_count}")
card2.metric("Highest Price", f"{highest_Price}")
card3.metric("Lowest Price", f"{lowest_Price}")
card4.metric("Top Airline", f"{top_airline}")

#-------------------------------------------------------
# Dashboard Tabs
tab1, tab2, tab3 = st.tabs(["🏠 Home", "📈 Insights", "🤖 Prediction"])

# introduction
with tab1:
    st.write("If you are a traveler looking to plan your next trip, or you are an airline or travel agency, "
         "you need to know about ticket and service price variations.\n"
         "Airline ticket pricing has become increasingly complex due to factors such as demand fluctuations and seasonal trends.\n"
         "\n"
         "My project aims to help you make the right decision and buy the best ticket at the best price by developing a predictive model "
         "that can accurately estimate flight fares based on the given features.")
   
    im1 = Image.open('R.jpg')
    st.image(im1)
