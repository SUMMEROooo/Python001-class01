学习笔记

# 安装的软件包版本（迁移时可做同一版本软件包的安装）
pip install -r requirements.txt

# 创建scrapy项目
scrapy startproject 项目名称（spiders）
scrapy genspider example example.com（最好是真正爬取的域名）

# 运行scrapy项目
scrapy crawl 爬虫名字

# setting文件USER_AGENT随机生成（有些网站可识别Scrapy，进而返回的页面与实际浏览器访问的不符）

# setting文件中ITEM_PIPELINES配置默认关闭，放开才能使用pipelines