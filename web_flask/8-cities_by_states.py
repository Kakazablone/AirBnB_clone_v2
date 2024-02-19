#!/usr/bin/python3
"""Importing Flask to run the web app"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/cities_by_states/', strict_slashes=False)
def states_list():
    """list states from database"""
    return render_template('8-cities_by_states.html',
                           states=storage.all(State))


app.run(host='0.0.0.0', port=5000)


@app.teardown_appcontext
def teardown_appcontext(exception):
    storage.close()
