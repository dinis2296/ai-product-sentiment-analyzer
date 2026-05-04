
# Fetch data from Hacker News API and save to CSV

import requests
import pandas as pd

# Get top story IDs
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
response = requests.get(url)
story_ids = response.json()[:50]

posts = []

for story_id in story_ids:
    story_url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
    story = requests.get(story_url).json()

    if story and "title" in story:
        posts.append({
            "title": story.get("title", ""),
            "score": story.get("score", 0),
            "comments": story.get("descendants", 0)
        })

df = pd.DataFrame(posts)

print(df.head())

df.to_csv("data.csv", index=False)
