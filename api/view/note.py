from flask import Blueprint, request, redirect, jsonify, Response
from api.database import DB_SESSION
from ..models import Note
import datetime

MOD_NOTE = Blueprint('note', __name__)


@MOD_NOTE.route('/get/notes', methods=['GET'])
def index():
    notes = Note.query
    return jsonify(notes=[i.serialize for i in notes.all()])


@MOD_NOTE.route('/get/note/<int:id>', methods=['GET'])
def get(id):
    note = Note.query.filter(Note.id == id)
    return jsonify(note=note.first().serialize)


@MOD_NOTE.route('/create/note/', methods=['POST'])
def create():
    r = request.get_json()

    # VALIDAÇÃO
    if 'date' in r:
        date = datetime.datetime.strptime(r['date'], '%Y-%m-%d')
    else:
        date = None

    if 'title' not in r:
        return Response('Bad Request: title é obrigatório', status=400)
    if 'content' not in r:
        return Response('Bad Request: content é obrigatório', status=400)
    if 'status' not in r:
        return Response('Bad Request: status é obrigatório', status=400)

    note = Note(r['title'], r['content'], date, r['status'])
    DB_SESSION.add(note)
    DB_SESSION.commit()

    return Response('Nota criada com sucesso!', status=200)


@MOD_NOTE.route('/update/note/<int:id>', methods=['PUT'])
def update(id):
    r = request.get_json()
    if 'date' in r:
        date = datetime.datetime.strptime(r['date'], '%Y-%m-%d')
    else:
        date = None
    note = Note.query.filter(Note.id == id).first()
    note.title = r['title'] if 'title' in r else note.title
    note.content = r['content'] if 'content' in r else note.content
    note.date = date if date else note.date
    note.status = r['status'] if 'status' in r else note.status
    DB_SESSION.commit()
    return jsonify({'status': 200, 'message': 'Nota atualizada com sucesso!'})


@MOD_NOTE.route('/delete/note/<int:id>', methods=['DELETE'])
def delete(id):
    Note.query.filter(Note.id == id).delete()
    DB_SESSION.commit()
    return jsonify({'status': 200, 'message': 'Nota deletada com sucesso!'})
