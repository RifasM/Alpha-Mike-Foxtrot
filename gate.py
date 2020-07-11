import scrapy
import re


class GateSpider(scrapy.Spider):
    name = "gate_spider"
    start_urls = [
        "https://www.gatequestions.com/",
    ]
    interesting_url = re.compile("https://questions.examside.com/"
                                 "past-years/gate/"
                                 "gate-\\w{2,3}/[\\w-]+/[\\w-]+")
    links = []

    def parse(self, response):
        for link in response.css("a"):
            if re.fullmatch(self.interesting_url, str(link)):
                self.links.append(link)

        for next_page in response.css('a'):
            yield response.follow(next_page, self.parse)

    print("Completed!")
    print("Interesting links: ")
    for link in links:
        print(link)
