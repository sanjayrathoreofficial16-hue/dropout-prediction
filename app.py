import pandas as pd
import pickle
import streamlit as st

# Title
st.title("Student Dropout Prediction System")

# Load dataset
df = pd.read_csv("data.csv", sep=';')

# Show dataset columns for debugging
st.write("Columns detected:", df.columns.tolist())

# Display dataset
st.subheader("Dataset Preview")
st.write(df.head())

# User Input
st.subheader("Enter Student Details")

# Gender column name is correct
gender = st.selectbox("Gender", df["Gender"].unique())

# Course column name is correct
course = st.selectbox("Course", df["Course"].unique())

# FIX: Marital Status column name has a SPACE
marital = st.selectbox("Marital Status", df["Marital status"].unique())

# Predict Button
if st.button("Predict Dropout"):
    st.success("Prediction will be shown here.")
