import cv2
import pydicom
import numpy as np

# loading image that supports both DICOM and standard formats
def load_image(filepath):
# Handling DICOM files
    if filepath.endswith(".dicom") or filepath.endswith(".dcm"):
        dicom_data = pydicom.dcmread(filepath)
        image = dicom_data.pixel_array
    else:
        image = cv2.imread(filepath)  # Open non-DICOM images using OpenCV
    
    return image

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
#---------------------------------------------------------------------#
# Preprocess medical images (resize, grayscale, etc.)
def preprocess_image(filepath):
    image = load_image(filepath)
    
    # Convert to grayscale
    if len(image.shape) == 3:  # Check if the image is not already grayscale
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Resize the image to 256x256
    image = cv2.resize(image, (256, 256))
    
    # Normalize pixel values to range 0-1
    image = image / 255.0
    
    return image

# Edge Detection using Canny method
def apply_edge_detection(image):
    edges = cv2.Canny(image, 100, 200)  # Canny edge detection
    return edges

# Image Segmentation using thresholding
def apply_segmentation(image):
    # Threshold the image to binary (for segmentation)
    _, segmented_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
    return segmented_image

# Noise Reduction using Gaussian Blur
def apply_denoise(image):
    # Apply Gaussian Blur to reduce noise
    denoised_image = cv2.GaussianBlur(image, (5, 5), 0)
    return denoised_image

# Main function to handle multiple image enhancements
def enhance_image(filepath, options):
    image = preprocess_image(filepath)
    
    # Apply enhancements based on user options
    if 'edge_detection' in options:
        image = apply_edge_detection(image)
    
    if 'segmentation' in options:
        image = apply_segmentation(image)
    
    if 'denoise' in options:
        image = apply_denoise(image)
    
    return image
