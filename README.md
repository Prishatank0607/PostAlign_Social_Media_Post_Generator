**PostAlign: AI-Driven Social Media Content Generator**

**Overview**

PostAlign is an AI-driven social media content generation platform designed to help users create high-quality, engaging posts with minimal effort. The system leverages advanced natural language processing (NLP) models to generate refined posts based on various input features such as tone, language, post length, and trending topics. By automating content creation, PostAlign empowers individuals and businesses to optimize their social media presence efficiently.

PostAlign processes raw posts and enhances them by enriching content with structured attributes. Users can customize posts by selecting specific tones, languages, and styles to match their target audience and platform requirements.

**Features**

**Data Preparation and Processing**

- Stores and processes posts in JSON format.
- Applies preprocessing techniques to enhance raw posts.
- Extracts and integrates features such as topic classification, post length categorization, and multilingual support.

**AI-Driven Content Generation**

- Utilizes Llama 3.2 for AI-powered post refinement.
- Supports multiple tones including Professional, Casual, Humorous, Inspirational, and Neutral.
- Generates posts in multiple languages: English, Hindi, Hinglish, Spanish, French, Arabic, Urdu, Bengali, Portuguese, and Russian.
- Adapts to trending topics for relevance and engagement.

**User Interface Development**

- Built using Streamlit for a simple and interactive web-based interface.
- Allows users to input parameters and generate tailored posts instantly.
- Provides real-time previews of AI-generated content.

**New Techniques Learned**

- Implementing NLP techniques for text enhancement and tone adaptation.
- Integrating Groq API, NewsAPI and LangChain for seamless AI-based content generation.
- Developing a lightweight and responsive frontend using Streamlit.

**Insights Generation**

- Enables users to compare different post tones and formats. Users can also customize post length (Short, Medium, Long) and select trending topics such as AI integration, remote work, digital transformation, DEI (Diversity, Equity, and Inclusion), sustainability, leadership, health, and global concerns for more tailored content.
- Provides AI-suggested enhancements based on best-performing content strategies.
- Assists in optimizing posts for social media engagement.

**How to Use**

1. Clone the repository:
   ```
   git clone https://github.com/Prishatank0607/PostAlign
   ```
2. Navigate to the project directory:
   ```
   cd PostAlign
   ```
3. Install required dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Run the application:
   ```
   streamlit run main.py
   ```
5. Interact with the system to generate AI-powered social media posts.

**Dependencies**

- Python libraries: pandas, NumPy, Streamlit
- AI model: Llama 3.2 via Groq API and NewsAPI
- Additional tools: LangChain for prompt processing

**Dataset Source**
The dataset consists of 60 manually created raw posts stored in JSON format, which are preprocessed and enriched before AI-based content generation.

