# paython内部库
import requests
# bs4第三方库
from bs4 import BeautifulSoup as bs
# 爬取数据存储
import pandas as pd

# 设置头信息-浏览器标识（同页面请求头信息）
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362'
cookie = '_csrf=bb84b6e06c672e9a96b16f619af9981aa25471a609c8200846433ca1739612e7; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593096809; uuid_n_v=v1; mojo-uuid=bbda844899f4211edae49a573bf7a3bd; uuid=A22CE1E0B6F311EA95E3C92BBC8FF019E60AAE97EF3749A1B9860BAFB724C58B; _lxsdk_cuid=172ebf82ff518-0473b3f1c322c9-71415a3b-144000-172ebf82ff7c8; __mta=210538794.1593096810689.1593096810689.1593096810689.1; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593096809; mojo-session-id={"id":"6916baafbec620c980d08a47174860ec","time":1593096810893}; mojo-trace-id=2; _lxsdk=A22CE1E0B6F311EA95E3C92BBC8FF019E60AAE97EF3749A1B9860BAFB724C58B; _lxsdk_s=172ebf82ffc-b88-ec3-bf1%7C%7C3'

# 设置头信息
header = {'User-Agent': user_agent, 'Cookie': cookie}

# 设置爬取的url地址
targetUrl = 'https://maoyan.com/films?showType=3'

# 模拟浏览器，发送请求，并返回响应结果（结果为html页面代码）
response = requests.get(targetUrl, headers = header)

# 使用bs4的html.parser方法解析响应结果
bs_res = bs(response.text, 'html.parser')

# 存放爬取数据集合
movieList = []

# 爬取目标前10部电影
tagMovieInfoIndex = 0
for curMovie in bs_res.find_all('div', attrs={'class': 'movie-hover-info'}):
    # 爬取超过10部，退出
    if tagMovieInfoIndex == 10 :
        break
    tagMovieInfoIndex = tagMovieInfoIndex + 1
    tagMovieTitleIndex = -1
    for movieInfo in curMovie.find_all('div', attrs={'class': 'movie-hover-title'}):
        tagMovieTitleIndex = tagMovieTitleIndex + 1
        # print(movieInfo)
        if tagMovieTitleIndex == 0 :
            # 电影名称
            print(movieInfo.find_all('span',)[0].text)
            movieList.append(movieInfo.find_all('span',)[0].text)
            continue
        if tagMovieTitleIndex == 1 :
            # 电影类型
            print(movieInfo.contents[2].strip())
            movieList.append(movieInfo.contents[2].strip())
            continue
        if tagMovieTitleIndex == 3 :
            # 上映时间
            print(movieInfo.contents[2].strip())
            movieList.append(movieInfo.contents[2].strip())
            break
movieTop10 = pd.DataFrame(data = movieList)

# 写入csv文件
movieTop10.to_csv('./movieTop10.csv', encoding='GBK', index=False, header=False)



