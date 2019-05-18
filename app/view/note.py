from flask import Blueprint, render_template, request
from ..models import Note

MOD_NOTE = Blueprint('portal', __name__)


@MOD_NOTE.route('/')
def index():
    notes = Note.query.all()
    return render_template('index.html', notes=notes)
