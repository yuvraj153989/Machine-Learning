import streamlit as st
import pickle 
import pandas as pd
import numpy as np
from PIL import Image
import sklearn
import glob
import os

model=pickle.load(open('model.sav','rb'))
st.title("Order Amount Prediction")
# st.sidebar.header('User Data')
image=Image.open('logo.png')
st.image(image)


# Function to take user input values
def user_report():
    DIVISION = st.number_input('DIVISION')
    Last_day_sales = st.number_input('Last_day_sales')
    unique_cust_id = st.number_input('unique_cust_id')
    Last1_Day_Sales = st.number_input('Last1-day Sales')
    Last1_Day_Diff = st.number_input('Last1-day Differences')
    Last2_Day_Diff = st.number_input('Last2-day Differences')

    user_report_data={
        'DIVISION':DIVISION,
        'Last_day_sales':Last_day_sales,
        'unique_cust_id':unique_cust_id,
        'Last1-day Sales':Last1_Day_Sales,
        'Last1-day Differences':Last1_Day_Diff,
        'Last2-day Differences':Last2_Day_Diff
    }

    report_data=pd.DataFrame(user_report_data,index=[0])
    return report_data

user_data=user_report()
st.header('User Data')
st.write(user_data)

amount_in_usd=model.predict(user_data)
st.subheader('Order Amount in USD')
st.subheader('$'+str(np.round(amount_in_usd[0],2)))