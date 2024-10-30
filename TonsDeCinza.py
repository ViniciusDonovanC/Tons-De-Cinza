import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import image

def gamma_expansion(c_srgb):
    return np.where(c_srgb <= 0.04045, c_srgb / 12.92, ((c_srgb + 0.055) / 1.055) ** 2.4)

def gamma_compression(c_linear):
    return np.where(c_linear <= 0.0031308, 12.92 * c_linear, 1.055 * (c_linear ** (1 / 2.4)) - 0.055)


RED = 0
GREEN = 1
BLUE = 2

uploaded_file = st.sidebar.file_uploader("Chose a File")

on = st.toggle("Binarizacao")

if on:
    threshold = st.slider("Binary threshold?", 0, 255, 25)
    pass

col1, col2, col3 = st.columns(3)
st.subheader(type(uploaded_file))   

with col1:
    if uploaded_file is not None:
        st.image(uploaded_file, caption="Imagem Original", width=200)

        img = np.array(uploaded_file)
        st.write(img)


with col2:
    if uploaded_file is not None:
        img_cinza_mean = np.mean(uploaded_file, axis=2)
        st.subheader(type(uploaded_file))
        st.image(uploaded_file, caption="Imagem Linear", width=200)
with col3:
    if uploaded_file is not None:
        st.subheader(type(uploaded_file))
        st.image(uploaded_file, caption="Imagem Gamma", width=200)
