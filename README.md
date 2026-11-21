# ✨ Verba AI – AI Writing & Document Assistant

Verba AI is an AI-powered writing and document assistant built using Python and Streamlit. It helps users write, improve, understand and organise text through a collection of intelligent writing tools.

[Try Verba AI](https://verba-ai.streamlit.app)
---
## Features

Verba AI currently offers six AI-powered tools:

| Tool | Description |
|---|---|
|  **Write** | Generate content based on your task, audience, tone and instructions. |
|  **Rewrite** | Improve existing text by adjusting its clarity, grammar, length and tone. |
|  **Understand** | Explain documents, answer questions and identify important information. |
|  **Summarize** | Turn lengthy text into concise and meaningful summaries. |
|  **Action Items** | Extract important tasks and actionable points from text. |
|  **Smart Reply** | Generate suitable replies based on the context of a message. |

## Technologies Used

- **Python**
- **Streamlit**
- **Groq API**
- **OpenAI GPT-OSS 20B**

## Project Structure
verba-ai/
│
├── app.py
├── ai_service.py
├── requirements.txt
├── .gitignore
│
└── tools/
    ├── __init__.py
    ├── write.py
    ├── rewrite.py
    ├── understand.py
    ├── summarize.py
    ├── action_items.py
    └── smart_reply.py
```

## ⚙️ Run Locally

Follow these steps to run Verba AI on your computer.

### 1. Clone the repository

```bash
git clone https://github.com/nishipatwari9-ops/verba-ai.git
```

### 2. Navigate to the project folder

```bash
cd verba-ai
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

For Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure your API key

Create a folder named `.streamlit` in the project directory.

Inside it, create a file named `secrets.toml` and add:

```toml
GROQ_API_KEY = "your_groq_api_key"
```

Get your API key from [Groq Console](https://console.groq.com/).

**Important:** Never upload your API key or `secrets.toml` file to GitHub.

### 7. Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

## ☁️ Deployment

Verba AI is deployed using **Streamlit Community Cloud** and is accessible online.

👉 [Open Verba AI](https://verba-ai.streamlit.app)

## Future Improvements

Planned features for future versions include:

- User registration and authentication
- Saving and managing previous work
- Writing history and saved drafts
- User feedback and suggestions
- Further UI and usability improvements

Developed as a personal AI application project to explore AI-powered writing assistance, API integration and web application development.
