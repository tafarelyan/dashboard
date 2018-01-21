from flask import Flask, jsonify, render_template

app = Flask(__name__)


@app.route('/')
def index():
    data = {
        'name': 'Tafarel',
        'age': 23,
    }
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
