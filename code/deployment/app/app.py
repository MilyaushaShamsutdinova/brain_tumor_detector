import streamlit as st
import requests
from PIL import Image

st.title("Brain Tumor Detection")

uploaded_file = st.file_uploader("Choose a brain MRI image...", type="jpg")

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)
    
    if st.button("Predict"):
        st.write("Classifying...")
        
        files = {"file": uploaded_file.getvalue()}
        response = requests.post("http://localhost:8000/predict", files=files)
        # response = requests.post("http://api:8000/predict", files=files)  # for docker file
        prediction = response.json()["prediction"]
        
        st.write(f"Prediction: {prediction}")
