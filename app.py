from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Enable debug mode
app.config["DEBUG"] = True

@app.route('/translate', methods=['POST'])
def translate():
    try:
        # Get the incoming JSON data
        data = request.get_json()
        print(f"Received data: {data}")  # Log incoming data

        # Check if the data is valid
        if not data:
            return jsonify({"error": "Invalid or missing JSON data"}), 400
        
        # Extract parameters from the incoming data
        text = data.get("text")
        source = data.get("source")
        target = data.get("target")

        # Ensure all required fields are present
        if not text or not source or not target:
            return jsonify({"error": "Missing required fields (text, source, target)"}), 400

        # Dummy translation logic for testing (you can replace this with actual translation logic)
        translated_text = f"Translated '{text}' from {source} to {target}"

        # Return the translated text as a JSON response
        return jsonify({"translated_text": translated_text})

    except Exception as e:
        # Log the exception for debugging
        print(f"Error: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    # Ensure the app is running on the correct host and port for Render
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
