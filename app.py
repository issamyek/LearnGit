import os
from flask import Flask
def create_app(test_config=None):

    app = Flask(__name__)

    @app.route('/')
    def get_greeting():
        greeting = "Hello" 
        return greeting


    return app

app = create_app()

if __name__ == '__main__':
    app.run()