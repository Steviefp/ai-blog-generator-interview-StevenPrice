from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def generate_blog_post(keyword, seo_data):
    prompt = f"""Write a blog post draft about {keyword}.
            Use this data, search volume: {seo_data['search_volume']}, keyword difficulty: {seo_data['keyword_difficulty']},
            average cpc: {seo_data["avg_cpc"]}
            Using HTML or markdown, Place 3 (replace the n with 1,2,3) {{AFF_LINK_n}} placeholders.
            Do not include any introductions or preamble. Start directly with the blog content, beginning with the title or first paragraph."""
    
    promptResponse = client.chat.completions.create(
        model='gpt-4o',
        messages=[{'role': 'user', 'content': prompt}],
        temperature = 0.7
    )

    return promptResponse.choices[0].message.content