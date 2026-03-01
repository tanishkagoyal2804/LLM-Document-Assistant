import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from transformers import pipeline


# Load Embedding Model (Global)


embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# Process Multiple PDFs


def process_multiple_pdfs(pdf_paths):

    all_documents = []

    # Load all PDFs
    for pdf_path in pdf_paths:
        loader = PyPDFLoader(pdf_path)
        docs = loader.load()
        all_documents.extend(docs)

    # Split into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150
    )

    chunks = text_splitter.split_documents(all_documents)

    # Create FAISS vector store
    vectorstore = FAISS.from_documents(chunks, embeddings)

    return vectorstore


# -------------------------------
# Generate Answer
# -------------------------------

def get_answer(vectorstore, query):

    docs_and_scores = vectorstore.similarity_search_with_score(query, k=3)

    docs = [doc for doc, score in docs_and_scores]
    scores = [score for doc, score in docs_and_scores]

    context = "\n\n".join([doc.page_content for doc in docs])

    generator = pipeline(
        "text-generation",
        model="google/flan-t5-small",
        max_new_tokens=200
    )

    prompt = f"""
    Answer the question based only on the context below.
    If answer not found, say "Not available in document."

    Context:
    {context}

    Question:
    {query}
    """

    result = generator(prompt)

    answer = result[0]["generated_text"]

    return answer, docs, scores