import os

from flask import Flask

from src.app.config import app_config
from src.app.routes import routes

app = Flask(__name__)
app.config.from_object(app_config[os.getenv('FLASK_ENV')])
routes(app)

@app.route("/")
def teste():
    return "<p>Home</p>"
    

@app.route("/dev")
def developer():
    return  "<p>Developer</p>"
