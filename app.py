import streamlit as st
import os
import time
from rag_pipeline import process_multiple_pdfs, get_answer


# Page Config


st.set_page_config(
    page_title="DocuMind AI",
    page_icon="📄",
    layout="wide"
)

st.title("📄 DocuMind AI")
st.markdown("### Multi-Document RAG Based Question Answering System")


# Upload Multiple PDFs


uploaded_files = st.file_uploader(
    "Upload PDF Documents",
    type="pdf",
    accept_multiple_files=True
)

if uploaded_files:

    os.makedirs("data", exist_ok=True)

    file_paths = []

    # Save uploaded files
    for uploaded_file in uploaded_files:
        file_path = f"data/{uploaded_file.name}"

        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        file_paths.append(file_path)

    st.success("✅ All PDFs Uploaded Successfully!")

    # Process documents
    with st.spinner("Processing documents and building vector index..."):
        vectorstore = process_multiple_pdfs(file_paths)

    st.success("📚 Documents Ready for Questions!")

    
    # Ask Question
  

    query = st.text_input("Ask a question about the uploaded documents")

    if query:

        with st.spinner("Generating answer..."):

            start_time = time.time()

            answer, docs, scores = get_answer(vectorstore, query)

            end_time = time.time()

       
        # Display Answer
        

        st.subheader("📌 Answer")
        st.write(answer)

        # Response Time
       

        response_time = round(end_time - start_time, 2)
        st.markdown(f"⏱ **Response Time:** {response_time} seconds")

       
        # Source References
       

        st.subheader("📚 Source References")

        for i, (doc, score) in enumerate(zip(docs, scores)):

            confidence = round((1 / (1 + score)) * 100, 2)

            with st.expander(f"Source {i+1} | Confidence: {confidence}%"):

                st.markdown(f"**Document:** {doc.metadata.get('source', 'Unknown')}")
                st.write(doc.page_content[:400])