# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
import streamlit as st
import pandas as pd
import numpy as np
import pickle


st.image("http://www.ehtp.ac.ma/images/lo.png")

st.markdown(f'<h1 style="color:#773723;text-align: center;font-size:48px;">{"Cloud Computing project"}</h1>', unsafe_allow_html=True)
st.markdown(f'<h1 style="color:#da9954;text-align: center;font-size:36px;">{"Indian Diabetes Prediction App"}</h1>', unsafe_allow_html=True)
st.markdown(f'<h1 style="color:#557caf;font-size:24px;">{"> Realized by: Mustapha El Idrissi"}</h1>', unsafe_allow_html=True)


st.sidebar.slider("Pregnancies", 0, 25)
st.sidebar.slider("Glucose", 0, 300)
st.sidebar.slider("Glucose", 0, 150)
st.sidebar.slider("Skin Thickness", 0, 100)
st.sidebar.slider("Insulin", 0, 1000)
st.sidebar.slider("BMI", 0.0, 100.0, 0.1)
st.sidebar.slider("Diabetes Pedigree Function", 0.00, 10.00, 0.01)
st.sidebar.slider("Age", 0, 120)



def show_results():
    st.subheader("User Input parameters")
    st.write("Outcome")

show_results()
