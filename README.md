# Iris Classification Model

A demo repository showcasing a complete machine learning pipeline for binary classification using the Iris dataset.

## Project Overview

This project demonstrates:
- Data loading and preprocessing (using scikit-learn's Iris dataset)
- Training a Random Forest classifier
- Evaluating the model using multiple metrics (AUC, Accuracy, Recall, Precision)
- Saving the trained model, scaler, and results

## Dataset

The Iris dataset is a classic machine learning dataset containing 150 samples of iris flowers with 4 features:
- Sepal length
- Sepal width
- Petal length
- Petal width

**Target Classes:** Binary classification (classes 0 and 1 from the original 3-class dataset)

## Model

**Algorithm:** Random Forest Classifier
- **n_estimators:** 100
- **max_depth:** 10
- **min_samples_split:** 5
- **min_samples_leaf:** 2

## Evaluation Metrics

The model is evaluated using the following metrics:
- **Accuracy:** Overall correctness of predictions
- **Precision:** True positives / (True positives + False positives)
- **Recall:** True positives / (True positives + False negatives)
- **AUC (Area Under Curve):** ROC-AUC score for model discrimination ability

## Project Structure

```
.
├── main.py                 # Main pipeline script
├── requirements.txt        # Python dependencies
├── README.md              # This file
└── model_results/         # Results directory
    ├── model.pkl          # Trained model (pickled)
    ├── scaler.pkl         # Feature scaler (pickled)
    ├── metrics.json       # Evaluation metrics
    ├── hyperparameters.json  # Model hyperparameters
    └── summary.json       # Complete summary with timestamp
```

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd iris-classification
```

2. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the complete pipeline:
```bash
python main.py
```

The script will:
1. Load the Iris dataset
2. Preprocess and split the data (80% train, 20% test)
3. Train the Random Forest model
4. Evaluate using AUC, Accuracy, Recall, and Precision
5. Save all results to the `model_results/` folder

## Results

After running `main.py`, you'll find:
- `model.pkl`: Serialized trained model
- `scaler.pkl`: Serialized feature scaler
- `metrics.json`: Evaluation metrics in JSON format
- `hyperparameters.json`: Model hyperparameters used for training
- `summary.json`: Complete summary with timestamp and all details

Example metrics output:
```json
{
    "accuracy": 1.0,
    "precision": 1.0,
    "recall": 1.0,
    "auc": 1.0
}
```

## Making Predictions with the Saved Model

```python
import pickle
import numpy as np

# Load model and scaler
with open('model_results/model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('model_results/scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

# Prepare new data (example)
new_data = np.array([[5.1, 3.5, 1.4, 0.2]])  # Raw features
scaled_data = scaler.transform(new_data)

# Make prediction
prediction = model.predict(scaled_data)
probability = model.predict_proba(scaled_data)

print(f"Prediction: {prediction[0]}")
print(f"Probability: {probability}")
```

## Requirements

- Python 3.8+
- scikit-learn
- numpy
- pandas
- matplotlib
- seaborn

## Author

Created as a demo ML pipeline project.

## License

This project is open source and available under the MIT License.
