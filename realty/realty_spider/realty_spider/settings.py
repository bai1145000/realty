import sys ,os
import django
from django.core.wsgi import get_wsgi_application


DJANGO_SETTINGS_MODULE = 'realty.settings' #django 配置
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath('.'))))
sys.path.append(BASE_DIR)

# sys.path.insert(0,"H:\\python-练习\\items\\realty")
os.environ['DJANGO_SETTINGS_MODULE'] = DJANGO_SETTINGS_MODULE 

# application = get_wsgi_application()
django.setup()



BOT_NAME = 'realty_spider'

SPIDER_MODULES = ['realty_spider.realty_spider.spiders']
NEWSPIDER_MODULE = 'realty_spider.realty_spider.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'realty (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy 
# 配置由Scrapy执行的最大并发请求(default: 16)
CONCURRENT_REQUESTS = 3

# Configure a delay for requests for the same website
# 为同一网站的请求配置一个延迟 (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = True

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
  "User-Agent":" Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
  "Referer":"https://www.fangstar.com/",
  # ' Sec-Fetch-Dest': 'document' ,
  # 'Sec-Fetch-Mode':' navigate',
  # 'Sec-Fetch-Site':' same-origin',
  # 'Sec-Fetch-User': '?1',
  # 'Upgrade-Insecure-Requests':1,
}

# PROXIES =[
# ]
DOWNLOAD_DELAY = 0.5  #下载延迟

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html


# SPIDER_MIDDLEWARES = {
  # 'realty_spider.realty_spider.middlewares.RealtySpiderMiddleware': 543,
  # 'realty_spider.realty_spider.middlewares.MyMiddleware':500
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'realty.middlewares.RealtyDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'realty_spider.realty_spider.pipelines.StringPipeline':300,  #str清洗
    'realty_spider.realty_spider.pipelines.FangxingErshouPipeline': 300,
    'realty_spider.realty_spider.pipelines.FangxingXiaoquPipeline': 300,
    'realty_spider.realty_spider.pipelines.FangxingRentPipeline':300,
     'realty_spider.realty_spider.pipelines.SavePipine':300  #保存
    # 'realty_spider.realty_spider.pipelines.FangxingSchoolPipeline':300
    #  'realty_spider.realty_spider.pipelines.ZhugeXiaoquPipeline': 300
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
