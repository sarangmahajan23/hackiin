import cv2
import os
import numpy as np

# Function to load images and labels
def load_images_from_folder(folder):
    images = []
    labels = []
    for folder_name in os.listdir(folder):
        f = folder_name
        folder_name = os.path.join(folder,folder_name)
        for filename in os.listdir(folder_name):
            img_path = os.path.join(folder_name, filename)
            img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
            if img is not None:
                images.append(img)
                labels.append(int(f))
    return images, labels

# Load images and labels from a folder
images, labels = load_images_from_folder('images')

print(labels)
# Initialize LBPH face recognizer
recognizer = cv2.face.LBPHFaceRecognizer_create()

# Train the recognizer
recognizer.train(images, np.array(labels))

# Save the trained model
recognizer.save('lbph_model.xml')
