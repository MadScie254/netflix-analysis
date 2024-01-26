import streamlit as st
import pandas as pd
import joblib

# Load the trained Random Forest model
model = joblib.load('random_forest_model.pkl')

# Define Streamlit UI
st.title('Netflix Stock Price Prediction')
st.sidebar.title('User Input')

# Define input fields
open_price = st.sidebar.number_input('Open Price')
high_price = st.sidebar.number_input('High Price')
low_price = st.sidebar.number_input('Low Price')
close_price = st.sidebar.number_input('Close Price')
volume = st.sidebar.number_input('Volume')

# Perform model inference
input_data = pd.DataFrame({'Open': [open_price], 'High': [high_price], 
                           'Low': [low_price], 'Close': [close_price], 
                           'Volume': [volume]})
prediction = model.predict(input_data)

# Display prediction
st.write('Predicted Adjusted Close Price:', prediction[0])
