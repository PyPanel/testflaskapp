from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "This is just a test app. It doesn't do much."

if __name__ == '__main__':
    app.run()
