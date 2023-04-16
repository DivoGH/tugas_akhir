import pandas as pd
import streamlit as st
from sklearn import linear_model
import numpy as np
from PIL import Image

img = Image.open('upb.png')
data1 = pd.read_csv('PrediksiMancing.csv')

st.image(img, width=260)
st.title('Prediksi Memancing')

umpan = data1['Umpan']
jam = data1['Jam']
harga = data1['Ikan']

varx = []

for i in range(len(umpan)):
    varx.append([umpan[i],jam[i]])

l_rg = linear_model.LinearRegression().fit(varx,harga)

## a = l_rg.intercept_
## b = l_rg.coef_
## c = l_rg.score(varx,harga)
## print(a)
## print(b)
## print(c)

ip_1 = st.number_input ("Masukan Jumlah Umpan 1-20 Umpan", 0)
ip_2 = st.number_input ("Masukan Jam Mancing 1-4 Jam", 0)

est = -1.3+(0.29*ip_1)+(0.14*ip_2)

if st.button ("Cek Hasil Tangkapan Ikan") :
    est = -1.3+(0.29*ip_1)+(0.14*ip_2)
    st.success(f"Prediksi Hasil Tangkapan Kamu adalah = {est} Ikan")