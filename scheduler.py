from datetime import datetime
from ai_generator_google import generate_blog_post
import seo_fetcher as seo
from apscheduler.schedulers.background import BackgroundScheduler


def routine():
    for i in seo.mock_data:
        seo_data = seo.get_seo_metrics(i)
        content = generate_blog_post(i,seo_data)

        filename = f"generated/{i}_{datetime.now().strftime('%Y-%m-%d')}.md"
        with open(filename, "w") as f:
            f.write(content)
        f.close()
        print(f"Generated post: {filename}")


def start_scheduler():
    scheduler = BackgroundScheduler()
    # for testing purposes 1 minute
    scheduler.add_job(routine, 'interval', minutes=1)
    scheduler.start()