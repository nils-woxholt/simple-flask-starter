from flask import Flask

app = Flask(__name__)

from app import api

if __name__ == "__main__":
    app.run()