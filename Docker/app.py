# app.py - a minimal flask api using flask_restful
from flask import Flask

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080")
