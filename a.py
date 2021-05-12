import streamlit as st

name=st.text_input('What is your name?')
selectbox = st.selectbox('What is your favorite food?',['Hambuger','Sandwich','Susi'])

st.write('Hello ' + name + '! Nice to meet you!')
st.write('Hola ' + name + '! Mucho gusto!')
