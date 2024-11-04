from flask import Blueprint, jsonify, request
from book_dao import BookDao
from book import Book

book_blueprint = Blueprint("book_blueprint", __name__)
book_dao = BookDao("books_example.db")


@book_blueprint.route("/books", methods=["POST"])
def add_book():
    data = request.get_json()
    new_book = Book(None, data["title"], data["author"], data["genre"], data["status"])
    book_dao.add_book(new_book)
    return jsonify({"message": "Book added"}), 201


@book_blueprint.route("/books", methods=["GET"])
def get_all_books():
    books = book_dao.get_all_books()
    return jsonify([book.to_dict() for book in books]), 200


@book_blueprint.route("/books/<int:book_id>", methods=["GET"])
def get_book(book_id):
    book = book_dao.get_book(book_id)
    if book:
        return jsonify(book.to_dict()), 200
    else:
        return jsonify({"message": "Book not found"}), 404


@book_blueprint.route("/books/<int:book_id>", methods=["PUT"])
def update_book(book_id):
    data = request.get_json()
    updated_book = Book(book_id, data["title"], data["author"], data["genre"], data["status"])
    if book_dao.update_book(updated_book):
        return jsonify({"message": "Book updated"}), 200
    else:
        return jsonify({"message": "Book not found or not updated"}), 404


@book_blueprint.route("/books/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    deleted = book_dao.delete_book(book_id)
    if deleted:
        return jsonify({"message": "Book deleted"}), 200
    else:
        return jsonify({"message": "Book not found or not deleted"}), 404
