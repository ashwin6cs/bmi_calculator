import streamlit as st
import mysql.connector

db = mysql.connector.connect(host="localhost", user="user_name", passwd="password", db="bmi")
mycursor = db.cursor()

name = st.text_input("Enter Your name", "Type Here ...")
result = name.title()

age = st.text_input("Enter Your Age", "Type Here ...")
result1 = age.title()

status = st.radio("Select Gender: ", ('Male', 'Female'))

try:
    weight = st.number_input("Enter your weight (in kgs)")
    # take height input in feet
    height = st.number_input('Enter your height (in feet)')
    bmi = weight / ((height / 3.28) ** 2)
except:
    st.text("Enter some value of height")

if st.button('Calculate BMI'):
    st.text("Your BMI Index is {}.".format(bmi))
    if bmi < 16:
        st.error("You are Extremely Underweight")
    elif 16 <= bmi < 18.5:
        st.warning("You are Underweight")
    elif 18.5 <= bmi < 25:
        st.success("Healthy")
    elif 25 <= bmi < 30:
        st.warning("Overweight")
    elif bmi >= 30:
        st.error("Extremely Overweight")
    sql = 'INSERT INTO calculator (name, age, gender, weight, height, bmi) values(%s, %s, %s, %s, %s, %s)'
    val = (str(name), int(age), str(status), float(weight), float(height), float(bmi))
    mycursor.execute(sql, val)
    db.commit()

