# bmi_calculator.py
import streamlit as st

# App title
st.title("BMI Calculator")

# User inputs
st.subheader("Enter your details:")
weight = st.number_input("Weight (kg)", min_value=0.0, step=0.1)
height = st.number_input("Height (cm)", min_value=0.0, step=0.1)

# BMI calculation
if st.button("Calculate BMI"):
    if height > 0:
        height_m = height / 100  # Convert cm to meters
        bmi = weight / (height_m ** 2)
        st.success(f"Your BMI is: **{bmi:.2f}**")

        # BMI category
        if bmi < 18.5:
            st.info("You are **Underweight**")
        elif 18.5 <= bmi < 24.9:
            st.success("You have a **Normal weight**")
        elif 25 <= bmi < 29.9:
            st.warning("You are **Overweight**")
        else:
            st.error("You are in the **Obese** range")
    else:
        st.error("Please enter a valid height greater than 0.")
