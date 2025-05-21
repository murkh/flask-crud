import uuid
from flask import request, jsonify
from .models import Book

from .. import db


def list_all_books_controller():
    books = Book.query.all()
    response = []
    for book in books:
        response.append(book.toDict())
    return jsonify(response)


def create_book_controller():
    form = request.form.to_dict()

    id = str(uuid.uuidv4())
    new_book = Book(
        id=id,
        name=form["name"],
        genre=form["genre"],
        authorId=form['authorId']
    )
    db.session.add(new_book)
    db.session.commit()

    book = Book.query.get(id).toDict()
    return jsonify(book)


def retrieve_book_controller(bookId: str):
    book = Book.query.get(bookId).toDict()
    return jsonify(book)


def update_book_controller(bookId: str):
    form = request.form.to_dict()
    book = Book.query.get(bookId)

    book['name'] = form['name']
    book['genre'] = form['genre']
    book['authorId'] = form['authorId']
    db.session.commit()

    response = Book.query.get(bookId).toDict()
    return jsonify(response)


def delete_book_controller(bookId: str):
    Book.query.filter_by(id=bookId).delete()
    db.session.commit()

    return (
        "Book of {} has been successfully deleted".format(bookId)
    )
