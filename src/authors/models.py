from sqlalchemy import inspect
from datetime import datetime
from sqlalchemy.orm import validates

from .. import db


class Author(db.Model):
    id = db.Column(db.String(50), primary_key=True,
                   nullable=False, unique=True)
    created = db.Column(db.DateTime(timezone=True), default=datetime.now())
    updated = db.Column(db.DateTime(timezone=True), onupdate=datetime.now())

    name = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(100), nullable=False)

    books = db.relationship("Book", back_populates='author')

    @validates('name')
    def empty_string_to_null(self, key, value):
        if isinstance(value, str) and value == "":
            return None
        else:
            return value

    def toDict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}
