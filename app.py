import streamlit as st

from utils.retriever import get_retriever
from utils.llm import get_llm

st.set_page_config(
    page_title="Research RAG",
    page_icon=" ",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    background: #050816;
    color: white;
}

.stApp {
    background: radial-gradient(circle at top, #0B1023 0%, #050816 60%);
}

section[data-testid="stSidebar"] {
    display: none;
}

.main .block-container {
    padding-top: 5rem;
    padding-left: 6rem;
    padding-right: 6rem;
    max-width: 1400px;
}

.title {
    font-size: 72px;
    font-weight: 700;
    text-align: center;
    margin-bottom: 18px;
    background: linear-gradient(
        90deg,
        #ffffff,
        #c4b5fd
    );
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.subtitle {
    color: #9CA3AF;
    font-size: 24px;
    text-align: center;
    margin-bottom: 55px;
}

.stTextInput > div > div > input {
    background: rgba(17, 24, 39, 0.92);
    border: 1px solid rgba(139, 92, 246, 0.4);
    border-radius: 22px;
    padding: 22px;
    color: white;
    font-size: 18px;
    transition: 0.3s;
}

.stTextInput > div > div > input:focus {
    border: 1px solid #8B5CF6;
    box-shadow: 0 0 22px rgba(139,92,246,0.4);
}

.answer-card {
    background: linear-gradient(
        135deg,
        rgba(16,185,129,0.10),
        rgba(59,130,246,0.08)
    );

    border: 1px solid rgba(255,255,255,0.08);

    border-radius: 28px;

    padding: 36px;

    margin-top: 30px;

    line-height: 1.9;

    font-size: 18px;

    backdrop-filter: blur(14px);
}

.section-title {
    font-size: 36px;
    font-weight: 700;
    margin-top: 55px;
    margin-bottom: 25px;
}

.source-card {
    background: rgba(17,24,39,0.72);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 24px;
    padding: 24px;
    min-height: 280px;
    transition: 0.3s;
    backdrop-filter: blur(14px);
}

.source-card:hover {
    transform: translateY(-6px);
    border: 1px solid rgba(139,92,246,0.5);
    box-shadow: 0 0 28px rgba(139,92,246,0.2);
}

.source-title {
    font-size: 18px;
    font-weight: 600;
    margin-bottom: 16px;
}

.page-badge {
    display: inline-block;
    background: rgba(139,92,246,0.16);
    border: 1px solid rgba(139,92,246,0.35);
    color: #C4B5FD;
    padding: 6px 14px;
    border-radius: 999px;
    font-size: 13px;
    margin-bottom: 18px;
}

</style>
""", unsafe_allow_html=True)

st.markdown(
    """
    <div class="title">
        Research Paper Assistant
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="subtitle">
        Ask questions about your uploaded research papers.
    </div>
    """,
    unsafe_allow_html=True
)

query = st.text_input(
    "",
    placeholder="Ask a research question..."
)

if query:

    with st.spinner("Searching papers..."):

        retriever = get_retriever()

        docs = retriever.invoke(query)

        context = "\n\n".join(
            [doc.page_content for doc in docs]
        )

        prompt = f"""
You are an expert AI research assistant.

Answer the user's question ONLY using the context below.

If the answer does not exist in the context,
say:
"I could not find enough information in the papers."

Context:
{context}

Question:
{query}

Detailed Answer:
"""

        llm = get_llm()

        response = llm.invoke(prompt)

    st.markdown(
        """
        <div class="section-title">
            Answer
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
<div class="answer-card">
{response.content}
</div>
""",
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="section-title">
            Sources
        </div>
        """,
        unsafe_allow_html=True
    )

    cols = st.columns(3)

    for idx, doc in enumerate(docs):

        source_name = doc.metadata.get(
            "source",
            "Unknown PDF"
        )

        page_number = doc.metadata.get(
            "page",
            "N/A"
        )

        preview = doc.page_content[:350]

        with cols[idx % 3]:

            st.markdown(
                f"""
<div class="source-card">

<div class="source-title">
 {source_name}
</div>

<div class="page-badge">
Page {page_number}
</div>

<div style="line-height:1.8; color:#D1D5DB;">
{preview}
</div>

</div>
""",
                unsafe_allow_html=True
            )