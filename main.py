import streamlit as st
import cv2
import numpy as np
from tensorflow.keras.models import load_model

model = load_model("Notebook/brain_tumor_model.keras")

Names = ['Glioma', 'Meningioma', 'No Tumor', 'Pituitary']

st.title("Brain Tumor Prediction Using Deep Learning")

uploaded_file = st.file_uploader(
    "Upload MRI Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    file_bytes = np.asarray(
        bytearray(uploaded_file.read()),
        dtype=np.uint8
    )

    image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    st.image(image, channels="BGR")

    if st.button("Predict"):

        img = cv2.resize(image, (224, 224))
        img = img / 255.0
        img = np.expand_dims(img, axis=0)

        prediction = model.predict(img)
        result = np.argmax(prediction)

        if result == 2:
            st.success("No Tumor Detected")
        else:
            st.error(f"Tumor Detected: {Names[result]}")