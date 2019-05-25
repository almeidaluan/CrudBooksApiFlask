from flask import Blueprint, current_app, request, jsonify
from .serializer import BookSchema
from .model import Book
bp_books = Blueprint('books', __name__)


@bp_books.route('/mostrar', methods=['GET'])
def mostrar():
    bs = BookSchema(many=True)
    result = Book.query.all()
    return bs.jsonify(result)


@bp_books.route('/deletar/<identificador>', methods=['GET'])
def deletar(identificador):

    Book.query.filter(Book.id == identificador).delete()
    current_app.db.session.commit()
    return jsonify("Deletado com Sucesso"), 204


@bp_books.route('/modificar', methods=['POST'])
def modificar():
    pass


@bp_books.route('/cadastrar', methods=['POST'])
def cadastrar():

    bs = BookSchema()
    book, error = bs.load(request.json)

    if error:
        return jsonify(error), 401
    current_app.db.session.add(book)
    current_app.db.session.commit()
    import ipdb
    ipdb.set_trace()
    return bs.jsonify(book), 201
