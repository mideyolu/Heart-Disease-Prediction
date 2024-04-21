import streamlit as st
import numpy as np
import joblib as jb

#encode mappings
encode_map ={
    'Gender': {'Female': 0, 'Male': 1},
    'Chest Pain': {'Typical Angina': 0, 'Atypical Angina': 1, 'Non-Anginal Pain': 2, 'Asymptomatic': 3},
    'Resting_Electrocardiographic': {'Normal': 0, 'Abnormal': 1, 'Left Ventricular Hypertrophy': 2},
    'Exercise_Angina': {'No': 0, 'Yes': 1},
    'Slope': {'Downsloping': 0, 'Upsloping': 1, 'Flat': 2},
    'Thalassemia': {'Reversible Defect': 1, 'Fixed Defect': 2, 'Normal': 3},
}

#loading the model
model = jb.load('../notebook/KNN_Heart_Disease_predictor.joblib')


#implementing the diagnosis
def diagnosis_heart_disease(age, gender, chest_pain, resting_bp, cholesterol, resting_electrocardiographic,
                            max_heart_rate, exercise_angina, oldpeak, slope, ca, thalassemia):
    gender = encode_map['Gender'][gender]
    chest_pain = encode_map['Chest Pain'][chest_pain]
    resting_electrocardiographic = encode_map['Resting_Electrocardiographic'][resting_electrocardiographic]
    exercise_angina = encode_map['Exercise_Angina'][exercise_angina]
    slope = encode_map['Slope'][slope]
    thalassemia = encode_map['Thalassemia'][thalassemia]

    input_data = np.array([[age, gender, chest_pain, resting_bp, cholesterol, resting_electrocardiographic,
                            max_heart_rate, exercise_angina, oldpeak, slope, ca, thalassemia]])
    prediction = model.predict(input_data)
    probability = round((model.predict_proba(input_data)[0][prediction[0]]) * 100 )
    return prediction[0], probability


st.markdown(
        """ 
        <style>
           
           .title{
                color: #8e0201;
                font-size: 2.4rem;
                margin-bottom: 1.2rem;
            }

            .content {
                font-size: 1.2rem;
                margin-bottom: 20px;
                color: #8e0201;
            }
        </style>
        """, unsafe_allow_html=True
    )


st.title('Prediction Page' )
st.markdown('<p class="title">Heart Disease Prediction</p>', unsafe_allow_html=True)

#input features
age =st.text_input('Age')
gender = st.selectbox('Gender', ['','Female', 'Male'])
chest_pain = st.selectbox('Chest Pain', ['','Typical Angina', 'Atypical Angina', 'Non-Anginal Pain', 'Asymptomatic'])
resting_bp = st.text_input('Resting Blood Pressure (mm Hg)')
cholesterol = st.text_input('Cholesterol (mg/dl)')
resting_electrocardiographic = st.selectbox('Resting Electrocardiographic', ['','Normal', 'Abnormal', 'Left Ventricular Hypertrophy'])
max_heart_rate = st.slider('Maximum Heart Rate', 60, 220, 100)
exercise_angina = st.selectbox('Exercise Induced Angina', ['','No', 'Yes'])
oldpeak = st.slider('ST Depression Induced by Exercise', 0.0, 6.2, 2.0)
slope = st.selectbox('Slope of Peak Exercise ST Segment', ['','Downsloping', 'Upsloping', 'Flat'])
ca = st.slider('Number of Major Vessels Colored by Fluoroscopy', 0, 3, 0)
thalassemia = st.selectbox('Thalassemia', ['','Reversible Defect', 'Fixed Defect', 'Normal'])

# Make prediction
if st.button('Predict'):
    prediction, probability = diagnosis_heart_disease(int(age), gender, chest_pain, int(resting_bp), int(cholesterol), resting_electrocardiographic,
                                        int(max_heart_rate), exercise_angina, oldpeak, slope, ca, thalassemia)
    if prediction == 0:
        st.success(f'The System Predicts: No Heart Disease Detected {probability}%')
    else:
        st.error(f'Heart Disease Detected {probability}%')
