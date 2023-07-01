import streamlit as st
import pickle 
import pandas as pd
import numpy as np
from PIL import Image
import sklearn
import glob
import os


run_left=int()
balls_left=int()
crr=float()
rrr=float()

teams=['Sunrisers Hyderabad',
 'Mumbai Indians',
 'Royal Challengers Bangalore', 
 'Kolkata Knight Riders',
 'Kings XI Punjab',
 'Chennai Super Kings',
 'Rajasthan Royals',
 'Delhi Capitals']

cities=['Hyderabad', 'Bangalore', 'Mumbai', 'Kolkata', 'Delhi', 'Chennai',
       'Jaipur', 'Cape Town', 'Port Elizabeth', 'Durban', 'Centurion',
       'East London', 'Johannesburg', 'Kimberley', 'Bloemfontein',
       'Ahmedabad', 'Cuttack', 'Nagpur', 'Visakhapatnam', 'Pune',
       'Raipur', 'Ranchi', 'Abu Dhabi', 'Sharjah', 'Bengaluru']

pipe=pickle.load(open('model.sav','rb'))
st.title("IPL Win Predictor")
image=Image.open('ipl.jpg')
st.image(image)

col1,col2=st.columns(2)
with col1:   #for taking input of Batting team
    batting_team=st.selectbox('Select the Batting Team',sorted(teams))
with col2:  #for bowling team
    bowling_team=st.selectbox('Select the Bowling Team',sorted(teams))

selected_city=st.selectbox("Select Host City",sorted(cities))  #for cities

target=st.number_input('Target')   #input for target

col3,col4,col5=st.columns(3)
with col3:
    score=st.number_input('Score')
with col4:
    overs=st.number_input('Overs Completed')
with col5:
    wickets=st.number_input("Wickets Out")

if st.button('Predict Probability'):
    run_left=target-score
    balls_left=120-(overs*6)
    wickets=10-wickets
    crr=score/overs
    rrr=(run_left*6)/balls_left

input_df=pd.DataFrame({'batting_team':[batting_team],'bowling_team':[bowling_team],'city':[selected_city],'runs_left':[run_left],'balls left':[balls_left],'wickets_left':[wickets],'total_runs_x':[target],'crr':[crr],'rrr':[rrr]})

st.table(input_df)

result=pipe.predict_proba(input_df) 
loss=result[0][0]
win=result[0][1]
st.header(batting_team + "- " + str(round(win*100))+"%")
st.header(bowling_team + "- " + str(round(loss*100))+"%")
