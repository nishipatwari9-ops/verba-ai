
import streamlit as st

from ai_service import generate_response


def show_summarize_tool():
    """Display the Verba AI summarization tool."""

    st.subheader("Summarize")

    st.write(
        "Turn long documents, articles, notes, and instructions "
        "into shorter, easier-to-read summaries."
    )

    document_text = st.text_area(
        "Text to summarize",
        placeholder="Paste an article, document, meeting notes, or other text...",
        height=260,
        key="summarize_document",
    )

    summary_style = st.selectbox(
        "Summary style",
        [
            "Short overview",
            "Detailed summary",
            "Bullet-point summary",
            "Key takeaways",
        ],
        key="summarize_style",
    )

    summary_length = st.selectbox(
        "Summary length",
        [
            "Very short",
            "Short",
            "Medium",
            "Detailed",
        ],
        key="summarize_length",
    )

    if st.button(
        "Summarize text",
        type="primary",
        use_container_width=True,
        key="summarize_button",
    ):
        if not document_text.strip():
            st.warning("Please paste some text to summarize.")

        else:
            prompt = (
                f"Summary style: {summary_style}\n"
                f"Summary length: {summary_length}\n\n"
                f"TEXT TO SUMMARIZE:\n{document_text.strip()}\n\n"
                "Follow the selected style and length. Preserve the "
                "main ideas and important facts. Do not add information "
                "that is not present in the original text. "
                "If the input is already short, summarize it appropriately."
            )

            try:
                with st.spinner("Verba AI is summarizing your text..."):
                    result = generate_response(
                        (
                            "You are Verba AI, a careful summarization "
                            "assistant. Produce accurate, readable "
                            "summaries without inventing facts."
                        ),
                        prompt,
                        st.secrets["GROQ_API_KEY"],
                    )

                st.session_state.results["Summarize"] = result

            except Exception as error:
                st.error(f"Could not summarize the text: {error}")

    if "Summarize" in st.session_state.results:
        st.divider()
        st.markdown("### Your result")

        result = st.session_state.results["Summarize"]
        st.markdown(result)

        st.download_button(
            "Download summary as a text file",
            data=result,
            file_name="verba_ai_summary.txt",
            mime="text/plain",
            use_container_width=True,
            key="download_summarize",
        )
