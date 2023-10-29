from flask import Flask, render_template, request, flash, redirect, url_for
from flask import jsonify
from flask_mail import Mail, Message
from decouple import config
import smtplib
from email.mime.text import MIMEText


app = Flask(__name__)

app.secret_key = config('SECRET_KEY')

#Mailer Configuration
smtp_server = config('MAIL_SERVER')
smtp_port = config('MAIL_PORT')
smtp_username = config('MAIL_USERNAME')
smtp_password = config('MAIL_PASSWORD')


# Main Pages #
@app.route("/", methods=["GET", "POST"])
def index():
    data = {"title": "Inicio", "page": "index"}
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
            response_data["success"] = True
        except Exception as e:
            error_message = str(e)
        
        return jsonify(response_data) 

         

    return render_template("site/index.html", data=data)


@app.route("/nosotros", methods=["GET", "POST"])
def nosotros():
    data = {"title": "Nosotros", "page": "index"}
    
    return render_template("site/nosotros.html", data=data)


@app.route("/contacto", methods=["GET", "POST"])
def contacto():
    data = {"title": "Contactanos", "page": "contacto"} 

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
    return render_template("site/contacto.html", data=data)


@app.route("/equipo", methods=["GET", "POST"])
def equipo():
    data = {"title": "Equipo", "page": "equipo"}    
    return render_template("site/equipo.html", data=data)


#############################################################


# Subpages #
@app.route("/virtualizacion", methods=["GET", "POST"])
def virtualizacion():
    data = {"title": "Virtualizacion", "page": "virtualizacion"}    
    return render_template("site/virtualizacion.html", data=data)


@app.route("/redes", methods=["GET", "POST"])
def redes():
    data = {"title": "Redes", "page": "redes"}    
    return render_template("site/redes.html", data=data)


@app.route("/computo", methods=["GET", "POST"])
def computo():
    data = {"title": "Computo", "page": "computo"}    
    return render_template("site/computo.html", data=data)


@app.route("/datacenter", methods=["GET", "POST"])
def datacenter():
    data = {"title": "Data center", "page": "datacenter"}    
    return render_template("site/datacenter.html", data=data)


@app.route("/server", methods=["GET", "POST"])
def server():
    data = {"title": "Servidores", "page": "server"}    
    return render_template("site/server.html", data=data)


@app.route("/tic", methods=["GET", "POST"])
def tic():
    data = {"title": "Soporte TIC", "page": "tic"}    
    return render_template("site/tic.html", data=data)


# Error Handler


@app.errorhandler(404)
def page_not_found(e):
    return render_template("site/404.html"), 404


if __name__ == "__main__":
    app.run(debug="true")
