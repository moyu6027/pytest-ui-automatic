"""
Locators and the URL for ScreenPy's ReadTheDocs homepage.
"""

from screenpy import Target

URL = "https://screenpy-docs.readthedocs.io/en/latest/"

WELCOME_MESSAGE = Target.the("welcome message").located_by(
    "#welcome-to-screenpy-s-documentation>h1"
)
GUIDED_TOUR_LINK = Target.the('homepage "Guided Tour" link').located_by(
    '#guided-tour a[href*="actors.html"]'
)

