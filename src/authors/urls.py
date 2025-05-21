from flask import request, Blueprint

authors_bp = Blueprint('authors', __name__)

from .controllers import create_author_controller, delete_author_controller, retrieve_author_controller, update_author_contoller, list_all_authors_controller


@authors_bp.route("/authors", methods=['GET', 'POST'])
def list_create_authors():
    if request.method == 'GET':
        return list_all_authors_controller()
    if request.method == 'POST':
        return create_author_controller()
    else:
        return 'METHOD NOT ALLOWED'


@authors_bp.route("/authors/<author_id>", methods=["GET", "PUT", "DELETE"])
def retrieve_update_destroy_authors(author_id):
    if request.method == 'GET':
        return retrieve_author_controller(author_id=author_id)
    if request.method == 'PUT':
        return update_author_contoller(author_id=author_id)
    if request.method == 'DELETE':
        return delete_author_controller(author_id=author_id)
    else:
        return 'METHOD NOT ALLOWED'
