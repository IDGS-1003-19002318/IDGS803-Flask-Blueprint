import flask


app = flask.Flask(__name__)
app.config['DEBUG'] = True


from Alumnos.routes import Alumnos
from Directivos.routes import Dire
from Maestros.routes import Maestros

@app.route("/", methods= ['GET'])
def home():
    return flask.jsonify({'Datos' : 'Home'})


if __name__ == '__main__':
    app.run(debug=True, port=3000)
