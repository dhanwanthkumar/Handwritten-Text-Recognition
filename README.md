# Handwritten-Digit-Recognition
The Handwritten Digit Recognition (HDR) project is an innovative application that employs Python programming to automate the process of converting handwritten text from images into digital, machine-readable text.

## Features

- **Capture Screen**: Capture handwritten digit drawings from the screen using the "Open Paint and capture the screen" button.
- **Generate Dataset**: Generate a dataset of captured images for training the model using the "Generate dataset" button.
- **Train Model**: Train a Support Vector Machine (SVM) model using the generated dataset, save it, and calculate accuracy using the "Train the model, save it, and calculate accuracy" button.
- **Live Prediction**: Perform live digit predictions by drawing on the screen and getting immediate predictions using the "Live prediction" button.

## Dependencies

This project relies on the following external libraries and modules:

- tkinter: Python's standard GUI library
- pyscreenshot: For taking screenshots
- os: For interacting with the operating system
- cv2 (OpenCV): For image processing and computer vision
- csv: For reading and writing CSV files
- glob: For file searching using wildcards
- pandas: For data manipulation and analysis
- scikit-learn (sklearn): For machine learning tools
- joblib: For saving and loading Python objects
- numpy: For numerical computations

## Installation

1. Clone this repository to your local machine.
2. Install the required dependencies.
3. Run the script `GUI HDR.py` to start the GUI application.

## Usage

1. Open the GUI application.
2. Use the provided buttons to perform various actions such as capturing screen drawings, generating a dataset, training a model, and making live predictions.

## Note

- Make sure to adjust any file paths, directory names, or environment-specific paths as needed to ensure the project works on your system.
