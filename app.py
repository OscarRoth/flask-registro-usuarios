from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def formulario():
    errores = []

    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']

        if nombre.strip() == '':
            errores.append('El nombre no puede estar vacío.')

        patron_email = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(patron_email, email):
            errores.append('El formato del email no es válido.')

        if errores:
            return render_template('formulario.html', errores=errores, nombre=nombre, email=email)

        return render_template('resultado.html', nombre=nombre, email=email)

    return render_template('formulario.html')
    
if __name__ == '__main__':
    app.run(debug=True)