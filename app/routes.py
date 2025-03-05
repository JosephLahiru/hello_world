from flask import Blueprint

main_routes = Blueprint('main_routes', __name__)

@main_routes.route('/hello')
def hello():
    return "hello world"