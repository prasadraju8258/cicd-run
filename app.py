# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World! This is Rajendra and i wanted to say helllo world to all of you'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
