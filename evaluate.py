# Computer Vision - Ballot Paper Classification
from utils import create_image_folders, load_images_from_folder
from tensorflow import keras
import pandas as pd
import config
import pickle


def evaluate_model(data_frame, process_data=False):
    """
    """
    encoder = None

    if process_data:
        res = create_image_folders(
            data_frame, data_dir=config.DATA_PATH, output_dir=config.PROCESSED_DATA_PATH
        )

    images, labels = load_images_from_folder(config.PROCESSED_DATA_PATH)

    with open(config.ENCODER_PATH, "rb") as f:
        encoder = pickle.load(f)

    encoded_y = encoder.fit_transform(labels)

    model = keras.models.load_model(config.MODEL_PATH)
    print(model.summary())
    res = model.evaluate(images, encoded_y, batch_size=16)
    return res


if __name__ == "__main__":
    df = pd.read_csv(config.CSV_PATH)
    result = evaluate_model(df, process_data=True)
    print(result)
