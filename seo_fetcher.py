from flask import abort


mock_data = {
    "wireless earbuds": {"search_volume": 12000, "keyword_difficulty": 35, "avg_cpc": 1.5},
    "monitor": {"search_volume": 8000, "keyword_difficulty": 45, "avg_cpc": 2.2},
    #"gaming laptop": {"search_volume": 15000, "keyword_difficulty": 50, "avg_cpc": 3.0},
    #"mechanical keyboard": {"search_volume": 7000, "keyword_difficulty": 40, "avg_cpc": 1.8},
}


def get_seo_metrics(keyword):
    
    lower_keyword = keyword.lower()

    if(lower_keyword in mock_data):
        return mock_data[lower_keyword]
    else:
        # abort 404 error if keyword is not in mock data
        abort(404, description=f"SEO metrics not found for keyword: {keyword}")
