#!/usr/bin/python3
"""Flask web application dev"""

from flask import Flask, render_template, url_for

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


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """Displays “n is a number” only if n is an integer"""
    if isinstance(n, int):
        return "{} is a number".format(n)
    

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Displays an HTML page only if n is integer"""
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
