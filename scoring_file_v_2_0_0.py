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


def user_input_features():
    Pregnancies = st.sidebar.slider("Pregnancies", 0, 25)
    Glucose = st.sidebar.slider("Glucose", 0, 300)
    BloodPressure = st.sidebar.slider("Glucose", 0, 150)
    SkinThickness = st.sidebar.slider("Skin Thickness", 0, 100)
    Insulin = st.sidebar.slider("Insulin", 0, 1000)
    BMI = st.sidebar.slider("BMI", 0.0, 100.0, 0.1)
    DiabetesPedigreeFunction = st.sidebar.slider("Diabetes Pedigree Function", 0.00, 10.00, 0.01)
    Age = st.sidebar.slider("Age", 0, 120)


    data = {"Pregnancies": Pregnancies,
            "Glucose": Glucose,
            "Blood Pressure": BloodPressure,
            "Skin Thickness": SkinThickness,
            "Insulin": Insulin,
            "BMI": BMI,
            "Diabetes Pedigree Function": DiabetesPedigreeFunction,
            "Age": Age}

    features = pd.DataFrame(data, index=[0])
    return features

def show_results():
    st.subheader("User Input parameters")
    st.write("Outcome")
    #model_Outcome = pickle.load(open("model.pkl", "rb"))
    #prediction = model_Outcome.predict(Outcome)
    #prediction_proba = model_Outcome.predict_proba(Outcome)
    #st.subheader("Class labels and their corresponding index number")
    #st.write(pd.DataFrame(model_Outcome.classes_))
    #st.subheader("Prediction")
    #st.write(prediction)
    #st.subheader("Prediction Probability")
    #st.write(prediction_proba)


Outcome = user_input_features()
show_results()
