# encoding: utf-8
"""
项目自定义钩子文件
"""
from pathlib import Path
from typing import Generator
from py.xml import html
import json

import allure
import pytest
from playwright.sync_api import sync_playwright, Browser
from slugify import slugify

from utils.constant import *

'''
@author: sean
@file: conftest.py
@time: 2021/9/13
@desc:
'''


@pytest.fixture(scope='session')
def page_auto(request):
    env_config = request.config.getoption('environment')
    base_url = request.config.getoption('base_url')
    with sync_playwright() as play:
        if os.getenv('DOCKER_RUN') or env_config == 'PIPELINE':
            browser = play.chromium.launch(headless=True, args=['--no-sandbox'])
        else:
            browser = play.chromium.launch(headless=False)
        # create a new incognito browser context.
        context = browser.new_context(base_url=base_url)
        # create a new page in a pristine context.
        page = context.new_page()
        global PAGE
        PAGE = page
        yield page
        browser.close()


PAGE = None


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin('html')

    # 获取钩子方法的调用结果
    outcome = yield
    # 从调用结果中获取测试结果
    test_result = outcome.get_result()
    test_result.extra = []

    # If the marker match one of the testing types, then mention it in the report
    types = ["smoke", "hotlink"]
    for type in types:
        marker_priority = item.get_closest_marker(type)
        if marker_priority:
            item.config._metadata["Test Type"] = marker_priority.name

            print(marker_priority)

    # 获取测试方法的参数
    if "page" not in item.funcargs:
        return "page not in item.funcargs"
    page = item.funcargs["page"]

    if test_result.when in ["setup", "call"]:
        xfail = hasattr(test_result, 'wasxfail')
        if test_result.failed or (test_result.skipped and xfail):
            allure.attach(page.screenshot(), name='screenshot', attachment_type=allure.attachment_type.PNG)
            allure.attach(page.content(), name='html_source', attachment_type=allure.attachment_type.HTML)
            if item.config.option.htmlpath is not None:
                report_dir = os.path.dirname(item.config.option.htmlpath)
                screen_img = str(Path("images") / f"{slugify(item.nodeid)}.png")
                capture_screenshot(report_dir, screen_img, page)
                if screen_img:
                    html = '<div><img src="%s" alt="screenshot" style="height:360px;" ' \
                           'onclick="window.open(this.src)" align="right"/></div>' % screen_img
                    test_result.extra.append(pytest_html.extras.html(html))


def capture_screenshot(report_dir, screen_img, page):
    """
    To capture screenshot and save it to 'images' folder inside the specific html report directory.
    """
    screenshot_dir = str(Path(report_dir) / os.path.dirname(screen_img))
    screen_img = str(Path(report_dir) / screen_img)
    # print("screenshot_dir:"+screenshot_dir)
    # print("screen_img:"+screen_img)
    if not os.path.exists(screenshot_dir):
        os.makedirs(screenshot_dir)

    page.screenshot(path=screen_img)


def pytest_addoption(parser):
    """
    To get password from command line argument
    """
    parser.addoption("--password", action="store", default="test", help="password")


@pytest.fixture(scope="module")
def password(request):
    return request.config.getoption("--password")


@pytest.fixture(scope="module")
def baseUrl(request):
    return request.config.getoption("--base-url")


@pytest.fixture(scope="module")
def headed(request):
    return request.config.getoption("--headed")


@pytest.fixture()
def browser_context_args(browser_context_args):
    """
    To override the browser context
    https://playwright.dev/python/docs/api/class-browser#browser-new-context
    """
    return {
        **browser_context_args,
        # "storage_state": {
        #             "cookies": [
        #                 {
        #                     "name": "token",
        #                     "value": response["token"],
        #                     "path": path,
        #                     "domain": domain,
        #                 },
        #             ]
        #         },
        # "record_video_dir": "videos"
        # "viewport": {
        #     "width": 1920,
        #     "height": 1080,
        # },
        "accept_downloads": True
    }

# @pytest.fixture
# def context(context):
#     """
#     To override the default timeout
#     """
#     context.set_default_timeout(45 * 1000)  # default to 30 seconds
#     # context.accept_downloads(True)
#     yield context


# def pytest_addoption(parser):
#     group = parser.getgroup("playwright", "Playwright")
#     group.addoption("--env",
#                     action="store",
#                     dest="environment",
#                     default="DEBUG",
#                     help="environment: DEBUG or PIPELINE")
#
#     group.addoption("--url",
#                     action="store",
#                     dest="base_url",
#                     help="Base Url for Test")


# def pytest_html_report_title(report):
#     report.title = "Test Report"
#
#
# def pytest_html_results_summary(prefix, summary, postfix):
#     # To get the summary info from 'info.json' and display in HTML report
#     # Make sure the file is located in the project root
#     info_file = os.path.dirname(__file__) + '/info.json'
#
#     if os.path.exists(info_file):
#         with open(info_file) as f:
#             data = json.load(f)
#         f.close()
#
#         if data:
#             summary = data['summary']
#             prefix.extend([html.p(summary + "")])
