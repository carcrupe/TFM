#!/usr/bin/env python
# coding: utf-8

# In[3]:

import streamlit as st
import numpy as np
import pandas as pd
import time
import pickle

# In[ ]:
st.title('Stroke Predictor')

df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})
df

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    st.line_chart(chart_data)
    
option = st.sidebar.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected:', option



'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done!'