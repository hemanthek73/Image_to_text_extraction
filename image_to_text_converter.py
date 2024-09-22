import cv2
import pytesseract
import easyocr
import streamlit as st
from PIL import Image
import numpy as np
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# Path to Tesseract OCR executable (Windows only)
# If you are using Linux or Mac, ensure tesseract is installed
# and available in your system's PATH.
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def preprocess_image(uploaded_file):
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    # Convert the image to grayscale for noise reduction
  
    if img is None or img.size == 0:
        st.error("Error: Could not load the image.")
        return None

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return gray

def extract_text_tesseract(image):
    # Convert image to string using Tesseract
    text = pytesseract.image_to_string(image)
    return text

# def extract_text_easyocr(image):
#     # Initialize EasyOCR reader
#     reader = easyocr.Reader(['en'],gpu=False)
#     result = reader.readtext(image)
    
#     # Extract the text from the result
#     extracted_text = ""
#     for (bbox, text, prob) in result:
#         extracted_text += f"{text}\n"
    
#     return extracted_text

def main():
    st.title("Image to Text Converter")
    st.write("This app extracts text from images using Tesseract or EasyOCR.")
    
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        preprocessed_image = preprocess_image(uploaded_file)
        
        if preprocessed_image is not None:
            # Display preprocessed image
            st.image(preprocessed_image, caption='Preprocessed Image', use_column_width=True)

            # Extract text using Tesseract
            st.subheader("Text Extracted using Tesseract OCR:")
            extracted_text = extract_text_tesseract(preprocessed_image)
            st.write(extracted_text)

            # Extract text using EasyOCR
            # st.subheader("Text Extracted using EasyOCR:")
            # extracted_text_easy = extract_text_easyocr(preprocessed_image)  # Pass the image array
            # st.write(extracted_text_easy)

if __name__ == "__main__":
    main()


