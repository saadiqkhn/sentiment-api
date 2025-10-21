from flask import Flask, request, jsonify
from transformers import pipeline

# Initialize sentiment classifier
classifier = pipeline("sentiment-analysis")

app = Flask(__name__)

@app.route("/")
def health():
    return jsonify({"status": "up"})

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    text = data.get("text")

    if not text:
        return jsonify({"error": "No text provided"}), 400

    result = classifier(text)[0]
    return jsonify({
        "text": text,
        "sentiment": result["label"],
        "confidence": round(result["score"], 3)
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

