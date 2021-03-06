
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

st.sidebar.write("Click βΆ to enjoy the music π΅πΆ")
st.sidebar.audio("our-dawn-is-hotter-than-day.mp3")
st.sidebar.audio("Blue bird.mp3")
st.sidebar.audio("Ready to love β SEVENTEEN.m4a")

st.title("β¨ Welcome to my Streamlit β¨")
st.title("")
st.write("β ο½₯ ο½‘οΎβ: .β½ . :βοΎ. ββββββ ο½₯ ο½‘οΎβ: .β½ . :βοΎ. ββββββ ο½₯ ο½‘οΎβ: .β½ . :βοΎ. ββββββ ο½₯ ο½‘οΎβ: .β½ . :βοΎ. β")
st.title("")
st.write("#### This page will help you calculate your BMI.")
st.write("I learn to build this page by joining  _AirAsia Academy_.")
st.write("I hope you enjoy trying my calculator.")
st.title("")
st.write("β ο½₯ ο½‘οΎβ: .β½ . :βοΎ. ββββββ ο½₯ ο½‘οΎβ: .β½ . :βοΎ. ββββββ ο½₯ ο½‘οΎβ: .β½ . :βοΎ. ββββββ ο½₯ ο½‘οΎβ: .β½ . :βοΎ. β")
st.title("")
st.header('BMI CALCULATOR')

image= Image.open("bmi.jpg")
st.image(image, caption='Β© Google')

st.info("What is BMI? π€")
st.success("Body mass index (BMI) is a value derived from the mass (weight) and height of a person.")

if st.checkbox(" β¬ Tick here for more information on BMI"):
    st.text("""
  Body mass index (BMI) is a personβs weight in kilograms divided by the square
  of height in meters. BMI is an easy way to classified the weight into underweight,
  healthy weight, overweight, and obesity. Fat cannot be calculated directly
  from BMI but somehow it related to body fat. Furthermore, BMI appears 
  to be as strongly correlated with various metabolic and disease outcome as are 
  these more direct measures of body fatness. """)

st.header("Let's check your BMI and steps to get a healthy body (ΰΈοΈ‘'-'οΈ )ΰΈ")
st.write(""" ### Please complete your details:""") 
name=st.text_input("Enter you name")
gender=st.radio("Choose you gender",("Male","Female"))
selection=st.selectbox("Select your age group",["10-17","18-25","26-34","35-44","45-54","55-64","65-74","75-79"])
height=st.slider("Your height(in metres)",0.50,2.20)
weight=st.slider("Your weight(in kilograms)",20,120)
bmi=weight/(height*height)


st.write("#### β οΈ Please click sumbit β οΈ")
if st.button("Submit"):
    result=("Hi "+str(name)+" your BMI is "+ str(bmi))
    st.subheader(result)

if bmi < 18.5:
    st.warning("You are too skinny!")
    if st.checkbox("It's okay, don't be discourage click to know some tips to gain weight."):
        st.info("β­ Don't skip any meals.")
        st.info("β­ Try smoothies and shakes.")
        st.info("β­ Eat plenty of proteins.")
        st.info("β­ Exercise.")
else:
        if bmi > 24.9 :
                st.warning("CAUTION! You are OVERWEIGHT or might be OBESE(> 30)!!")
                if st.checkbox("Time to change you lifestyle, click to know more."):
                        st.info("β­ Healthy Eating Habits.")
                        st.info("β­ Have a balanced Diet")
                        st.info("β­ Health-related physical fitness.")
                        st.info("β­ Drink plenty of water.")
        else :
                st.success("Your BMI is normal, Good Job!")
                if st.checkbox("Tick here to know how to maintain a good bmi."):
                        st.info("β­ Exercise regularly.")
                        st.info("β­ Limit Unhealthy Foods and Eat Healthy Meals.")
                        st.info("β­ Get Enough Good Sleep.")

if bmi>24.9:
    if (gender=="Female"):
        img1=Image.open("obese_woman.jpg")
        st.image(img1,width=400)
    else:   
        img2=Image.open("obese_man.jpg")
        st.image(img2,width=400)
else :
        if bmi<18.5:
                if (gender=="Female"):
                        img3=Image.open("skinny_woman.jpg")
                        st.image(img3,width=400)
                else:   
                        img4=Image.open("skinny_man.jpg")
                        st.image(img4,width=400)
        else:
                if (gender=="Male"):
                        img5=Image.open("normal_man.jpg")
                        st.image(img5,width=400)
                else :
                        img6=Image.open("normal_woman.jpg")
                        st.image(img6,width=400)

st.title("")
st.title("")
st.write("Inspired and credit to https://github.com/d2Anubis/streamlit_bmi")