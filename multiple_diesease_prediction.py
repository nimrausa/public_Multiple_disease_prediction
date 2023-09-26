# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 21:06:41 2022

@author: nisiddiqui
"""

import pickle #load saved models
import streamlit as st  #for web page
import sys

sys.path.insert(1, "streamlit_option_menu")
from streamlit_option_menu import option_menu
import numpy as np


#loading the saved models
diabetes_model=pickle.load(open('diabetes_model.sav','rb'))
heart_disease_model=pickle.load(open('heart_disease_model.sav','rb'))
parkinsons_model=pickle.load(open('parkinsons_model.sav','rb'))




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
        Pregnancies = st.slider('Number of Pregnancies', min_value=0, max_value=17, value=0, key='pregnancies')
        
    
    # Glucose Level
    with col2:
        Glucose = st.slider('Glucose Level', min_value=70.0, max_value=140.0, value=100.0, step=0.1, key='glucose_level')

        more_glucose = {
            "Description": "The person's fasting blood sugar level (measured in mg/dL).",
            "Normal Value": "For a normal person, the typical fasting blood glucose level is around 70 to 100 mg/dL."
        }

        if st.button("More (Glucose)", key="more_glucose"):
            st.write(more_glucose)
    
    # Blood Pressure value
    with col3:
        BloodPressure = st.slider('Blood Pressure value', min_value=0.0, max_value=300.0, value=120.0, key='blood_pressure')
        more_blood_pressure = {
            "Description": "The person's blood pressure measurement (systolic/diastolic in mm Hg).",
            "Normal Value": "For a normal adult, the typical blood pressure reading is around 120/80 mm Hg."
        }
        if st.button("More (Blood Pressure)", key="more_blood_pressure"):
            st.write(more_blood_pressure)
    
    # Skin Thickness value
    with col1:
        SkinThickness = st.slider('Skin Thickness value', min_value=0.0, max_value=100.0, value=20.0, key='skin_thickness')
        more_skin_thickness = {
            "Description": "The thickness of the person's skinfold at a specific location (measured in mm).",
            "Normal Value": "For a normal person, the skin thickness at this location typically falls within a range of 10 to 30 mm."
        }
        if st.button("More (Skin Thickness)", key="more_skin_thickness"):
            st.write(more_skin_thickness)
    
    # Insulin Level
    with col2:
        Insulin = st.slider('Insulin Level', min_value=0.0, max_value=1000.0, value=150.0, key='insulin')

        more_insulin = {
            "Description": "The person's insulin level (measured in mu U/mL).",
            "Normal Value": "For a normal person without diabetes, the typical fasting insulin level falls within the range of 5 to 15 mu U/mL. "
        }
        if st.button("More (Insulin)", key="more_insulin"):
            st.write(more_insulin)
    
    # BMI value
    with col3:
        BMI = st.slider('BMI value', min_value=10.0, max_value=50.0, value=25.0, step=0.1, key='bmi')
        more_bmi = {
            "Description": "The Body Mass Index (BMI) is a measure of a person's body weight in relation to their height (kg/m^2).",
            "Normal Value": "Normal BMI values typically fall within the range of 18.5 to 24.9."
        }
        if st.button("More (BMI)", key="more_bmi"):
            st.write(more_bmi)
    
    # Diabetes Pedigree Function value
    with col1:
        DiabetesPedigreeFunction = st.slider('Diabetes Pedigree Function value', min_value=0.0, max_value=8.0, value=0.627, step=0.1, key='diabetes_pedigree_function')
        more_diabetes_pedigree = {
            "Description": "The Diabetes Pedigree Function measures the genetic predisposition of a person to diabetes.",
            "Normal Value": "For a normal person with no known genetic predisposition to diabetes, the Diabetes Pedigree Function value is typically low, often close to 0.0."

        }
        if st.button("More (Diabetes Pedigree Function)", key="more_diabetes_pedigree"):
            st.write(more_diabetes_pedigree)
    
    # Age of the Person
    with col2:
        Age = st.slider('Age of the Person', min_value=18.0, max_value=100.0, value=30.0, step=1.0, key='age')

        more_age = {
            "Description": "The age of the person in years.",
           
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
        age = st.slider('Age', min_value=0, max_value=100, value=40, key='age')


    with col2:
        sex = st.slider('Sex', min_value=0, max_value=1, value=1, key='sex')

        more_sex = {
        "Description": "The person's sex (1 = male; 0 = female).",
        
        }

        if st.button("More (Sex)", key="more_sex"):
            st.write(more_sex)

    with col3:
        cp = st.slider('Chest Pain types', min_value=0, max_value=3, value=1, key='cp')

        more_cp = {
        0: "Value 0 This value represents the absence of chest pain or discomfort. It indicates that the individual reports no chest pain symptoms.",
        1: "Value 1 This value typically represents mild or non-specific discomfort in the chest. It may include sensations such as minor discomfort, pressure, or a vague feeling of unease. This category is generally considered less severe.",
        2: "Value 2: The value 3 often represents intense or severe chest pain. It may indicate significant chest discomfort or pain, which is more likely to be associated with heart-related issues. This category can include symptoms such as severe chest pain, tightness, or a crushing sensation."
        }

        if st.button("More (Chest Pain Types)", key="more_cp"):
            st.write(more_cp)

    with col1:
        trestbps = st.slider('Resting Blood Pressure (mm Hg)', min_value=0, max_value=200, value=120, key='trestbps')

        more_trestbps = {
        "Description": "The person's resting blood pressure measured in mm Hg.",
        "Normal Value": "For a normal adult, the typical resting blood pressure reading is around 120/80 mm Hg."
        }
        if st.button("More (Resting Blood Pressure)", key="more_trestbps"):
            st.write(more_trestbps)

    with col2:
        chol = st.slider('Serum Cholesterol (mg/dL)', min_value=100, max_value=400, value=200, key='chol')

        more_chol = {
        "Description": "The person's serum cholesterol level measured in mg/dL.",
        "Normal Value": "For a normal person, the typical serum cholesterol level is around 150 to 200 mg/dL."
        }

        if st.button("More (Serum Cholesterol)", key="more_chol"):
            st.write(more_chol)

    with col3:
        fbs = st.slider('Fasting Blood Sugar (>120 mg/dL)', min_value=0, max_value=1, value=0, key='fbs')

        more_fbs = {
        "Description": "Whether the person has fasting blood sugar greater than 120 mg/dL (1 = true; 0 = false).",
        "Normal Value": "A normal fasting blood sugar level is typically below 100 mg/dL. A value of 0 (false) in this field indicates a normal fasting blood sugar level."
        }

        if st.button("More (Fasting Blood Sugar)", key="more_fbs"):
            st.write(more_fbs)

    with col1:
        restecg = st.slider('Resting Electrocardiographic Results', min_value=0, max_value=2, value=0, key='restecg')

        more_restecg = {
        0: "Value 0 indicates a normal resting electrocardiographic result.",
        1: "Value 1 suggests an abnormal resting electrocardiographic result, which could indicate possible heart-related issues.",
        2: "Value 2 indicates a result that is probably not relevant for this dataset."
        }

        if st.button("More (Resting Electrocardiographic Results)", key="more_restecg"):
            st.write(more_restecg)

    with col2:
        thalach = st.slider('Maximum Heart Rate Achieved', min_value=50, max_value=220, value=150, key='thalach')

        more_thalach = {
            "Description": "The maximum heart rate achieved during exercise.",
            "Normal Value": "The normal maximum heart rate for adults can vary but is often estimated as 220 minus your age."
        }
        if st.button("More (Maximum Heart Rate Achieved)", key="more_thalach"):
            st.write(more_thalach)

    with col3:
        exang = st.slider('Exercise Induced Angina', min_value=0, max_value=1, value=0, key='exang')

        more_exang = {
            "Description": "Whether exercise induced angina is present (1 = yes; 0 = no).",
            "Normal Value": "A normal value of 0 (no) indicates the absence of exercise-induced angina, which is a typical result for a healthy individual."
        }

        if st.button("More (Exercise Induced Angina)", key="more_exang"):
            st.write(more_exang)

    with col1:
        oldpeak = st.slider('ST Depression Induced by Exercise', min_value=0.0, max_value=6.2, value=0.0, step=0.1, key='oldpeak')

        more_oldpeak = {
            "Description": "ST depression induced by exercise relative to rest (measured in mm).",
            "Normal Value": "The normal range for ST depression values can vary. It's important to consult with a healthcare professional for interpretation in a clinical context."
        }

        if st.button("More (ST Depression)", key="more_oldpeak"):
            st.write(more_oldpeak)

    with col2:
        slope = st.slider('Slope of Peak Exercise ST Segment', min_value=0, max_value=2, value=1, key='slope')

        more_slope = {
            0: "Value 0 (Upsloping): This value represents an ECG (electrocardiogram) pattern where the ST segment of the ECG tracing slopes in an upward direction during the peak of exercise. An upsloping ST segment is typically considered normal and may indicate a lower likelihood of coronary artery disease (CAD). It's often seen in individuals with a healthy heart.",
            1: "Value 1 (Flat): A value of 1 indicates a flat or horizontal ST segment during the peak of exercise. A flat ST segment can be suggestive of certain heart abnormalities or ischemia (reduced blood flow to the heart muscle). It may warrant further investigation and medical evaluation.",
            2: "Value 2 (Downsloping): A value of 2 means that the ST segment of the ECG tracing slopes in a downward direction during the peak of exercise. A downsloping ST segment is more strongly associated with ischemia and can be an indicator of reduced blood flow to the heart muscle during physical exertion. It's often considered abnormal and may warrant medical attention."
        }

        if st.button("More (Slope of Peak Exercise ST Segment)", key="more_slope"):
            st.write(more_slope)

    with col3:
        ca = st.slider('Major Vessels Colored by Fluoroscopy', min_value=0, max_value=3, value=0, key='ca')

        more_ca = {
            0: "Value 0 means that there are no significant blockages in the major coronary arteries, indicating good blood flow to the heart.",
            1: "Value 1 suggests that one major coronary artery shows significant blockage or narrowing, indicating some level of blockage.",
            2: "Value 2 indicates that two major coronary arteries are affected by significant blockages or narrowing, indicating a moderate level of blockage.",
            3: "Value 3 may indicate that three major coronary arteries have significant blockages, suggesting a higher level of blockage and potentially more severe heart disease."
        }

        if st.button("More (Major Vessels Colored by Fluoroscopy)", key="more_ca"):
            st.write(more_ca)

    with col1:
        thal = st.slider('Thal (0 = Normal, 1 = Fixed Defect, 2 = Reversible Defect)', min_value=0, max_value=2, value=0, key='thal')

        more_thal = {
            0: "Value 0 indicates a normal thalassemia test result.",
            1: "Value 1 suggests a fixed defect in the thalassemia test, which can be associated with heart issues.",
            2: "Value 2 indicates a reversible defect in the thalassemia test, which may also be related to heart problems."
        }

        if st.button("More (Thal)", key="more_thal"):
            st.write(more_thal)
            
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        a=np.array([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]], dtype=float)
        heart_prediction = heart_disease_model.predict(a)  
                        
        b = np.array( heart_prediction, dtype=float) #  convert using numpy
        if (b[0] == 1):
          heart_diagnosis = 'The person does not have any heart disease'
        else:
          heart_diagnosis = 'The person is having heart disease'
        
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