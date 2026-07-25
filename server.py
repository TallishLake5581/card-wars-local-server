from flask import Flask, jsonify, request, send_from_directory

app = Flask(__name__)

@app.route('/b/ss/<path:subpath>', methods=['GET', 'POST'])
def handle_analytics(subpath):
    return "1", 200, {'Content-Type': 'text/plain'}

@app.route('/api/config', methods=['GET'])
def game_config():
    response_data = {
        "status": "success",
        "message": "Local server connected successfully"
    }
    return jsonify(response_data), 200

@app.route('/persist/static/manifest.json')
def serve_manifest():
    return jsonify({
        "status": "success",
        "version": "1.0",
        "assets": []
    })

@app.route('/persist/static/<path:filename>')
def serve_static_files(filename):
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
