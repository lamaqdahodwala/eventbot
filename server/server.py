from flask import Flask

app = Flask('app')

@app.route('/')
def hello():
    return "Hello"

def main():
    app.run('0.0.0.0')

if __name__ == '__main__':
    main()