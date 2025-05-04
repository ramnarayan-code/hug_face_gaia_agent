import wikipediaapi

class WikipediaTool:
    """
    A tool for searching and retrieving Wikipedia article summaries.

    This class provides functionality to search Wikipedia articles and retrieve their summaries
    using the Wikipedia-API library.

    Attributes:
        None

    Methods:
        search(query): Searches Wikipedia for the given query and returns article summary.
    """
    def search(self, query):
        try:
            wiki = wikipediaapi.Wikipedia(language="en", user_agent="MinimalAgent/1.0")
            page = wiki.page(query)
            if not page.exists():
                return "No Wikipedia page found."
            return page.summary[:1000]
        except Exception as e:
            return f"An error occurred: {e}"