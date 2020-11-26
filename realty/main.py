
from scrapy.cmdline import execute
import sys
import os
# 获取当前脚本路径
# dirpath = 'H:\python-练习\items\realty\realty_spider\realty_spider\spiders'

# 添加环境变量
# sys.path.append(dirpath)
# 启动爬虫,第三个参数为爬虫name
execute(['scrapy','crawl','fangxing_xiaoqu'])
# execute(['scrapy','crawl','fangxing'])
# execute(['scrapy','crawl','fangxing_rent'])
# execute(['scrapy','crawl','zhuge_xiaoqu'])
# execute(['scrapy','crawl','fangxing_school'])

