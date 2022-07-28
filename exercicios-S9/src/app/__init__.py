import os

from flask import Flask

from src.app.config import app_config

app = Flask(__name__)
app.config.from_object(app_config[os.getenv('FLASK_ENV')])

@app.route("/")
def teste():
    return "<p>Meu teste</p>"
    

@app.route("/developer")
def developer():
    return  "<p>Developer Front End</p>"
