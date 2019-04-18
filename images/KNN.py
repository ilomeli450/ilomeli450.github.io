from __future__ import print_function
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
from sklearn import datasets
from skimage import exposure
import numpy as np
import imutils
import cv2
import sklearn
import mnist_demo
from datetime import datetime

k = 5
IMAGE_SIZE = 28

# Loading data and preprocess the data
testX, testY = mnist_demo.read_mnist('MNIST_data/t10k-images-idx3-ubyte.gz',
                                'MNIST_data/t10k-labels-idx1-ubyte.gz')

trainX, trainY = mnist_demo.read_mnist('MNIST_data/train-images-idx3-ubyte.gz',
                                'MNIST_data/train-labels-idx1-ubyte.gz')

trainX = trainX.reshape(-1, IMAGE_SIZE*IMAGE_SIZE).astype(np.float32)
trainX = trainX * (2.0/255.0) - 1.0
trainY = trainY.reshape(-1, 1).ravel()

testX = testX.reshape(-1, IMAGE_SIZE*IMAGE_SIZE).astype(np.float32)
testX = testX * (2.0/255.0) - 1.0
testY = testY.reshape(-1, 1).ravel()

# Choose the last 10000 training samples to estimate the training error,
# since it is costly to run through all 60,000 images using KNN
trainXslice = trainX[59000:,]
trainYslice = trainY[59000:,]

print("Data Prep Done!")

# Now, loading the model

model = KNeighborsClassifier(n_neighbors=k)

trainStart = datetime.now()
model.fit(trainX, trainY)
train_time = datetime.now() - trainStart

print("Done fitting!")

# Estimating the training error
trainYPredict = model.predict(trainXslice)
print(classification_report(trainYslice, trainYPredict))

# Estimating the test error
testStart = datetime.now()
testYPredict = model.predict(testX)
test_time = datetime.now() - testStart
print(classification_report(testY, testYPredict))

print("Training time: ", train_time.total_seconds())
print("Testing time: ", test_time.total_seconds())
print("k = ",k)















