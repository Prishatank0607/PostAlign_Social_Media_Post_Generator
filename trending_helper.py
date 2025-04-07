import requests
import os

# Load API key from environment variables for security
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
NEWS_API_URL = "https://newsapi.org/v2/top-headlines?country=us&apiKey="

def fetch_trending_topics():
    """Fetch trending topics from NewsAPI and return a list of headlines or keywords."""
    try:
        response = requests.get(f"{NEWS_API_URL}{NEWS_API_KEY}")
        data = response.json()
        if "articles" in data:
            return [article["title"] for article in data["articles"][:5]]  # Return top 5 trending topics
        return ["No trending topics available"]
    except Exception as e:
        print("Error fetching trending topics:", e)
        return ["Error fetching data"]

if __name__ == "__main__":
    print(fetch_trending_topics())  # Test the function
