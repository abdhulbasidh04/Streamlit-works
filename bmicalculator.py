import streamlit as st
st.title("BMI")
weight=st.number_input("Enter the weight",min_value=0)
height=st.number_input("Enter the height",min_value=0)
btn=st.button("BMI")
if btn:
    bmi=weight/((height/100)**2)
    st.write(bmi)
    if bmi<18.5:
        st.info("Under Weight")
    elif 18.5<=bmi<25:
        st.success("normal")
    elif 25<=bmi<30:
        st.warning("overweight")
    elif bmi>30:
        st.error("obesity")