import wikipediaapi

class WikipediaTool:
     def search(self, query):
        try:
            wiki = wikipediaapi.Wikipedia(language="en", user_agent="MinimalAgent/1.0")
            page = wiki.page(query)
            if not page.exists():
                return "No Wikipedia page found."
            return page.summary[:1000]
        except Exception as e:
            return f"An error occurred: {e}"