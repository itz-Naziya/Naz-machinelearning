import streamlit as st
import pandas as pd

st.title('🎈 Machine learning app')

st.info('This app builds a machine learning model')

with st.expander('Data'):
  st.write('**Raw Data**')
  df=pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
  df

  st.write('**X**')
  X=df.drop('species',axis=1)
  X

  st.write('**y**')
  y=df.species
  y

with st.expander('Data Visualization'):
  #"bill_length_mm","bill_depth_mm","flipper_length_mm","body_mass_g"
  st.scatter_chart(data=df, x= 'bill_length_mm',y='body_mass_g',color='species')

#data preparations
with st.sidebar:
  st.header('Input Feautures') 
  #"species","island","bill_length_mm","bill_depth_mm","flipper_length_mm","body_mass_g","sex"
  island=st.selectbox('Island',('Biscoe','Torgersen','Dream') 
  gender=st.selectbox('Gender',('male','female'))
  bill_length_mm=st.slider('Bill length (mm)',32.1,59.6,43.9)
  
