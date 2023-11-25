from flask import Flask, render_template, request
from urllib.parse import unquote
import auth

DEVELOPMENT_ENV = True
app = Flask(__name__)
conn = auth.connect_db(auth.db_config)
auth.create_users_table(conn)
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

@app.route("/patient")
def patient():
    return render_template("patient.html", app_data=app_data)

@app.route("/validate", methods=["post"])
def validate():
    encoded_username = request.args.get('username')
    decoded_username = unquote(encoded_username)
    encoded_password = request.args.get('password')
    decoded_password = unquote(encoded_password)
    is_valid = auth.check_login(conn, decoded_username, decoded_password)
    print(decoded_username)
    print(decoded_password)
    print("valid:",is_valid)
    if is_valid:
        return {"valid": "success"}
    else:
        return {"valid": "failure"}
    
@app.route("/registeruser", methods=["post"])
def registeruser():
    encoded_username = request.args.get('username')
    decoded_username = unquote(encoded_username)
    encoded_password = request.args.get('password')
    decoded_password = unquote(encoded_password)
    is_valid = auth.check_login(conn, decoded_username, decoded_password)
    print(decoded_username)
    print(decoded_password)
    print("valid:",is_valid)
    if is_valid:
        return {"valid": "success"}
    else:
        return {"valid": "failure"}

if __name__ == "__main__":
    app.run(debug=DEVELOPMENT_ENV, host='0.0.0.0', port=9000)
