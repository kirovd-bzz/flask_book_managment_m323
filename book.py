class Book:
    def __init__(self, book_id, title, author, genre, status):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.genre = genre
        self.status = status

    def to_dict(self):
        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "genre": self.genre,
            "status": self.status
        }
