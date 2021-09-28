from screenpy import Actor, given, then, when
from screenpy.actions import Open, See, Wait
from screenpy.pacing import act, scene
from screenpy.questions import Text
from screenpy.resolutions import ContainsTheText

from screen_play.ui import home_page


@act("Login")
@scene("Open NewMonitor Login Page")
def test_login_home_page(Sean: Actor) -> None:

    given(Sean).was_able_to(Open.their_browser_on(home_page.URL))

    when(Sean).attempts_to(
        Wait.for_the(home_page.HOME_PAGE_MESSAGE).to_appear(),
    )

    then(Sean).should(
        See.the(Text.of_the(home_page.HOME_PAGE_MESSAGE), ContainsTheText("登录"))
    )


