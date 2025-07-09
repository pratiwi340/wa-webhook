from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/')
def index():
    return 'Webhook WA aktif!'

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("Pesan diterima:", data)
    return {'status': 'OK'}, 200

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
