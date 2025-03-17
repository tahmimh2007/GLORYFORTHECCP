from flask import Flask, render_template, redirect, url_for, request, session
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import sqlite3
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
DATABASE = 'site.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with app.app_context():
        db = get_db_connection()
        with app.open_resource('schema.sql') as f:
            db.executescript(f.read().decode('utf8'))
        db.commit()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = generate_password_hash(request.form['password'], method='sha256')
        conn = get_db_connection()
        conn.execute('INSERT INTO user (username, email, password) VALUES (?, ?, ?)',
                     (username, email, password))
        conn.commit()
        conn.close()
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        conn = get_db_connection()
        user = conn.execute('SELECT * FROM user WHERE email = ?', (email,)).fetchone()
        conn.close()
        if user and check_password_hash(user['password'], password):
            session['user_id'] = user['id']
            return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('login'))

@app.route('/dashboard')
def dashboard():
    if 'user_id' in session:
        conn = get_db_connection()
        blogs = conn.execute('SELECT * FROM blog WHERE user_id = ?', (session['user_id'],)).fetchall()
        conn.close()
        return render_template('dashboard.html', blogs=blogs)
    return redirect(url_for('login'))

@app.route('/blog/new', methods=['GET', 'POST'])
def new_blog():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        title = request.form['title']
        conn = get_db_connection()
        conn.execute('INSERT INTO blog (user_id, title) VALUES (?, ?)',
                     (session['user_id'], title))
        conn.commit()
        conn.close()
        return redirect(url_for('dashboard'))
    return render_template('new_blog.html')

@app.route('/blog/<int:blog_id>/entry/new', methods=['GET', 'POST'])
def new_entry(blog_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        conn = get_db_connection()
        conn.execute('INSERT INTO entry (blog_id, title, content, timestamp) VALUES (?, ?, ?, ?)',
                     (blog_id, title, content, datetime.utcnow()))
        conn.commit()
        conn.close()
        return redirect(url_for('view_blog', blog_id=blog_id))
    return render_template('new_entry.html')

@app.route('/blog/<int:blog_id>')
def view_blog(blog_id):
    conn = get_db_connection()
    blog = conn.execute('SELECT * FROM blog WHERE id = ?', (blog_id,)).fetchone()
    entries = conn.execute('SELECT * FROM entry WHERE blog_id = ?', (blog_id,)).fetchall()
    conn.close()
    return render_template('view_blog.html', blog=blog, entries=entries)

@app.route('/blog/<int:blog_id>/entry/<int:entry_id>/edit', methods=['GET', 'POST'])
def edit_entry(blog_id, entry_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    conn = get_db_connection()
    entry = conn.execute('SELECT * FROM entry WHERE id = ?', (entry_id,)).fetchone()
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        conn.execute('UPDATE entry SET title = ?, content = ? WHERE id = ?',
                     (title, content, entry_id))
        conn.commit()
        conn.close()
        return redirect(url_for('view_blog', blog_id=blog_id))
    conn.close()
    return render_template('edit_entry.html', entry=entry)

@app.route('/blogs')
def view_blogs():
    conn = get_db_connection()
    blogs = conn.execute('SELECT * FROM blog').fetchall()
    conn.close()
    return render_template('view_blogs.html', blogs=blogs)

if __name__ == '__main__':
    if not os.path.exists(DATABASE):
        init_db()
    app.run(debug=True)
