class QuoteModel:
    """Class describing quote with a body and an author."""

    def __init__(self, body, author):
        self.body = body
        self.author = author

    def __repr__(self):
        """Represent a quote as a body with an author"""
        return f"{self.body}-{self.author}"
