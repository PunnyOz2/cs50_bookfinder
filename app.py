from flask import Flask, render_template, session, redirect, url_for, request
from models import *
import os

app = Flask(__name__)
app.secret_key = 'HiTherePun'
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ['DATABASE_URL']
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search")
def search():
    q = request.args.get('q')
    q2 = q.upper()
    q2 = "%{}%".format(q2)
    books = Book.query.filter(Book.title.ilike(q2)).all()
    authors = Author.query.filter(Author.name.ilike(q2)).all()
    return render_template("search.html",q=q,books=books)

@app.route("/books/<int:id>")
def books(id):
    book = Book.query.get(id)
    author = Author.query.get(book.author_id)
    return render_template("books.html",book=book,author=author)

@app.route("/authors/<int:id>")
def authors(id):
    author = Author.query.get(id)
    # author.books

    books = Book.query.filter(Book.author_id==author.id).all()
    return render_template("authors.html",author=author,books=books)