from flask import Flask
from controllers.cursos import bp as cursos_bp
from controllers.estudiantes import bp as estudiantes_bp

app = Flask(__name__)
app.secret_key = "clave_estudiantes_cursos"
app.register_blueprint(cursos_bp)
app.register_blueprint(estudiantes_bp)

if __name__ == "__main__":
    app.run(debug=True)