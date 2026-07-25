import os
from flask import Flask, request
from flask import send_from_directory, jsonify

app = Flask(__name__)


@app.route("/")
def home():
  return "Server is Running!", 200


@app.route("/persist/static/<path:filename>")
def get_file(filename):
  print(f"File requested: {filename}")
  return send_from_directory("persist/static", filename)


@app.errorhandler(404)
def not_found(e):
  print(f"Missing path: {request.path}")
  return jsonify({"status": "error"}), 404


if __name__ == "__main__":
  app.run(host="0.0.0.0", port=10000)
