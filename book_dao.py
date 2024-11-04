import sqlite3
from book import Book


class BookDao:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""DROP TABLE IF EXISTS books""")
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS books (
                book_id INTEGER PRIMARY KEY,
                title TEXT,
                author TEXT,
                genre TEXT,
                status TEXT
            )"""
        )
        self.conn.commit()

    def add_book(self, book):
        self.cursor.execute(
            "INSERT INTO books (title, author, genre, status) VALUES (?, ?, ?, ?)",
            (book.title, book.author, book.genre, book.status)
        )
        self.conn.commit()

    def get_book(self, book_id):
        self.cursor.execute("SELECT * FROM books WHERE book_id = ?", (book_id,))
        row = self.cursor.fetchone()
        return Book(*row) if row else None

    def get_all_books(self):
        self.cursor.execute("SELECT * FROM books")
        rows = self.cursor.fetchall()
        return [Book(*row) for row in rows]

    def update_book(self, book):
        self.cursor.execute(
            "UPDATE books SET title = ?, author = ?, genre = ?, status = ? WHERE book_id = ?",
            (book.title, book.author, book.genre, book.status, book.book_id)
        )
        self.conn.commit()
        return self.cursor.rowcount > 0

    def delete_book(self, book_id):
        self.cursor.execute("DELETE FROM books WHERE book_id = ?", (book_id,))
        self.conn.commit()
        return self.cursor.rowcount > 0

    def close(self):
        self.conn.close()
