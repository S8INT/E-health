import cv2
import pydicom
import numpy as np

# Preprocess medical images (resize, grayscale, etc.)
def preprocess_image(filepath):
    # Handling DICOM files
    if filepath.endswith(".dicom") or filepath.endswith(".dcm"):
        dicom_data = pydicom.dcmread(filepath)
        image = dicom_data.pixel_array
    else:
        image = cv2.imread(filepath)  # Open non-DICOM images using OpenCV

    # Convert to grayscale
    if len(image.shape) == 3:  # Check if the image is not already grayscale
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Resize the image to 256x256
    image = cv2.resize(image, (256, 256))

    # Normalize pixel values to range 0-1
    image = image / 255.0

    return image
