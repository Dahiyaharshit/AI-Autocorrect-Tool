from flask import Flask, render_template, request, jsonify
from backend.autocorrect import correct_text

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/correct', methods=['POST'])
def correct():

    data = request.get_json()

    text = data['text']

    corrected = correct_text(text)

    original_words = text.split()
    corrected_words = corrected.split()

    changes = 0

    for i in range(min(len(original_words), len(corrected_words))):
        if original_words[i] != corrected_words[i]:
            changes += 1

    return jsonify({
        "original": text,
        "corrected": corrected,
        "changes": changes
    })

if __name__ == '__main__':
    app.run(debug=True)