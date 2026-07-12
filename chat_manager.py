from database import get_connection


# ----------------------------
# Create New Chat
# ----------------------------
def create_chat(title="New Chat"):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO chats(title)
        VALUES(?)
        """,
        (title,)
    )

    conn.commit()

    chat_id = cursor.lastrowid

    conn.close()

    return chat_id


# ----------------------------
# Get All Chats
# ----------------------------
def get_all_chats():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM chats
        ORDER BY id DESC
        """
    )

    chats = cursor.fetchall()

    conn.close()

    return chats


# ----------------------------
# Save Message
# ----------------------------
def save_message(chat_id, role, content):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO messages
        (chat_id, role, content)

        VALUES(?,?,?)
        """,
        (
            chat_id,
            role,
            content
        )
    )

    conn.commit()

    conn.close()


# ----------------------------
# Load Messages
# ----------------------------
def load_messages(chat_id):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT role,content

        FROM messages

        WHERE chat_id=?

        ORDER BY id
        """,
        (chat_id,)
    )

    rows = cursor.fetchall()

    conn.close()

    return [
        {
            "role": row["role"],
            "content": row["content"]
        }
        for row in rows
    ]


# ----------------------------
# Delete Chat
# ----------------------------
def delete_chat(chat_id):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM messages
        WHERE chat_id=?
        """,
        (chat_id,)
    )

    cursor.execute(
        """
        DELETE FROM chats
        WHERE id=?
        """,
        (chat_id,)
    )

    conn.commit()

    conn.close()


# ----------------------------
# Rename Chat
# ----------------------------
def rename_chat(chat_id, title):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE chats

        SET title=?

        WHERE id=?
        """,
        (
            title,
            chat_id
        )
    )

    conn.commit()

    conn.close()


# ----------------------------
# Get Single Chat
# ----------------------------
def get_chat(chat_id):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *

        FROM chats

        WHERE id=?
        """,
        (chat_id,)
    )

    chat = cursor.fetchone()

    conn.close()

    return chat