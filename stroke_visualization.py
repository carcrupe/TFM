#!/usr/bin/env python
# coding: utf-8

# In[3]:

import streamlit as st
import numpy as np
import pandas as pd
import pickle
#from PIL import Image

# In[ ]:
st.title('Get to know your heart')
st.subheader('Predict your heart status')

clf_loaded = pickle.load(open("best.model","rb"))

st.sidebar.title('Set parameters')

#Default paramenters of a healthy patient
ageInit= 45
'''heightInit= 165
weightInit= 65'''
sPressureInit= 120
dPressureInit= 80
cholesterolInit= 1


age = st.sidebar.number_input('Age', value=ageInit)

'''sexDict = {'Male':1, 'Female':2}
sex = st.sidebar.selectbox('Sex', ['Male','Female'])
sex = sexDict[sex]

height = st.sidebar.number_input('Height (cm)', value=heightInit)

weight = st.sidebar.number_input('Weight (Kg)', value=weightInit)'''

sPressure = st.sidebar.number_input('Systolic Pressure',value=sPressureInit)

dPressure = st.sidebar.number_input('Diastolic Pressure',value=dPressureInit)

pulse = sPressure-dPressure

cholesterolDict = {'Low: <200 mg/dL':1, 'High: 200-240 mg/dL':2, 'Very high: >240 mg/dL':3}
cholesterol = st.sidebar.selectbox('Cholresterol', ['Low: <200 mg/dL', 'High: 200-240 mg/dL', 'Very high: >240 mg/dL'])
cholesterol = cholesterolDict[cholesterol]

'''diabetes = st.sidebar.checkbox('Diabetes')

smoker = st.sidebar.checkbox('Smoker')

alcoholic = st.sidebar.checkbox('Alcoholic')

sport = st.sidebar.checkbox('Active Sport')'''


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
