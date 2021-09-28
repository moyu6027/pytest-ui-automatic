"""
Locators and the URL for ScreenPy's Actions docs page.
"""

from screenpy import Target

URL = "https://screenpy-docs.readthedocs.io/en/latest/topics/actions.html"

UP_NEXT_LINK = Target.the('Actions "Up Next" link').located_by(
    "#up-next a.reference"
)

