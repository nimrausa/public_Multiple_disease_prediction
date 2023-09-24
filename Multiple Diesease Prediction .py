# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 21:06:41 2022

@author: nisiddiqui
"""

import pickle #load saved models
import streamlit as st  #for web page

from streamlit_option_menu import option_menu
import numpy as np


#loading the saved models
diabetes_model=pickle.load(open('C:/Users/nimra/OneDrive/Desktop/MachineLearning/saved dieases/diabetes_model.sav','rb'))
heart_disease_model=pickle.load(open('C:/Users/nimra/OneDrive/Desktop/MachineLearning/saved dieases/heart_disease_model.sav','rb'))
parkinsons_model=pickle.load(open('C:/Users/nimra/OneDrive/Desktop/MachineLearning/saved dieases/parkinsons_model.sav','rb'))




# loading the saved models




# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                          
                          ['Diabetes Prediction',
                           'Heart Disease Prediction',
                           'Parkinsons Prediction'],
                          icons=['activity','heart','person'],
                          default_index=0)
    
    
# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction using ML')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    

    # Number of Pregnancies
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies', placeholder='Eg= 1, 2, 3...')
        more_pregnancies = {
            "Description": "The number of times the person has been pregnant.",
            "Range": "The range for this field depends on the dataset, but typically it is a positive integer."
        }
        if st.button("More (Pregnancies)", key="more_pregnancies"):
            st.write(more_pregnancies)
    
    # Glucose Level
    with col2:
        Glucose = st.text_input('Glucose Level', placeholder='Eg= 1, 2, 3...')
        more_glucose = {
            "Description": "The person's fasting blood sugar level (measured in mg/dL).",
            "Range": "The range for this field typically falls within a normal blood sugar level, around 70-140 mg/dL."
        }
        if st.button("More (Glucose)", key="more_glucose"):
            st.write(more_glucose)
    
    # Blood Pressure value
    with col3:
        BloodPressure = st.text_input('Blood Pressure value', placeholder='Eg= 1, 2, 3...')
        more_blood_pressure = {
            "Description": "The person's blood pressure measurement (systolic/diastolic in mm Hg).",
            "Range": "A normal blood pressure range is around 90/60 mm Hg to 120/80 mm Hg."
        }
        if st.button("More (Blood Pressure)", key="more_blood_pressure"):
            st.write(more_blood_pressure)
    
    # Skin Thickness value
    with col1:
        SkinThickness = st.text_input('Skin Thickness value', placeholder='Eg= 1, 2, 3...')
        more_skin_thickness = {
            "Description": "The thickness of the person's skinfold at a specific location (measured in mm).",
            "Range": "Skin thickness values can vary but are generally positive numbers."
        }
        if st.button("More (Skin Thickness)", key="more_skin_thickness"):
            st.write(more_skin_thickness)
    
    # Insulin Level
    with col2:
        Insulin = st.text_input('Insulin Level', placeholder='Eg= 1, 2, 3...')
        more_insulin = {
            "Description": "The person's insulin level (measured in mu U/mL).",
            "Range": "Insulin levels can vary, but they are typically within the range of 2-30 mu U/mL for fasting insulin."
        }
        if st.button("More (Insulin)", key="more_insulin"):
            st.write(more_insulin)
    
    # BMI value
    with col3:
        BMI = st.text_input('BMI value', placeholder='Eg= 1, 2, 3...')
        more_bmi = {
            "Description": "The Body Mass Index (BMI) is a measure of a person's body weight in relation to their height (kg/m^2).",
            "Range": "Normal BMI values typically fall within the range of 18.5 to 24.9."
        }
        if st.button("More (BMI)", key="more_bmi"):
            st.write(more_bmi)
    
    # Diabetes Pedigree Function value
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value', placeholder='Eg= 1, 2, 3...')
        more_diabetes_pedigree = {
            "Description": "The Diabetes Pedigree Function measures the genetic predisposition of a person to diabetes.",
            "Range": "Diabetes Pedigree Function values can vary but are generally positive numbers."
        }
        if st.button("More (Diabetes Pedigree Function)", key="more_diabetes_pedigree"):
            st.write(more_diabetes_pedigree)
    
    # Age of the Person
    with col2:
        Age = st.text_input('Age of the Person', placeholder='Eg= 1, 2, 3...')
        more_age = {
            "Description": "The age of the person in years.",
            "Range": "Age is a positive integer and should be within a reasonable human lifespan range."
        }
        if st.button("More (Age)", key="more_age"):
            st.write(more_age)
    
        
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'The person is diabetic'
        else:
          diab_diagnosis = 'The person is not diabetic'
        
    st.success(diab_diagnosis)




# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age', placeholder='Age in years')
        
    with col2:
        sex = st.text_input('Sex', placeholder='1 = male; 0 = female')
        
    with col3:
        cp = st.text_input('Chest Pain types', placeholder='Eg= 0,1,2 or 3')
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure (in mm Hg )', placeholder='range varies from 94 to 200')
        
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl', placeholder='range varies from 126 to 564')
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl', placeholder='1 = true; 0 = false.')
        
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results', placeholder='values 0,1,2')
        
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved', placeholder='range varies from 71 to 202')
        
    with col3:
        exang = st.text_input('Exercise Induced Angina', placeholder='1 = yes; 0 = no')
        
    with col1:
        oldpeak = st.text_input('oldpeak-ST depression induced by exercise relative to rest', placeholder='range varies from 0 to 6.2')
        
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment(ECG waveform during physical exercise).', placeholder='0:upsloping,1:Flat,2:Downsloping')
        
    with col3:
        # Description
       

        ca = st.text_input('Major vessels colored by flourosopy', placeholder='Enter a number from 0 to 3')
        more_info = {
    0: "Value 0 means that there are no significant blockages in the major coronary arteries, indicating good blood flow to the heart. Additional information can be added here.",
    1: "Value 1 suggests that one major coronary artery shows significant blockage or narrowing, indicating some level of blockage. Additional information can be added here.",
    2: "Value 2 indicates that two major coronary arteries are affected by significant blockages or narrowing, indicating a moderate level of blockage. Additional information can be added here."
}
        if st.button("More"):
            st.write(more_info)
  
    
                
        
    with col1:
        thal = st.text_input('Thal: 0 = normal; 1 = fixed defect; 2 = reversable defect', placeholder='Eg= 0,1, or 2')
        
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        a=np.array([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]], dtype=float)
        heart_prediction = heart_disease_model.predict(a)  
                        
        b = np.array( heart_prediction, dtype=float) #  convert using numpy
        if (b[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)
        
    
    

# Parkinson's Prediction Page
if (selected == "Parkinsons Prediction"):
    
    # page title
    st.title("Parkinson's Disease Prediction using ML")
    
    col1, col2, col3 = st.columns(3)  
    
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)- Average vocal fundamental frequency (fo):', placeholder='Eg= 100, 120, 140...')
        more_fo = {
    "Range: Typically, the fundamental frequency for a human voice would fall within the range of 50 Hz to 300 Hz."
}
        if st.button("More (fo)",key="more_fo"):
            st.write(more_fo)
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)-Maximum vocal fundamental frequency (fhi):', placeholder= 'Eg= 150, 160, 170...')
        more_fhi = {
    "Range: This value is expected to be higher than the average fundamental frequency, so a typical range might be 80 Hz to 350 Hz."
}
        if st.button("More (Fhi)", key="more_fhi"):
            st.write(more_fhi)
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)-Minimum vocal fundamental frequency (flo):', placeholder='Eg= 80, 90, 100..')
        more_flo = {
    "Range: This value is expected to be lower than the average fundamental frequency, so a typical range might be 40 Hz to 150 Hz.."
}
        if st.button("More (flo)", key="more_flo"):
            st.write(more_flo)
    with col1:
        Jitter_percent = st.text_input('MDVP:Jitter(%)-Measures of variation in fundamental frequency  (Jitter_percent):', placeholder='Eg= 0.1, 0.2, 0.3...')
        more_Jitter_percent = {
    "Range: Jitter percentage is typically expressed as a decimal fraction, so it should be between 0 and 1"
}
        if st.button("More (Jitter_percent)",  key="more_Jitter_percent"):
            st.write(more_Jitter_percent)
    with col2:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)-Measures of variation in fundamental frequency (Jitter_Abs):', placeholder='Eg= 0.001, 0.002, 0.003...')
        more_Jitter_Abs = {
    "Range: Jitter absolute values can vary but are generally small, typically below 0.01.1"
}
        if st.button("More (Jitter_Abs)", key="more_Jitter_Abs"):
            st.write(more_Jitter_Abs)
    with col3:
        RAP = st.text_input('MDVP:RAP- MDVP relative amplitude perturbation (RAP)', placeholder='Eg= 0.001, 0.002, 0.003...')
        more_RAP = {
    "Range: Similar to Jitter absolute values, RAP values are generally small."
}
        if st.button("More RAP",key="RAP"):
            st.write(RAP)
    with col1:
        PPQ = st.text_input('MDVP:PPQ- MDVP five-point period perturbation quotient (PPQ):', placeholder='Eg= 0.001, 0.002, 0.003...')
        
    with col2:
        DDP = st.text_input('Jitter:DDP- Average absolute difference of differences between jitter cycles', placeholder='Eg= 1,2,3....')
       
      
    with col3:
        Shimmer = st.text_input('MDVP:Shimmer - Measures of variation in amplitude', placeholder='Eg= 0.1, 0.2, 0.3...')
        more_shimmer = {
        "Description": "Shimmer is a measure of variation in amplitude. It represents the variability in the amplitude of vocal fold vibrations.",
        "Range": "Shimmer values are typically expressed as a decimal fraction, so it should be between 0 and 1."
}
        if st.button("More (Shimmer)",key="more_shimmer"):
            st.write(more_shimmer)

    with col1:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB) - Measures of variation in amplitude IN dB', placeholder='Eg= 1, 2, 3...')
        more_shimmer_db = {
            "Description": "Shimmer (dB) measures the variation in amplitude in decibels (dB). It is another way to quantify amplitude variation.",
            "Range": "Shimmer (dB) values can vary but are generally small and positive numbers."
}
        if st.button("More (Shimmer dB)",key="more_shimmer_db"):
            st.write(more_shimmer_db)
    
    with col2:
        APQ3 = st.text_input('Shimmer:APQ3 - Measures of variation in amplitude (Three-point amplitude perturbation quotient)', placeholder='Eg= 1, 2, 3...')
        more_apq3 = {
            "Description": "APQ3 is a measure of amplitude perturbation. It quantifies amplitude variations using a three-point method.",
            "Range": "APQ3 values can vary but are generally positive numbers."
}
        if st.button("More (APQ3)", key="more_apq3"):
            st.write(more_apq3)
    
    
            
    with col3:
        APQ5 = st.text_input('Shimmer:APQ5 - Measures of variation in amplitude (Five-point amplitude perturbation quotient)', placeholder='Eg= 1, 2, 3...')
        more_apq5 = {
            "Description": "APQ5 is another measure of amplitude perturbation, using a five-point method to quantify amplitude variations.",
            "Range": "APQ5 values can vary but are generally positive numbers."
}
        if st.button("More (APQ5)", key="more_apq5"):
            st.write(more_apq5)
    
    with col1:
        APQ = st.text_input('MDVP:APQ - Measures of variation in amplitude (MDVP 11-point amplitude perturbation quotient)', placeholder='Eg= 1, 2, 3...')
        more_apq = {
            "Description": "MDVP:APQ is a more comprehensive measure of amplitude perturbation, using an 11-point method to quantify amplitude variations.",
            "Range": "MDVP:APQ values can vary but are generally positive numbers."
}
        if st.button("More (MDVP:APQ)", key="more_apq"):
            st.write(more_apq)
    
    with col2:
        DDA = st.text_input('Shimmer:DDA - Measures of Average absolute differences between the amplitudes of consecutive periods', placeholder='Eg= 1, 2, 3...')
        more_dda = {
            "Description": "DDA measures the average absolute differences between the amplitudes of consecutive periods in the voice signal.",
            "Range": "DDA values can vary but are generally positive numbers."
}
        if st.button("More (Shimmer:DDA)", key="more_dda"):
            st.write(more_dda)
    
    with col3:
        NHR = st.text_input('NHR (Noise-to-harmonics ratio) - Measures of the ratio of noise to tonal components in the voice', placeholder='Eg= 1, 2, 3...')
        more_nhr = {
            "Description": "NHR quantifies the ratio of noise to tonal components in the voice signal. It helps assess the noisiness of the voice.",
            "Range": "NHR values can vary but are generally positive numbers."
}
        if st.button("More (NHR)",  key="more_nhr"):
            st.write(more_nhr)
    
    with col1:
        HNR = st.text_input('HNR (Harmonics-to-noise ratio) - Measures of the ratio of noise to tonal components in the voice', placeholder='Eg= 1, 2, 3...')
        more_hnr = {
            "Description": "HNR quantifies the ratio of harmonics to noise in the voice signal. Higher values indicate clearer tones.",
            "Range": "HNR values can vary but are generally positive numbers."
}
        if st.button("More (HNR)", key="more_hnr"):
            st.write(more_hnr)
            
    with col2:
        RPDE = st.text_input('RPDE - Recurrence period density entropy measure', placeholder='Eg= 0.1, 0.2, 0.3...')
        more_rpde = {
            "Description": "RPDE is a measure of recurrence period density entropy. It quantifies the irregularity of the time intervals between similar patterns in a signal.",
            "Range": "RPDE values can vary but are generally positive numbers."
}
        if st.button("More (RPDE)", key="more_rpde"):
            st.write(more_rpde)
    
    with col3:
        DFA = st.text_input('DFA - Signal fractal scaling exponent of detrended fluctuation analysis', placeholder='Eg= 0.1, 0.2, 0.3...')
        more_dfa = {
            "Description": "DFA measures the self-similarity or fractal scaling properties of a signal. It assesses the presence of long-range correlations.",
            "Range": "DFA values can vary, typically between 0 and 2."
}
        if st.button("More (DFA)", key="more_dfa"):
            st.write(more_dfa)
    
    with col1:
        spread1 = st.text_input('spread1 - Two nonlinear measures of fundamental', placeholder='Eg= 1, 2, 3...')
        more_spread1 = {
            "Description": "Spread1 includes two nonlinear measures related to fundamental frequency variation. It assesses the spread of the frequency distribution.",
            "Range": "Spread1 values can vary and depend on the specific measurement method."
}
        if st.button("More (spread1)", key="more_spread1"):
            st.write(more_spread1)
    
    with col2:
        spread2 = st.text_input('spread2 - Nonlinear measures of fundamental frequency variation', placeholder='Eg= 1, 2, 3...')
        more_spread2 = {
            "Description": "Spread2 includes nonlinear measures related to fundamental frequency variation. It assesses the spread of the frequency distribution.",
            "Range": "Spread2 values can vary and depend on the specific measurement method."
}
        if st.button("More (spread2)",  key="more_spread2"):
            st.write(more_spread2)
    
    with col3:
        D2 = st.text_input('D2 (Correlation dimension) - Nonlinear dynamical complexity measures', placeholder='Eg= 1, 2, 3...')
        more_d2 = {
            "Description": "D2, or Correlation dimension, is a measure of the nonlinear dynamical complexity of a system. It quantifies the complexity of attractors in a phase space.",
            "Range": "D2 values can vary but are generally positive numbers."
}
        if st.button("More (D2)",key="more_d2"):
            st.write(more_d2)
    
    with col1:
        PPE = st.text_input('PPE (Pitch period entropy) - Nonlinear measures of fundamental frequency variation', placeholder='Eg= 1, 2, 3...')
        more_ppe = {
            "Description": "PPE, or Pitch period entropy, measures the entropy of pitch periods in a speech signal. It quantifies the irregularity of pitch periods.",
            "Range": "PPE values can vary but are generally positive numbers."
}
        if st.button("More (PPE)",key="more_ppe"):
            st.write(more_ppe)

    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
        
        if (parkinsons_prediction[0] == 1):
          parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
          parkinsons_diagnosis = "The person does not have Parkinson's disease"
        
    st.success(parkinsons_diagnosis)