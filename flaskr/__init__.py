import os
import requests
from flask import Flask, request, render_template
import json
import psycopg2
from psycopg2 import sql
from hashlib import sha256
import auth as auth

app = Flask(__name__)

app_data = {
    "name": "medi-sight"
}

# Metered Secret Key
METERED_SECRET_KEY = os.environ.get("METERED_SECRET_KEY")
# Metered Domain
METERED_DOMAIN = os.environ.get("METERED_DOMAIN")

# API Route to create a meeting room
@app.route("/api/create/room", methods=['POST'])
def create_room():
    
    url = "https://" + METERED_DOMAIN + "/api/v1/room/" + "?secretKey=" + METERED_SECRET_KEY
    
    payload = {
    "privacy": "public",
    "ejectAtRoomExp": False,
    "notBeforeUnixSec": 0,
    "maxParticipants": 0,
    "autoJoin": True,
    "enableRequestToJoin": True,
    "enableChat": True,
    "enableScreenSharing": True,
    "joinVideoOn": False,
    "joinAudioOn": False,
    "recordRoom": True,
    "ejectAfterElapsedTimeInSec": 0,
    "meetingJoinWebhook": "string",
    "endMeetingAfterNoActivityInSec": 1800,  # Example value for 5 minutes
    "audioOnlyRoom": False
}

    headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}
        
    r = requests.post(url, json=payload, headers=headers)
    x = r.json()
    return x["roomName"]



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
            return True
        except psycopg2.errors.UniqueViolation:
            print("Username already exists")
            conn.rollback()
            return False

@app.route("/validatelogin", methods=["post"])
def validatelogin():
    encoded_username = request.args.get('username')
    encoded_password = request.args.get('password')
    is_valid = auth.check_login(conn, encoded_username, encoded_password)
    print("valid:",is_valid)
    if is_valid:
        return {"valid": "success"}
    else:
        return {"valid": "failure"}
    
@app.route("/validatesignup", methods=["post"])
def validatesignup():
    encoded_username = request.args.get('username')
    encoded_password = request.args.get('password')
    is_valid = auth.register_user(conn, encoded_username, encoded_password)
    print(encoded_username)
    print(encoded_password)
    print("valid:",is_valid)
    if is_valid:
        return {"valid": "success"}
    else:
        return {"valid": "failure"}
    
    
# Database configuration
db_config = {
    'host': '34.130.250.144',
    'dbname': 'members',
    'user': 'postgres',
    'password': 'hack@&w123'
}

# Establish a connection to the database
def connect_db(config):
    return psycopg2.connect(**config)

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


# Main function to test the login system
def main():
    conn = connect_db(db_config)
    create_users_table(conn)

if __name__ == '__main__':
    main()
