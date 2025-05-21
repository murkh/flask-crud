from datetime import datetime
from sqlalchemy import inspect
from sqlalchemy.orm import validates

from .. import db


class Book(db.Model):
    id = db.Column(db.String(50), primary_key=True,
                   nullable=False, unique=True)
    created = db.Column(db.DateTime(timezone=True), default=datetime.now())
    updated = db.Column(db.DateTime(timezone=True), onupdate=datetime.now())

    name = db.Column(db.String(200), unique=True, nullable=False)
    genre = db.Column(db.String(20), nullable=False)

    authorId = db.Column(db.String(100), db.ForeignKey("author.id"))
    author = db.relationship("Author", back_populates="books")

    @validates('name')
    def empty_string_to_null(self, key: str, value: str):
        if isinstance(value, str) and value == '':
            return None
        else:
            return value

    def toDict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}
