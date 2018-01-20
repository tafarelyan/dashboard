from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    payload = {
        'type': 'line',
        'data': {
            'labels': ['One', 'Two', 'Three', 'Four', 'Five'],
            'datasets': [{
                'label': 'Test Line Chart',
                'data': [1, 2, 3, 4, 5]
            }],
        },
        'options': '',
    }
    return render_template('index.html', payload=payload)

if __name__ == '__main__':
    app.run(debug=True)
