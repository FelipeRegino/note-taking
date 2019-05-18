from flask import Blueprint, render_template, request, redirect, jsonify
from app.database import DB_SESSION
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
    if r['date']:
        date = datetime.datetime.strptime(r['date'], '%Y-%m-%d')
    else:
        date = None
    note = Note(r['title'], r['content'], date, r['status'])
    DB_SESSION.add(note)
    DB_SESSION.commit()
    return jsonify({'status': 200, 'message': 'Nota criada com sucesso!'})


@MOD_NOTE.route('/update/note/<int:id>', methods=['PUT'])
def update(id):
    r = request.get_json()
    if r['date']:
        date = datetime.datetime.strptime(r['date'], '%Y-%m-%d')
    else:
        date = None
    note = Note.query.filter(Note.id == id).first()
    note.title = r['title'] if r['title'] else note.title
    note.content = r['content'] if r['content'] else note.content
    note.date = date if date else note.date
    note.status = r['status'] if r['status'] else note.status
    DB_SESSION.commit()
    return jsonify({'status': 200, 'message': 'Nota atualizada com sucesso!'})


@MOD_NOTE.route('/delete/note/<int:id>', methods=['DELETE'])
def delete(id):
    Note.query.filter(Note.id == id).delete()
    DB_SESSION.commit()
    return jsonify({'status': 200, 'message': 'Nota deletada com sucesso!'})
