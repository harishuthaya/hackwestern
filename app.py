from flask import Flask, render_template, request

DEVELOPMENT_ENV = True

app = Flask(__name__)

text_content = ""

app_data = {
    "name": "medi-sight"
}


@app.route("/")
def index():
    return render_template("index.html", app_data=app_data)

@app.route("/login")
def login():
    return render_template("login.html", app_data=app_data)

@app.route("/signup")
def signup():
    return render_template("signup.html", app_data=app_data)


if __name__ == "__main__":
    app.run(debug=DEVELOPMENT_ENV, host='0.0.0.0')
