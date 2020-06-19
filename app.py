# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 22:33:28 2020

@author: kolhe
"""

import pickle
import time
import pandas as pd
import numpy as np
import streamlit as st
import streamlit_theme as stt
from sklearn.linear_model import LogisticRegression

# load the model from disk
filename = 'log_model.sav'
model = pickle.load(open(filename, 'rb'))


questions = ["1) When we need it, we can take our discussions with my spouse from the beginning and correct it.",
"2) We don't have time at home as partners.",
"3) We are like two strangers who share the same environment at home rather than family.",
"4) I know how my spouse wants to be taken care of when she/he sick.",
"5) I feel aggressive when I argue with my spouse.",
"6) I'd rather stay silent than discuss with my spouse.",
"7) Even if I'm right in the discussion, I stay silent to hurt my spouse.",
"8) I wouldn't hesitate to tell my spouse about her/his inadequacy."]


hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

# title and subheader
st.title("Relationship Health Analyzer")
st.subheader("Note:  Do not rely on the results. Try to improve your relationship life.")
st.subheader("True love stories never have endings ...")


st.sidebar.header("About")
st.sidebar.text("Created by: Shivam Kolhe")
if(st.sidebar.button('Get the contact info')):
    st.sidebar.text("Email: kolhe.shivam17@gmail.com")
    st.sidebar.text("Linkedin: https://in.linkedin.com/in/shivamkolhe8")

    


info = """All responses are to be answered on a 5-point scale i.e. 
(0=Never, 1=Seldom, 2=Averagely, 3=Frequently, 4=Always)"""

st.warning(info)

response = {"Never": 0, "Seldom": 1, "Averagely": 2, "Frequently": 3, "Always": 4}

q1_text = st.info(questions[0])
q1_radio = st.radio("Select your response: ", tuple(response.keys()), key=0)
q1 = response[q1_radio]
print('q1', q1)

q2_text = st.info(questions[1])
q2_radio = st.radio("Select your response: ", tuple(response.keys()), key=1)
q2 = response[q2_radio]
print('q2', q2)

q3_text = st.info(questions[2])
q3_radio = st.radio("Select your response: ", tuple(response.keys()), key=2)
q3 = response[q3_radio]

q4_text = st.info(questions[3])
q4_radio = st.radio("Select your response: ", tuple(response.keys()), key=3)
q4 = response[q4_radio]

q5_text = st.info(questions[4])
q5_radio = st.radio("Select your response: ", tuple(response.keys()), key=4)
q5 = response[q5_radio]

q6_text = st.info(questions[5])
q6_radio = st.radio("Select your response: ", tuple(response.keys()), key=5)
q6 = response[q6_radio]

q7_text = st.info(questions[6])
q7_radio = st.radio("Select your response: ", tuple(response.keys()), key=6)
q7 = response[q7_radio]

q8_text = st.info(questions[7])
q8_radio = st.radio("Select your response: ", tuple(response.keys()), key=7)
q8 = response[q8_radio]


st.write("Click the button below to check your relationship health")
if(st.button("Check your relationship health")):
    result = model.predict_proba(np.array([[q1,q2,q3,q4,q5,q6,q7,q8]]))
    
    result = round(result[0][1] * 100, 2)
    
    if(result <= 5):
        st.success("There is a {}% chance that you will face problems in your relationship.".format(result))
        st.success("Wooohooo... You have a perfect relationship!!!")
        st.balloons()
        
    elif(result > 5 and result <=30):
        st.info("There is a {}% chance that you will face problems in your relationship.".format(result))
        st.info("You still have some time to repair the problems and make it a healthy relationship. Try to sort out the problems before its too late. Have a healthy conversation with your partner.")
        
    elif(result > 30 and result <=80):
        st.info("There is a {}% chance that you will face problems in your relationship.".format(result))
        st.info("You still have some time to repair the problems and make it a healthy relationship. Try to sort out the problems before its too late. Have a healthy conversation with your partner.")
        
    else:
        st.error("There is a {}% chance that you will face problems in your relationship.".format(result))
        st.info("You are in a terrible situation right now. Try to sort out the problems before its too late. Have a healthy conversation with your partner")

