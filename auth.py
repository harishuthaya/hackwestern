import psycopg2
from psycopg2 import sql
from hashlib import sha256

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

# Check login credentials
def check_login(conn, username, password):
    with conn.cursor() as cur:
        cur.execute("SELECT password_hash FROM users WHERE username = %s", (username,))
        result = cur.fetchone()
        if result and result[0] == sha256(password.encode()).hexdigest():
            return True
        return False

# Main function to test the login system
def main():
    conn = connect_db(db_config)
    create_users_table(conn)

    # Example usage
    register_user(conn, 'test', 'test')
    login_success = check_login(conn, 'test', 'test')
    print("Login successful:", login_success)

if __name__ == '__main__':
    main()
