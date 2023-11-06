from flask import Flask, render_template
from routes.landingIndex import landingIndex
from decouple import config


app = Flask(__name__)

app.secret_key = config("SECRET_KEY")

# Routes

app.register_blueprint(landingIndex)


# Error Handler
@app.errorhandler(404)
def page_not_found(e):
    return render_template("site/404.html"), 404


if __name__ == "__main__":
    app.run(debug="true")
