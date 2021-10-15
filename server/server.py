from flask import Flask

app = Flask('app')

@app.route('/')
def hello():
    return "Hello"

app.run('0.0.0.0')