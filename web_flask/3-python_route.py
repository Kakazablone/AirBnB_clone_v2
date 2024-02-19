#!/usr/bin/python3
"""Flask web application dev"""

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


@app.route("/c/<text>", strict_slashes=False)
def c_fun(text):
    """Displays C followed by the value in text variable"""
    return "C {}".format(text.replace("_", " "))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    """Displays Python followed by the value in text variable"""
    return "Python {}".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
