from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/b/ss/<path:subpath>', methods=['GET', 'POST'])
def handle_analytics(subpath):
    return "1", 200, {'Content-Type': 'text/html; charset=utf-8'}

@app.route('/api/config', methods=['GET', 'POST'])
def game_config():
    response_data = {
        "status": "success",
        "message": "Local server connected successfully"
    }
    return jsonify(response_data), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
