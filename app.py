from flask import Flask, jsonify, request
from book_blueprint import book_blueprint

app = Flask(__name__)
app.secret_key = "supersecretkey"
app.register_blueprint(book_blueprint)


@app.route("/", methods=["GET"])
def api_menu():
    menu = {
        "message": "Welcome to the Book Management API!",
        "endpoints": {
            "GET /books": "Retrieve a list of all books",
            "POST /books": "Add a new book (requires title, author, genre, and status in JSON)",
            "GET /books/<book_id>": "Retrieve details of a specific book by its ID",
            "PUT /books/<book_id>": "Update an existing book by its ID (requires title, author, genre, and status in JSON)",
            "DELETE /books/<book_id>": "Delete a book by its ID",
            "GET /books/available": "Retrieve a list of all available books"
        }
    }
    return jsonify(menu), 200


if __name__ == "__main__":
    app.run(debug=True)
