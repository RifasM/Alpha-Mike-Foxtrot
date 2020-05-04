import scrapy
import csv


class VTUSpider(scrapy.Spider):
    name = 'vtu-spider'
    start_urls = ['https://www.vtu4u.com/results/1cr17cs066?cbse=1']

    sgpa = [['name', 'sem1', 'sem2', 'sem3', 'sem4', 'sem5']]

    def parse(self, response):
        for student in response.css('table.table-hover'):

            """
            VTUSpider.sgpa.append(['https://www.indiabix.com/'+(puzzles.css('img ::attr(src)')[0].extract())[1:],
                                        puzzles.css('table>tr>td>span ::text')[2].get(),
                                        puzzles.css('table>tr>td ::text')[5].get()])"""
            yield {'name': student.css('.ng-scope').extract(),
                       'sem2': student.css('table>tr>td ::text').get()}

        for next_page in response.css('p.mx-pager>a'):
            yield response.follow(next_page, self.parse)

        with open('cse.csv', 'w') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerows(VTUSpider.sgpa)
            csvFile.close()
