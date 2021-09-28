"""
Locators and the URL for ScreenPy's Questions docs page.
"""

from screenpy import Target

URL = "https://screenpy-docs.readthedocs.io/en/latest/topics/questions.html"

UP_NEXT_LINK = Target.the('Questions "Up Next" link').located_by(
    "#up-next a.reference"
)

