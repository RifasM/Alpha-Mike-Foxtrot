import csv

import scrapy
import re


class GateSpider(scrapy.Spider):
    name = "gate_spider"
    start_urls = [
        "https://questions.examside.com",
    ]
    """interesting_url = re.compile("https://questions.examside.com/
                                    past-years/gate/question/
                                    [\w-]+.htm")"""
    interesting_url = re.compile("https://questions.examside.com/"
                                 "past-years/gate/"
                                 "gate-ece/[\\w-]+/[\\w-]+")
    links = []

    def parse(self, response):
        anchor = response.css("a::attr(href)").getall()
        for link in anchor:
            link = self.start_urls[0] + link
            if re.match(self.interesting_url, str(link)):
                print(">>> Link found!\n\tAppending")
                self.links.append(link)

        for next_page in anchor:
            yield response.follow(self.start_urls[0]+next_page, self.parse)

    print("Completed!")
    print("Writing to csv File: ")

    with open('gate.csv', 'w') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(links)
        csvFile.close()
