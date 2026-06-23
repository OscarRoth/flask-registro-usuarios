from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def formulario():
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        return render_template('resultado.html', nombre=nombre, email=email)

    return render_template('formulario.html')

if __name__ == '__main__':
    app.run(debug=True)