# Ballot Paper Classification - Computer Vision Project

## Demo

<p align="center">
<img src="./example.png"  />
</p>

## Model

The model is trained on ResNet50 architecture.

<p align="center">
<img src="./loss_plot.png"  />
</p>

## Prepare the data for Evaluation

Prepare your dataset to proceed with the model. Your data folder structure should be on following format:

├── data <- Root data folder
│ ├── 0 <- Sub data folder with it's associated label
| ├── img1.jpeg <- Image file with same filename as on csv file

To structure data this way, while running `evaluate.py` make sure to change `process_data` param to `True`

## Evaluate data

The `evaluate.py` function will evaluate the provided data and returns the evaluation report as an output.

```
python evaluate.py
```

# Flask App

To run the flask app, use the following command.

```
python app.py
```
