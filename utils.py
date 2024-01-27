import os
from os import listdir
from numpy import asarray
import cv2
import config


def create_image_folders(
    data_frame, data_dir, output_dir, size=(150, 150),
):
    """
    """
    images = []
    labels = []

    for filename in data_frame["Data"].values:
        save_path = os.path.join(
            output_dir, str(df[df["Data"] == filename]["Label"].values[0])
        )
        if not os.path.exists(save_path):
            os.makedirs(save_path)

        img = cv2.imread(os.path.join(data_dir, filename))
        if img is not None:
            img = cv2.resize(img, size)

            p = os.path.join(save_path, filename)
            cv2.imwrite(p, img)
    return True


def load_images_from_folder(path):
    """
    """

    images = []
    labels = []
    for folder in listdir(path):
        for image in listdir(os.path.join(path, folder)):
            img = cv2.imread(os.path.join(path, folder, image))
            images.append(img)
            labels.append(asarray(os.path.basename(os.path.join(path, folder))))
    return asarray(images), asarray(labels)
