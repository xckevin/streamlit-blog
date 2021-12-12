import  streamlit as st
import os

dir = os.path.join(os.getcwd(), 'files')

def getAllFiles():
    return os.listdir(dir)

def readFile(x):
    with open(x, 'r', encoding='UTF-8') as f:
        d = f.read()
        return d    

st.sidebar.header('List')
file = st.sidebar.selectbox('', getAllFiles())

if file:
    st.markdown(readFile(os.path.join(dir, file)))
else:
    st.write("Hi bro, this is my blog")
