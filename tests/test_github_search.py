"""
An example of a test module that follows the typical pytest test
structure. These tests show off how to use custom tasks and Questions,
though they are a little bit contrived.
"""

from screenpy import Actor, given, then, when
from screenpy.actions import Open, See
from screenpy.pacing import act, scene
from screenpy.resolutions import (
    ContainsTheText,
    ContainTheText,
    DoesNot,
    IsEqualTo,
    ReadsExactly,
)

from screen_play.questions.number_of_search_results import NumberOfSearchResults
from screen_play.questions.search_results_message import SearchResultsMessage
from screen_play.tasks.github_page.search_github import SearchGitHub
from screen_play.ui.github_page.github_home_page import URL


@act("Search")
@scene("Search for the ScreenPy repository on GitHub")
def test_search_for_screenpy(Sean: Actor) -> None:
    """GitHub search finds the screenpy repository."""
    given(Sean).was_able_to(Open.their_browser_on(URL))
    when(Sean).attempts_to(SearchGitHub.for_text("perrygoy/screenpy"))
    then(Sean).should(
        See.the(SearchResultsMessage(), DoesNot(ContainTheText("couldn’t"))),
        See.the(SearchResultsMessage(), ReadsExactly("1 repository result")),
        See.the(NumberOfSearchResults(), IsEqualTo(1)),
    )


@act("Search")
@scene("Search for a nonexistant repository on GitHub")
def test_search_for_nonexistent_repo(Sean: Actor) -> None:
    """GitHub search fails to find a nonexistant repository."""
    non_existant_repository = "perrygoy/i-never-made-this-repo"

    given(Sean).was_able_to(Open.their_browser_on(URL))
    when(Sean).attempts_to(SearchGitHub.for_text(non_existant_repository))
    then(Sean).should(
        See.the(SearchResultsMessage(), ContainsTheText("We couldn’t find any")),
        See.the(SearchResultsMessage(), ContainsTheText(non_existant_repository)),
        See.the(NumberOfSearchResults(), IsEqualTo(0)),
    )
