from flask import Flask, request, jsonify
from libretranslatepy import LibreTranslateAPI

app = Flask(__name__)
lt = LibreTranslateAPI("https://translate.argosopentech.com/")  # Free LibreTranslate server

@app.route('/')
def home():
    return jsonify({"message": "LibreTranslate API is running!"})

@app.route('/translate', methods=['POST'])
def translate():
    data = request.json
    text = data.get("text")
    source_lang = data.get("source", "auto")  # Auto-detect if not provided
    target_lang = data.get("target", "en")  # Default to English

    if not text:
        return jsonify({"error": "No text provided"}), 400

    try:
        translated_text = lt.translate(text, source_lang, target_lang)
        return jsonify({"translated_text": translated_text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
