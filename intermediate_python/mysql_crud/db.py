import mysql.connector


def get_connection():
    """Return MySQL database connection."""
    try:
        return mysql.connector.connect(
            host="localhost",
            user="userpython",
            password="mypassword",
            database="company_db",
        )
    except mysql.connector.Error as err:
        print("Database connection error:", err)
        return None