from screenpy import given, when, then, Actor
from screenpy.actions import Click, See, Wait
from screenpy.questions import Text
from screenpy.resolutions import ContainsTheText

from screen_play.tasks.docs_page.start import Start
from screen_play.ui import (
    docs_page,
)
from screen_play.ui.docs_page import docs_page, resolutions_page, questions_page, actors_page, actions_page, abilities_page, targets_page


def test_open_docspage_pytest(Sean: Actor) -> None:
    """A simple example to show a test using pytest fixtures"""
    given(Sean).was_able_to(Start.on_the_docs_page())

    then(Sean).should(
        See.the(Text.of_the(docs_page.WELCOME_MESSAGE), ContainsTheText("ScreenPy"))
    )


def test_take_guided_tour_pytest(Sean: Actor) -> None:
    """A more involved example using pytest fixtures."""
    given(Sean).was_able_to(Start.on_the_docs_page())

    when(Sean).attempts_to(
        Click.on_the(docs_page.GUIDED_TOUR_LINK),
        Wait.for_the(actors_page.UP_NEXT_LINK).to_appear(),
        Click.on_the(actors_page.UP_NEXT_LINK),
        Wait.for_the(abilities_page.UP_NEXT_LINK).to_appear(),
        Click.on_the(abilities_page.UP_NEXT_LINK),
        Wait.for_the(targets_page.UP_NEXT_LINK).to_appear(),
        Click.on_the(targets_page.UP_NEXT_LINK),
        Wait.for_the(actions_page.UP_NEXT_LINK).to_appear(),
        Click.on_the(actions_page.UP_NEXT_LINK),
        Wait.for_the(questions_page.UP_NEXT_LINK).to_appear(),
        Click.on_the(questions_page.UP_NEXT_LINK),
        Wait.for_the(resolutions_page.UP_NEXT_SECTION).to_appear(),
    )

    then(Sean).should(
        See.the(
            Text.of_the(resolutions_page.UP_NEXT_SECTION),
            ContainsTheText("concludes here!"),
        ),
        See.the(
            Text.of_the(resolutions_page.UP_NEXT_SECTION),
            ContainsTheText("Thanks for using ScreenPy!"),
        ),
    )
