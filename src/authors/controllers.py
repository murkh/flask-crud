from flask import request, jsonify
import uuid

from .. import db
from .models import Author


def list_all_authors_controller():
    authors = Author.query.all()
    response = []
    for author in authors:
        response.append(author.toDict())

    return jsonify(response)


def create_author_controller():
    form = request.form.to_dict()

    id = str(uuid.uuid4())
    new_author = Author(
        id=id,
        name=form['name'],
        country=form['country'],
    )
    db.session.add(new_author)
    db.session.commit()

    response = Author.query.get(id).toDict()
    return jsonify(response)


def retrieve_author_controller(author_id):
    response = Author.query.get(author_id).toDict()
    return jsonify(response)


def update_author_contoller(author_id):
    form = request.form.to_dict()
    author = Author.query.get(author_id)

    author.name = form['name']
    author.country = form['country']
    db.session.commit()

    response = author.query.get(author_id).toDict()
    return jsonify(response)


def delete_author_controller(author_id):
    Author.query.filter_by(id=author_id).delete()
    db.session.commit()

    return ('Author with Id "{}" deleted successfully'.format(author_id))
