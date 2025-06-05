from flask import Flask, jsonify, request

from ai_generator_google import generate_blog_post
from scheduler import start_scheduler
from seo_fetcher import get_seo_metrics

app = Flask(__name__)

# starts scheduler soon as application begins
start_scheduler()

@app.route('/generate', methods=['GET'])

# grabs keyword from url, if keyword exists, grabs mock seo_data, and generate blog_post, returns json
def generate():
    keyword = request.args.get('keyword')
    
    # error 400 if no keyword
    if not keyword:
        return jsonify({'error': "Provide a keyword"}), 400

    seo_data = get_seo_metrics(keyword)
    content = generate_blog_post(keyword, seo_data)

    return jsonify({
        "keyword": keyword,
        "seo_data": seo_data,
        "post": content
    })


if __name__ == "__main__":
    app.run(debug=True)