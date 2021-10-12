import numpy as np
import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dense, Flatten
from tensorflow.keras.utils import to_categorical


# Load Image Dataset
train_images = mnist.train_images()
train_labels = mnist.train_labels()
test_images = mnist.test_images()
test_labels = mnist.test_labels()


#Image Pre-processing

# Normalizing the images
train_images = (train_images / 255) - 0.5
test_images = (test_images / 255) - 0.5

# Reshaping the images
train_images = np.expand_dims(train_images, axis=3)
test_images = np.expand_dims(test_images, axis=3)

num_filters = 8
filter_size = 3
pool_size = 2

# Define Sequential Keras model
model = Sequential([
  Conv2D(num_filters, filter_size, input_shape=(28, 28, 1)),
  MaxPooling2D(pool_size=pool_size),
  Flatten(),
  Dense(10, activation='softmax'),
])

# Compilating Sequential Keras Model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Training of Sequential Keras Model
model.fit(train_images, to_categorical(train_labels), epochs=3, validation_data=(test_images, to_categorical(test_labels)))

# Prediction of First Five Image's Label
predictions = model.predict(test_images[:5])

# Print Model's predictions & actual labels
print(np.argmax(predictions, axis=1)) 
print(test_labels[:5])