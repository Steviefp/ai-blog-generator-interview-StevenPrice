import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# generates blog_post with prompt + keyword, returns the response replacing AFF_LINK_N with dummy links
def generate_blog_post(keyword, seo_data):
    prompt = f"""Write a blog post draft about {keyword}.
            Use this data, search volume: {seo_data['search_volume']}, keyword difficulty: {seo_data['keyword_difficulty']},
            average cpc: {seo_data["avg_cpc"]}
            Using HTML or markdown, Place 3 (replace the n with 1,2,3) {{AFF_LINK_n}} placeholders.
            Do not include any introductions or preamble. Start directly with the blog content, beginning with the title or first paragraph."""
    
    response = client.models.generate_content(
        model="gemini-2.5-flash-preview-05-20",
        contents=prompt
    )

    # replace links with dummy links
    
    return response.text.replace("{AFF_LINK_1}", "https://example.com/aff1") \
                  .replace("{AFF_LINK_2}", "https://example.com/aff2") \
                  .replace("{AFF_LINK_3}", "https://example.com/aff3")

