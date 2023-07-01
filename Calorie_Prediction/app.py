import streamlit as st
import pickle
import sklearn
import pandas as pd
import numpy as np
from PIL import Image


model=pickle.load(open('model.sav','rb'))
st.title("Calorie Burning Prediction")
st.sidebar.header("Input User Data")
image=Image.open('cal.jpg')
st.image(image,'')

def user_report():
    Gender=st.sidebar.slider("Gender",0,1,1)
    Age=st.sidebar.slider("Age",15,100,1)	
    Height=st.sidebar.slider("Height",123,230,1)
    Weight=st.sidebar.slider("Weight",36,150,1)
    Duration=st.sidebar.slider("Duration",1,500,1)
    Heart_Rate=st.sidebar.slider("Hert Rate",67,128,1)
    Body_Temp=st.sidebar.slider("Body Temperature",37,42,1)

    user_report_data={
        'Gender':Gender,'Age':Age,'Height':Height,'Weight':Weight,'Duration':Duration,
        'Heart_Rate':Heart_Rate,'Body_Temp':Body_Temp
    }
    report_data=pd.DataFrame(user_report_data,index=[0])
    return report_data

user_data=user_report()
st.header("User Data")
st.write(user_data)

calories=model.predict(user_data)
st.subheader("User Calorie")
st.subheader(str(np.round(calories[0],2)),"Joules") 