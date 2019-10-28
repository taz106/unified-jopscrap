# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import psycopg2

class JobscrapperPipeline(object):
    def open_spider(self, spider):
        hostname = 'localhost'
        username = 'testuser'
        password = 'testuser' # your password
        database = 'jobad'
        self.connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
        self.cur = self.connection.cursor()

    def close_spider(self, spider):
        self.cur.close()
        self.connection.close()

    def process_item(self, item, spider):
        self.cur.execute(
            "insert into tempjobad(title, description, company_name, location, ad_url) \
                select %s, %s, %s, %s, %s \
                    where not exists (select * from tempjobad where title = %s AND company_name = %s))", 
                    (item['title'],item['description'], item['company_name'], item['location'], item['ad_url'], item['title'], item['company_name'])
        )
        self.connection.commit()
        return item


class TutorialPipeline(object):

    def open_spider(self, spider):
        hostname = 'localhost'
        username = 'testuser'
        password = 'testuser' # your password
        database = 'jobad'
        self.connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
        self.cur = self.connection.cursor()

    def close_spider(self, spider):
        self.cur.close()
        self.connection.close()

    def process_item(self, item, spider):
        self.cur.execute("insert into quotes(content,author) values(%s,%s)",(item['content'],item['author']))
        self.connection.commit()
        return item
