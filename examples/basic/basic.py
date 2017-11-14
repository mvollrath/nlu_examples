#!/usr/bin/env python3
# Toy example of categorizing phrases with a neural network.
# Each phrase may describe either an animal or a place.

from keras.models import Sequential
from keras import layers
from keras import optimizers
import numpy as np

# Our language only has 3 words:
# dirty, dog and park.

# Each training example is a vector representing the entire vocabulary.
# If a word exists in the phrase, that element is a 1.
# Otherwise, it is a 0.

training_X = np.array([
    [0, 1, 0],  # dog
    [0, 0, 1],  # park
    [1, 1, 1],  # dirty dog park
    [1, 1, 0],  # dirty dog
    [0, 1, 1],  # dog park
    [1, 0, 1],  # dirty park
])

# We are classifying each phrase into one of two categories:
# animal or place.
# Output categories are vectorized much like our input word vectors.

training_Y = np.array([
    [1, 0],  # dog = animal
    [0, 1],  # park = place
    [0, 1],  # dirty dog park = place
    [1, 0],  # dirty dog = animal
    [0, 1],  # dog park = place
    [0, 1],  # dirty park = place
])

# Since we only have a handful of training examples, crank up the learning rate.

optimizer = optimizers.RMSprop(lr=0.08)

# Build our simple model, which only has an output layer with two neurons.

model = Sequential()
model.add(layers.Dense(2, input_shape=(3,), activation='softmax'))

model.compile(
    optimizer=optimizer,
    loss='binary_crossentropy',
    metrics=['accuracy'],
)
model.summary()

# Train the model on our training dataset.

model.fit(
    x=training_X,
    y=training_Y,
    epochs=20,
)

# Evaluate the accuracy of our model against the training dataset (again).
# Ideally we would evaluate a previously-unseen validation data set.

print('evaluating model...')
results = model.evaluate(
    x=training_X,
    y=training_Y,
)
print('loss: {:.6f} accuracy: {}%'.format(results[0], results[1] * 100))

# Predict each training example and output the (relative) confidence.
# Ideally we would predict a previously-unseen validation data set.

predictions = model.predict(training_X)

words = [
    'dirty',
    'dog',
    'park',
]
classes = [
    'animal',
    'place',
]

for i in range(len(predictions)):
    x = training_X[i]
    y = predictions[i]
    phrase = ' '.join([words[j] for j in range(len(words)) if x[j] == 1])
    confidence = max(y)
    classification = classes[list(y).index(confidence)]
    print('{} => {} ({:.2f}%)'.format(phrase, classification, confidence * 100))
