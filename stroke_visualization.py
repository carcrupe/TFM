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

cholesterolDict = {'Low: <200 mg/dL':1, 'High: 200-240 mg/dL':2, 'Very high: >240 mg/dL':3}
cholesterol = st.sidebar.selectbox('Cholresterol', ['Low: <200 mg/dL', 'High: 200-240 mg/dL', 'Very high: >240 mg/dL'])
cholesterol = cholesterolDict[cholesterol]

diabetes = st.sidebar.checkbox('Diabetes')

smoker = st.sidebar.checkbox('Smoker')

alcoholic = st.sidebar.checkbox('Alcoholic')

sport = st.sidebar.checkbox('Active Sport')


inputData = [age, sex, height, weight, sPressure,
       dPressure, cholesterol, diabetes, smoker, alcoholic,
       sport]
columns=['Age','Sex','Height','Weight','SystolicPressure',
'DiastolicPressure','Diabetes','Cholesterol','Smoker','Alcoholic',
'ActiveSport','Target']

data_original = pd.read_csv("stroke_data_for_modeling.csv", sep=';', usecols=columns)

donated_data= data_original

donated_data.to_csv('donated_data.csv', sep=',')

if st.button('Predict'):

    pred = clf_loaded.predict([inputData])
    if(pred == 0):
        'Your heart is safe!'
    else:
        'Your should take care of your heart, go see the doctor for further tests'
#        imageLocation.image(image)

st.title('Donate your heart')
st.subheader('Help us improve the predictor')

st.write('Your data is really appreciated. Sending your parameters, you improve stroke predictions and save lives.') 


previousStroke = st.checkbox('Did you have a stroke episode with these data?')

#if the user selects the previousstroke checkbox, the target is set to 1. The donated data would be related to a stroke event.
if st.button('Donate'):

    inputData.append(previousStroke)
    st.write(len(inputData))
    donated_data = pd.read_csv('donated_data.csv',sep=',', usecols=columns)

    donated_data.loc[len(donated_data)]= inputData
    donated_data.loc[len(donated_data)+1]= inputData
    st.write(len(donated_data))
    donated_data.to_csv('donated_data.csv', sep=',')
    st.write(donated_data.tail(5))

    

