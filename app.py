import streamlit as st
import joblib
st.title("Loan Approval Process Automation by Tanay")
model=joblib.load('C:/Users/marad/Downloads/datasets/ld.joblib')
gender=st.number_input("Enter the Gender Male:0, Female:1 : ")
married=st.number_input("Enter the Married Single:0, Married:1 : ")
income=st.number_input("Enter the income of the Applicant : ")
la=st.number_input("Enter the Loan Amount of the Applicant : ")
if st.button("Predict Approval"):
    prediction=model.predict([[gender,married,income,la]])
    if prediction=='Y':
        st.text("Loan Approved by Tanay Kumar")
    else:
        st.text("Loan Rejected by Tanay Kumar")
