from llm_helper import llm
from few_shot import FewShotPosts
from trending_helper import fetch_trending_topics

few_shot = FewShotPosts()


def get_length_str(length):
    if length == "Short":
        return "1 to 5 lines"
    if length == "Medium":
        return "6 to 10 lines"
    if length == "Long":
        return "11 to 15 lines"


def generate_post(length, language, tag, tone):
    prompt = get_prompt(length, language, tag, tone)
    response = llm.invoke(prompt)
    return response.content


def get_prompt(length, language, tag, tone):
    length_str = get_length_str(length)

    prompt = f'''
    Generate a LinkedIn post using the below information. No preamble.

    1) Topic: {tag}
    2) Length: {length_str}
    3) Language: {language}
    4) Tone: {tone}
    If Language is Hinglish then it means it is a mix of Hindi and English. 
    The script for the generated post should can be in any top 10 languages in the world like English, Hinglish(English + Hindi) Mandarin, Chinese, Hindi, Spanish, French, Arabic, Bengali, Portuguese, Russian, and Urdu..
    '''
    # prompt = prompt.format(post_topic=tag, post_length=length_str, post_language=language)

    examples = few_shot.get_filtered_posts(length, language, tag, tone)

    if len(examples) > 0:
        prompt += "4) Use the writing style as per the following examples."

    for i, post in enumerate(examples):
        post_text = post['text']
        prompt += f'\n\n Example {i+1}: \n\n {post_text}'

        if i == 1: # Use max two samples
            break

    return prompt

def generate_post_with_trend(user_topic=None, tone="neutral", length="medium", language="English"):
    """
    Generates a post based on user-specified topic or a trending topic.
    """
    topics = fetch_trending_topics()  # Get trending topics
    chosen_topic = user_topic if user_topic else topics[0]  # Use user topic if provided, else first trending topic

    print(f"Generating post for topic: {chosen_topic}")  # Debugging

    return generate_post(chosen_topic, tone, length, language)

if __name__ == "__main__":
    print(generate_post("Medium", "English", "Mental Health", "Professional"))
