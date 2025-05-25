<h1>🧠 AI Research Assistant using LangChain</h1>

<p>This project is an AI-powered research assistant built with <strong>LangChain</strong>, <strong>Anthropic Claude</strong>, and various tools like <strong>DuckDuckGo search</strong>, <strong>Wikipedia</strong>, and a <strong>save-to-file utility</strong>. It generates research summaries using LLMs and integrates external tools to retrieve and persist information effectively.</p>

<hr/>

<h2>🚀 Features</h2>
<ul>
  <li>✅ Ask research questions via command-line input</li>
  <li>🔍 Retrieve up-to-date info using <strong>DuckDuckGo</strong></li>
  <li>📚 Get definitions or summaries using <strong>Wikipedia</strong></li>
  <li>💾 Save results automatically to a <code>.txt</code> file</li>
  <li>🤖 Responses are structured using <strong>Pydantic models</strong></li>
  <li>🧩 Powered by <strong>Claude 3.5 Sonnet</strong> via <code>langchain-anthropic</code></li>
</ul>

<hr/>

<h2>📁 Project Structure</h2>
<pre>
.
├── Main.py                 # Main app logic
├── tools.py                # Tools: DuckDuckGo, Wikipedia, Save-to-file
├── requirements.txt        # Project dependencies
└── research_output.txt     # Output file where research results are saved
</pre>

<hr/>

<h2>📦 Requirements</h2>
<ul>
  <li>Python 3.8+</li>
  <li>API key for <strong>Anthropic Claude</strong> (via <code>.env</code> file)</li>
</ul>

<hr/>

<h2>🔧 Installation</h2>
<ol>
  <li><strong>Clone the repository</strong>
    <pre><code>git clone &lt;your-repo-url&gt;
cd &lt;project-folder&gt;</code></pre>
  </li>
  <li><strong>Install dependencies</strong>
    <pre><code>pip install -r requirements.txt</code></pre>
  </li>
  <li><strong>Create a <code>.env</code> file</strong> with your Anthropic API key:
    <pre><code>ANTHROPIC_API_KEY=your_api_key_here</code></pre>
  </li>
</ol>

<hr/>

<h2>🛠 Tools Used</h2>

<h3>1. DuckDuckGo Search Tool</h3>
<p>Searches the web for relevant information on the given query.</p>

<h3>2. Wikipedia Tool</h3>
<p>Fetches summaries and definitions from Wikipedia.</p>

<h3>3. Save Tool</h3>
<p>Saves the final structured output to <code>research_output.txt</code>.</p>

<hr/>

<h2>✨ How It Works</h2>
<ul>
  <li>You enter a research query.</li>
  <li>Claude 3.5 Sonnet processes the query with help from tools.</li>
  <li>The response is structured into:
    <ul>
      <li>Topic</li>
      <li>Summary</li>
      <li>Sources</li>
      <li>Tools used</li>
    </ul>
  </li>
  <li>The structured response is printed and optionally saved.</li>
</ul>

<hr/>

<h2>🧪 Example</h2>
<pre><code>Enter your research query: What are the latest advancements in quantum computing?</code></pre>

<pre><code>--- Research Output ---
Timestamp: 2025-05-25 18:42:10

Topic: Quantum Computing
Summary: Recent breakthroughs include IBM's 127-qubit processor and Google's quantum supremacy demonstration...
Sources: [link1, link2, ...]
Tools Used: ['DuckDuckGo', 'Wikipedia']
</code></pre>

<hr/>

<h2>📤 Future Improvements</h2>
<ul>
  <li>Integrate OpenAI GPT models (e.g., GPT-4)</li>
  <li>Add PDF export and citation generator</li>
  <li>Build a web interface (Flask or Streamlit)</li>
  <li>Add real-time chat mode</li>
</ul>

<hr/>

<h2>📜 License</h2>
<p>MIT License. See <code>LICENSE</code> file for more details.</p>

<hr/>

<h2>👨‍💻 Author</h2>
<p>
  Md Abdul Rahman<br/>
  ✉️ <a href="mailto:abdul.rahman.190704@gmail.com">My Email</a><br/>
  🌐 <a href="https://famous-swan-0ebc70.netlify.app/">My Portfolio</a><br/>
  🐍 Python | 🤖 AI | 📚 ML | 🌐 Web
</p>