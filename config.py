import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMG_OUTPUT_PATH = os.path.join(os.path.dirname(__file__), "output.jpeg")

ENCODER_PATH = os.path.join(BASE_DIR, "artifacts", "encoder.pkl")
MODEL_PATH = os.path.join(BASE_DIR, 'artifacts'. 'model.h5')

## Change to your data path
DATA_PATH = os.path.join(BASE_DIR, 'data')
PROCESSED_DATA_PATH = os.path.join(DATA_PATH, 'processed_data')
CSV_PATH = ''