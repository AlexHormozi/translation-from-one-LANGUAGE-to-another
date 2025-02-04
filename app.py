from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# Set LibreTranslate URL (you can change this to your own instance if you are self-hosting)
LIBRE_TRANSLATE_URL = "https://libretranslate.de/translate"

@app.route('/translate', methods=['POST'])
def translate():
    try:
        data = request.get_json()
        print(f"Received data: {data}")  # Log incoming data

        if not data:
            return jsonify({"error": "Invalid or missing JSON data"}), 400

        # Extract parameters from the request body
        text = data.get("text")
        source = data.get("source")
        target = data.get("target")

        # Validate the parameters
        if not text or not source or not target:
            return jsonify({"error": "Missing required fields (text, source, target)"}), 400

        # Prepare the payload for the LibreTranslate API
        payload = {
            'q': text,
            'source': source,
            'target': target
        }

        # Send POST request to LibreTranslate API
        response = requests.post(LIBRE_TRANSLATE_URL, data=payload)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            translated_text = response.json()['translatedText']
            return jsonify({"translated_text": translated_text})
        else:
            return jsonify({"error": "Translation failed, try again later."}), 500

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
