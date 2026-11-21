
import streamlit as st

from ai_service import generate_response


def show_rewrite_tool():
    """Display the Verba AI text rewriting tool."""

    st.subheader("Rewrite & Improve")

    st.write(
        "Improve clarity, fix grammar, adjust tone, or simplify "
        "your text while preserving its original meaning."
    )

    original_text = st.text_area(
        "Text to improve",
        placeholder="Paste the text you want to rewrite...",
        height=220,
        key="rewrite_original_text",
    )

    rewrite_goal = st.selectbox(
        "What would you like to improve?",
        [
            "Improve clarity",
            "Correct grammar and spelling",
            "Make it more concise",
            "Make it more detailed",
            "Change the tone",
            "Remove repetition",
            "Simplify the language",
        ],
        key="rewrite_goal",
    )

    rewrite_tone = st.selectbox(
        "Desired tone",
        [
            "Professional",
            "Formal",
            "Friendly",
            "Polite",
            "Assertive",
            "Persuasive",
            "Academic",
            "Simple and conversational",
        ],
        key="rewrite_tone",
    )

    if st.button(
        "Improve text",
        type="primary",
        use_container_width=True,
        key="rewrite_button",
    ):
        if not original_text.strip():
            st.warning("Please enter some text first.")

        else:
            prompt = (
                f"Task: {rewrite_goal}\n"
                f"Desired tone: {rewrite_tone}\n\n"
                f"Original text:\n{original_text}\n\n"
                "Preserve the original meaning and factual details. "
                "Do not add unsupported information. "
                "Return only the improved text."
            )

            try:
                with st.spinner("Verba AI is improving your text..."):
                    result = generate_response(
                        "You are Verba AI, an expert writing editor.",
                        prompt,
                        st.secrets["GROQ_API_KEY"],
                    )

                st.session_state.results[
                    f"Rewrite: {rewrite_goal}: {rewrite_tone}"
                ] = result
            except Exception as error:
                st.error(f"Could not improve text: {error}")
