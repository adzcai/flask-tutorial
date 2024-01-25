from flask import Flask
app = Flask(__name__)

# an example of a *route*, a concept for organizing server endpoints
@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()
