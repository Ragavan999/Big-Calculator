import streamlit as st
import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Not divisible by zero"
    else:
        return x / y

def squareroot(x):
    return math.sqrt(x)

def powerof(x,y):
    return x**y

st.header("Big Calculator")
st.markdown("**Created by Ragavan Manikandan**")

num1 = st.number_input("Enter the First Number", value=0)
num2 = st.number_input("Enter the Second Number", value=0)

operation = st.selectbox("Select operation", ["Addition", "Subtraction", "Multiplication", "Division", "SquareRoot(Put the number in First Number)", "PowerOf"])

if st.button("Calculate"):
    if operation == "Addition":
        result = add(num1, num2)
    elif operation == "Subtraction":
        result = subtract(num1, num2)
    elif operation == "Multiplication":
        result = multiply(num1, num2)
    elif operation == "Division":
        result = divide(num1, num2)
    elif operation == "SquareRoot(Put the number in First Number)":
        result = squareroot(num1)
    elif operation == "PowerOf":
        result = powerof(num1, num2)    
    else:
        result = "Invalid Operation"

    st.write(f"The result is: {result}")
