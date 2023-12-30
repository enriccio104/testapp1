from flask import Flask, request, jsonify

app = Flask(__name__)
messages = []

@app.route('/send', methods=['POST'])
def send_message():
    data = request.get_json()
    user = data.get('user')
    message = data.get('message')

    if user and message:
        messages.append({'user': user, 'message': message})
        return jsonify({'status': 'Message sent successfully'})
    else:
        return jsonify({'status': 'Error: Missing user or message'}), 400

@app.route('/get_messages', methods=['GET'])
def get_messages():
    return jsonify({'messages': messages})

if __name__ == '__main__':
    app.run(debug=True)
