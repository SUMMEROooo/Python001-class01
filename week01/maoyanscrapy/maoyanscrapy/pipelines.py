# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class MaoyanscrapyPipeline:
    def process_item(self, item, spider):
        movie_name = item['movie_name']
        movie_type = item['movie_type']
        movie_time = item['movie_time']
        output = f'"{movie_name}","{movie_type}","{movie_time}"\r\n'
        with open('./maoyanTop10ByScrapy.csv', 'a+', encoding='utf-8') as article:
            article.write(output)
            # with.open默认会关，如下代码可不写
            article.close
        return item
