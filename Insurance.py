import pickle
import numpy as np
import pandas as pd

# load the model from disk
loaded_model = pickle.load(open('insurance_RF.pkl', 'rb'))

import streamlit as st

# Creating the Titles and Image
st.title("Predict insurance charges")
st.header("Calculating the insurance charges that could be charged by an insurer based on a person's attributes")

# Building dropdown for features sex and smoker.
df = pd.DataFrame({'New_sex': ['Male','Female'],
                      'smoker': ['Yes', 'No'],
                      'Diabetes': ['Yes', 'No'],
                      'BloodPressureProblems': ['Yes', 'No'],
                      'KnownAllergies': ['Yes', 'No'],
                      'HistoryOfCancerInFamily': ['Yes', 'No'],
                      'AnyTransplants': ['Yes', 'No'],
                      'AnyChronicDiseases': ['Yes', 'No']}) 
    
# Building dropdown for region feature.
df1 = pd.DataFrame({'region' : ['southeast' ,'northwest' ,'southwest' ,'northeast']})
    
# Take the users input
New_sex = st.selectbox("Select Sex", df['New_sex'].unique())
print(New_sex)
smoker = st.selectbox("Are you a smoker", df['smoker'].unique())
print(smoker)
region = st.selectbox("Which region do you belong to?", df1['region'].unique())
print(region)
Age = st.slider("What is your age?", 18, 100)
print(Age)
bmi = st.slider("What is your bmi?", 10, 60)
print(bmi)
children = st.slider("Number of children", 0, 10)
print(children)
Height = st.slider("What is your height?",100 , 300)
Weight = st.slider('What is your weight?', 30,150)
Diabetes = st.selectbox("Diabetes", df['Diabetes'].unique())
print(Diabetes)
BloodPressureProblems = st.selectbox("BloodPressureProblems", df['BloodPressureProblems'].unique())
KnownAllergies = st.selectbox("KnownAllergies", df['KnownAllergies'].unique())
HistoryOfCancerInFamily = st.selectbox("HistoryOfCancerInFamily", df['HistoryOfCancerInFamily'].unique())
NumberOfMajorSurgeries = st.slider("Number of surgeries", 0, 5)
AnyTransplants = st.selectbox("AnyTransplants", df['AnyTransplants'].unique())
AnyChronicDiseases = st.selectbox("AnyChronicDiseases", df['AnyChronicDiseases'].unique())


# converting text input to numeric to get back predictions from backend model.
if New_sex == 'male':
    gender = 1
else:
    gender = 0
    
if smoker == 'yes':
    smoke = 1
else:
    smoke = 0

if Diabetes == 'yes':
    Diabetes = 1
else:
    Diabetes = 0

if BloodPressureProblems == 'yes':
    smoBloodPressureProblemske = 1
else:
    BloodPressureProblems = 0

if KnownAllergies == 'yes':
    KnownAllergies = 1
else:
    KnownAllergies = 0

if HistoryOfCancerInFamily == 'yes':
    HistoryOfCancerInFamily = 1
else:
    HistoryOfCancerInFamily = 0

if NumberOfMajorSurgeries == 'yes':
    NumberOfMajorSurgeries = 1
else:
    NumberOfMajorSurgeries = 0

if AnyTransplants == 'yes':
    AnyTransplants = 1
else:
    AnyTransplants = 0

if AnyChronicDiseases == 'yes':
    AnyChronicDiseases = 1
else:
    AnyChronicDiseases = 0
    
if region == 'southeast':
    reg = 2
elif region == 'northwest':
    reg = 3
elif region == 'southwest':
    reg = 1
else:
    reg = 0
    
# store the inputs

features = [gender, smoke, reg, Age, bmi, children , Weight, Height, Diabetes , KnownAllergies, AnyChronicDiseases, AnyTransplants , NumberOfMajorSurgeries, HistoryOfCancerInFamily , BloodPressureProblems ]

# convert user inputs into an array for the model

int_features = [int(x) for x in features]
final_features = [np.array(int_features)]

# Final prediction
if st.button('Predict'):           # when the submit button is pressed
    prediction =  loaded_model.predict(final_features)
    st.balloons()
    st.success('Your insurance charges would be dollar:',round(prediction[0],2))
    
