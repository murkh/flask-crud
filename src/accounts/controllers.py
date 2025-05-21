from flask import request, jsonify
import uuid

from .. import db
from .models import Account


def list_all_accounts_controller():
    accounts = Account.query.all()
    response = []
    for account in accounts:
        response.append(account.toDict())
    return jsonify(response)


def create_account_controller():
    form = request.form.to_dict()

    id = str(uuid.uuid4())
    new_account = Account(
        id=id,
        email=form['email'],
        username=form['username'],
        dob=form['dob'],
        country=form['country'],
        phone_number=form['phone_number'],
    )
    db.session.add(new_account)
    db.session.commit()

    response = Account.query.get(id).toDict()
    return jsonify(response)


def retrieve_account_controller(account_id):
    response = Account.query.get(account_id).toDict()
    return jsonify(response)


def update_account_contoller(account_id):
    form = request.form.to_dict()
    account = Account.query.get(account_id)

    account.email = form['email']
    account.username = form['username']
    account.dob = form['dob']
    account.country = form['country']
    account.phone_number = form['phone_number']
    db.session.commit()

    response = Account.query.get(account_id).toDict()
    return jsonify(response)


def delete_account_controller(account_id):
    Account.query.filter_by(id=account_id).delete()
    db.session.commit()

    return ('Account with Id "{}" deleted successfully'.format(account_id))
