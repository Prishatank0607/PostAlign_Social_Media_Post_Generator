import streamlit as st
from few_shot import FewShotPosts
from post_generator import generate_post
from post_generator import generate_post_with_trend
from trending_helper import fetch_trending_topics

st.set_page_config(page_title="PostAlign", layout="wide")

# Fetch trending topics
trending_topics = fetch_trending_topics()

st.sidebar.title("🔥 Trending Topics")
for topic in trending_topics:
    st.sidebar.write(f"- {topic}")

# Custom CSS for styling
st.markdown("""
    <style>
        /* Overall body styling */
        body {
            background-color: #333333; /* Dark grey background */
            color: #ffffff;           /* White text */
            font-family: 'Verdana', sans-serif;
        }

        /* Streamlit app background */
        .stApp {
            background-color: #444444; /* Slightly lighter grey */
        }

        .header {
            font-size: 36px;
            text-align: center;
            font-weight: bold;
            color: #ffffff;  /* White text */
            margin-bottom: 10px;
        }
        

        .subheader {
            font-size: 18px;
            text-align: center;
            color: #ffffff;  /* White text */
        }
            

        .nav-bar {
            text-align: center;
            padding: 10px;
            background: #666666; /* Complementary grey for the nav bar */
            border-radius: 10px;
            margin-bottom: 20px;
        }

        .nav-bar a {
            color: #ffffff;  /* White text for navigation links */
            text-decoration: none;
            padding: 10px 20px;
            margin: 0 10px;
            font-weight: bold;
        }

        .card {
            background: #555555; /* Darker grey for cards */
            padding: 20px;
            border-radius: 15px;
            text-align: center;
            box-shadow: 0px 4px 10px rgba(255, 255, 255, 0.1);
            transition: 0.3s;
        }
        .card:hover {
            transform: scale(1.05);
        }
        
        .nav-box {
    text-align: center;
    padding: 5px; 
    background-size: 15px 15px; 
    border-radius: 5px; 
    margin-top: 5px; 
    margin-bottom: 5px; 
}
.nav-box a {
    color: #ffffff;
    text-decoration: none;
    font-size: 16px; /* Smaller font size */
    font-weight: bold;
    padding: 5px 10px; /* Smaller padding for the link/button */
    border: 1px solid #ffffff; /* Thinner border */
    border-radius: 3px; /* Reduced border radius */
    transition: background 0.3s;
}
.nav-box a:hover {
    background: rgba(102, 102, 102, 0.7);
}

        .btn {
            background: #888888;
            color: #ffffff;
            padding: 10px;
            border-radius: 8px;
            font-weight: bold;
            cursor: pointer;
            transition: 0.3s;
            display: inline-block;
            width: 100%;
            border: none;
        }
        .btn:hover {
            background: #aaaaaa;
        }
    </style>
""", unsafe_allow_html=True)



# Navigation Bar
st.markdown("""
    <div class='nav-bar'>
        <a href='#home'>🏠 Home</a>
        <a href='#aboutus'>📂 About Us</a>
        <a href='#postus'>📝 Post Generator</a>
        <a href='#contactus'>📞 Contact Us</a>
    </div>
""", unsafe_allow_html=True)


# Home Section (anchor id = "home")
st.markdown("""
    <div id="home" class="home-us" style="text-align: center;">
        <h2>PostAlign: AI-Driven Social Media Content Generator</h2>
        <p>
            Create AI-powered posts with ease
        </p>
    </div>
""", unsafe_allow_html=True)

st.markdown("""
    <div class='nav-box'>
        <a href="#aboutus">Let's Go!</a>
    </div>
""", unsafe_allow_html=True)
st.markdown("<br><br>", unsafe_allow_html=True)

# About Us Section (anchor id = "aboutus")
st.markdown("""
    <div id="aboutus" padding: 40px 20px; background: #444444; border-radius: 10px; margin-bottom: 20px;">
        <h4>About PostAlign</h4>
        <p>
            Welcome to PostAlign—where cutting-edge AI meets creative content generation. Our platform harnesses the power of advanced language models like <strong>LLaMA 3.2</strong> and the modular capabilities of <strong>LangChain</strong> to deliver dynamic, AI-driven social media posts across multiple languages. 
        </p>
        <p>
            By combining LLaMA's robust natural language processing with LangChain's innovative approach to building complex AI workflows, PostAlign empowers content creators, marketers, and businesses to effortlessly generate engaging posts on trending topics—ranging from remote work and digital transformation to sustainability and leadership.
        </p>
        <p>
            Join us on our journey to revolutionize social media content creation and experience how next-generation AI can transform the way you communicate online.
        </p>
    </div>
""", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# Post Generator Section (anchor id = "postus")
st.markdown("""
    <div id="postus">
        <h4>📝 Generate Your Post</h4>
        <p>
            Create and customize your post effortlessly!
        </p>
    </div>
""", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# **Topic Selection Method**
st.markdown("##### **📌 Select How You Want to Choose a Topic**")
topic_selection = st.radio(
    "",
    ["🔥 Trending Topics", "✍️ Manual Topic Selection", "📌 Select from Given Tags"],
    key="topic_source"
)
st.markdown("<br><br>", unsafe_allow_html=True)

# **Topic Selection Based on Choice**
selected_topic = None
if topic_selection == "🔥 Trending Topics":
    st.markdown("##### **🔥 Generate post on Trending Topics**")
    selected_topic = st.selectbox("Select a Trending Topic:", options=trending_topics, key="trending_topic")

elif topic_selection == "✍️ Manual Topic Selection":
    st.markdown("##### **✍️ Enter Your Custom Topic**")
    selected_topic = st.text_input("Enter Your Topic:", placeholder="Type your topic here...", key="custom_topic")

elif topic_selection == "📌 Select from Given Tags":
    st.markdown("##### **📌 Choose from Suggested Tags**")
    fs = FewShotPosts()
    tags = fs.get_tags()
    selected_topic = st.selectbox("Select a Topic:", options=tags, key="tag_selection")
st.markdown("<br><br>", unsafe_allow_html=True)

# **Common Options for Post Customization**
st.markdown("##### **⚙️ Customize Your Post**")
col1, col2, col3 = st.columns(3)

with col1:
    selected_length = st.selectbox("Length", options=["Short", "Medium", "Long"], key="length_selection")
with col2:
    selected_language = st.selectbox("Language", options=["English", "Hindi", "Hinglish", "Spanish", "French", "Arabic", "Urdu", "Bengali", "Portuguese", "Russian"], key="language_selection")
with col3:
    selected_tone = st.selectbox("Tone", options=["Professional", "Casual", "Humorous", "Inspirational", "Neutral"], key="tone_selection")

# **Post Generation Button**
if selected_topic and st.button("🚀 Generate Post"):
    post = generate_post(selected_length, selected_language, selected_topic, selected_tone)
    st.success("✅ Your AI-generated post:")
    st.write(post)


st.markdown("""
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    <div id="contactus" style="text-align: center; padding: 20px; background: #444444; border-radius: 10px; margin-bottom: 20px;">
        <h4>Contact Us</h4>
        <p>
            Connect with us on social media or send your queries directly!
        </p>
        <div style="margin: 20px 0;">
            <i class="fab fa-google" style="font-size:40px; margin:0 10px;"></i>
            <i class="fab fa-linkedin-in" style="font-size:40px; margin:0 10px;"></i>
            <i class="fab fa-instagram" style="font-size:40px; margin:0 10px;"></i>
            <i class="fab fa-twitter" style="font-size:40px; margin:0 10px;"></i>
        </div>
        <div style="margin-top: 20px;">
            <h5>Send us a Query</h5>
            <textarea style="width: 80%; height: 100px; border-radius: 5px; padding: 10px; border: none;" placeholder="Type your message here..."></textarea>
        </div>
    </div>
""", unsafe_allow_html=True)


if st.button("📩 Send Query", key="send", help="Click to send your query"):
        st.success("Your query has been sent!")



