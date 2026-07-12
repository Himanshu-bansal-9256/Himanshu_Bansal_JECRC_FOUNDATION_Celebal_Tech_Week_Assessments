def build_chat_history(messages, limit=6):
    """
    Convert previous chat messages into text.
    """

    history = []

    recent_messages = messages[-limit:]

    for msg in recent_messages:

        role = msg["role"].capitalize()

        history.append(
            f"{role}: {msg['content']}"
        )

    return "\n".join(history)