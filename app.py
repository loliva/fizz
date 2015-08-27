from flask import Flask, request, render_template
from func import fizzbuzz

app = Flask(__name__)

@app.route ('/')
def hello_world():
    return 'Hello World :)'

@app.route('/<val>', methods=['POST', 'GET'])
def main(val):
    if request.method == 'POST':
        resultado = fizzbuzz(val)
        return render_template('default.html', resultado=resultado)

    return render_template('default.html')

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')

