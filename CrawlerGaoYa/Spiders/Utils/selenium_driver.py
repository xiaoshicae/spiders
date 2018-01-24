import logging
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.proxy import Proxy
from selenium.webdriver.common.proxy import ProxyType
# from CrawlerGaoYa.Spiders.Utils.getproxy import get_proxies
from .getproxy import get_proxies
logger = logging.getLogger('selenium')


def selenium_driver(url):
    capabilities = DesiredCapabilities.CHROME.copy()
    proxies = get_proxies()
    if proxies:
        proxies = proxies['http']
    proxy = Proxy({'proxyType': ProxyType.MANUAL, 'httpProxy': proxies})
    proxy.add_to_capabilities(capabilities)

    # driver = webdriver.PhantomJS(desired_capabilities=capabilities)
    driver = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe',
                              desired_capabilities=capabilities)
    driver.implicitly_wait(20)
    html = None
    try:
        driver.get(url)
        html = driver.page_source
    except Exception as e:
        logger.error(e)
    finally:
        driver.quit()
    return html


if __name__ == '__main__':
    html = selenium_driver('http://qy1.sfda.gov.cn/datasearch/face3/dir.html')
    print(html)
