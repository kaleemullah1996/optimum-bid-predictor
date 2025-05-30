import streamlit as st
import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model

# Load model
model = load_model("rf.keras")

# Title
st.set_page_config(page_title="Optimum Bid Predictor")
st.title("🏗️ Optimum Bidding Percentage Predictor")
st.markdown("Enter project features to predict the most competitive bid percentage.")

# Input form
def get_user_input():
    # Replace these with actual feature names used in your model
    feature1 = st.number_input("Project Size/NIT Amount", format="%.2f")
    feature2 = st.number_input("Earnest Money", format="%.2f")
    feature3 = st.number_input("Number of Active Contractors", format="%.2f")
    feature4 = st.number_input("Earnest Money Percentage", format="%.2f")
    feature5 = st.number_input("Competitor Bid Percentage 1", format="%.2f")
    feature6 = st.number_input("Competitor Bid Percentage 2", format="%.2f")
    feature7 = st.number_input("Exchange Rate", format="%.2f")
    feature8 = st.number_input("Inflation CPI", format="%.2f")
    feature9 = st.number_input("Bricks New First Class Per 1000", format="%.2f")
    feature10 = st.number_input("Bajri (Raita) Per Truck of 100 CFT", format="%.2f")
    feature11 = st.number_input("Sand (Mixed) Per Truck of 100 CFT", format="%.2f")
    feature12 = st.number_input("Cement Per Bag", format="%.2f")
    feature13 = st.number_input("Timber Log (Shesham) Per CM", format="%.2f")
    feature14 = st.number_input("Iron Bar (1/2" Round MS Bars) Per Tonne", format="%.2f")
    feature15 = st.number_input("Mason (Raj) Per Day", format="%.2f")
    feature16 = st.number_input("Labourer (Unskilled) Per Day", format="%.2f")
    feature17 = st.number_input("Tender Opening Year", format="%.2f")

    # Add or remove based on your model
    features = np.array([[feature1, feature2, feature3, feature4, feature5, feature6, feature7, feature8, feature9, feature10, feature11, feature12, feature13, feature14, feature15, feature16, feature17]])  # Shape: (1, num_features)
    return features

# Collect input
input_data = get_user_input()

# Predict button
if st.button("🔮 Predict"):
    prediction = model.predict(input_data)[0][0]
    st.success(f"✅ Predicted Optimum Bid: **{prediction:.2f}%**")
