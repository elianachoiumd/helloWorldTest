from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World from elie choi!'


if __name__ == '__main__':
    app.run()

@app.route('hello')
def hello():
    return render_template('helloWorld.html')