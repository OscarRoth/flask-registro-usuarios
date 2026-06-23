from flask import Flask, render_template, request
import re

app = Flask(__name__)

usuarios = []

@app.route('/', methods=['GET', 'POST'])
def formulario():
    errores = []

    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        edad = request.form['edad']
        carrera = request.form['carrera']
        comentarios = request.form['comentarios']

        if edad == '':
            errores.append('La edad es obligatoria.')

        if carrera == '':
            errores.append('Debe seleccionar una carrera.')

        if nombre.strip() == '':
            errores.append('El nombre no puede estar vacío.')

        patron_email = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(patron_email, email):
            errores.append('El formato del email no es válido.')

        if errores:
            return render_template(
                'formulario.html',
                errores=errores,
                nombre=nombre,
                email=email,
                edad=edad,
                carrera=carrera,
                comentarios=comentarios
            )
        
        usuarios.append({
            'nombre': nombre,
            'email': email,
            'edad': edad,
            'carrera': carrera,
            'comentarios': comentarios
        })

        return render_template(
            'resultado.html',
            nombre=nombre,
            email=email,
            edad=edad,
            carrera=carrera,
            comentarios=comentarios
        )

    return render_template('formulario.html')

@app.route('/usuarios')
def listar_usuarios():
    return render_template('usuarios.html', usuarios=usuarios)
    
if __name__ == '__main__':
    app.run(debug=True)