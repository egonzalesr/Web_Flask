from flask import Blueprint, render_template, request
from flask import jsonify
from decouple import config
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# Mailer Configuration
smtp_server = config("MAIL_SERVER")
smtp_port = config("MAIL_PORT")
smtp_username = config("MAIL_USERNAME")
smtp_password = config("MAIL_PASSWORD")

landingIndex = Blueprint("landingIndex", __name__)


@landingIndex.route("/")
def index():
    data = {"title": "Inicio", "page": "index"}
    return render_template("site/index.html", data=data)


@landingIndex.route("/nosotros")
def nosotros():
    data = {"title": "Nosotros", "page": "index"}

    return render_template("site/nosotros.html", data=data)


@landingIndex.route("/contacto")
def contacto():
    data = {"title": "Contactanos", "page": "contacto"}
    return render_template("site/contacto.html", data=data)


@landingIndex.route("/equipo")
def equipo():
    data = {"title": "Equipo", "page": "equipo"}
    return render_template("site/equipo.html", data=data)


#############################################################


# Subpages #
@landingIndex.route("/virtualizacion")
def virtualizacion():
    data = {"title": "Virtualizacion", "page": "virtualizacion"}
    return render_template("site/virtualizacion.html", data=data)


@landingIndex.route("/redes")
def redes():
    data = {"title": "Redes", "page": "redes"}
    return render_template("site/redes.html", data=data)


@landingIndex.route("/computo")
def computo():
    data = {"title": "Computo", "page": "computo"}
    return render_template("site/computo.html", data=data)


@landingIndex.route("/datacenter")
def datacenter():
    data = {"title": "Data center", "page": "datacenter"}
    return render_template("site/datacenter.html", data=data)


@landingIndex.route("/server")
def server():
    data = {"title": "Servidores", "page": "server"}
    return render_template("site/server.html", data=data)


@landingIndex.route("/tic")
def tic():
    data = {"title": "Soporte TIC", "page": "tic"}
    return render_template("site/tic.html", data=data)


# Mails


@landingIndex.route("/formulario_contacto", methods=["GET", "POST"])
def formulario_contacto():
    response_data = {"success": False, "message": "Solicitud Enviada con éxito"}
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("mail")
        phone = request.form.get("phone")
        message = request.form.get("message")

        msg = MIMEText(message)
        msg["Subject"] = f"Solicitud de contacto de {name}"
        msg["From"] = smtp_username
        msg["To"] = email

        try:
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.sendmail(smtp_username, [email], msg.as_string())
            server.quit()
        except Exception as e:
            error_message = str(e)

        response_data = {"success": True, "message": "Solicitud Enviada con éxito"}
        return jsonify(response_data)

    return


@landingIndex.route("/formulario_boletin", methods=["GET", "POST"])
def formulario_boletin():
    response_data = {"success": False, "message": "Solicitud Enviada con éxito"}
    if request.method == "POST":
        email = request.form.get("SubscribeMail")
        message = f"El email {email} se quiere recibir nuestro boletín"
        msg = MIMEMultipart()
        msg.attach(MIMEText(message, "plain"))
        msg["Subject"] = "Nuevo Boletín"
        msg["From"] = smtp_username
        msg["To"] = smtp_username

        try:
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.sendmail(smtp_username, [smtp_username], msg.as_string())
            server.quit()
        except Exception as e:
            error_message = str(e)

        response_data = {"success": True, "message": "Solicitud Enviada con éxito"}
        return jsonify(response_data)

    return
