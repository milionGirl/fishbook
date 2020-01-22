#urllib
#requests
import requests


class HTTP:
    # scrapy并发多线程爬虫, requests + beautiful soap
    @staticmethod
    def get(url, return_json = True):
        #r对象中包括http headers,大部分接口都是restful,
        r = requests.get(url)
        if r.status_code !=200:
            return {} if return_json else ''
        return r.json() if return_json else r.text
        '''
        if return_json:
            return r.json()
        else:
            return r.text
        '''