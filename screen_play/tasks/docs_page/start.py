from screenpy import AnActor
from screenpy.actions import Open

from screen_play.ui.docs_page import docs_page


class Start:
    """
    A very simple task that starts on the ScreenPy docs homepage.
    """

    @staticmethod
    def on_the_docs_page() -> "Start":
        """Sets the URL to be the homepage."""
        return Start(docs_page.URL)

    def perform_as(self, the_actor: AnActor) -> None:
        """
        Asks the Actor to visit the specified URL in their browser.

        Args:
            the_actor: the Actor who will perform this task.

        Raises:
            UnableToPerformException: if the Actor does not possess the
                Ability to BrowseTheWeb.
        """
        the_actor.attempts_to(Open.their_browser_on(self.location))

    def __init__(self, location: str) -> None:
        self.location = location
