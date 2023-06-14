from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from . extensions import db, bcrypt
from project.models.posts import Post

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return (render_template('index.html'))

@main.route('/newsfeed')
@login_required
def newsfeed():
    posts = Post.query.all()
    return (render_template('newsfeed.html', posts=posts, name=current_user.name))
    #return (render_template('context.html', name=current_user.name))
    

@main.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            new_post = Post(title=title, content=content)
            db.session.add(new_post)
            db.session.commit()
            return redirect(url_for('main.newsfeed'))
    return render_template('create.html')


