import streamlit as st
import random
import string

def generat_password(lenght, use_digits, use_special):
    charactors = string.ascii_letters  # Includes uppercase and lowercase letters

    if use_digits:
        charactors += string.digits # Adds numbers(0-9) if selected

    if use_special:
        charactors += string.punctuation # Adds special characters (! @ # $ % ^ & * etc.) if selected

  # Generate a password by randomly selecting characters based on the length provided
    return ''.join(random.choice(charactors) for _ in range(lenght))

st.title("Password Generator")

length = st.slider("select password Lenght",min_value=6, max_value=32, value=12)

use_digits = st.checkbox("Include Digits")

use_special = st.checkbox("Include special characters") 

if st.button("Generate Password"):
     password = generat_password(length,use_digits,use_special)
     st.write(f"Generate Password:`{password}`")

     st.write("--------------------")
     
     st.write("Build with ❤️ by [Aqsa](https://github.com/Aqsa513)")


