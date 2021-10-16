from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.applications.vgg16 import preprocess_input
from tensorflow.keras.applications.vgg16 import decode_predictions
from tensorflow.keras.applications.vgg16 import VGG16

# Load Keras VGG16 Model
model = VGG16()
# Load Test Image
image = load_img('mug.jpg', target_size=(224, 224))

# Image Pre Processing

image = img_to_array(image)
image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
image = preprocess_input(image)

# Predict probabilities vector
yhat = model.predict(image)
# Convertion of probabilities to class labels
label = decode_predictions(yhat)
# Retrieve the most likely result, e.g. highest probability
label = label[0][0]
# Print classification
print('%s (%.2f%%)' % (label[1], label[2]*100))