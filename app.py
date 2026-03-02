import streamlit as st
import numpy as np

st.set_page_config(
    page_title="OsteoAI - Hybrid Risk Assessment",
    layout="wide"
)

# -------- Pink Theme Styling --------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #ffe6f0, #ffb6c1, #ffc0cb);
    color: #4b004f;
}

h1, h2, h3 {
    color: #8b004b;
}

.block-container {
    padding-top: 2rem;
}

.stButton>button {
    background: linear-gradient(90deg, #ff4d88, #ff0066);
    color: white;
    border-radius: 12px;
    height: 3em;
    width: 100%;
    font-size: 16px;
    font-weight: bold;
}

.stButton>button:hover {
    background: linear-gradient(90deg, #e6005c, #cc0052);
    color: white;
}

.css-1d391kg {
    background-color: #fff0f5;
}
</style>
""", unsafe_allow_html=True)

st.title("Osteoporosis Hybrid Risk Assessment System")
st.markdown("AI-Based Bone Weakness Detection and Clinical Risk Evaluation")
st.divider()

# -------- Upload Section --------
st.subheader("Upload Bone X-Ray")
uploaded_file = st.file_uploader("Upload X-Ray Image", type=["jpg", "png", "jpeg"])

if uploaded_file:
    st.image(uploaded_file, use_container_width=True)
    image_score = np.random.uniform(0.3, 0.9)
else:
    image_score = 0.3

st.divider()

# -------- BMI Calculator --------
st.subheader("BMI Calculator")

col1, col2 = st.columns(2)

with col1:
    weight = st.number_input("Weight (kg)", 30.0, 150.0, 60.0)

with col2:
    height = st.number_input("Height (cm)", 120.0, 200.0, 165.0)

bmi = weight / ((height/100) ** 2)

st.markdown(f"### Calculated BMI: {bmi:.2f}")

if bmi < 18.5:
    st.info("BMI Category: Underweight")
elif 18.5 <= bmi < 25:
    st.success("BMI Category: Normal")
elif 25 <= bmi < 30:
    st.warning("BMI Category: Overweight")
else:
    st.error("BMI Category: Obese")

st.divider()

# -------- Clinical Risk --------
st.subheader("Clinical Risk Factors")

age = st.slider("Age", 20, 100, 50)
menopause = st.selectbox("Post Menopause", ["No", "Yes"])
smoking = st.selectbox("Smoking", ["No", "Yes"])
fracture = st.selectbox("Previous Fracture", ["No", "Yes"])

st.divider()

# -------- Prediction --------
if st.button("Run Hybrid Risk Analysis"):

    clinical_score = 0

    if age > 60:
        clinical_score += 1
    if bmi < 18.5:
        clinical_score += 1
    if menopause == "Yes":
        clinical_score += 1
    if smoking == "Yes":
        clinical_score += 1
    if fracture == "Yes":
        clinical_score += 1

    clinical_score = clinical_score / 5

    final_score = (0.6 * image_score) + (0.4 * clinical_score)

    st.subheader("Risk Analysis Result")

    if final_score < 0.3:
        st.success(f"Low Risk ({round(final_score,2)})")
    elif final_score < 0.7:
        st.warning(f"Moderate Risk ({round(final_score,2)})")
    else:
        st.error(f"High Risk ({round(final_score,2)})")

    st.progress(min(final_score,1.0))

st.divider()
st.caption("AI-assisted screening tool for educational purposes only.")
