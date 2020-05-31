#!/usr/bin/env python
# coding: utf-8

# In[3]:

import streamlit as st
import numpy as np
import pandas as pd
import pickle
from PIL import Image


# In[ ]:
st.title('Get to know your heart')
st.subheader('Set your parameters and click predict')

clf_loaded = pickle.load(open("best.model","rb"))

data = pd.read_csv("stroke_data_for_modeling.csv", sep=';')

#st.write(data.head(5))

st.sidebar.title('Set parameters')

#Initial paramenters of a healthy patient
ageInit= 45
heightInit= 165
weightInit= 65
sPressureInit= 120
dPressureInit= 80
cholesterolInit= 1


age = st.sidebar.number_input('Age', value=ageInit)

sexDict = {'Male':1, 'Female':2}
sex = st.sidebar.selectbox('Sex', ['Male','Female'])
sex = sexDict[sex]

height = st.sidebar.number_input('Height (cm)', value=heightInit)

weight = st.sidebar.number_input('Weight (Kg)', value=weightInit)

sPressure = st.sidebar.number_input('Systolic Pressure',value=sPressureInit)

dPressure = st.sidebar.number_input('Diastolic Pressure',value=dPressureInit)

cholesterol = st.sidebar.number_input('Cholresterol 1 = low, 2 = high, 3 = very high', value=cholesterolInit)

diabetes = st.sidebar.checkbox('Diabetes')

smoker = st.sidebar.checkbox('Smoker')

alcoholic = st.sidebar.checkbox('Alcoholic')

sport = st.sidebar.checkbox('Active Sport')


inputData = [age, sex, height, weight, sPressure,
       dPressure, cholesterol, diabetes, smoker, alcoholic,
       sport]

#image = Image.open('safeHeart.png')
#imageLocation = st.empty()
#imageLocation.image(image)

if st.button('Predict'):
    pred = clf_loaded.predict([inputData])
    if(pred == 0):
        'You are safe!'
    else:
        'You should see the doctor for further tests'
#        imageLocation.image(image)

