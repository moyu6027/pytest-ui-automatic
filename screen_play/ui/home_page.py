from screenpy import Target
from selenium.webdriver.common.by import By

# URL = "http://172.17.162.166:35041/"

URL = "/"

HOME_PAGE_MESSAGE = Target.the("home page message").located_by(
    "div.next-form-item-control > button > span"
)
