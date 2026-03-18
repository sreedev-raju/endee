import streamlit as st
from rag_pipeline import process_urls, get_rag_answer

st.set_page_config(page_title="RAG Chatbot", layout="centered")

st.title(" Sreedev AI Assistant")


if "processed" not in st.session_state:
    st.session_state.processed = False

if "messages" not in st.session_state:
    st.session_state.messages = []



st.subheader(" Enter Portfolio URL")

url = st.text_input("Portfolio URL")

if st.button(" Process URL"):
    if not url:
        st.warning("Please enter a URL")
    else:
        with st.spinner("Processing..."):
            process_urls([url])
        st.session_state.processed = True
        st.success("Data processed successfully!")


st.markdown("---")



for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])



if prompt := st.chat_input("Ask something about the portfolio..."):

    if not st.session_state.processed:
        st.warning(" Please process URL first")
    else:
        # user message
        st.session_state.messages.append({"role": "user", "content": prompt})

        with st.chat_message("user"):
            st.markdown(prompt)

        # assistant response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                answer = get_rag_answer(prompt)

            st.markdown(answer)

        st.session_state.messages.append({"role": "assistant", "content": answer})