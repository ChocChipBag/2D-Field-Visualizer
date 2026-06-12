import cv2
import numpy as np
from tkinter import filedialog, Tk, Label, Button
from PIL import Image, ImageTk
import tkinter as tk



def remove_non_white_pixels_opencv(image_path, output_path, white_threshold=240):
    """
    Remove non-white pixels using OpenCV
    """
    # Read image
    img = cv2.imread(image_path)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Create mask for white pixels
    white_mask = np.all(img_rgb > white_threshold, axis=2)

    # Create RGBA image with alpha channel
    rgba = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)

    # Set alpha to 0 for non-white pixels
    rgba[~white_mask, 3] = 0

    # Save as PNG
    cv2.imwrite(output_path, rgba)

    return rgba