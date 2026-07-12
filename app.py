import os
import shutil
import streamlit as st
from config import DATA_FOLDER
from utils.rag_pipeline import RAGPipeline
from database import create_tables
from chat_manager import (
    create_chat,
    get_all_chats,
    load_messages,
    save_message
)

#PAGE CONFIG 

st.set_page_config(
    page_title="Smart Research Assistant",
    page_icon="🤖",
    layout="wide"
)
create_tables()

# CSS 

def load_css():
    with open("styles.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()

with st.sidebar:

    st.title("Chats")

    if st.button("➕ New Chat"):

        chat_id = create_chat("New Chat")

        st.session_state.current_chat = chat_id

        st.session_state.messages = []

        st.rerun()

    st.divider()

    chats = get_all_chats()

    for chat in chats:

        if st.button(
            chat["title"],
            key=f"chat_{chat['id']}"
        ):

            st.session_state.current_chat = chat["id"]

            st.session_state.messages = load_messages(
                chat["id"]
            )

            st.rerun()

# HEADER 

st.markdown(
"""
<div class="hero">

<h1>Smart Research Assistant</h1>

<p>
Chat with your PDF documents using
<b>Hybrid RAG</b>,
<b>FAISS</b>,
<b>BM25</b> &
<b>Groq</b>.
</p>

</div>
""",
unsafe_allow_html=True
)

#  PIPELINE 

pipeline = RAGPipeline()

# CHAT HISTORY

if "current_chat" not in st.session_state:

    chats = get_all_chats()

    if chats:
        st.session_state.current_chat = chats[0]["id"]
    else:
        st.session_state.current_chat = create_chat("New Chat")

if "messages" not in st.session_state:

    st.session_state.messages = load_messages(
        st.session_state.current_chat
    )

#FILE UPLOAD 

uploaded_files = st.file_uploader(
    "Upload PDF Documents",
    type=["pdf"],
    accept_multiple_files=True
)

# NO FILE

if not uploaded_files:

    st.markdown(
    """
    <div class="welcome-box">

    <h2> Upload one or more PDF files</h2>
    <p>
    Start chatting with your documents.
    </p>
    </div>
    """,
    unsafe_allow_html=True
    )
    col1, col2, col3 = st.columns(3)
    with col1:
        st.info("Summarize documents")
    with col2:
        st.info("Ask questions")
    with col3:
        st.info("⚖ Compare PDFs")
    st.stop()

# Delete old vector database when new PDFs are uploaded
if os.path.exists("vectorstore"):
    shutil.rmtree("vectorstore")

# SAVE PDF

os.makedirs(DATA_FOLDER, exist_ok=True)

pdf_paths = []

for uploaded_file in uploaded_files:

    path = os.path.join(
        DATA_FOLDER,
        uploaded_file.name
    )

    with open(path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    pdf_paths.append(path)

if (
    "processed_files" not in st.session_state
    or st.session_state.processed_files != [f.name for f in uploaded_files]
):

    pages, chunks = pipeline.process_pdfs(pdf_paths)

    st.session_state.pages = pages
    st.session_state.chunks = chunks

    st.session_state.processed_files = [
        f.name for f in uploaded_files
    ]

else:

    pages = st.session_state.pages
    chunks = st.session_state.chunks

#FILE CHIPS 

st.markdown("### 📎 Uploaded Files")
cols = st.columns(len(uploaded_files))
for i, file in enumerate(uploaded_files):
    with cols[i]:
        st.success(file.name)

# CHAT
st.divider()
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

#  INPUT 
question = st.chat_input(
    "Ask anything about your documents..."
)
if question:
    user_message = {
    "role": "user",
    "content": question
    }
    st.session_state.messages.append(user_message)

    save_message(
        st.session_state.current_chat,
        "user",
        question
    )
    with st.chat_message("user"):
        st.markdown(question)
    with st.chat_message("assistant"):
        thinking = st.empty()
        thinking.info("Searching documents...")
        answer, docs = pipeline.ask_question(
            question,
            st.session_state.messages
        )
        thinking.info("Generating answer...")
        thinking.empty()
        st.markdown(answer)
        with st.expander("References"):
            for i, doc in enumerate(docs):
                file_name = os.path.basename(
                    doc.metadata.get(
                        "source",
                        "Unknown"
                    )
                )
                page = doc.metadata.get(
                    "page_label",
                    doc.metadata.get(
                        "page",
                        "Unknown"
                    )
                )

                st.markdown(
                f"""
### {file_name}

**Page :** {page}
                """
                )

                if st.button(
                    f"Show Context {i+1}",
                    key=i
                ):
                    st.info(doc.page_content)

    assistant_message = {
        "role": "assistant",
        "content": answer
    }

    st.session_state.messages.append(
        assistant_message
    )

    save_message(
        st.session_state.current_chat,
        "assistant",
        answer
    )
# FOOTER 
st.markdown("---")
st.caption(
    "Built with using Streamlit • LangChain • Hybrid RAG • Groq"
)