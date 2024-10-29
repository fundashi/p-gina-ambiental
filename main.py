from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<a href="/miruta"> Ir siguiente ruta </a>'


@app.route("/miruta")


def prueba() :
    return '''
            <form action= "/formulario" method="post">

            <input type="text" name="nombre">

            <button type="submit"> Enviar </button>

            </form>
          '''

@app.route("/formulario", methods=["post"])
def control():
    anime = request.form.get("nombre")
    return f'<h1> Hola, bienvenido {anime} </h1>'

app.run(debug=True)