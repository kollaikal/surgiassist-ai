import streamlit as st
import requests

st.set_page_config(page_title="SurgiAssist AI", layout="centered")
st.title("🩺 SurgiAssist AI")
st.markdown("Ask any surgical or medical question. Powered by **Cerebras + PubMed**.")

question = st.text_input("Enter your medical query:")

if st.button("Get Answer") and question:
    with st.spinner("Contacting medical assistant AI..."):
        response = requests.post("http://localhost:8000/ask", json={"question": question})
        if response.ok:
            data = response.json()
            answer = data["answer"]
            sources = data.get("sources", [])

            st.success("Answer ready!")

            # Intelligent header
            st.markdown("AI Clinical Assistant")
            st.markdown("*Hi! I’m **SurgiAssist**, your AI-powered assistant trained to provide medical answers using PubMed research.*")

            # Parse optional formatting from answer if user prompt handled it
            if "### Final Answer" in answer:
                summary = answer.split("### Final Answer")[-1].strip()
                st.markdown("### Summary")
                st.info(summary)

            if "### Thought Process" in answer:
                thought = answer.split("### Thought Process")[-1].split("### Final Answer")[0].strip()
                st.markdown("### Thought Process")
                st.markdown(f"<div style='color:gray'>{thought}</div>", unsafe_allow_html=True)

            # Full answer (regardless of summary or not)
            if not ("### Final Answer" in answer and "### Thought Process" in answer):
                st.markdown("### 💡 Answer")
                st.markdown(answer)

            # Sources
            if sources:
                st.markdown("### Sources")
                for i, src in enumerate(sources, 1):
                    st.markdown(f"**Source {i}:** {src}")
                    st.markdown("---")
            else:
                st.markdown("⚠️ No medical sources were relevant to this query.")

            # Feedback UI
            st.markdown("---")
            st.markdown("Was this helpful?")
            col1, col2 = st.columns(2)
            with col1:
                st.button("👍 Yes")
            with col2:
                st.button("👎 No")

        else:
            st.error("❌ Failed to get an answer. Check backend or API key.")
