import streamlit as st
from pathlib import Path
from semantic_search import search

st.title("Semantic Search Demo")

query = st.text_input("Enter your query:")

if query:
    try:
        # Pass Path instead of string
        results = search(index_dir=Path("./index"), query=query, top_k=5)
        st.write("### Top Results")
        for r in results:
            st.write(f"{r['doc_id']} | score={r['score']:.4f}")
            st.write(r['snippet'])
    except Exception as e:
        st.error(f"Error: {e}")
