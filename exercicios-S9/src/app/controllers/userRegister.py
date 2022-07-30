from flask import Blueprint

users = Blueprint('users', __name__, url_prefix="/user")

@users.route("/", methods=['GET'])

def list_users():
    return {"data": ["Kaua", "kaua@email.com", "12345678", "12345678901"] }


