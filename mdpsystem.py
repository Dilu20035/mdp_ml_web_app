# -*- coding: utf-8 -*-

import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import time
from PIL import Image


# loading the saved models

diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))

parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))

covid_model = pickle.load(open("covid.pkl", 'rb'))

st.set_page_config(
    page_title="MDP-Detector",
    page_icon=":Shark:",
    layout="centered",
    initial_sidebar_state="auto",
)

# Set the theme colors
st.markdown(
    """
    <style>
    :root {
        --primary-color: #B21F33;
        --background-color: #002b36;
        --secondary-background-color: #586e75;
        --text-color: #fafafa;
        --font: sans-serif;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# sidebar for navigation
with st.sidebar:
    st.title("Hello, Welcome!!")
    selected = option_menu('Multiple Disease Detection System',     
                          ['Home',
                              'Diabetes Prediction',
                           'Heart Disease Prediction',
                           'Parkinsons Prediction',
                           'Covid Prediction',
                          'About'],
                          icons=['house-fill','activity','heart','person','asterisk','bi-info-circle-fill'],
                          default_index=0)
    
#Home page
st.markdown("<h1 style='text-align: center; font: bold; color: 0e1117;'>MULTIPLE DISEASE DETECTOR</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: grey;'>[Don’t let diseases catch you off guard]</h3>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center;'>                           </h1>", unsafe_allow_html=True)
    

if (selected == 'Home'):
    st.title('  ')
    image = Image.open("image.png")
    st.image(image, use_column_width=True)
    st.markdown("""
        ## Diabetes:

        - Diabetes, also known as diabetes mellitus, is a chronic medical condition that occurs when the body is unable to properly regulate blood sugar levels. Blood sugar, or glucose, is the primary source of energy for the body's cells and tissues. However, in people with diabetes, the body cannot use glucose effectively, leading to high blood sugar levels.
        - Diabetes can lead to a variety of complications, including damage to the eyes, kidneys, nerves, and cardiovascular system. It is therefore important for people with diabetes to manage their blood sugar levels and receive regular medical check-ups to prevent or manage any complications.
        - Symptoms of diabetes include increased thirst and hunger, frequent urination, fatigue, blurred vision, and slow healing of cuts and bruises. However, some people with diabetes may not experience any symptoms at all, which is why regular screening is important, especially for individuals with risk factors such as a family history of diabetes, obesity, or a sedentary lifestyle.
        - In conclusion, diabetes is a chronic medical condition that affects the body's ability to regulate blood sugar levels. It can lead to a variety of complications, but with proper management and medical care, people with diabetes can live full and healthy lives.

        ## Heart Disease:

        - Heart disease, also known as cardiovascular disease, is a group of conditions that affect the heart and blood vessels. It is one of the leading causes of death worldwide and includes conditions such as coronary artery disease, heart failure, and arrhythmias.
        - Heart failure occurs when the heart is unable to pump blood effectively, leading to symptoms such as shortness of breath, fatigue, and swelling in the legs and ankles. Arrhythmias are abnormal heart rhythms that can cause the heart to beat too fast, too slow, or irregularly.
        - Symptoms of heart disease can vary depending on the type of condition but may include chest pain or discomfort, shortness of breath, fatigue, dizziness, nausea, and sweating. It is important to seek medical attention if you experience any of these symptoms.
        - In conclusion, heart disease is a group of conditions that affect the heart and blood vessels and can lead to serious complications. Lifestyle changes and medical care can help prevent and manage heart disease, but it is important to be aware of the symptoms and seek medical attention if necessary.
        
        ## Parkinson's Disease:

        - Parkinson's disease is a progressive neurological disorder that affects movement. It occurs when the brain cells that produce the neurotransmitter dopamine are damaged or destroyed, leading to a decrease in dopamine levels. Dopamine is a chemical messenger that helps to control movement and coordination.
        - The symptoms of Parkinson's disease can vary from person to person but typically include tremors, stiffness, slowness of movement, and difficulty with balance and coordination. As the disease progresses, it can also cause cognitive and behavioral changes, including memory loss and depression.
        - While the cause of Parkinson's disease is not fully understood, it is believed to involve a combination of genetic and environmental factors. There is currently no cure for Parkinson's disease, but medications and therapies can help to manage symptoms and improve quality of life. These may include dopamine replacement therapy, physical therapy, and deep brain stimulation.
        - In conclusion, Parkinson's disease is a progressive neurological disorder that affects movement and coordination. While there is no cure for the disease, medications and therapies can help to manage symptoms and improve quality of life. Support and resources are available to help individuals and their families cope with the challenges of living with Parkinson's disease.

        ## Covid Disease:

        - COVID-19, formally known as Coronavirus Disease 2019, is a highly contagious respiratory illness caused by the novel coronavirus SARS-CoV-2, which was first identified in Wuhan, China, in late 2019. This disease quickly spread globally, resulting in a pandemic that continues to affect populations worldwide.
        - The symptoms of COVID-19 can range from mild to severe and may include fever, cough, shortness of breath, fatigue, body aches, sore throat, loss of taste or smell, and gastrointestinal symptoms. Severe cases can lead to pneumonia, acute respiratory distress syndrome (ARDS), and even death, particularly among older adults and individuals with underlying health conditions.
        - The primary mode of transmission for COVID-19 is through respiratory droplets generated when an infected person coughs, sneezes, talks, or even breathes. The virus can also spread through contact with contaminated surfaces and subsequent hand-to-face contact. Understanding these modes of transmission has led to the widespread adoption of preventive measures such as mask-wearing, social distancing, frequent handwashing, and vaccination campaigns to curb the spread of the virus.
        - In conclusion, COVID-19 has presented an unprecedented global challenge, impacting public health, economies, and daily life. While vaccines have emerged as a critical tool in controlling the pandemic, ongoing research and vigilance in adhering to public health guidelines remain crucial in our efforts to manage and eventually overcome this disease. COVID-19 has highlighted the importance of global collaboration in the face of health crises and serves as a reminder of the need for preparedness in the face of emerging infectious diseases.
        """)

    

# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction using ML')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose Level')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    
    with col2:
        Insulin = st.text_input('Insulin Level')
    
    with col3:
        BMI = st.text_input('BMI value')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
    with col2:
        Age = st.text_input('Age of the Person')
    
    
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
        age = st.text_input('Age')
        
    with col2:
        sex = st.text_input('Sex')
        
    with col3:
        cp = st.text_input('Chest Pain types')
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
        
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
        
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
        
    with col3:
        exang = st.text_input('Exercise Induced Angina')
        
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
        
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
        
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
        
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)
        
    
    

# Parkinson's Prediction Page
if (selected == "Parkinsons Prediction"):
    
    # page title
    st.title("Parkinson's Disease Prediction using ML")
    
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
        
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
        
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
        
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
        
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
        
    with col1:
        RAP = st.text_input('MDVP:RAP')
        
    with col2:
        PPQ = st.text_input('MDVP:PPQ')
        
    with col3:
        DDP = st.text_input('Jitter:DDP')
        
    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')
        
    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
        
    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')
        
    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')
        
    with col3:
        APQ = st.text_input('MDVP:APQ')
        
    with col4:
        DDA = st.text_input('Shimmer:DDA')
        
    with col5:
        NHR = st.text_input('NHR')
        
    with col1:
        HNR = st.text_input('HNR')
        
    with col2:
        RPDE = st.text_input('RPDE')
        
    with col3:
        DFA = st.text_input('DFA')
        
    with col4:
        spread1 = st.text_input('spread1')
        
    with col5:
        spread2 = st.text_input('spread2')
        
    with col1:
        D2 = st.text_input('D2')
        
    with col2:
        PPE = st.text_input('PPE')
        
    
    
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

# CORONA Prediction Page

st.title(' ')
if (selected == 'Covid Prediction'):
    
    # page title
    st.title('Covid Prediction Using ML')
    
    
    # getting the input data from the user
    col1, col2= st.columns(2)
    
    with col1:
        cough = st.selectbox( 'Cough : 0 FOR NO, 1 FOR YES ',
          ('0', '1'))
    
    with col2:
        fever = st.selectbox( 'Fever: 0 FOR NO, 1 FOR YES',
          ('0', '1'))
    
    with col1:
       sore_throat =st.selectbox( 'Sore throat: 0 FOR NO, 1 FOR YES',
          ('0', '1'))
    
    with col2:
        shortness_of_breath = st.selectbox( 'Shortness of breath: 0 FOR NO, 1 FOR YES',
          ('0', '1'))
    
    with col1:
        head_ache = st.selectbox( 'Head ache: 0 FOR NO, 1 FOR YES',
          ('0', '1'))
    
    with col2:
        age_60_and_above = st.selectbox( 'Age 60 and above: 0 FOR NO, 1 FOR YES',
          ('0', '1'))
    
    with col1:
        gender = st.selectbox( 'Gender: 0 FOR M, 1 FOR F',
          ('0', '1'))
    
    with col2:
        test_indication = st.selectbox( 'Test indication: 0 FOR ABROAD, 1 FOR CONTACT, 2 FOR OTHER',
          ('0', '1','2'))
    
    
    # code for Prediction
    covid_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Corona Test Result'):
        Covid_Prediction = covid_model.predict([[cough,fever,sore_throat,shortness_of_breath,head_ache,age_60_and_above,gender,test_indication]])
        
        if (Covid_Prediction[0] == 1):
          st.error('The person has covid')
        else:
          st.success('The person does not have covid')


    
if (selected == 'About'):
    st.title("About")
    st.markdown("""
    - Our project, titled **'Multiple Disease Prediction System,'** is a machine learning-based system designed to predict diseases such as diabetes, heart disease, and Parkinson's disease. To achieve this, we employed various algorithms, including K-Nearest Neighbors (KNN), Random Forest, Naive Bayes, Logistic Regression, and Support Vector Machines (SVM), for classification. These algorithms were utilized to predict the disease based on the available dataset.
    - The aim of our project is to help individuals predict diseases with accuracy, which can enable them to take necessary precautions and reduce the risks of contracting such diseases. We developed the project for learning purposes, with the aim of improving it further in the future.
    - To make our project accessible and user-friendly, we deployed it using Streamlit, an open-source app framework used for building web applications. This deployment enables individuals to use our system with ease and access the predictions on the go.
    - In conclusion, our project is an innovative machine learning-based system designed to predict multiple diseases with high accuracy using various algorithms. With its deployment on Streamlit, individuals can access the system easily and use it to predict diseases, which can help them take necessary precautions and reduce the risks of contracting such diseases.
      """)
    
        
    


