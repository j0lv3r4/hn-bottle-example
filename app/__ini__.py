from datetime import datetime
from bottle import get, post, request, template, redirect, run
import dataset

db = dataset.connect('sqlite:///database.sqlite')
entries_table = db['entries']


@get('/')
def show_entries():
    entries = entries_table.all()
    entries_sorted = sorted(entries, reverse=True)
    return template('./app/entries', entries=entries_sorted)


@post('/add')
def add_entry():
    entry = request.forms.get('entry')
    entries_table.insert(dict(
        text=entry,
        created_by=datetime.utcnow(),
    ))
    return redirect('/')


run(reloader=True, debug=True)
