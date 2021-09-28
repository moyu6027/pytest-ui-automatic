"""
Fixtures for UI & API testing.
"""
from typing import Generator

import allure
import pytest
from screenpy import AnActor
from screenpy.abilities import BrowseTheWeb, MakeAPIRequests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as Co


@pytest.fixture
def Sean(headed) -> Generator:
    """An Actor who can make Web UI test."""
    options = webdriver.ChromeOptions()
    if not headed:
        options.headless = True
    # ... other setup, maybe
    driver = webdriver.Chrome(options=options)

    the_actor = AnActor.named("Sean").who_can(BrowseTheWeb.using(driver))
    yield the_actor
    the_actor.exit_stage_left()


@pytest.fixture
def Nan() -> Generator:
    """An Actor who can make API requests."""
    the_actor = AnActor.named("Nan").who_can(MakeAPIRequests())
    yield the_actor
    the_actor.exit_stage_left()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    # 获取钩子方法的调用结果
    outcome = yield
    # 从调用结果中获取测试结果
    test_result = outcome.get_result()

    chrome_options = Co()
    # chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)

    if test_result.when in ["setup", "call"]:
        xfail = hasattr(test_result, 'wasxfail')
        if test_result.failed or (test_result.skipped and xfail):
            allure.attach(driver.get_screenshot_as_png(), name='screenshot', attachment_type=allure.attachment_type.PNG)
