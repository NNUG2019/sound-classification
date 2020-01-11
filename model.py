from datasetTrain import X_traindata #ladowanie obrazkow do trenowania
from labelsService import labelsTrain #ladowanie labelsów do trenowania
from datasetTest import X_testdata #ladowanie obrazkow do testowania
from masklabels import dumperlabels #ladowanie labelsów od testowania
import tensorflow as tf
from tensorflow import keras
import numpy as np
from matplotlib import pyplot as plt


mnist = keras.datasets.mnist
print('Data loading...')
(X_traindata, labelsTrain), (X_testdata, dumperlabels) = mnist.load_data()
print('Done!')

# print(X_traindata.shape)
# print(X_testdata.shape)

X_traindata = X_traindata.reshape(60000, 28, 28, 1)
X_testdata = X_testdata.reshape(10000, 28, 28, 1)
X_testdata = X_testdata.astype(np.float)
print('Reshape sucess!')


"""
model_cnn = keras.Sequential([
    keras.layers.Conv2D(32, 3, activation="relu", input_shape=(28, 28, 1)),
    keras.layers.Conv2D(64, 3, activation="relu"),
    keras.layers.MaxPooling2D((2, 2)),
    keras.layers.Dropout(0.25),
    keras.layers.Flatten(),
    keras.layers.Dense(128, activation="relu"),
    keras.layers.Dropout(0.4),
    keras.layers.Dense(10, activation='softmax')
])

model_cnn.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
model_cnn.summary()
model_cnn.fit(X_traindata, labelsTrain, validation_split=0.1, epochs=10)

model_cnn.save("model.h5")
print("Model saved to file model.h5")

test_loss, test_acc = model_cnn.evaluate(X_testdata,  dumperlabels, verbose=2)
print('\nTest accuracy:', test_acc)
"""
# Recreate the exact same model, including its weights and the optimizer
new_model = tf.keras.models.load_model('model.h5')

X_testdata = X_testdata / 255
print(dumperlabels[10:])
predictions = new_model.predict(X_testdata)
type(predictions)
print(predictions.shape)
print(predictions[0])

im=X_testdata[24].reshape(1,28,28,1)
print(new_model.predict(im))

