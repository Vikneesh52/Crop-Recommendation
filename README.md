# Crop Recommendation System

This project implements a Crop Recommendation System using machine learning algorithms. It helps predict the appropriate crop based on input features such as temperature, humidity, rainfall, etc.

## Prerequisites

- Python 3.x
- Required Python packages: `scikit-learn`, `pandas`

## Installation

1. Clone the repository:
   git clone https://github.com/Vikneesh52/Crop-Recommendation
2. Install the required Python packages:
   pip install scikit-learn pandas

## Usage

1. Train the model:
   
   - Run the Python script `train_model.py` to train the crop recommendation model. The script will read the data from `crop_recommendation.csv`, split it into training and testing datasets, and train the model using different algorithms such as Support Vector Machines, Random Forest, Gaussian Naive Bayes, and K-Nearest Neighbors. The trained model will be saved as `Crop_Recommendation.pkl`.

2. Make predictions:

   - Modify the Python script `make_predictions.py` to obtain random input values from the user or provide input values programmatically. The script loads the trained model from `Crop_Recommendation.pkl`, prompts the user to enter input feature values, prepares the input data, and makes predictions using the loaded model. The predicted crop will be displayed on the console.

3. Run the prediction script:

   - Execute the Python script `make_predictions.py` to make predictions using the trained model. Follow the on-screen prompts to enter input feature values or modify the script to provide input values programmatically.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
