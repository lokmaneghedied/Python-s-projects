from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_cors import cross_origin, CORS
import json
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(app)
app.config['CORS_HEADERS'] = "content-type"
cors = CORS(app, resources={r"/foo": {"origins": "*"}})


class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(20), nullable=False, default='N/A')
    date_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.utcnow)

    def __repr__(self):
        return 'Blog post' + str(self.id)


with app.app_context():
    db.create_all()


# @app.route('/posts/home')
# def home():
#     return render_template('home.html')


@app.route('/posts', methods=["GET"])
@cross_origin(origin="localhost", headers=["content-type", "Authorization", "Access-Control-Allow-Origin"])
def posts():
    all_posts = BlogPost.query.order_by(BlogPost.date_posted).all()
    n_all_posts = []
    for post in all_posts:
        postObject = {
            'id': post.__dict__['id'],
            'title': post.__dict__['title'],
            'content': post.__dict__['content'],
            'author': post.__dict__['author'],
        }
        n_all_posts.append(postObject)
    return json.dumps({"posts": n_all_posts})


@app.route('/posts/delete/<int:id>', methods=['GET', 'DELETE'])
@cross_origin(origin="localhost", headers=["content-type", "Authorization", "Access-Control-Allow-Origin"])
def delete(id):
    post = BlogPost.query.get(id)
    db.session.delete(post)
    db.session.commit()
    return 'h'


@app.route("/posts/edit", methods=['GET', 'PUT'])
@cross_origin(origin="localhost", headers=["content-type", "Authorization", "Access-Control-Allow-Origin"])
def edit():
    #id = request.get_json(force=True)['id']
    post = BlogPost.query.get(request.get_json(force=True)['id'])
    post.title = request.get_json(force=True)['title']
    post.content = request.get_json(force=True)['content']
    post.author = request.get_json(force=True)['author']
    db.session.commit()
    return 'h'


@app.route("/posts/new_post", methods=['GET', 'POST'])
@cross_origin(origin="localhost", headers=["content-type", "Authorization", "Access-Control-Allow-Origin"])
def new_post():
    post_title = request.get_json(force=True)['title']
    post_content = request.get_json(force=True)['content']
    post_author = request.get_json(force=True)['author']
    db.session.add(BlogPost(title=post_title,
                   content=post_content, author=post_author))
    db.session.commit()
    return "h"


if __name__ == "__main__":
    app.run(debug=True)
