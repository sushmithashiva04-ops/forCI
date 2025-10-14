from flask import Flask, jsonify
from flask_cors import CORS
# trial
app = Flask(__name__)
CORS(app)  # allow frontend to access API

@app.route('/')
def home():
    return jsonify({"message": "Hello from backend!"})

@app.route('/data')
def data():
    return jsonify({"data": [1, 2, 3, 4, 5]})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
