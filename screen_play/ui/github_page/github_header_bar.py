"""
Locators for elements in the GitHub header bar.
"""
from screenpy import Target

SEARCH_INPUT = Target.the("Github header's search input").located_by(
    "input.header-search-input"
)