import scrapy
import re
import csv


class QuestionSpider(scrapy.Spider):
    name = "question_spider"
    start_urls = ["https://questions.examside.com/past-years/gate/question/the-initial-charge-in-the-1-f-capacitor-present-in-the-circu-gate-ee-2017-set-2-marks-1-5a8bc108f36b6.htm"]

    """with open("gate.csv") as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            start_urls.append(row)"""
    def parse(self, response):
        type = response.css("div.question-body>h3").get()
        question = response.css("div.question-body>div::text").get()
        diagram = response.css("div.question-body>div>img::attr(src)").get()
        answer = response.css("div.option-item::attr(date-op-id)").get()

        yield {
            "type": type,
            "question": question,
            "diagram": diagram,
            "answer": answer
        }
