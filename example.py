import streamlit as st

st.title('My Streamlit App')
st.write("This is a simple web app to display data and interact with users.")

# Input widget
age = st.slider('Select your age', 0, 100)

# Display user input
st.write(f'Your age is {age}')
