import scrapy
import re
import csv


class QuestionSpider(scrapy.Spider):
    name = "question_spider"
    start_urls = ["https://questions.examside.com/past-years/gate/question/the-initial-charge-in-the-1-f-capacitor-present-in-the-circu-gate-ee-2017-set-2-marks-1-5a8bc108f36b6.htm",
                  "https://questions.examside.com/past-years/gate/question/in-the-following-figure-c1-and-c2-are-ideal-capacitors-c1-ha-gate-ee-2012-marks-1-5a8bcb82e8e7f.htm"]

    """with open("gate.csv") as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            start_urls.append(row)"""
    def parse(self, response):
        question_meta = response.css("div.question-body>h3::text").get()
        question = response.css("div.question-body>div").extract_first()
        diagram = response.css("div.question-body>div>img::attr(src)").get()
        options = response.css("div.question-options>div>div.pa-4").extract()
        answer = response.css("div.option-item::attr(date-op-id)").get()
        if answer is None:
            answer = response.css("div.question-solution-container>div.text-center>b::text").get()
            options = None

        yield {
            "question_meta": question_meta,
            "question": question,
            "diagram": diagram,
            "answer": answer,
            "options": options
        }
