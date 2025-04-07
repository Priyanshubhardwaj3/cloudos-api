from flask import Flask, request, jsonify
import numpy as np
import tensorflow as tf

# Load your AI kernel
model = tf.keras.models.load_model("model.keras")

app = Flask(__name__)

@app.route("/")
def welcome():
    return "Cloud AI OS Kernel is running!"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    cpu = data.get("cpu")
    ram = data.get("ram")
    if cpu is None or ram is None:
        return jsonify({"error": "Missing CPU or RAM input"}), 400

    input_data = np.array([[cpu, ram]])
    prediction = model.predict(input_data)
    return jsonify({"priority": float(prediction[0][0])})

if __name__ == "__main__":
    app.run(debug=True)
