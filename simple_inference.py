from tensorflow import keras
import numpy as np
import cv2
import pickle


img = cv2.imread("output.jpeg")
img = cv2.resize(img, (150, 150))


with open("encoder.pkl", "rb") as f:
    encoder = pickle.load(f)


model = keras.models.load_model("model.h5")


res = model.predict(np.expand_dims(img, axis=0))

print(encoder.inverse_transform(res))
