from flask import Flask
from .routes import main_routes


app = Flask(__name__)
app.register_blueprint(main_routes)


if __name__ == '__main__':
    app.run(port=5000, host="0.0.0.0", debug=True)
