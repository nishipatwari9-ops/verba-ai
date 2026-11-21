
import streamlit as st
from ai_service import generate_response
from tools.write import show_write_tool
from tools.understand import show_understand_tool
from tools.rewrite import show_rewrite_tool
from tools.summarize import show_summarize_tool
from tools.action_items import show_action_items_tool
from tools.smart_reply import show_smart_reply_tool


# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Verba AI",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded",
)


# --------------------------------------------------
# Styling
# --------------------------------------------------

st.markdown(
    """
    <style>
    @import url(
        'https://fonts.googleapis.com/css2?family=Nunito+Sans:wght@400;500;600;700;800&family=Pacifico&display=swap'
    );

    :root {
        --lavender: #8066A8;
        --lavender-dark: #604B83;
        --lavender-pale: #F0E9F8;
        --sage: #789F8A;
        --sage-hover: #668B77;
        --background: #FBF9FC;
        --surface: #FFFFFF;
        --text: #393344;
        --muted: #81798D;
        --border: #E9E2EF;
    }

    /* Main application */
    .stApp {
        background: var(--background);
        color: var(--text);
        font-family: 'Nunito Sans', sans-serif;
    }

    /* General typography */
    .stApp p,
    .stApp label,
    .stApp input,
    .stApp textarea {
        font-family: 'Nunito Sans', sans-serif;
    }

    /* Main content layout */
    .block-container {
        max-width: 1050px;
        padding-top: 2.5rem;
        padding-bottom: 3rem;
    }

    /* --------------------------------------------------
       Branding
       -------------------------------------------------- */

    .brand {
        font-family: 'Pacifico', cursive;
        font-size: 30px;
        font-weight: 400;
        letter-spacing: 0;
        color: var(--lavender-dark);
        margin-bottom: 6px;
        line-height: 1.7;
    }

    .main-brand {
        font-family: 'Pacifico', cursive;
        font-size: 34px;
        font-weight: 400;
        letter-spacing: 0;
        color: var(--lavender-dark);
        margin-bottom: 10px;
        line-height: 1.6;
    }

    .subtitle {
        color: var(--muted);
        font-family: 'Nunito Sans', sans-serif;
        font-size: 15px;
        line-height: 1.7;
        margin-bottom: 28px;
    }

    .section-heading {
        font-family: 'Nunito Sans', sans-serif;
        font-size: 25px;
        font-weight: 800;
        letter-spacing: -0.3px;
        color: var(--text);
        margin-bottom: 10px;
    }

    /* --------------------------------------------------
       Sidebar
       -------------------------------------------------- */

    section[data-testid="stSidebar"] {
        background: linear-gradient(
            180deg,
            #F1EAF9 0%,
            #EAE1F5 100%
        );
        border-right: 1px solid #DED2EB;
    }

    section[data-testid="stSidebar"] > div {
        padding-top: 1.5rem;
    }

    /* Sidebar typography */
    section[data-testid="stSidebar"] * {
        font-family: 'Nunito Sans', sans-serif;
    }

    /* Keep Pacifico for sidebar branding */
    section[data-testid="stSidebar"] .brand {
        font-family: 'Pacifico', cursive !important;
        font-size: 30px;
        font-weight: 400;
        color: #604B83;
        margin: 0.3rem 0 0.5rem;
        line-height: 1.7;
    }

    /* Workspace heading */
    section[data-testid="stSidebar"]
    [data-testid="stMarkdownContainer"] strong {
        color: #76608F;
        font-size: 13px;
        font-weight: 800;
        letter-spacing: 1.5px;
    }

    /* Sidebar navigation buttons */
    section[data-testid="stSidebar"]
    div[data-testid="stButton"] > button {
        border-radius: 14px;
        min-height: 47px;
        padding: 0.65rem 1rem;
        font-family: 'Nunito Sans', sans-serif;
        font-size: 16px;
        font-weight: 800;
        letter-spacing: 0.1px;
        transition: all 0.18s ease;
    }

    /* Selected navigation button */
    section[data-testid="stSidebar"]
    div[data-testid="stButton"] > button[kind="primary"] {
        background: #789F8A;
        color: #FFFFFF;
        border: 1px solid #789F8A;
        box-shadow: 0 4px 10px rgba(77, 105, 88, 0.16);
    }

    section[data-testid="stSidebar"]
    div[data-testid="stButton"] > button[kind="primary"]:hover {
        background: #668B77;
        border-color: #668B77;
        color: #FFFFFF;
        transform: translateY(-1px);
    }

    /* Unselected navigation buttons */
    section[data-testid="stSidebar"]
    div[data-testid="stButton"] > button[kind="secondary"] {
        background: rgba(255, 255, 255, 0.76);
        color: #655577;
        border: 1px solid #DDD1E9;
        box-shadow: 0 2px 5px rgba(92, 70, 119, 0.03);
    }

    section[data-testid="stSidebar"]
    div[data-testid="stButton"] > button[kind="secondary"]:hover {
        background: #E2D6F0;
        color: #604B83;
        border-color: #C7B4DD;
        transform: translateY(-1px);
    }

    /* Sidebar dividers */
    section[data-testid="stSidebar"] hr {
        border-color: #D9CBE7;
        margin-top: 1.1rem;
        margin-bottom: 1.1rem;
    }

    /* Sidebar captions */
    section[data-testid="stSidebar"]
    [data-testid="stCaptionContainer"] {
        color: #81718F;
        font-size: 12px;
        font-weight: 600;
    }

    /* --------------------------------------------------
       Main buttons
       -------------------------------------------------- */

    div[data-testid="stButton"] > button {
        border-radius: 12px;
        min-height: 43px;
        font-family: 'Nunito Sans', sans-serif;
        font-weight: 700;
        transition: all 0.2s ease;
    }

    div[data-testid="stButton"] > button[kind="primary"] {
        background: var(--sage);
        color: white;
        border: 1px solid var(--sage);
    }

    div[data-testid="stButton"] > button[kind="primary"]:hover {
        background: var(--sage-hover);
        border-color: var(--sage-hover);
        color: white;
    }

    div[data-testid="stButton"] > button[kind="secondary"] {
        background: rgba(255, 255, 255, 0.72);
        color: #554968;
        border: 1px solid #DDD3E7;
    }

    div[data-testid="stButton"] > button[kind="secondary"]:hover {
        background: #E7DDF2;
        border-color: #CBB9DF;
        color: var(--lavender-dark);
    }

    /* --------------------------------------------------
       Input fields
       -------------------------------------------------- */

    div[data-testid="stTextInput"] input,
    div[data-testid="stTextArea"] textarea,
    div[data-testid="stSelectbox"] div[data-baseweb="select"] > div {
        border-radius: 11px;
        border-color: #E3DCE9;
        background: var(--surface);
        font-family: 'Nunito Sans', sans-serif;
    }

    div[data-testid="stTextInput"] input:focus,
    div[data-testid="stTextArea"] textarea:focus {
        border-color: #B5A0D0;
        box-shadow: 0 0 0 1px #B5A0D0;
    }

    /* Labels */
    label,
    [data-testid="stWidgetLabel"] p {
        color: #554D62;
        font-family: 'Nunito Sans', sans-serif;
        font-weight: 700;
    }

    /* --------------------------------------------------
       Dividers, alerts and downloads
       -------------------------------------------------- */

    hr {
        border-color: var(--border);
    }

    div[data-testid="stAlert"] {
        border-radius: 12px;
    }

    div[data-testid="stDownloadButton"] > button {
        border-radius: 11px;
        border-color: #D8CBE5;
        color: var(--lavender-dark);
        background: #F4EFF9;
        font-family: 'Nunito Sans', sans-serif;
        font-weight: 700;
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# --------------------------------------------------
# Session State
# --------------------------------------------------

if "active_tool" not in st.session_state:
    st.session_state.active_tool = "Write"

if "results" not in st.session_state:
    st.session_state.results = {}


# --------------------------------------------------
# Sidebar Navigation
# --------------------------------------------------

with st.sidebar:
    st.markdown(
        '<div class="brand">✨ Verba AI</div>',
        unsafe_allow_html=True,
    )

    st.caption("Your friendly AI writing companion")

    st.divider()

    st.markdown("**WORKSPACE**")

    tools = [
        "Write",
        "Rewrite",
        "Understand",
        "Summarize",
        "Action Items",
        "Smart Reply",
    ]

    for tool in tools:
        if st.button(
            tool,
            key=f"nav_{tool}",
            use_container_width=True,
            type=(
                "primary"
                if st.session_state.active_tool == tool
                else "secondary"
            ),
        ):
            st.session_state.active_tool = tool
            st.rerun()

    st.divider()

    st.caption("More features coming soon")
    st.caption("Accounts and saved work will be added later.")


# --------------------------------------------------
# Main Header
# --------------------------------------------------

st.markdown(
    '<div class="main-brand">Your ideas, made clearer.</div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="subtitle">'
    'Write, improve and understand text with a little help from AI.'
    '</div>',
    unsafe_allow_html=True,
)

active_tool = st.session_state.active_tool

st.markdown(
    f'<div class="section-heading">{active_tool}</div>',
    unsafe_allow_html=True,
)


# --------------------------------------------------
# Feature Forms
# --------------------------------------------------

if active_tool == "Write":
    show_write_tool()

elif active_tool == "Rewrite":
    show_rewrite_tool()

elif active_tool == "Understand":
    show_understand_tool()

elif active_tool == "Summarize":
    show_summarize_tool()

elif active_tool == "Action Items":
    show_action_items_tool()

elif active_tool == "Smart Reply":
    show_smart_reply_tool()

else:
    st.info(
        f"The {active_tool} workspace is planned for the next development "
        "stage. We'll implement and test each feature one at a time."
    )


# --------------------------------------------------
# Display Results for Write and Rewrite
# --------------------------------------------------

if active_tool == "Write":
    result_key = "Write"

elif active_tool == "Rewrite":
    result_key = (
        f"Rewrite: {st.session_state.get('rewrite_goal', 'Improve clarity')}"
        f": {st.session_state.get('rewrite_tone', 'Professional')}"
    )

else:
    result_key = None

if result_key and result_key in st.session_state.results:
    st.divider()
    st.markdown("### Your result")

    st.write(st.session_state.results[result_key])

    st.download_button(
        "Download result as a text file",
        data=st.session_state.results[result_key],
        file_name="verba_ai_result.txt",
        mime="text/plain",
        use_container_width=True,
    )

