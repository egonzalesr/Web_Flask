from flask import Flask, render_template, request
from flask_mail import Mail, Message


app = Flask(__name__)

#  Configuración de Flask-Mail para enviar correos electrónicos #
"""
app.config["MAIL_SERVER"] = "smtp.example.com"  # Reemplaza  servidor SMTP
app.config["MAIL_PORT"] = 587  # Puerto SMTP
app.config["MAIL_USERNAME"] = "mail@mail.com"  # Dirección de correo electrónico
app.config["MAIL_PASSWORD"] = "password"  # Contraseña de correo electrónico
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USE_SSL"] = False

mail = Mail(app)


def contact():
    subject = "Nuevo cliente"
    sender = "insertar_correo"

    if request.method == "POST":
        name = request.form["name"]
        mail = request.form["mail"]
        phone = request.form["phone"]
        message = request.form["message"]

        try:
            msg = Message(subject, sender, mail)
            msg.body = message
            mail.send(msg)
            return "Correo electrónico enviado con éxito"
        except Exception as e:
            return f"Error al enviar el correo electrónico: {str(e)}"
"""


# Main Pages #
@app.route("/", methods=["GET", "POST"])
def index():
    data = {"title": "Inicio", "page": "index"}
    # contact()
    return render_template("site/index.html", data=data)


@app.route("/nosotros", methods=["GET", "POST"])
def nosotros():
    data = {"title": "Nosotros", "page": "index"}
    # contact()
    return render_template("site/nosotros.html", data=data)


# @app.route("/servicios", methods=["GET", "POST"])
# def servicios():
#    data = {"title": "Nuestros Servicios"}
#    return render_template("site/servicios.html", data=data)


@app.route("/contacto", methods=["GET", "POST"])
def contacto():
    data = {"title": "Contactanos", "page": "contacto"}
    # contact()
    return render_template("site/contacto.html", data=data)


@app.route("/equipo", methods=["GET", "POST"])
def equipo():
    data = {"title": "Equipo", "page": "equipo"}
    # contact()
    return render_template("site/equipo.html", data=data)


#############################################################


# Subpages #
@app.route("/virtualizacion", methods=["GET", "POST"])
def virtualizacion():
    data = {"title": "Virtualizacion", "page": "virtualizacion"}
    # contact()
    return render_template("site/virtualizacion.html", data=data)


@app.route("/redes", methods=["GET", "POST"])
def redes():
    data = {"title": "Redes", "page": "redes"}
    # contact()
    return render_template("site/redes.html", data=data)


@app.route("/computo", methods=["GET", "POST"])
def computo():
    data = {"title": "Computo", "page": "computo"}
    # contact()
    return render_template("site/computo.html", data=data)


@app.route("/datacenter", methods=["GET", "POST"])
def datacenter():
    data = {"title": "Data center", "page": "datacenter"}
    # contact()
    return render_template("site/datacenter.html", data=data)


@app.route("/server", methods=["GET", "POST"])
def server():
    data = {"title": "Servidores", "page": "server"}
    # contact()
    return render_template("site/server.html", data=data)


@app.route("/tic", methods=["GET", "POST"])
def tic():
    data = {"title": "Soporte TIC", "page": "tic"}
    # contact()
    return render_template("site/tic.html", data=data)


# Error Handler


@app.errorhandler(404)
def page_not_found(e):
    return render_template("site/404.html"), 404


if __name__ == "__main__":
    app.run(debug="true")
