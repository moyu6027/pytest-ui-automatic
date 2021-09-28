"""
Locators and the URL for ScreenPy's Abilities docs page.
"""

from screenpy import Target

URL = "https://screenpy-docs.readthedocs.io/en/latest/topics/abilities.html"

UP_NEXT_LINK = Target.the('Abilities "Up Next" link').located_by(
    "#up-next a.reference"
)

