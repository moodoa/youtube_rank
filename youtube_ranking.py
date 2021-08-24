import requests
from bs4 import BeautifulSoup

def _get_top_video(location, category):
    video_info = {}
    text = requests.get(f"https://tw.noxinfluencer.com/youtube-video-rank/top-{location}-{category}-video-day").text
    soup = BeautifulSoup(text, "lxml")
    top1 = soup.select_one("div#number-one-video")
    video_info["title"] = top1.select_one("a")["title"]
    video_info["followers"] = top1.select_one("span.sub").string
    video_info["channel"] = top1.select_one("a.name").string
    video_analytics_url = top1.select_one("a.video-title")["href"]
    website = "https://www.youtube.com/watch?v="
    video_code = video_analytics_url.split("/")[-1]
    video_info["url"] = website+video_code
    return video_info
