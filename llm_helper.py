from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()
llm = ChatGroq(groq_api_key=os.getenv("GROQ_API_KEY"), model_name="llama-3.1-8b-instant")
news_api_key = os.getenv("NEWS_API_KEY")  # Fetch NewsAPI key from environment variables
NEWS_API_URL = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={news_api_key}"

if __name__ == "__main__":
    response = llm.invoke("How pets understand humans? ")
    print(response.content)





