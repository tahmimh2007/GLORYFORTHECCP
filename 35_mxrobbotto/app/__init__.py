from flask import Flask, render_template, redirect, url_for, request, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(150), nullable=False)

class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    blog_id = db.Column(db.Integer, db.ForeignKey('blog.id'), nullable=False)
    title = db.Column(db.String(150), nullable=False)
    content = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = generate_password_hash(request.form['password'], method='sha256')
        new_user = User(username=username, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('login'))

@app.route('/dashboard')
def dashboard():
    if 'user_id' in session:
        return 'Logged in as user_id {}'.format(session['user_id'])
    return redirect(url_for('login'))

@app.route('/blog/new', methods=['GET', 'POST'])
def new_blog():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        title = request.form['title']
        new_blog = Blog(title=title, user_id=session['user_id'])
        db.session.add(new_blog)
        db.session.commit()
        return redirect(url_for('dashboard'))
    return render_template('new_blog.html')

@app.route('/blog/<int:blog_id>/entry/new', methods=['GET', 'POST'])
def new_entry(blog_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        new_entry = Entry(title=title, content=content, blog_id=blog_id, timestamp=datetime.utcnow())
        db.session.add(new_entry)
        db.session.commit()
        return redirect(url_for('view_blog', blog_id=blog_id))
    return render_template('new_entry.html')

@app.route('/blog/<int:blog_id>')
def view_blog(blog_id):
    blog = Blog.query.get_or_404(blog_id)
    entries = Entry.query.filter_by(blog_id=blog.id).all()
    return render_template('view_blog.html', blog=blog, entries=entries)

@app.route('/blog/<int:blog_id>/entry/<int:entry_id>/edit', methods=['GET', 'POST'])
def edit_entry(blog_id, entry_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    entry = Entry.query.get_or_404(entry_id)
    if request.method == 'POST':
        entry.title = request.form['title']
        entry.content = request.form['content']
        db.session.commit()
        return redirect(url_for('view_blog', blog_id=blog_id))
    return render_template('edit_entry.html', entry=entry)

@app.route('/blogs')
def view_blogs():
    blogs = Blog.query.all()
    return render_template('view_blogs.html', blogs=blogs)

if __name__ == '__main__':
    app.run(debug=True)
