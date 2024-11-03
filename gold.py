import streamlit as st
import numpy as np
import math
import joblib  # Import joblib for loading the model

# Load the saved model and polynomial transformer
poly_model = joblib.load('polynomial_model.joblib')
poly = joblib.load('polynomial_transformer.joblib')

# Title of the app
st.title("Gold Price Predictor - By Dheeraj")

# User input for year
year = st.number_input("Enter the year:", value=2024, step=1)

# Add a button to calculate the gold price
if st.button("Calculate"):
    # Logic for prediction
    if year <= 2024:
        # Calculate gold price using the provided formula
        gold_price = math.exp(-189.0625 + 0.0978 * year)
        st.write(f"The predicted gold price for the year {year} is: ₹{gold_price:.2f}")
    else:
        # Prepare input for polynomial model
        year_array = np.array([[year]])  # Reshape for the model
        year_poly = poly.transform(year_array)  # Transform the input year
        predicted_price = poly_model.predict(year_poly)  # Make prediction
        st.write(f"The predicted gold price for the year {year} is: ₹{predicted_price[0]:.2f}")

    # Note about potential fluctuation with explanation
    st.warning("Note: There could be a fluctuation of +/- ₹300 on average.")
    st.markdown("""
        The price of gold is influenced by various factors, including market demand, geopolitical stability, 
        inflation rates, and currency fluctuations. These variables can cause the gold price to vary significantly 
        in the short term. As a result, while the predicted price gives an estimate based on historical data, 
        actual market prices may differ. For study purposes only.
    """)

# Run the Streamlit app
if __name__ == "__main__":
    st.write("Note: The predictions are based on the provided formula and the trained polynomial model.")



