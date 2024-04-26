from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    print("Test CI/CD action")
    return 'Hello, Docker!'