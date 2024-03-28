import streamlit as st
import pandas as pd

st.title("🌜🌜Wedsite Developing using Python")
st.header("🌟Wedsite Developing using Python🌟")

st.subheader("🌝Phurin Kwanjira🌝")
st.image('012.jpg')

dt=pd.read_csv('./data/iris.csv')
st.write(dt.head(10))