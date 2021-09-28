import os


class Constant:
    # 工作空间根目录
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

    # page_objects
    PAGE_OBJECTS_DIR = os.path.join(BASE_DIR, "page_objects")

    # config
    CONFIG_DIR = os.path.join(BASE_DIR, "config")

    # resource
    RESOURCE_DIR = os.path.join(BASE_DIR, "resource")

    # testcases
    CASES_DIR = os.path.join(BASE_DIR, "tests")

    # features
    FEATURE_DIR = os.path.join(CASES_DIR, "features")

    # utils
    UTILS_DIR = os.path.join(BASE_DIR, "utils")

    # allure-report
    REPORT_DIR = os.path.join(BASE_DIR, "allure-report")