
import streamlit as st

st.set_page_config(
    page_title="NewsLens AI",
    page_icon="📰",
    layout="wide"
)

st.title("📰 NewsLens AI")
st.subheader("News Summarization and Evaluation")

st.write(
    "This project compares extractive and abstractive "
    "summarization techniques."
)

st.info(
    "Methods: Lead-3, TF-IDF, TextRank and BART"
)

article = st.text_area(
    "Enter your news article",
    height=200,
    placeholder="Paste a news article here..."
)

if st.button("Analyze Article"):
    if article.strip():
        st.success("Article received successfully!")
        st.write("Word count:", len(article.split()))
    else:
        st.warning("Please enter a news article.")
