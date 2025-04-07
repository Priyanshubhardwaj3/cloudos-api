import tensorflow as tf
import numpy as np

# Example model
X = np.array([[20, 40], [50, 60], [80, 90]])
y = np.array([1, 2, 3])

model = tf.keras.Sequential([
    tf.keras.layers.Dense(8, activation='relu', input_shape=(2,)),
    tf.keras.layers.Dense(1)
])
model.compile(optimizer='adam', loss='mse')
model.fit(X, y, epochs=10)

model.save("model.keras")  # Instead of .h5

