
import streamlit as st

from ai_service import generate_response


def show_write_tool():
    """Display the Verba AI writing tool."""

    st.subheader("Write Something")

    st.write(
        "Create letters, emails, requests, and other written content "
        "with a style that suits your needs."
    )

    task = st.text_input(
        "What would you like to write?",
        placeholder="e.g. A request letter to my professor",
        key="write_task",
    )

    audience = st.text_input(
        "Who is it for?",
        placeholder="e.g. Professor, colleague, general audience",
        key="write_audience",
    )

    tone = st.selectbox(
        "Writing style",
        [
            "Professional",
            "Formal",
            "Friendly",
            "Polite",
            "Academic",
            "Simple and conversational",
        ],
        key="write_tone",
    )

    details = st.text_area(
        "Details to include",
        placeholder=(
            "Share the important points you want the text to cover..."
        ),
        height=150,
        key="write_details",
    )

    if st.button(
        "Generate text",
        type="primary",
        use_container_width=True,
        key="write_button",
    ):
        if not task.strip() or not details.strip():
            st.warning(
                "Please enter the writing task and its details."
            )

        else:
            prompt = (
                f"Writing task: {task}\n"
                f"Intended audience: {audience or 'Not specified'}\n"
                f"Style: {tone}\n"
                f"Details to include:\n{details}\n\n"
                "Write a clear, well-structured response. "
                "Do not invent facts or details. "
                "Return only the requested text."
            )

            try:
                with st.spinner("Verba AI is writing..."):
                    result = generate_response(
                        "You are Verba AI, a helpful writing assistant.",
                        prompt,
                        st.secrets["GROQ_API_KEY"],
                    )

                st.session_state.results["Write"] = result

            except Exception as error:
                st.error(f"Could not generate text: {error}")
