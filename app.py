from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mail import Mail, Message
from decouple import config


app = Flask(__name__)

app.secret_key = config('SECRET_KEY')

#  Configuración de Flask-Mail para enviar correos electrónicos #

app.config["MAIL_SERVER"] = config('MAIL_SERVER')
app.config["MAIL_PORT"] = config('MAIL_PORT')
app.config["MAIL_USERNAME"] = config('MAIL_USERNAME')
app.config["MAIL_PASSWORD"] = config('MAIL_PASSWORD')
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USE_SSL"] = False

mail = Mail(app)


# Main Pages #
@app.route("/", methods=["GET", "POST"])
def index():
    data = {"title": "Inicio", "page": "index"}

    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("mail")
        phone = request.form.get("phone")
        message = request.form.get("message")

        try:
            msg = Message('Solicitud de contacto', sender='tu_correo_electronico', recipients=['correo_destino'])
            msg.body = f'Nombre: {name}\nEmail: {email}\nTeléfono: {phone}\nMensaje: {message}'
            mail.send(msg)
            flash("Solicitud enviada con éxito", "success")
        except Exception as e:
            flash("No se pudo enviar el mensaje", "error")

        return redirect(url_for("index"))

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

        try:
            msg = Message('Solicitud de contacto', sender='tu_correo_electronico', recipients=['correo_destino'])
            msg.body = f'Nombre: {name}\nEmail: {email}\nTeléfono: {phone}\nMensaje: {message}'
            app.send(msg)
            flash("Solicitud enviada con éxito", "success")
        except Exception as e:
            flash("No se pudo enviar el mensaje", "error")

        return redirect(url_for("contacto"))
      
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
