import scrapy
from scrapy_playwright.page import PageMethod

class IpoSpider(scrapy.Spider):
    name = 'ipo'
    allowed_domains = ['nepsebajar.com']
    start_urls = ['https://www.nepsebajar.com/ipo-pipelinewewe']
    def start_requests(self):
        yield scrapy.Request(self.start_urls[0],
                            meta=dict(
                                playwright=True,
                                playwright_include_page=True,
                                playwright_page_methods=[
                                    # This where we can implement scrolling if we want
                                    PageMethod('wait_for_selector', 'table#example tbody tr'),
                                ]
                            )
                            )
    async def parse(self, response):
        tabledata= response.css('table#example tbody tr')
        # opening json file 
        with open('ipodata.json', 'w') as f:
            f.write('[')
            for data in tabledata:
                company_name = (data.css('td:nth-child(1) a::text').get()).strip()
                symbol = (data.css('td:nth-child(2) a::text').get()).strip()
                total_issue_unit = int(data.css('td:nth-child(3)::text').get())
                issue_type_info = data.css('td:nth-child(4)::text').get().strip()
                if '-' in issue_type_info:
                    issue_type_info = data.css('td:nth-child(4)::text').get().split('-')[1].strip()
                if 'For' in issue_type_info:
                    issue_type = issue_type_info.split('For')[1].strip()
                else:
                    issue_type = issue_type_info
                issue_manager = (data.css('td:nth-child(5)::text').get()).strip()
                opening_date = data.css('td:nth-child(6)::text').get().replace('/', '-')
                closing_date = data.css('td:nth-child(7)::text').get().replace('/', '-')
                f.write('{\n')
                f.write(f'"company_name": "{company_name}",\n"symbol":"{symbol}",\n"total_unit": {total_issue_unit},\n"issue_type":"{issue_type}",\n"issue_manager":"{issue_manager}",\n"opening_date": "{opening_date}",\n"closing_date": "{closing_date}"\n')
                f.write('},')
            f.write(']')
                
    
