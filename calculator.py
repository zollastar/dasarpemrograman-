# streamlit_calculator.py

import streamlit as st
import math_operations as mo

st.title("Simple Calculator")

x = st.number_input("Enter the first number:")
y = st.number_input("Enter the second number:")

operation = st.selectbox("Select an operation",
                         ("Add", "Subtract", "Multiply", "Divide"))

result = None

if st.button("Calculate"):
    if operation == "Add":
        result = mo.add(x, y)
    elif operation == "Subtract":
        result = mo.subtract(x, y)
    elif operation == "Multiply":
        result = mo.multiply(x, y)
    elif operation == "Divide":
        try:
            result = mo.divide(x, y)
        except ZeroDivisionError:
            st.error("Division by zero is not allowed.")

if result is not None:
    st.success(f"Result: {result}")
