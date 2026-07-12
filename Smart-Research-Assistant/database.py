import sqlite3

DATABASE_NAME = "research_assistant.db"


def get_connection():
    conn = sqlite3.connect(
        DATABASE_NAME,
        check_same_thread=False
    )

    conn.row_factory = sqlite3.Row

    return conn


def create_tables():

    conn = get_connection()

    cursor = conn.cursor()

    # -----------------------------
    # Chats Table
    # -----------------------------
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS chats(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        title TEXT,

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

    )
    """)

    # -----------------------------
    # Messages Table
    # -----------------------------
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS messages(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        chat_id INTEGER,

        role TEXT,

        content TEXT,

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

        FOREIGN KEY(chat_id)
        REFERENCES chats(id)

    )
    """)

    # -----------------------------
    # Uploaded PDFs
    # -----------------------------
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS documents(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        filename TEXT,

        pages INTEGER,

        chunks INTEGER,

        uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

    )
    """)

    conn.commit()

    conn.close()

if __name__ == "__main__":

    create_tables()

    print("Database and Tables Created Successfully!")