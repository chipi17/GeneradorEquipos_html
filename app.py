from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nombres = request.form.getlist('nombre')
        random.shuffle(nombres)
        mitad = len(nombres) // 2
        equipo_A = nombres[:mitad]
        equipo_B = nombres[mitad:]
        return render_template('equipos.html', equipo_A=equipo_A, equipo_B=equipo_B)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
