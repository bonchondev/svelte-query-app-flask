from pathlib import Path
from flask import Flask, send_from_directory
from flask_cors import CORS

app = Flask(__name__)

CORS(app)


@app.get("/")
def home():
    return {"message": "information"}


@app.get("/data")
def data():
    return {"message": "data"}


@app.get("/docs")
def docs():
    files = Path("static") / "docs"
    return {"documents": [doc.name for doc in files.iterdir() if doc.is_file()]}


@app.get("/output/<path:path>")
def output(path):
    return send_from_directory("static/docs", path)


if __name__ == "__main__":
    app.run(debug=True)
