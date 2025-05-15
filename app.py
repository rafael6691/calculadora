from flask import Flask, render_template, request
import numpy as np
from scipy.integrate import simpson

app = Flask(__name__)

def calcular_trapecio(c, v, a, b):
    x = np.linspace(a, b, len(c))
    y = np.array(c) * np.array(v)
    return float(np.trapz(y, x))

def calcular_simpson(c, v, a, b):
    x = np.linspace(a, b, len(c))
    y = np.array(c) * np.array(v)
    return float(simpson(y, x))

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        c = list(map(float, request.form['c'].split(',')))
        v = list(map(float, request.form['v'].split(',')))
        a = float(request.form['a'])
        b = float(request.form['b'])
        metodo = request.form['metodo']
        if metodo == 'trapecio':
            Q = calcular_trapecio(c, v, a, b)
        else:
            Q = calcular_simpson(c, v, a, b)
        return render_template('result.html', Q=Q, metodo=metodo)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

