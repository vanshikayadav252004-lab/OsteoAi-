import streamlit as st
import numpy as np

# Page Config
st.set_page_config(
    page_title="Osteoporosis Hybrid Risk Assessment",
    page_icon="🦴",
    layout="wide"
)

# Custom CSS (Futuristic Purple Theme)
st.markdown("""
<style>
.stApp {
    background: linear-gradient(to bottom right, #2b1055, #4b0082, #6a0dad);
    color: white;
}
.card {
    background: rgba(255,255,255,0.08);
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 0px 20px rgba(255,255,255,0.2);
    margin-bottom: 20px;
}
.risk-low {
    background-color: #1f8f4e;
    padding: 15px;
    border-radius: 10px;
    text-align: center;
}
.risk-moderate {
    background-color: #e6a100;
    padding: 15px;
    border-radius: 10px;
    text-align: center;
}
.risk-high {
    background-color: #c0392b;
    padding: 15px;
    border-radius: 10px;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 style='text-align:center;'>🧠 Osteoporosis Hybrid Risk Assessment System</h1>", unsafe_allow_html=True)
st.divider()

# Upload Section
st.markdown("## 🦴 Upload Bone X-Ray")
uploaded_file = st.file_uploader("Upload X-ray Image", type=["jpg","png","jpeg"])

st.divider()

# Clinical Input Section
st.markdown("## 📝 Enter Clinical Risk Factors")

col1, col2 = st.columns(2)

with col1:
    age = st.slider("Age", 30, 85, 50)
    bmi = st.slider("BMI", 15, 40, 22)

with col2:
    menopause = st.radio("Post-Menopausal?", ["No","Yes"])
    fracture = st.radio("Previous Fracture?", ["No","Yes"])

st.divider()

# Analysis Button
if st.button("⚡ Run Analysis & Scoring"):

    st.markdown("## 🔬 Analysis & Scoring")

    # Image Score (Simulated AI Detection)
    if uploaded_file:
        image_score = np.random.uniform(0.2, 0.9)
    else:
        image_score = 0.3  # default if no image

    # Clinical Score Calculation
    clinical_score = 0
    if age > 60:
        clinical_score += 0.3
    if bmi < 20:
        clinical_score += 0.2
    if menopause == "Yes":
        clinical_score += 0.3
    if fracture == "Yes":
        clinical_score += 0.2

    clinical_score = min(clinical_score, 1.0)

    st.markdown("### 🧮 Image Score (Bone Weakness Detection)")
    st.progress(image_score)

    st.markdown("### 📊 Clinical Risk Score (Patient Data Evaluation)")
    st.progress(clinical_score)

    st.divider()

    # Hybrid Formula
    hybrid_score = (0.6 * image_score) + (0.4 * clinical_score)

    st.markdown("## ⚙ Hybrid Risk Formula")
    st.markdown(f"""
    ### 0.6 × Image Score + 0.4 × Clinical Score  
    ### Final Hybrid Risk Score = **{hybrid_score:.2f}**
    """)

    st.divider()

    # Risk Classification
    st.markdown("## 🚦 Risk Classification")

    if hybrid_score <= 0.3:
        st.markdown("<div class='risk-low'><h3>LOW RISK (0 – 0.3)</h3></div>", unsafe_allow_html=True)
    elif 0.3 < hybrid_score <= 0.7:
        st.markdown("<div class='risk-moderate'><h3>MODERATE RISK (0.3 – 0.7)</h3></div>", unsafe_allow_html=True)
    else:
        st.markdown("<div class='risk-high'><h3>HIGH RISK (> 0.7)</h3></div>", unsafe_allow_html=True)

st.divider()
st.markdown("⚠ AI-assisted screening tool for educational purposes only.")
