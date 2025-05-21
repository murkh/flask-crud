from flask import request, Blueprint

accounts_bp = Blueprint('accounts', __name__)

from .controllers import list_all_accounts_controller, create_account_controller, delete_account_controller, retrieve_account_controller, update_account_contoller


@accounts_bp.route("/accounts", methods=['GET', 'POST'])
def list_create_accounts():
    if request.method == 'GET':
        return list_all_accounts_controller()
    if request.method == 'POST':
        return create_account_controller()
    else:
        return 'METHOD NOT ALLOWED'


@accounts_bp.route("/accounts/<account_id>", methods=["GET", "PUT", "DELETE"])
def retrieve_update_destroy_accounts(account_id):
    if request.method == 'GET':
        return retrieve_account_controller(account_id=account_id)
    if request.method == 'PUT':
        return update_account_contoller(account_id=account_id)
    if request.method == 'DELETE':
        return delete_account_controller(account_id=account_id)
    else:
        return 'METHOD NOT ALLOWED'
