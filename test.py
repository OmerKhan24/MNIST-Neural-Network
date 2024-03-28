import matplotlib.pyplot as plt
import importlib.util
import os

# Get the current working directory
current_dir = os.getcwd()

filename = "neural_network.py"
spec = importlib.util.spec_from_file_location(current_dir, filename)
train = importlib.util.module_from_spec(spec)
spec.loader.exec_module(train) 

def make_predictions(X, W1, b1, W2, b2):
    _, _, _, A2 = train.forward_prop(W1, b1, W2, b2, X)
    predictions = train.get_predictions(A2)
    return predictions

def test_prediction(index, W1, b1, W2, b2):
    current_image = train.X_train[:, index, None]
    prediction = make_predictions(train.X_train[:, index, None], W1, b1, W2, b2)
    label = train.Y_train[index]
    print("Prediction: ", prediction)
    print("Label: ", label)
    
    current_image = current_image.reshape((28, 28)) * 255
    plt.gray()
    plt.imshow(current_image, interpolation='nearest')
    plt.show()

number = int(input(print("Enter the index no to test(0-1000)")))
test_prediction(number,train.W1, train.b1, train.W2, train.b2)