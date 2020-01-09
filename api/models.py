# 注意从__init__导入db
from api import db


class Publisher(db.Model):
    __tablename__ = "publisher"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)


class Book(db.Model):
    __tablename__ = 'book'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(32), index=True, nullable=False)
    publisher_id = db.Column(db.Integer, db.ForeignKey("publisher.id", ondelete='CASCADE'))

    # 仅用于查询,不会生成表格,返回api数据时,字段需要与该字段一致
    publisher = db.relationship("Publisher", backref="publisher_of_book", cascade='all, delete')

    authors = db.relationship("Author", secondary="booktoauthor", backref="books", cascade='all, delete',
                              passive_deletes=True)


class Author(db.Model):
    __tablename__ = "author"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)


class BookToAuthor(db.Model):
    __tablename__ = "booktoauthor"

    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey("book.id"))
    author_id = db.Column(db.Integer, db.ForeignKey("author.id"))

    __table_args__ = (
        db.UniqueConstraint("book_id", "author_id", name="uni_book_author"),
    )
