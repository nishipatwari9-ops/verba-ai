
import streamlit as st

from ai_service import generate_response


def show_action_items_tool():
    """Display the Verba AI action items tool."""

    st.subheader("Action Items")

    st.write(
        "Turn meeting notes, emails, and instructions into a clear "
        "list of tasks, deadlines, and follow-up actions."
    )

    source_text = st.text_area(
        "Paste your notes or instructions",
        placeholder=(
            "Paste meeting notes, project instructions, an email, "
            "or any text containing tasks..."
        ),
        height=260,
        key="action_items_source",
    )

    output_style = st.selectbox(
        "How should the action items be organized?",
        [
            "Task list",
            "Priority-based list",
            "Table with deadlines and responsibilities",
        ],
        key="action_items_style",
    )

    if st.button(
        "Extract action items",
        type="primary",
        use_container_width=True,
        key="action_items_button",
    ):
        if not source_text.strip():
            st.warning("Please paste some notes or instructions first.")

        else:
            prompt = (
                f"Output format: {output_style}\n\n"
                f"SOURCE TEXT:\n{source_text.strip()}\n\n"
                "Extract actionable tasks and follow-up actions explicitly "
                "stated or clearly required by the source. Include deadlines "
                "and responsible people only when the source provides them. "
                "Do not invent tasks, owners, or dates. Mark unspecified "
                "deadlines or owners as 'Not specified' when relevant. "
                "If no action items are present, say so clearly."
            )

            try:
                with st.spinner("Verba AI is extracting action items..."):
                    result = generate_response(
                        (
                            "You are Verba AI, a careful productivity "
                            "assistant. Extract practical action items "
                            "accurately and never invent details."
                        ),
                        prompt,
                        st.secrets["GROQ_API_KEY"],
                    )

                st.session_state.results["Action Items"] = result

            except Exception as error:
                st.error(f"Could not extract action items: {error}")

    if "Action Items" in st.session_state.results:
        st.divider()
        st.markdown("### Your result")

        result = st.session_state.results["Action Items"]
        st.markdown(result)

        st.download_button(
            "Download action items as a text file",
            data=result,
            file_name="verba_ai_action_items.txt",
            mime="text/plain",
            use_container_width=True,
            key="download_action_items",
        )
