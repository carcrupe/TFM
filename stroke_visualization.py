
import streamlit as st
import numpy as np
import pandas as pd
import pickle
#from PIL import Image

st.title('Get to know your heart')
st.subheader('Predict your heart status')

clf_loaded = pickle.load(open("notebooks_models/best.model","rb"))

st.sidebar.title('Set parameters')

#Default paramenters of a healthy patient
ageInit= 45
sPressureInit= 120
dPressureInit= 80
cholesterolInit= 1

age = st.sidebar.number_input('Age', value=ageInit)

sPressure = st.sidebar.number_input('Systolic Pressure',value=sPressureInit)

dPressure = st.sidebar.number_input('Diastolic Pressure',value=dPressureInit)

pulse = sPressure-dPressure

cholesterolDict = {'Low: <200 mg/dL':1, 'High: 200-240 mg/dL':2, 'Very high: >240 mg/dL':3}
cholesterol = st.sidebar.selectbox('Cholresterol', ['Low: <200 mg/dL', 'High: 200-240 mg/dL', 'Very high: >240 mg/dL'])
cholesterol = cholesterolDict[cholesterol]

inputData = [age, sPressure,
       dPressure, cholesterol, pulse]
columns=['Age','SystolicPressure',
'DiastolicPressure','Pulse','Target']

if st.button('Predict'):

    pred = clf_loaded.predict([inputData])
    if(pred == 0):
        'Your heart is safe!'
    else:
        'Your should take care of your heart, go see the doctor for further tests'
#        imageLocation.image(image)
