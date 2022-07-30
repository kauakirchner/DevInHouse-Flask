from flask import Flask
from src.app.controllers.userRegister import users

def routes(app: Flask):
    app.register_blueprint(users)