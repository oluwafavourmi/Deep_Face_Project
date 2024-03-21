import streamlit as st
from deepface import DeepFace
from PIL import Image

def detect_face(image):
    demography = DeepFace.analyze(image)
    return demography

st.title('Age, Emotion Detection')

uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_image is not None:
    image = Image.open(uploaded_image)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    st.write("")
    st.write("Analyzing...")
    output = detect_face(image)
    st.write(output)