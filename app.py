import streamlit as st
from summarizer import summarize_code

st.set_page_config(page_title="Code Summarizer", layout="centered")

st.title("🧠 Code Summarizer using CodeT5")
st.markdown("""
This tool generates a **natural language summary** for your code snippet using a deep learning model (`CodeT5`).  
Useful for code documentation, understanding legacy code, or research in deep learning for software engineering.
""")

# Example function
example_code = '''def calculate_average(nums):\n    total = sum(nums)\n    count = len(nums)\n    return total / count'''

# Load example button
if st.button("📥 Load Example Code"):
    st.session_state.code_input = example_code

# Input area
code_input = st.text_area("Paste your source code here:", height=300, key="code_input")

# Summarize
if st.button("🔍 Summarize Code"):
    if code_input.strip():
        with st.spinner("Generating summary..."):
            summary = summarize_code(code_input)
        st.success("✅ Summary generated!")
        st.subheader("📝 Summary:")
        st.write(summary)
    else:
        st.warning("Please paste some code to summarize.")
