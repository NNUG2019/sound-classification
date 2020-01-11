import tensorflow as tf
from tensorflow import keras
import numpy as np
from matplotlib import pyplot as plt
from datasetTest import X_testdata #ladowanie obrazkow do testowania
from masklabels import dumperlabels #ladowanie labelsów od testowania

# Recreate the exact same model, including its weights and the optimizer
new_model = tf.keras.models.load_model('model.h5')

print(X_testdata.shape)
predictions = new_model.predict(X_testdata)
plt.imshow(X_testdata[0])
print(dumperlabels[0])
plt.imshow(X_testdata[4])