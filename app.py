import streamlit as st
from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import google.generativeai as genai
from dotenv import load_dotenv
import os

# ==========================
# Gemini Configuration
# ==========================

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

llm = genai.GenerativeModel(
    "gemini-2.5-flash"
)

# ==========================
# Load Embedding Model Once
# ==========================

@st.cache_resource
def load_embedding_model():
    return SentenceTransformer(
        "all-MiniLM-L6-v2"
    )

embedding_model = load_embedding_model()

# ==========================
# PDF Text Extraction
# ==========================

def extract_text(pdf):

    reader = PdfReader(pdf)

    text = ""

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text

# ==========================
# Chunking with Overlap
# ==========================

def chunk_text(
    text,
    chunk_size=1500,
    overlap=300
):

    chunks = []

    start = 0

    while start < len(text):

        end = start + chunk_size

        chunks.append(
            text[start:end]
        )

        start += chunk_size - overlap

    return chunks

# ==========================
# Create FAISS Index
# ==========================

def create_vector_store(chunks):

    embeddings = embedding_model.encode(
        chunks
    )

    embeddings = np.array(
        embeddings
    ).astype("float32")

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(
        dimension
    )

    index.add(
        embeddings
    )

    return index

# ==========================
# Retrieve Relevant Chunks
# ==========================

def retrieve_chunks(
    question,
    chunks,
    index
):

    question_embedding = embedding_model.encode(
        [question]
    )

    question_embedding = np.array(
        question_embedding
    ).astype("float32")

    distances, indices = index.search(
        question_embedding,
        3
    )

    retrieved_chunks = []

    for idx in indices[0]:

        if idx < len(chunks):

            retrieved_chunks.append(
                chunks[idx]
            )

    return "\n\n".join(
        retrieved_chunks
    )

# ==========================
# Gemini Answer Generation
# ==========================

def generate_answer(
    question,
    context
):

    prompt = f"""
You are a PDF assistant.

Answer ONLY from the provided context.

If the answer exists in the context,
give a complete answer.

If the answer is not available,
reply:

Answer not found in PDF.

Context:
{context}

Question:
{question}
"""

    response = llm.generate_content(
        prompt
    )

    return response.text

# ==========================
# Streamlit Page Config
# ==========================

st.set_page_config(
    page_title="PDF Chat Assistant",
    page_icon="📚",
    layout="wide"
)

st.title("📚 PDF Chat Assistant")

# ==========================
# Session State
# ==========================

if "messages" not in st.session_state:
    st.session_state.messages = []

# ==========================
# PDF Upload
# ==========================

pdf = st.file_uploader(
    "Upload PDF",
    type="pdf"
)

# ==========================
# Process PDF Only Once
# ==========================

if pdf:

    if (
        "current_pdf" not in st.session_state
        or st.session_state.current_pdf != pdf.name
    ):

        with st.spinner(
            "Processing PDF..."
        ):

            text = extract_text(pdf)

            chunks = chunk_text(text)

            index = create_vector_store(
                chunks
            )

            st.session_state.index = index
            st.session_state.chunks = chunks
            st.session_state.current_pdf = pdf.name

            # Clear old chat when new PDF uploaded
            st.session_state.messages = []

    st.success(
        "PDF processed successfully!"
    )

    # ==========================
    # Display Chat History
    # ==========================

    for message in st.session_state.messages:

        with st.chat_message(
            message["role"]
        ):
            st.markdown(
                message["content"]
            )

    # ==========================
    # Chat Input
    # ==========================

    question = st.chat_input(
        "Ask anything from the PDF..."
    )

    if question:

        # User Message

        with st.chat_message(
            "user"
        ):
            st.markdown(question)

        st.session_state.messages.append(
            {
                "role": "user",
                "content": question
            }
        )

        # Retrieve Context

        context = retrieve_chunks(
            question,
            st.session_state.chunks,
            st.session_state.index
        )

        # Generate Answer

        with st.spinner(
            "Thinking..."
        ):

            answer = generate_answer(
                question,
                context
            )

        # Assistant Message

        with st.chat_message(
            "assistant"
        ):
            st.markdown(answer)

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )

        # Debug Section

        with st.expander(
            "View Retrieved Context"
        ):
            st.write(context)

else:

    st.info(
        "Upload a PDF to start chatting."
    )