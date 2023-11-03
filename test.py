import cv2
import tkinter as tk
from PIL import Image, ImageTk

# Function to capture an image from the webcam
def capture_image():
    # Open the webcam
    cap = cv2.VideoCapture(0)

    # Check if the webcam is opened successfully
    if not cap.isOpened():
        print("Failed to open the webcam")
        return

    # Read the current frame from the webcam
    ret, frame = cap.read()

    # Check if frame is successfully read
    if not ret:
        print("Failed to capture frame")
        return

    # Release the webcam
    cap.release()

    return frame

# Function to display the captured image with text
def display_image_with_text(image):
    # Create a Tkinter window
    window = tk.Tk()

    # Convert the image to PIL format
    pil_image = Image.fromarray(image)

    # Create a Tkinter-compatible image
    tk_image = ImageTk.PhotoImage(pil_image)

    # Create a label widget to display the image
    image_label = tk.Label(window, image=tk_image)
    image_label.pack()

    # Add the text at the center of the image
    text_label = tk.Label(window, text="Access Granted", font=("Arial", 24))
    text_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    # Start the Tkinter event loop
    window.mainloop()

# Capture an image from the webcam
image = capture_image()

# Display the captured image with text
display_image_with_text(image)
