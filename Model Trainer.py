import cv2
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC
import pickle
import os

# Create directory for storing trained model
model_dir = 'models'
if not os.path.exists(model_dir):
    os.makedirs(model_dir)

# Initialize list of images, labels, and subject IDs
images = []
labels = []
subject_ids = []

# Load sample images and labels
sample_dir = 'samples'
for subject_dir in os.listdir(sample_dir):
    subject_id = subject_dir.split('_')[0]
    for image_file in os.listdir(os.path.join(sample_dir, subject_dir)):
        image = cv2.imread(os.path.join(sample_dir, subject_dir, image_file), cv2.IMREAD_GRAYSCALE)
        images.append(image)
        labels.append(subject_id)
        subject_ids.append(subject_id)

# Encode labels
le = LabelEncoder()
labels = le.fit_transform(labels)

# Create and train SVM classifier
model = SVC(C=1.0, kernel='linear', probability=True)
model.fit(images, labels)

# Save the trained model
model_path = os.path.join(model_dir, 'model.pkl')
with open(model_path, 'wb') as f:
    pickle.dump(model, f)