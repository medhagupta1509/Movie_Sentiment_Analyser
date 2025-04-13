#!/usr/bin/env python
# coding: utf-8

# In[1]:





# In[7]:


import pickle
import streamlit as st
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)


# In[8]:


# UI and prediction
st.title("🎬 Movie Review Sentiment Analyzer")
user_input = st.text_area("Enter your movie review:")

if st.button("Predict"):
    input_vector = vectorizer.transform([user_input])
    prediction = model.predict(input_vector)[0]

    if prediction == 1:
        st.success("😊 Positive Sentiment")
    else:
        st.error("☹️ Negative Sentiment")





# In[ ]:




