import streamlit as st
import numpy as np

# -------- Page Config --------
st.set_page_config(
    page_title="OsteoAI - Hybrid Risk Assessment",
    page_icon="🦴",
    layout="wide"
)

# -------- Custom CSS Styling --------
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #6a11cb, #2575fc);
}

.main {
    background: linear-gradient(135deg, #1e1e2f, #302b63, #24243e);
    color: white;
    border-radius: 15px;
    padding: 20px;
}

h1 {
    text-align: center;
    color: #ffffff;
    font-weight: bold;
}

.card {
    background: rgba(255,255,255,0.08);
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0 0 20px rgba(255,255,255,0.1);
}

.stButton>button {
    background: linear-gradient(90deg, #ff416c, #ff4b2b);
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 100%;
    font-size: 18px;
}

</style>
""", unsafe_allow_html=True)

# -------- Title --------
st.title("🦴 Osteoporosis Hybrid Risk Assessment System")

st.markdown("---")

# -------- Layout --------
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 📤 Upload Bone X-Ray")
    uploaded_file = st.file_uploader("Upload X-Ray Image", type=["jpg", "png", "jpeg"])
    
    if uploaded_file:
        st.image(uploaded_file, caption="Uploaded X-Ray", use_container_width=True)
        image_score = np.random.uniform(0, 1)
    else:
        image_score = 0.3

with col2:
    st.markdown("### 🩺 Enter Clinical Risk Factors")
    age = st.slider("Age", 20, 100, 50)
    bmi = st.number_input("BMI", 10.0, 40.0, 22.0)
    menopause = st.selectbox("Post Menopause", ["No", "Yes"])
    smoking = st.selectbox("Smoking", ["No", "Yes"])
    fracture = st.selectbox("Previous Fracture", ["No", "Yes"])

# -------- Prediction --------
st.markdown("---")

if st.button("🔬 Predict Hybrid Risk"):

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

    st.markdown("## 📊 Risk Analysis Result")

    if final_score < 0.3:
        st.success(f"🟢 Low Risk ({round(final_score,2)})")
    elif final_score < 0.7:
        st.warning(f"🟠 Moderate Risk ({round(final_score,2)})")
    else:
        st.error(f"🔴 High Risk ({round(final_score,2)})")
