#Streamlit WEB UI for Heart Disease Prediction

import streamlit as st
import pandas as pd
import numpy as np
import joblib as jb
import os


#loading the saved model
model = jb.load('../notebook/KNN-Heart-Disease-predictor.joblib')


# Encoding mapping
encode_map ={
    'Gender': {'Female': 0, 'Male': 1},
    'Chest Pain': {'Typical Angina': 0, 'Atypical Angina': 1, 'Non-Anginal Pain': 2, 'Asymptomatic': 3},
    'Resting_Electrocardiographic': {'Normal': 0, 'Abnormal': 1, 'Left Ventricular Hypertrophy': 2},
    'Exercise_Angina': {'No': 0, 'Yes': 1},
    'Slope': {'Downsloping': 0, 'Upsloping': 1, 'Flat': 2},
    'Thalassemia': {'Reversible Defect': 1, 'Fixed Defect': 2, 'Normal': 3},
}


#Home Page

def home():
    st.markdown(
        """ 
        <style>
           
           .heading{
                color: #8e0201;
                font-size: 2.5rem;
                margin-bottom: 1.2rem;
              
           }
           .title{
                color: #8e0201;
                font-size: 2.2rem;
                margin-bottom: 1.2rem;
            }

            .content {
                font-size: 1.2rem;
                margin-bottom: 20px;
                color: #8e0201;
            }
            .author{
                
                font-size: 1.1rem;
                color: #8e0201;
                font-style:italic;
            }
        </style>
        """, unsafe_allow_html=True
    )
    st.title('Home Page' )
    st.markdown('<p class="title">Welcome to the Heart Disease Prediction Web App!</p>', unsafe_allow_html=True)
    st.markdown('<p class="author">Developed by Oluwuyi Olumide!</p>', unsafe_allow_html=True)
    st.markdown('<p class="content">Please use the side navigation bar to navigate to different pages.</p>', unsafe_allow_html=True)

# Prediction page
def prediction():
    st.title('Heart Disease Prediction')
    st.sidebar.title('User Input')


#createing the streamlit web app
def main():
    #add  side navigation bar
    st.sidebar.title('Navigation')
    page = st.sidebar.radio('Go to', ['Home', 'Prediction'])

    if page == 'Home':
        home()
    elif page == 'Prediction':
        prediction()


#run tha app

if __name__ == '__main__':
    main()

