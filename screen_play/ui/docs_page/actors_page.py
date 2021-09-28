"""
Locators and the URL for ScreenPy's Actors docs page.
"""

from screenpy import Target

URL = "https://screenpy-docs.readthedocs.io/en/latest/topics/actors.html"

UP_NEXT_LINK = Target.the('Actors "Up Next" link').located_by(
    "#up-next a.reference"
)

