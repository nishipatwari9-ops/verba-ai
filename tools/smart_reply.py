

import streamlit as st
from ai_service import generate_response


def show_smart_reply_tool():
    st.subheader("Smart Reply")

    st.write(
        "Draft a suitable reply to an email or message. "
        "Choose your intention and preferred tone."
    )

    # Message the user wants to reply to
    message_text = st.text_area(
        "Paste the message you received",
        height=220,
        placeholder="Paste the email or message here...",
        key="smart_reply_message",
    )

    # Purpose of the reply
    reply_goal = st.selectbox(
        "What would you like your reply to do?",
        [
            "Reply to the message",
            "Accept an invitation or request",
            "Politely decline",
            "Ask for clarification",
            "Request more information",
            "Send a follow-up",
        ],
        key="smart_reply_goal",
    )

    # Tone of the reply
    reply_tone = st.selectbox(
        "Choose a tone",
        [
            "Professional",
            "Formal",
            "Friendly",
            "Polite",
            "Assertive",
        ],
        key="smart_reply_tone",
    )

    # Optional information to include
    extra_details = st.text_area(
        "Additional details (optional)",
        placeholder="Add any points you want to include...",
        key="smart_reply_details",
    )

    if st.button("Generate reply", use_container_width=True):
        if not message_text.strip():
            st.warning(
                "Please paste the message you want to reply to."
            )

        else:
            prompt = f"""
Draft a reply to the message below.

USER'S GOAL:
{reply_goal}

PREFERRED TONE:
{reply_tone}

ORIGINAL MESSAGE:
{message_text}

ADDITIONAL DETAILS:
{extra_details if extra_details.strip() else "None provided."}

Instructions:
- Write a clear, natural, ready-to-edit reply.
- Follow the user's chosen goal and tone.
- Use the original message as context.
- Do not invent personal facts or commitments.
- Do not claim the user has completed something unless stated.
- Use placeholders if essential information is missing.
- Return only the drafted reply, without explanations.
"""

            with st.spinner("Drafting your reply..."):
                try:
                    result = generate_response(
                        system_prompt=(
                            "You are Verba AI, a helpful writing "
                            "assistant that drafts clear and "
                            "appropriate replies to messages."
                        ),
                        user_input=prompt,
                        api_key=st.secrets["GROQ_API_KEY"],
                    )

                    # Save the generated reply
                    st.session_state.results["Smart Reply"] = result

                except Exception as error:
                    st.error(
                        f"Could not generate a reply: {error}"
                    )

    # Display the generated reply
    result = st.session_state.results.get("Smart Reply")

    if result:
        st.markdown("---")
        st.markdown("### Your reply")
        st.markdown(result)

        st.download_button(
            "Download reply",
            data=result,
            file_name="smart_reply.txt",
            mime="text/plain",
            use_container_width=True,
        )
