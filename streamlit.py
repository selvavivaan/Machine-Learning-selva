# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 17:31:48 2023

@author: Admin
"""

#import numpy as np
import pickle
import streamlit as st


loaded_model =pickle.load(open("D:/MAchine Learning/Diabetes/DiabeticModel.sav",'rb'))

def prediction(Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age):

    # #Changing the input_data to numpy array
    # input_data_as_numpy_array = np.asarray(input_data)

    # #reshape the array as we are predicting for one instance
    # input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(
        [[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

    if prediction == 0:
        pred = 'This person is not diabetic'
    else:
        pred = 'This person is diabetic'
    return pred


def main():
    #giving a title
    st.title('Diabetes Prediction Web App')

    #gettin the input data from the user
    Pregnancies = st.text_input('Number of Pregnancies')
    Glucose = st.text_input('Glucose Value')
    BloodPressure = st.text_input('BloodPressure Value')
    SkinThickness = st.text_input('SkinThickness Value')
    Insulin = st.text_input('Insulin Level')
    BMI = st.text_input('BMI Value')
    DiabetesPedigreeFunction = st.text_input('DiabetesPedigreeFunction Value')
    Age = st.text_input('Age of the Person')


    #code for prediction
    diagnosis = ''

    # create the button for prediction
    if st.button('Diabetes Test Result'):
        diagnosis = prediction(Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age)

    st.success(diagnosis)

if __name__ == '__main__':
    main()


# import pickle
# import streamlit as st

# # loading the trained model
# pickle_in = open('D:/MAchine Learning/Diabetes/Diabetic_Model.sav', 'rb')
# classifier = pickle.load(pickle_in)



# @st.cache()
# # defining the function which will make the prediction using the data which the user inputs
# def prediction(Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age):
    
#     # Making predictions
    # prediction = classifier.predict(
    #     [[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

    # if prediction == 0:
    #     pred = 'This person is not diabetic'
    # else:
    #     pred = 'This person is diabetic'
    # return pred


# # this is the main function in which we define our webpage
# def main():
#     # front end elements of the web page
#     html_temp = """ 
#     <div style ="background-color:yellow;padding:13px"> 
#     <h1 style ="color:black;text-align:center;">Diabetes Prediction Web App</h1> 
#     </div> 
#     """

#     # display the front end aspect
#     st.markdown(html_temp, unsafe_allow_html=True)

#    #gettin the input data from the user
#     Pregnancies = st.text_input('Number of Pregnancies')
#     Glucose = st.text_input('Gulcose Value')
#     BloodPressure = st.text_input('BloodPressure Value')
#     SkinThickness = st.text_input('SkinThickness Value')
#     Insulin = st.text_input('Insulin Level')
#     BMI = st.text_input('BMI Value')
#     DiabetesPedigreeFunction = st.text_input('DiabetesPedigreeFunction Value')
#     Age = st.text_input('Age of the Person')
#     result = ""

#     # when 'Predict' is clicked, make the prediction and store it
#     if st.button("Predict"):
#         result = prediction(Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age)
#         st.success(result)


# if __name__ == '__main__':
#     main()
