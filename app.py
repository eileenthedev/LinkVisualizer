import json

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/data')
def data():
    with open('links.json') as f:
        data = json.load(f)
    return json.dumps(data)


if __name__ == '__main__':
    app.run(debug=True)
