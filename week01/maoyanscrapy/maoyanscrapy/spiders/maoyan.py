import scrapy
# 导入items包
from maoyanscrapy.items import MaoyanscrapyItem
# 导入选择器
from scrapy.selector import Selector

class MaoyanSpider(scrapy.Spider):
    # 爬虫名称
    name = 'maoyan'
    # 允许爬的域名范围
    allowed_domains = ['maoyan.com']
    # 爬的地址
    start_urls = ['https://maoyan.com/films?showType=3']

    # 默认爬取start_urls中的页面内容，即调用方法start_requests(self)
    # 若不只是爬取start_urls中的内容，可注释parse方法，重写start_requests方法
    def parse(self, response):
        #pass
        # 接收解析的数据
        # items = []
        # 通过选择器使用xpath获取
        movies = Selector(response=response).xpath('//div[@class="movie-hover-info"]')
        #print(movies)
        # 爬取目标前10部电影
        tag_movie_info_idx = 0
        for cur_movie in movies :
            item = MaoyanscrapyItem()
            # 爬取超过10部，退出
            if tag_movie_info_idx == 10 :
                break
            tag_movie_info_idx = tag_movie_info_idx + 1
            tag_movie_title_idx = -1
            cur_movie_infos = cur_movie.xpath('./div[@class="movie-hover-title"]')
            for movie_info in cur_movie_infos :
                tag_movie_title_idx = tag_movie_title_idx + 1
                #print(movie_info)
                if tag_movie_title_idx == 0 :
                    # 电影名称
                    print(movie_info.xpath('span/text()').extract_first())
                    item['movie_name'] = movie_info.xpath('span/text()').extract_first()
                    continue
                if tag_movie_title_idx == 1 :
                    # 电影类型
                    print(movie_info.xpath('.//text()').extract()[2].strip())
                    item['movie_type'] = movie_info.xpath('.//text()').extract()[2].strip()
                    continue
                break
            # 上映时间
            cur_movie_time = cur_movie.xpath('./div[@class="movie-hover-title movie-hover-brief"]//text()').extract()[2].strip()
            print(cur_movie_time)
            item['movie_time'] = cur_movie_time
            yield item
