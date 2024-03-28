import streamlit as st
import pandas as pd

st.title("🌜🌜Wedsite Developing using Python")
#st.header("🌟Wedsite Developing using Python🌟")
st.subheader("🌝Phurin Kwanjira🌝")
st.image('012.jpg')


dt=pd.read_csv('./data/iris.csv')

st.subheader("ข้อมูลดอกไม้ Iris")
st.write(dt.head(10))
#Index(['sepal.length', 'sepal.width', 'petal.length', 'petal.width',
#       'variety'], 

st.subheader("สถิติข้อมูลดอกไม้ Iris")
st.write('ผลรวม')
cl1,cl2,cl3,cl4=st.columns(4)
cl1.write(dt['sepal.length'].sum())
cl2.write(dt['sepal.width'].sum())
cl3.write(dt['petal.length'].sum())
cl4.write(dt['petal.width'].sum())
cols=['sepal.length', 'sepal.width','petal.length']
dx=dt[cols]
st.bar_chart(dx,x='sepal.length',y='sepal.width',color='petal.length')

st.write('ค่าเฉลี่ย')
cl11,cl12,cl13,cl14=st.columns(4)
cl11.write(dt['sepal.length'].mean())
cl12.write(dt['sepal.width'].mean())
cl13.write(dt['petal.length'].mean())
cl14.write(dt['petal.width'].mean())

st.write('ค่ามากที่สุด')
cl21,cl22,cl23,cl24=st.columns(4)
cl21.write(dt['sepal.length'].max())
cl22.write(dt['sepal.width'].max())
cl23.write(dt['petal.length'].max())
cl24.write(dt['petal.width'].max())

st.write('ค่าน้อยที่สุด')
cl31,cl32,cl33,cl34=st.columns(4)
cl31.write(dt['sepal.length'].min())
cl32.write(dt['sepal.width'].min())
cl33.write(dt['petal.length'].min())
cl34.write(dt['petal.width'].min())