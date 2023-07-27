import scrapy

class YoutubeSpider(scrapy.Spider):
    name = "youtube"
    start_urls = [
        "https://www.youtube.com/results?search_query="
    ]

    def parse(self, response):
        for song in self.settings.get("SONGS", []):
            query = f"{song['name']} {song['artist']} youtube"
            url = f"https://www.youtube.com/results?search_query={query}"
            yield scrapy.Request(url, callback=self.parse_video_link, meta={"song": song})

    def parse_video_link(self, response):
        song = response.meta["song"]
        video_link_element = response.css("a.yt-uix-tile-link").get()
        if video_link_element:
            video_link = response.urljoin(video_link_element)
            yield {
                "song": song["name"],
                "artist": song["artist"],
                "youtube_link": video_link,
            }
        else:
            yield {
                "song": song["name"],
                "artist": song["artist"],
                "youtube_link": None,
            }
