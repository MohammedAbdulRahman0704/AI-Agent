<div align="center">
  <h1>🧠 AI Research Assistant using LangChain</h1>
  <p>An AI-powered research assistant leveraging <strong>LangChain</strong>, <strong>Anthropic Claude</strong>, and tools like <strong>DuckDuckGo search</strong>, <strong>Wikipedia</strong>, and a save-to-file utility to generate research summaries and effectively manage information.</p>
  <hr style="border: 1px solid #d3d3d3;">
</div>

## 🚀 Features

- ✅ Ask research questions via command-line input
- 🔍 Retrieve up-to-date info using **DuckDuckGo**
- 📚 Get definitions or summaries using **Wikipedia**
- 💾 Save results automatically to a `.txt` file
- 🤖 Responses are structured using **Pydantic models**
- 🧩 Powered by **Claude 3.5 Sonnet** via `langchain-anthropic`

<hr style="border: 1px solid #d3d3d3;">

## 📁 Project Structure

.
├── Main.py             # Main app logic
├── tools.py            # Tools: DuckDuckGo, Wikipedia, Save-to-file
├── requirements.txt    # Project dependencies
└── research_output.txt # Output file where research results are saved


<hr style="border: 1px solid #d3d3d3;">

## 📦 Requirements

- Python 3.8+
- API key for **Anthropic Claude** (via `.env` file)

<hr style="border: 1px solid #d3d3d3;">

## 🔧 Installation

1.  **Clone the repository**
    ```bash
    git clone <your-repo-url>
    cd <project-folder>
    ```
2.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Create a `.env` file** with your Anthropic API key:
    ```
    ANTHROPIC_API_KEY=your_api_key_here
    ```

<hr style="border: 1px solid #d3d3d3;">

## 🛠 Tools Used

### 1. DuckDuckGo Search Tool

<p>Searches the web for relevant information on the given query.</p>

### 2. Wikipedia Tool

<p>Fetches summaries and definitions from Wikipedia.</p>

### 3. Save Tool

<p>Saves the final structured output to <code>research_output.txt</code>.</p>

<hr style="border: 1px solid #d3d3d3;">

## ✨ How It Works

- You enter a research query.
- Claude 3.5 Sonnet processes the query with help from tools.
- The response is structured into:
  - Topic
  - Summary
  - Sources
  - Tools used
- The structured response is printed and optionally saved.

<hr style="border: 1px solid #d3d3d3;">

## 🧪 Example

Enter your research query: What are the latest advancements in quantum computing?


--- Research Output ---
Timestamp: 2025-05-25 18:42:10

Topic: Quantum Computing
Summary: Recent breakthroughs include IBM's 127-qubit processor and Google's quantum supremacy demonstration...
Sources: [link1, link2, ...]
Tools Used: ['DuckDuckGo', 'Wikipedia']


<hr style="border: 1px solid #d3d3d3;">

## 📤 Future Improvements

- Integrate OpenAI GPT models (e.g., GPT-4)
- Add PDF export and citation generator
- Build a web interface (Flask or Streamlit)
- Add real-time chat mode

<hr style="border: 1px solid #d3d3d3;">

## 📜 License

MIT License. See `LICENSE` file for more details.

<hr style="border: 1px solid #d3d3d3;">

## 👨‍💻 Author

Md Abdul Rahman<br/>
✉️ [My Email](mailto:abdul.rahman.190704@gmail.com)<br/>
🌐 [My Portfolio](https://famous-swan-0ebc70.netlify.app/)<br/>
🐍 Python | 🤖 AI | 📚 ML | 🌐 Web