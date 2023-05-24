import streamlit as st
import  matplotlib.pyplot as plt
import seaborn as sns

st.title('Hello World!!!')

st.header('Web application for Model Building')

st.subheader('Mini web application')

user_name = st.text_input('Enter Your name')

greetings  = f'Welcome {user_name}'

st.header(greetings)


import pandas as pd
dict = {'name':['vanessa','christopher','chinasa','rex'],
'sex':['f','m','m','m'],'power':[30,20,20,40]}

df = pd.DataFrame(dict)

st.table(df)


# Create a bar chart using Matplotlib
fig, ax = plt.subplots()
ax.bar(df['name'], df['power'],color ='red')
ax.set_xlabel('name')
ax.set_ylabel('power')
ax.set_title('Bar Chart')

# Display the barchart using streamlit

st.pyplot (fig)