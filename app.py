import os
os.environ["TOKENIZERS_PARALLELISM"] = "false"
os.environ["PYTORCH_NO_CUDA_MEMORY_CACHING"] = "1"
import streamlit as st
from summarizer import summarize_code


# Page config
st.set_page_config(
    page_title="Code Summarizer | CodeT5",
    page_icon="🔮",
    layout="wide"
)

# Title and header
st.markdown("""
    <style>
        .main-title {
            font-size: 40px;
            font-weight: 700;
            color: #4A90E2;
        }
        .subtitle {
            font-size: 20px;
            margin-bottom: 30px;
        }
    </style>
    <div class='main-title'>🧠 Code Summarizer using CodeT5</div>
    <div class='subtitle'>
        Developed by <b>Rahul Kavati</b>  |  Course: <i>581 Advanced Software Engineering</i>, CSUDH
        <br><br>
        Generate natural language summaries of source code using <b>CodeT5</b> model.
        Useful for documentation, legacy code comprehension, and software research.
    </div>
""", unsafe_allow_html=True)

# Example code snippet
example_code = '''
def calculate_average(nums):
    total = sum(nums)
    count = len(nums)
    return total / count
'''

# Two-column layout
col1, col2 = st.columns([3, 2])

with col1:
    st.markdown("### 📄 Input Code")
    code_input = st.text_area("Paste your source code here:", height=300, key="code_input")

    if st.button("📂 Load Example Code"):
        st.session_state.code_input = example_code

with col2:
    st.markdown("### 🔍 Output Summary")
    if st.button("🔍 Summarize Code"):
        if code_input.strip():
            with st.spinner("Generating summary using CodeT5 model..."):
                summary = summarize_code(code_input)
            st.success("Summary generated successfully!")
            st.markdown(f"""
            <div class='summary-box'>
            {summary}
            </div>
        """, unsafe_allow_html=True)

        else:
            st.warning("Please paste a code snippet to generate summary.")

# Footer
st.markdown("""
    <hr>
    <center>
        <small>Powered by <b>HuggingFace Transformers</b> and <b>Streamlit</b></small>
    </center>
""", unsafe_allow_html=True)
