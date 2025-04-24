import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load model
model = joblib.load("clf.pkl")
required_features = model.feature_names_in_

# Human-readable mappings
sex_map = {"Male": 1, "Female": 0}
cp_map = {
    "Typical Angina": 0,
    "Atypical Angina": 1,
    "Non-anginal Pain": 2,
    "Asymptomatic": 3
}
fbs_map = {"Yes (> 120 mg/dl)": 1, "No": 0}
restecg_map = {
    "Normal": 0,
    "ST-T Wave Abnormality": 1,
    "Left Ventricular Hypertrophy": 2
}
exang_map = {"Yes": 1, "No": 0}
slope_map = {
    "Upsloping": 0,
    "Flat": 1,
    "Downsloping": 2
}
thal_map = {
    "Normal": 1,
    "Fixed Defect": 2,
    "Reversible Defect": 3
}

# App UI
st.markdown("<h1 style='color: blue;'>Heart Disease Risk Analyzer ❤️‍🩹</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='color: blue;'>Enter your health stats to estimate your heart disease risk!</h3>", unsafe_allow_html=True)

# Input fields
user_inputs = {}

user_inputs["age"] = st.number_input("Age", min_value=12, max_value=120, step=1)
user_inputs["sex"] = sex_map[st.radio("Sex", list(sex_map.keys()))]
user_inputs["cp"] = cp_map[st.selectbox("Chest Pain Type", list(cp_map.keys()))]
user_inputs["trestbps"] = st.number_input("Resting Blood Pressure (mm Hg)", min_value=80, max_value=200, step=1)
user_inputs["chol"] = st.number_input("Serum Cholesterol (mg/dl)", min_value=100, max_value=600, step=1)
user_inputs["fbs"] = fbs_map[st.selectbox("Fasting Blood Sugar > 120 mg/dl", list(fbs_map.keys()))]
user_inputs["restecg"] = restecg_map[st.selectbox("Resting ECG", list(restecg_map.keys()))]
user_inputs["thalach"] = st.number_input("Max Heart Rate Achieved", min_value=60, max_value=250, step=1)
user_inputs["exang"] = exang_map[st.radio("Exercise Induced Angina", list(exang_map.keys()))]
user_inputs["oldpeak"] = st.number_input("ST Depression (Oldpeak)", min_value=0.0, max_value=6.0, step=0.1)
user_inputs["slope"] = slope_map[st.selectbox("Slope of the ST Segment", list(slope_map.keys()))]
user_inputs["ca"] = st.selectbox("Number of Major Vessels (0–3) Colored by Fluoroscopy", [0, 1, 2, 3])
user_inputs["thal"] = thal_map[st.selectbox("Thalassemia Type", list(thal_map.keys()))]

# Prediction
if st.button("Check My Risk"):
    input_df = pd.DataFrame([user_inputs])[required_features]
    proba = model.predict_proba(input_df)[0][1]
    risk_percent = round(proba * 100, 2)

    st.markdown("---")
    st.subheader("🧠 Risk Evaluation Result")
    st.markdown(
        f"<h2 style='color: black;'>You have a <span style='color:red'>{risk_percent}%</span> chance of having heart disease.</h2>",
        unsafe_allow_html=True
    )

    # Advice based on level
    if risk_percent < 30:
        st.success("👍 Your heart seems healthy! Stay active, eat well, and keep it up!")
    elif 30 <= risk_percent < 70:
        st.warning("⚠️ Moderate risk. Please consult a doctor for a routine check-up.")
    else:
        st.error("❗ High risk detected! It is advisable to seek medical consultation immediately.")
