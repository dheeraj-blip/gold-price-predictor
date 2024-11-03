import streamlit as st
import math

# Set the title of the app
st.title("Gold Price Predictor")

# Input for the number of years
years = st.number_input("Enter the year:", min_value=1947, step=1)

# Calculate the gold price based on the provided formula
gold_price = math.exp(-189.0625 + 0.0978 * years)

# Display the predicted gold price
st.write(f"Predicted Gold Price (per gram): ₹{gold_price:.2f}")

# Note about potential fluctuation with explanation
st.warning("Note: There could be a fluctuation of +/- ₹300 on average.")
st.markdown("""
    The price of gold is influenced by various factors, including market demand, geopolitical stability, 
    inflation rates, and currency fluctuations. These variables can cause the gold price to vary significantly 
    in the short term. As a result, while the predicted price gives an estimate based on historical data, 
    actual market prices may differ by approximately ₹300 on average. It’s always advisable to consider these 
    factors when making financial decisions related to gold investments.
""")
