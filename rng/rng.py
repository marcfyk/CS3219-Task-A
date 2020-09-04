from random import randint
from flask import Flask

app = Flask(__name__)

@app.route('/')
def get_numbers():
    lower_bound = 1
    upper_bound = 10
    return {
        'x': randint(lower_bound, upper_bound),
        'y': randint(lower_bound, upper_bound)
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5001')
