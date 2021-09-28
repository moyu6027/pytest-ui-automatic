"""
Locators and the URL for ScreenPy's Targets docs page.
"""

from screenpy import Target

URL = "https://screenpy-docs.readthedocs.io/en/latest/topics/targets.html"

UP_NEXT_LINK = Target.the('Targets "Up Next" link').located_by(
    "#up-next a.reference"
)

