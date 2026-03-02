import streamlit as st
import numpy as np

st.set_page_config(page_title="OsteoAI", page_icon="🦴")

st.title("🦴 OsteoAI")
st.subheader("Osteoporosis Early Risk Screening System")

st.markdown("---")

age = st.number_input("Age", 20, 100, 45)
bmi = st.number_input("BMI", 10.0, 50.0, 22.0)
menopause = st.selectbox("Menopause Status", ["No", "Yes"])
smoking = st.selectbox("Smoking History", ["No", "Yes"])
fracture = st.selectbox("Previous Fracture", ["No", "Yes"])

if st.button("Predict Risk"):

    score = 0

    if age > 60:
        score += 1
    if bmi < 18.5:
        score += 1
    if menopause == "Yes":
        score += 1
    if smoking == "Yes":
        score += 1
    if fracture == "Yes":
        score += 1

    if score <= 1:
        st.success("Low Risk")
    elif score <= 3:
        st.warning("Moderate Risk")
    else:
        st.error("High Risk")

    st.write("Risk Score:", score)

    st.caption("⚠ Screening tool only. Clinical confirmation required.")
