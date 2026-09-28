import streamlit as st

st.title("division")
n1=st.number_input("Enter first number",min_value=0)
# print(n1)
n2=st.number_input("Enter second number",min_value=0)
# print(n2)
btn=st.button("Divide")
if btn: #when button clicks it will execute if block
    result=n1/n2
    # print(result)
    st.write(result) # to show in interface