from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/persist/static/manifest.json")
def m():
  return jsonify({"status": "success", "files": []})


@app.route("/persist/static/<path:f>")
def s(f):
  return "", 200


@app.route("/")
def h():
  return "OK", 200


if __name__ == "__main__":
  app.run(host="0.0.0.0", port=10000)
