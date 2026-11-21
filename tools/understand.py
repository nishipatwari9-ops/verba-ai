
import streamlit as st

from ai_service import generate_response


def show_understand_tool():
    """Display the document understanding tool."""

    st.subheader("Understand a Document")

    st.write(
        "Paste a notice, instruction, or document to understand "
        "it, find important details, or check for unclear information."
    )

    document_text = st.text_area(
        "Paste your document",
        placeholder="Paste your document here...",
        height=200,
        key="understand_document",
    )

    understanding_task = st.selectbox(
        "What would you like Verba AI to do?",
        [
            "Explain in simple language",
            "Ask a question about the text",
            "Find important information",
            "Identify missing or ambiguous information",
        ],
        key="understand_task",
    )

    question = ""

    if understanding_task == "Ask a question about the text":
        question = st.text_input(
            "Your question",
            placeholder="What is the submission deadline?",
            key="understand_question",
        )

    if st.button(
        "Understand document",
        type="primary",
        use_container_width=True,
        key="understand_button",
    ):
        if not document_text.strip():
            st.warning("Please paste a document first.")

        elif (
            understanding_task == "Ask a question about the text"
            and not question.strip()
        ):
            st.warning("Please enter a question.")

        else:
            task_instructions = {
                "Explain in simple language": (
                    "Explain the document in simple language using "
                    "short paragraphs. Focus on what it means. "
                    "Do not invent information."
                ),
                "Ask a question about the text": (
                    "Answer only the user's specific question in "
                    "one or two sentences. Use only information "
                    "explicitly stated in the document. If the "
                    "answer is unavailable, say: "
                    "'The document does not specify this.'\n\n"
                    f"Question: {question}"
                ),
                "Find important information": (
                    "Extract important facts without explaining "
                    "the entire document. Use these headings when "
                    "supported by the text: Deadline, Submission "
                    "Method, Fees or Penalties, Requirements, "
                    "and Exceptions. Do not invent missing details."
                ),
                "Identify missing or ambiguous information": (
                    "Check the document for details that are "
                    "genuinely missing, unclear, or contradictory. "
                    "List each issue and explain what needs "
                    "clarification. Do not provide a general summary. "
                    "If no meaningful issues are evident, say so."
                ),
            }

            prompt = (
                f"TASK:\n"
                f"{task_instructions[understanding_task]}\n\n"
                f"DOCUMENT:\n{document_text.strip()}\n\n"
                "Follow the requested task. Do not invent facts."
            )

            try:
                with st.spinner("Verba AI is working..."):
                    result = generate_response(
                        (
                            "You are Verba AI, a careful document "
                            "understanding assistant. Be accurate, "
                            "clear, and transparent about uncertainty."
                        ),
                        prompt,
                        st.secrets["GROQ_API_KEY"],
                    )

                # Save each action's result separately.
                st.session_state[
                    f"understand_result_{understanding_task}"
                ] = result

            except Exception as error:
                st.error(f"Could not process the document: {error}")

    # Display the result for the currently selected action.
    result_key = f"understand_result_{understanding_task}"

    if result_key in st.session_state:
        st.divider()
        st.markdown("### Your result")

        result = st.session_state[result_key]

        st.markdown(result)

        st.download_button(
            "Download result as a text file",
            data=result,
            file_name=(
                "verba_ai_"
                f"{understanding_task.lower().replace(' ', '_')}.txt"
            ),
            mime="text/plain",
            use_container_width=True,
            key=f"download_{result_key}",
        )
