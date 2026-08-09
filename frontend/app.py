
import streamlit as st
import pandas as pd
import requests

# Base URL of the Flask backend
BACKEND_URL = "http://backend:7860"


st.title("SuperKart Sales Forecast App") #Complete the code to define the title of the app.

# Input fields for product and store data
Product_Weight = st.number_input("Product Weight", min_value=0.0, value=12.66)
Product_Sugar_Content = st.selectbox("Product Sugar Content", ["Low Sugar", "Regular", "No Sugar"])
Product_Allocated_Area = st.number_input("Product Allocated Area", min_value=0.0, value=0.0687) #Complete the code to define the UI element for Product_Allocated_Area
Product_MRP = st.number_input("Product MRP", min_value=0.0, value=147.03) #Complete the code to define the UI element for Product_MRP
Store_Size = st.selectbox("Store Size", ["Medium", "High", "Small"]) #Complete the code to define the UI element for Store_Size
Store_Location_City_Type = st.selectbox("Store Location City Type", ["Tier 2", "Tier 1", "Tier 3"]) #Complete the code to define the UI element for Store_Location_City_Type
Store_Type = st.selectbox("Store Type", ["Supermarket Type2", "Departmental Store", "Supermarket Type1", "Food Mart"]) #Complete the code to define the UI element for Store_Type
Product_Id_char = st.selectbox("Product ID Character", ["FD", "NC", "DR"]) #Complete the code to define the UI element for Product_Id_char
Store_Age_Years = st.number_input("Store Age (Years)", min_value=0, value=24) #Complete the code to define the UI element for Store_Age_Years
Product_Type_Category = st.selectbox("Product Type Category", ["Non Perishables", "Perishables"]) #Complete the code to define the UI element for Product_Type_Category

product_data = {
    "Product_Weight": Product_Weight,
    "Product_Sugar_Content": Product_Sugar_Content,
    "Product_Allocated_Area": Product_Allocated_Area,
    "Product_MRP": Product_MRP,
    "Store_Size": Store_Size,
    "Store_Location_City_Type": Store_Location_City_Type,
    "Store_Type": Store_Type,
    "Product_Id_char": Product_Id_char,
    "Store_Age_Years": Store_Age_Years,
    "Product_Type_Category": Product_Type_Category
}

if st.button("Predict", type='primary'):
    # Replace with your deployed backend API URL when using GitHub Codespaces.
    # For Codespaces, this will typically be the forwarded port URL for your Flask app.
    # For example, if your Flask app is running on port 7860, the URL might be something like:
    # backend_api_url = "https://<YOUR_CODESPACE_NAME>-7860.app.github.dev/v1/predict"
    #backend_api_url = "<YOUR_GITHUB_CODESPACES_BACKEND_API_URL>/v1/predict"
    #response = requests.post(backend_api_url, json=product_data) # Complete the code to enter user name and space name to correctly define the endpoint
    
    response = requests.post(f"{BACKEND_URL}/v1/predict", json=input_data.to_dict(orient='records')[0])  # Send data to Flask API
    if response.status_code == 200:
        result = response.json()
        predicted_sales = result["Sales"]
        st.write(f"Predicted Product Store Sales Total: ₹{predicted_sales:.2f}")
    else:
        st.error("Error in API request. Please ensure the backend is running and the URL is correct.")
