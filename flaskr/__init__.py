import os
import requests
from flask import Flask, request, render_template
import json
import psycopg2
from psycopg2 import sql
from hashlib import sha256
from urllib.parse import unquote

sys.path.append('')
import auth
from urllib.parse import unquote
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

app_data = {
    "name": "medi-sight"
}

# Database configuration
db_config = {
    'host': '34.130.250.144',
    'dbname': 'members',
    'user': 'postgres',
    'password': 'hack@&w123'
}

# Metered Secret Key
METERED_SECRET_KEY = os.environ.get("METERED_SECRET_KEY")
# Metered Domain
METERED_DOMAIN = os.environ.get("METERED_DOMAIN")
print("metereddomain:", METERED_DOMAIN)

# API Route to create a meeting room
@app.route("/api/create/room", methods=['POST'])
def create_room():
    
    url = "https://" + METERED_DOMAIN + "/api/v1/room/" + "?secretKey=" + METERED_SECRET_KEY
    
    payload = {
    "privacy": "public",
    "ejectAtRoomExp": False,
    "notBeforeUnixSec": 0,
    "autoJoin": True,
    "enableRequestToJoin": True,
    "enableChat": True,
    "enableScreenSharing": True,
    "joinVideoOn": False,
    "joinAudioOn": False,
    "recordRoom": True,
    "ejectAfterElapsedTimeInSec": 0,
    "meetingJoinWebhook": "string",
    "endMeetingAfterNoActivityInSec": 600,  # Example value for 10 minutes
    "audioOnlyRoom": False
}

    headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}
        
    r = requests.post(url, json=payload, headers=headers)
    x = r.json()
    return {'roomName': x["roomName"]}



# API Route to validate meeting
@app.route("/api/validate-meeting")
def validate_meeting():
    roomName = request.args.get("roomName")
    if roomName:
        r = requests.get("https://" + METERED_DOMAIN + "/api/v1/room/" +
                         roomName + "?secretKey=" + METERED_SECRET_KEY)
        
        data = r.json()
        if (data.get("roomName")):
            return {"roomFound": True}
        else:
            return {"roomFound": False}
    else:
        return {
            "success": False,
            "message": "Please specify roomName"
        }


# API Route to fetch the Metered Domain
@app.route("/api/metered-domain")
def get_metered_domain():
    return {"METERED_DOMAIN": METERED_DOMAIN}


DEVELOPMENT_ENV = True
conn = auth.connect_db(auth.db_config)
auth.create_users_table(conn)
text_content = ""


@app.route("/")
def index():
    return render_template("index.html", app_data=app_data)

@app.route("/login")
def login():
    return render_template("login.html", app_data=app_data)

@app.route("/signup")
def signup():
    return render_template("signup.html", app_data=app_data)

@app.route("/doctordash")
def doctordash():
    return render_template("dashboard.html", app_data=app_data, issue="hello")


# Establish a connection to the database
def connect_db(config):
    return psycopg2.connect(**config)


def get_unresolved_issues():
    conn = conn = connect_db(db_config)
    cur = conn.cursor()
    cur.execute("SELECT * FROM issues WHERE resolved = False")
    issues = cur.fetchall()
    cur.close()
    conn.close()
    return issues

@app.route("/api/get/patients", methods=["POST"])
def get_patients():
    # as of now, provides all patients, but needs to validate req is from doc
    conn = conn = connect_db(db_config)
    cur = conn.cursor()
    with conn.cursor() as cur:
        print("hello!")
        cur.execute("SELECT * FROM users WHERE doctor = false")
        result = cur.fetchall()
        return result

@app.route("/med/dashboard")
def dashboard():
    unresolved_issues = get_unresolved_issues()
    return render_template('dashboard.html', issues=unresolved_issues)



# Establish a connection to the database
def connect_db(config):
    return psycopg2.connect(**config)


def get_unresolved_issues():
    conn = connect_db(db_config)
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE resolved = False")
    issues = cur.fetchall()
    cur.close()
    conn.close()
    return issues

@app.route("/med/dashboard")
def dashboard():
    unresolved_issues = get_unresolved_issues()
    return render_template('dashboard.html', issues=unresolved_issues)


# Check login credentials
def check_login(conn, username, password):
    with conn.cursor() as cur:
        cur.execute("SELECT password_hash FROM users WHERE username = %s", (username,))
        result = cur.fetchone()
        if result and result[0] == sha256(password.encode()).hexdigest():
            return True
        return False

# Register a new user
def register_user(conn, username, password):
    with conn.cursor() as cur:
        hashed_password = sha256(password.encode()).hexdigest()
        try:
            cur.execute("INSERT INTO users (username, password_hash) VALUES (%s, %s)", (username, hashed_password))
            conn.commit()
        except psycopg2.errors.UniqueViolation:
            print("Username already exists")
            conn.rollback()

@app.route("/video")
def video():
    roomName = request.args.get('roomname')
    return render_template("video.html", app_data=app_data, roomName=roomName)

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
    
    
# Create users table
def create_users_table(conn):
    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                username VARCHAR(50) UNIQUE NOT NULL,
                password_hash VARCHAR(64) NOT NULL
            )
        """)
        conn.commit()


"""# Main function to test the login system
def main():
    conn = connect_db(db_config)
    create_users_table(conn)

   # Example usage
    register_user(conn, 'test', 'test')
    login_success = check_login(conn, 'test', 'test')
    print("Login successful:", login_success)
"""