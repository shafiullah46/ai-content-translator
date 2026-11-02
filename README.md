# 🌍 AI Content Translator

![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![OpenAI](https://img.shields.io/badge/OpenAI-API-green.svg)
![Status](https://img.shields.io/badge/Status-Completed-success.svg)

An intelligent, Python-based multilingual translation microservice designed to convert English text into multiple target languages (Spanish and French) simultaneously using OpenAI's API.

---

## 🚀 Key Features

- **Multilingual Output Generation:** Parameterized prompts designed to fetch structured multi-language translations in a single API call.
- **Optimized Temperature:** Configured at `temperature=0.7` to balance linguistic fluidity and accurate translation.
- **Resilient Fallback Parsing:** Built-in multi-tier response handler to safely process standard OpenAI responses and custom mock environments.
- **Environment Security:** Secures credentials via system environment variables (`OPENAI_API_KEY`, `OPENAI_API_BASE`).

---

## 🛠️ Tech Stack

- **Language:** Python 3.x
- **SDK:** `openai` (Official Python Library)
- **Environment:** Virtualenv (`venv`)

---

## ⚙️ Installation & Usage

### 1. Clone the Repository
```bash
git clone [https://github.com/shafiullah46/ai-content-translator.git](https://github.com/shafiullah46/ai-content-translator.git)
cd ai-content-translator

2. Virtual Environment Setup
python -m venv venv
# On Windows PowerShell:
.\venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate

3. Install Dependencies
pip install openai

4. Set Environment Variables & Run
# On Windows PowerShell:
$env:OPENAI_API_KEY="your_api_key_here"
$env:OPENAI_API_BASE="your_base_url_here"

# Run the translator script
python translator.py

💻 Sample Execution
Input Text: "Good morning, how are you?"

Generated Translations:

Spanish: ¡Buenos días, ¿cómo estás?!

French: Bonjour, comment ça va ?

👨‍💻 Author
Shafiullah Niazi

Deputy Director ML/DevOps | Cloud & AI Infrastructure Specialist
