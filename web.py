import streamlit as st
from deepface import DeepFace
import keras
from keras.preprocessing import image
from keras.models import load_model
from keras.preprocessing.image import img_to_array 
import numpy as np

def detect_face(image):
    demography = DeepFace.analyze(image)
    return demography

st.title('Age, Emotion Detection')

uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])
if uploaded_image is None:
    st.write('No file is uploaded here')

else:
    image = image.load_image(uploaded_image)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    st.write("")
    st.write("Analyzing...")
    output = detect_face(image)
    st.write(output)