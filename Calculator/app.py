from flask import Flask, render_template
from handler import Calculator

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_index():
    return render_template('index.html')

@app.route('/number/<string:number>', methods=['GET'])
def get_number(number):
    result = Calculator.get_number(number=number)
    return render_template('index.html', result=result)

@app.route('/operator/<string:operator>', methods=['GET'])
def get_operator(operator):
    result = Calculator.get_operator(operator=operator)
    return render_template('index.html', result=result)

@app.route('/calculate', methods=['GET'])
def get_result():
    result = Calculator.get_result()
    return render_template('index.html', result=result)

@app.route('/cancel', methods=['GET'])
def clear_screen():
    result = Calculator.clear_screen()
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
