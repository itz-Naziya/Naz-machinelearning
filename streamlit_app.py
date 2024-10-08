import streamlit as st
import pandas as pd

st.title('🎈 Machine learning app')

st.info('This app builds a machine learning model')

with st.expander('Data'):
  st.write('**Raw Data**')
  df=pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
  df

  st.write('**X**')
  X_raw=df.drop('species',axis=1)
  X_raw

  st.write('**y**')
  y_raw=df.species
  y_raw

with st.expander('Data Visualization'):
  #"bill_length_mm","bill_depth_mm","flipper_length_mm","body_mass_g"
  st.scatter_chart(data=df, x= 'bill_length_mm',y='body_mass_g',color='species')

#input featires
with st.sidebar:
  st.header('Input Features') 
  #"bill_depth_mm","flipper_length_mm","body_mass_g","sex"
  island=st.selectbox('Island',('Biscoe','Torgersen','Dream')) 
  bill_length_mm=st.slider('Bill length (mm)',32.1,59.6,43.9)
  bill_depth_mm=st.slider('Bill Depth (mm)' , 13.1,21.5,17.2)
  flipper_length_mm=st.slider('Flipper Length (mm) ', 172.0, 231.0, 201.0)
  body_mass_g=st.slider('Body mass (g)' , 2700.0 , 6300.0 , 4207.0 )
  gender=st.selectbox('Gender',('male','female'))

  #create a dataframe for input features
  data={'island' : island , 'bill_length_mm' : bill_length_mm, ' bill_depth_mm ' : bill_depth_mm , 
        ' flipper_length_mm' : flipper_length_mm , ' body_mass_g ' : body_mass_g ,
        ' sex': gender }
  input_df= pd.DataFrame(data , index = [0])
  input_penguins = pd.concat([input_df , X_raw ],axis=0)


#Data preparation
#encode X
encode = ['island', 'sex']
df_penguins=pd.get_dummies(input_penguins,columns=encode)
input_row = df_penguins[:1]

#encode Y
target_mapper = { 'Adelie' :0, 
                 'Chinstrap': 1 , 
                 'Gentoo' :2 }
def target_encode(val):
  return target_mapper[val]

y=y_raw.apply(target_encode)
y
y_raw

with st.expander('Data Preparation'):
  st.write('**Encoded X (Input penguin)**')
  input_row
  st.write('**Encoded y**')
  y

  












