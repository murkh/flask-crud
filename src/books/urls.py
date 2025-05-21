from flask import request, Blueprint

books_bp = Blueprint('books', __name__)

from .controllers import create_book_controller, delete_book_controller, list_all_books_controller, retrieve_book_controller, update_book_controller


@books_bp.route("/books", methods=["GET", "POST"])
def list_create_books():
    if request.method == 'GET':
        return list_all_books_controller()
    if request.method == 'POST':
        return create_book_controller()
    else:
        return 'METHOD NOT ALLOWED'


@books_bp.route("/books/<book_id>", methods=["GET", "PUT", "DELETE"])
def retrieve_update_destroy_books(book_id):
    if request.method == 'GET':
        return retrieve_book_controller(book_id=book_id)
    if request.method == 'PUT':
        return update_book_controller(book_id=book_id)
    if request.method == 'DELETE':
        return delete_book_controller(book_id=book_id)
    else:
        return 'METHOD NOT ALLOWED'
