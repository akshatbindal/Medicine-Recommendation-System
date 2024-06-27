import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from src.pipeline.predict import CustomData, PredictPipeline
from src.utils import other_results

# Load data
df = pd.read_csv("artifacts/Training.csv")
symptoms_list = df.columns[:-1].to_list()
symptoms_dict = {col: idx for idx, col in enumerate(df.columns[:-1])}
target_features = df['prognosis']

# Streamlit app
st.title("Medicine Recommendation System")

# Sidebar for input
st.sidebar.header("Input Symptoms")
symptom1 = st.sidebar.selectbox('Symptom 1', options=[""] + symptoms_list)
symptom2 = st.sidebar.selectbox('Symptom 2', options=[""] + symptoms_list)
symptom3 = st.sidebar.selectbox('Symptom 3', options=[""] + symptoms_list)
symptom4 = st.sidebar.selectbox('Symptom 4', options=[""] + symptoms_list)

if st.sidebar.button("Predict"):
    # Process input
    data = CustomData(
        symptom1=symptom1,
        symptom2=symptom2,
        symptom3=symptom3,
        symptom4=symptom4,
    )
    pred_df = data.get_data_as_one_hot_encoding(symptoms_dict=symptoms_dict)
    
    # Prediction
    predict_pipeline = PredictPipeline()
    result = predict_pipeline.predict(pred_df)

    # Decode result
    label_encoder = LabelEncoder()
    label_encoder.fit(target_features)
    predicted_disease = label_encoder.inverse_transform(result)[0]

    # Get other results
    description, precaution, medicine, diet, workout = other_results(predicted_disease)

    # Display results
    st.subheader("Predicted Disease")
    st.write(predicted_disease)

    st.subheader("Description")
    st.write(description)

    st.subheader("Prescription Details")
    
    with st.expander("Precautions"):
        for prec in precaution:
            st.write(prec)

    with st.expander("Medications"):
        for med in medicine:
            st.write(med)

    with st.expander("Diet"):
        for d in diet:
            st.write(d)

    with st.expander("Workout"):
        for wo in workout:
            st.write(wo)
else:
    st.write("Please select symptoms and click on Predict.")
