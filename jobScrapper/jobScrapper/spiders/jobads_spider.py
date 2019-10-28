import scrapy
from jobScrapper.items import JobscrapperItem 


class JobAdsSpider(scrapy.Spider):
    name = "jobads"
    start_urls = [
        'https://se.indeed.com/jobb?l=sweden&start=0',
        'https://se.indeed.com/jobb?l=sweden&start=10',
        'https://se.indeed.com/jobb?l=sweden&start=20'
    ]

    adurls = []

    def parse(self, response):
        for jobad in response.css('div.jobsearch-SerpJobCard.row.result'):
            self.adurls.append('https://se.indeed.com' + jobad.css("a.jobtitle").attrib['href'])
            print(self.adurls)
            # yield {
            #     'title': jobad.css("a.jobtitle").attrib['title'],
            #     'url': jobad.css("a.jobtitle").attrib['href']
            # }
            # joburl = jobad.css("a.jobtitle").attrib['href']
            # if joburl is not None:
            #     yield response.follow(joburl, callback=self.parsepage)
        for adurl in self.adurls:
            request = scrapy.Request(adurl, callback=self.parsepage, cb_kwargs=dict(ad_url=adurl))
            yield request

    def parsepage(self, response, ad_url):
        jobad = response.css('div.jobsearch-JobComponent')
        
        jobad_title = jobad.css('h3.jobsearch-JobInfoHeader-title::text').get()
        jobad_description = ''.join(jobad.xpath('//div[@id="jobDescriptionText"]/descendant::text()').extract())
        jobad_company_name = jobad.css('h4.jobsearch-CompanyReview--heading::text').get()
        jobad_location = jobad.css('span.jobsearch-JobMetadataHeader-iconLabel::text').get()

        jobScrapperItem = JobscrapperItem(title=jobad_title, description=jobad_description, company_name=jobad_company_name, location=jobad_location, ad_url = ad_url)
        print(jobScrapperItem, end="=======================================>")
        yield jobScrapperItem