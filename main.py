from flask import Flask, request, jsonify
import os
import openai
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 这里启用了跨域访问
openai.api_key = "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"

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json(force=True)
    message = data.get('message')

    if not message:
        return jsonify({'error': 'No message provided.'}), 400

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{
            "role": "user",
            "content": message
        }]
    )

    response = completion.choices[0].message.content

    return jsonify({'response': response})

if __name__ == '__main__':    
    app.run(host='0.0.0.0', port=80, debug=True)
