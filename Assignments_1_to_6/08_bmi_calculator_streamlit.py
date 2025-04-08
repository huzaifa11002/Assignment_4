import streamlit as st

st.title('BMI Calculator 🖩')
st.write('This is a simple BMI calculator')


weight = st.number_input('Enter your weight (in kg)', step=0.1)
height = st.number_input('Enter your height (in m)', step=0.1)

if st.button('Calculate BMI', key='bmi'):
    if weight == 0 or height == 0:
        st.write('Please enter valid values')
    else:
        bmi = weight / (height**2)
        st.write(f'Your BMI is {bmi:.2f}')
        if bmi < 18.5:
            st.write('You are underweight')
        elif bmi >= 18.5 and bmi < 25:
            st.write('You are normal weight')
        elif bmi >= 25 and bmi < 30:
            st.write('You are overweight')
        else:
            st.write('You are obese')