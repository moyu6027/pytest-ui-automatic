"""
Locators and the URL for ScreenPy's Resolutions docs page.
"""

from screenpy import Target

URL = "https://screenpy-docs.readthedocs.io/en/latest/topics/resolutions.html"

UP_NEXT_SECTION = Target.the('"Up Next" section').located_by(
    "#up-next"
)

