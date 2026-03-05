# 👨‍🍳 Personal Chef AI Agent

An intelligent, context-aware AI Agent built with **LangChain** and **LangGraph** that helps users turn their kitchen leftovers into delicious meals using real-time web searching.

## 🌟 Overview
This project leverages the **Gemini 2.5 Flash** model and the **Tavily Search API** to create a conversational chef. It doesn't just guess recipes; it searches the live web to find the best culinary matches for the specific ingredients you have on hand.

## 🚀 Key Features
* **Real-time Recipe Discovery**: Uses the Tavily search tool to find current recipes online.
* **Persistent Memory**: Powered by `InMemorySaver`, allowing the agent to remember your ingredients across multiple turns of conversation.
* **Detailed Instructions**: Can provide summaries or full step-by-step cooking guides upon request.
* **Advanced Reasoning**: Utilizes Google's `gemini-2.5-flash` for high-speed, accurate tool calling.



## 🛠️ Technical Setup

### Prerequisites
You will need the following API keys stored in your environment or Colab secrets:
* `GOOGLE_API_KEY`: For the Gemini model.
* `TAVILY_API_KEY`: For web search capabilities.
* `LANGCHAIN_API_KEY`: (Optional) For LangSmith tracing.

### Dependencies
```bash
pip install -U langchain-google-genai tavily-python langgraph