
from flask import Flask, request, render_template
from application.servicio import Servicio
from application.usuarios import Usuario

app = Flask(__name__, template_folder='application/templates')


@app.route('/', methods=['POST', 'GET'])
def __init__():
    # Compruebo si es un POST
    if request.method == 'POST':
        # Llamo a la clase que inicia el servicio
        Servicio(request.json)
        return render_template('home.html')

    # Si es una peticion GET le devuelvo la home html
    if request.method == 'GET':
        return render_template('home.html')


@app.route('/listado_usuarios', methods=['GET'])
def list_users():
    usuarios = Usuario()
    misusuarios = usuarios.listadoUsuarios()
    return render_template('listado_usuarios.html', usuarios=misusuarios)


if __name__ == "__main__":
    app.run()
