import sqlite3

DB_NAME = "support.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def create_tables():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        telegram_id INTEGER PRIMARY KEY,
        username TEXT,
        first_name TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tickets(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        telegram_id INTEGER,
        category TEXT,
        status TEXT DEFAULT 'open',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS messages(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ticket_id INTEGER,
        sender TEXT,
        text TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()


def add_user(user):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT OR IGNORE INTO users
        VALUES (?, ?, ?)
        """,
        (
            user.id,
            user.username,
            user.first_name
        )
    )

    conn.commit()
    conn.close()


def create_ticket(telegram_id, category):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO tickets(telegram_id, category)
        VALUES (?, ?)
        """,
        (
            telegram_id,
            category
        )
    )

    ticket_id = cursor.lastrowid

    conn.commit()
    conn.close()

    return ticket_id


def save_message(ticket_id, sender, text):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO messages(ticket_id, sender, text)
        VALUES (?, ?, ?)
        """,
        (
            ticket_id,
            sender,
            text
        )
    )

    conn.commit()
    conn.close()