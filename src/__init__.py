from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/heartbeat', methods=['GET'])
def heartbeat():
    return jsonify({
        "status": "Ok",
        "message": "badum badum badum"
        }), 200


