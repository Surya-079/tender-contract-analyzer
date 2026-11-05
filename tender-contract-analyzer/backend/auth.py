import sqlite3
import bcrypt

DB_NAME = "users.db"


def create_database():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
            username TEXT PRIMARY KEY,
            password BLOB
        )
    """)

    conn.commit()
    conn.close()


def register_user(username, password):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT username FROM users WHERE username=?",
        (username,)
    )

    if cursor.fetchone():
        conn.close()
        return False, "Username already exists."

    hashed_password = bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt()
    )

    cursor.execute(
        "INSERT INTO users VALUES(?, ?)",
        (username, hashed_password)
    )

    conn.commit()
    conn.close()

    return True, "Registration Successful."


def login_user(username, password):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT password FROM users WHERE username=?",
        (username,)
    )

    row = cursor.fetchone()

    conn.close()

    if row is None:
        return False

    stored_password = row[0]

    if bcrypt.checkpw(password.encode(), stored_password):
        return True

    return False