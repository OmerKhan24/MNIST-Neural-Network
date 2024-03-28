# Neural Network Training and Testing

This repository contains Python code for training a neural network model using stochastic gradient descent and testing its performance on a dataset. The neural network architecture includes two hidden layers with ReLU activation and a softmax output layer.

## Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
   - [Training](#training-the-neural-network)
   - [Testing](#teting-the-model)
3. [Code Overview](#code-overview)
4. [License](#license)

## Installation

1. Clone the repository:
   ```bash
   git clone https://https://github.com/OmerKhan24/MNIST-Neural-Network.git

2. To run the code, you need to have Python installed on your system. Additionally, you'll need the following libraries:

- NumPy
- pandas
- matplotlib

  You can install these libraries using pip:
   ```bash
   pip install numpy pandas matplotlib

## Usage

1. Clone this repository to your local machine.
2. Navigate to the repository directory.

  ### Training the Neural Network:
  
  - Open the `neural_network.py` file in your preferred Python environment.
  - Run the script to train the neural network model.
  - Adjust the hyperparameters such as the number of iterations and learning rate as needed.
  
  ### Testing the Model:
  
  - After training, you can test the model using the provided testing functions.
  - The `test_prediction` function allows you to make predictions on specific examples from the training dataset.
  - Customize the testing function to suit your testing requirements.

## Code Overview

The main components of the code include:

- Initialization: Initializing the weights and biases for the neural network layers.
- Forward Propagation: Performing forward propagation to compute the output of the neural network.
- Back Propagation: Implementing backpropagation to calculate gradients and update the model parameters.
- Testing: Functions for testing the trained model on custom data or specific examples from the dataset.

## License

This code is provided under the [MIT License](https://github.com/OmerKhan24/MNIST-Neural-Network/blob/main/LICENSE). Feel free to use and modify it according to your needs.


