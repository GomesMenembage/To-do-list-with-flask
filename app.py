from flask import Flask, render_template, redirect, url_for, request
from models import db, Note, Category
from forms import NoteForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notes.db'
app.config['SECRET_KEY'] = 'chave-secreta'
db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/')
def index():
    keyword = request.args.get('keyword')
    if keyword:
        notes = Note.query.filter(Note.title.contains(keyword) | Note.content.contains(keyword)).all()
    else:
        notes = Note.query.all()
    return render_template('index.html', notes=notes)

@app.route('/add', methods=['GET', 'POST'])
def add_note():
    form = NoteForm()
    form.category.choices = [(c.id, c.name) for c in Category.query.all()]
    if form.validate_on_submit():
        new_note = Note(
            title=form.title.data,
            content=form.content.data,
            category_id=form.category.data
        )
        db.session.add(new_note)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('addnotas.html', form=form)

@app.route('/categories')
def manage_categories():
    categories = Category.query.all()
    return render_template('categorias.html', categories=categories)