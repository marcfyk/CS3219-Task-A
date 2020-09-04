from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def get_calculation():
    x, y = int(request.args.get('x')), int(request.args.get('y'))
    return {
        'sum': x + y,
        'difference': abs(x - y),
        'product': x * y,
        'division': x / y,
        'exponent': x ** y
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5002')
