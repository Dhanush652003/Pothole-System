# Pothole-Detection-And-Repair-Management-System

## Overview
This project aims to develop a pothole detection system utilizing the YOLOv8 object detection algorithm. Potholes pose significant risks to road users and can cause damage to vehicles. Automating their detection can aid in timely repairs, thereby enhancing road safety and minimizing infrastructure damage.

## Features

### 1. Pothole Detection
The Pothole Detection feature utilizes the YOLOv8 object detection algorithm to identify and locate potholes on roads. Potholes pose significant risks to road users and can cause damage to vehicles. This feature aids in timely repairs, thereby enhancing road safety and minimizing infrastructure damage.

### 2. Concrete Strength Estimation
The Concrete Strength Estimation feature allows users to estimate the strength of concrete structures. It includes functionalities for data visualization, data information, and estimation. Understanding concrete strength is crucial for assessing the durability and stability of infrastructure projects.

### 3. Asphalt Quality Detection
The Asphalt Quality Detection feature assesses the quality of asphalt used in road construction. It includes functionalities for data loading, prediction, and data information. Evaluating asphalt quality is essential for ensuring the longevity and performance of road surfaces.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Dataset](#dataset)
- [Training](#training)
- [Evaluation](#evaluation)
- [License](#license)

## Installation
To set up the project locally, follow these steps:
1. Clone the repository:
   ```bash
   git clone https://github.com/Dhanush653/Pothole-Detection-And-Repair-Management-System.git

Navigate into the project directory:
cd Pothole-Detection-And-Repair-Management-System

Install dependencies:
- pip install opencv-contrib-python-headless
- pip install ultralytics
- pip install streamlit==1.26.0
- pip install seaborn
- pip install numpy
- pip install matplotlib
- pip install pandas
- pip install scikit_learn
       (or)
- pip install -r requirements.txt

## Usage
Train the YOLOv8 model using the provided dataset or your custom dataset. Use the training script and specify the configuration file as an argument

To run the pothole detection system, execute the following command:
- streamlit run App.py

## Dataset
You can use your own dataset for training the model. Ensure that the dataset follows the required format compatible with YOLOv8. If you don't have a dataset, consider acquiring one from publicly(Kaggle or Roboflow) available sources or create your own dataset.

## Training
Training the YOLOv8 model involves configuring the model architecture, specifying hyperparameters, and providing the dataset. Use the configuration file to initiate the training process. Monitor the training progress and adjust hyperparameters as necessary to achieve better performance.

## Evaluation
Evaluate the trained model's performance using metrics such as mean Average Precision (mAP), Intersection over Union (IoU), etc. Use a separate validation dataset or split your dataset into training and validation subsets to assess the model's generalization ability.

## License
This project is licensed under the MIT License, which means you are free to use, modify, and distribute the code for commercial or non-commercial purposes. Refer to the LICENSE file for more information.

Dhanush653. This README provides detailed instructions for installation, usage, dataset handling, training, evaluation, contributing, and licensing of the project.
