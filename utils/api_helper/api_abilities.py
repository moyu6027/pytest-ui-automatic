import allure
import httpx
import json as complexjson

import simplejson
from httpx import Response, HTTPError

from utils import Log


class ApiAbilities(object):
    def __init__(self):
        self.log = Log.LogInfo()

    def requests(self, host, url, method, data=None, json=None, **kwargs):
        url = host + url
        headers = dict(**kwargs).get("headers")
        params = dict(**kwargs).get("params")
        files = dict(**kwargs).get("files")
        cookies = dict(**kwargs).get("cookies")
        self.request_log(url, method, data, json, params, headers, files, cookies)
        try:
            response = httpx.request(method, url, data=data, json=json, **kwargs)
        except httpx.RequestError as e:
            self.log.error(e)
            raise
        except Exception as e:
            self.log.error(e)
            raise

        time_consuming = response.elapsed.microseconds / 1000
        time_total = response.elapsed.total_seconds()
        response_dicts = dict()
        response_dicts['code'] = response.status_code
        try:
            if response.status_code != 200:
                response_dicts['body'] = response.text
            else:
                response_dicts['body'] = response.json()
        except json.decoder.JSONDecodeError:
            response_dicts['body'] = ''
        except simplejson.errors.JSONDecodeError:
            response_dicts['body'] = ''
        except Exception as e:
            self.log.error(e)
            raise
        response_dicts['text'] = response.text
        response_dicts['time_consuming'] = time_consuming
        response_dicts['time_total'] = time_total

        self.log.info('返回结果：%s' % response_dicts)
        with allure.step(method + "请求接口"):
            allure.attach(name="请求接口", body=str(url))
            allure.attach(name="请求方式", body=str(method))
            allure.attach(name="请求header", body=str(headers))
            allure.attach(name="请求Data参数", body=str(data))
            allure.attach(name="请求Json参数", body=str(json))
            allure.attach(name="请求参数", body=str(params))
            allure.attach(name="返回状态码", body=str(response.status_code))
            allure.attach(name="返回内容", body=response.content)
        return response_dicts

    def request_log(self, url, method, data=None, json=None, params=None, headers=None, files=None, cookies=None,
                    **kwargs):
        self.log.info("接口请求地址 ==>> {}".format(url))
        self.log.info("接口请求方式 ==>> {}".format(method))
        # Python3中，json在做dumps操作时，会将中文转换成unicode编码，因此设置 ensure_ascii=False
        self.log.info("接口请求头 ==>> {}".format(complexjson.dumps(headers, indent=4, ensure_ascii=False)))
        self.log.info("接口请求 params 参数 ==>> {}".format(complexjson.dumps(params, indent=4, ensure_ascii=False)))
        self.log.info("接口请求体 data 参数 ==>> {}".format(complexjson.dumps(data, indent=4, ensure_ascii=False)))
        self.log.info("接口请求体 json 参数 ==>> {}".format(complexjson.dumps(json, indent=4, ensure_ascii=False)))
        self.log.info("接口上传附件 files 参数 ==>> {}".format(files))
        self.log.info("接口 cookies 参数 ==>> {}".format(complexjson.dumps(cookies, indent=4, ensure_ascii=False)))
