from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_core.tools import Tool
from datetime import datetime

def save_to_txt(data: str, filename: str = "research_output.txt"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_text = f"--- Research Output ---\nTimestamp: {timestamp}\n\n{data}\n\n"
    """Saves the given data to a text file."""
    with open(filename, "a", encoding="utf-8") as f:
        f.write(formatted_text)

save_tool = Tool(
    name="save_text_to_file",
    func=save_to_txt,
    description="Saves the research output to a text file. Input should be the data to save.",
)

search = DuckDuckGoSearchRun()
search_tool = Tool(
    name="search",
    func=search.run,
    description="Useful for searching the web for information. Input should be a search query.",
)

api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=1000)
wiki_tool = WikipediaQueryRun(api_wrapper=api_wrapper)