from numpy import loadtxt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense


# Load Dataset From File
dataset = loadtxt('pima-indians-diabetes.csv', delimiter=',')

# Split into input (X) and output label (y) variables
X = dataset[:,0:8]
y = dataset[:,8]

# Define Sequential Keras model
model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# Compiling Sequential Keras model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Training of Sequential Keras Model
model.fit(X, y, epochs=150, batch_size=10)

# Evaluation of Sequential Keras Model 
_, accuracy = model.evaluate(X, y)
print('Accuracy: %.2f' % (accuracy*100))