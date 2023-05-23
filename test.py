import streamlit as st

st.title('Hello World!!!')

st.header('Web application for Model Building')

st.subheader('Mini web application')

user_name = st.text_input('Enter Your name')

greetings  = f'Welcome {user_name}, This is your Mini web application design'

st.header(greetings)