#!/usr/bin/python3
"""Flask web application dev
listening on 0.0.0.0, port 5000"""

from flask import Flask

app = Flask("__name__")


@app.route('/', strict_slashes=False)
def root():
    """Displays a given text"""
    return ("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays HBNB"""
    return ("HBNB")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
