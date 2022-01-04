from flask import Flask, request, render_template, url_for
from utils import *
from pprint import pprint
import os

posts, comments, bookmarks = load_data()
app = Flask(__name__, static_url_path='/static')


@app.route("/",)
def page_index():
    return render_template("index.html", posts=posts)


@app.route("/search/")
def search_page():
    search_query = request.args.get("word")
    searched_posts = search_func(posts, search_query)
    return render_template("search.html", posts=searched_posts[:9], num=len(searched_posts))    # цифра - количество постов

@app.route("/tag/<tagword>/")
def tag_pages(tagword):
    tag_posts = tag_func(posts, tagword)
    print(tag_posts[0]['pic'])
    return render_template("tag.html", posts=tag_posts, tagword=tagword)


@app.route("/user_feed/<username>/")
def user_feed(username):
    user_posts = user_posts_func(posts, username)
    return render_template("user-feed.html", posts=user_posts)


@app.route("/posts/<int:postid>/", methods=["GET", "POST"])
def post(postid):
    bookmarks == bookmark_read()
    if request.method == "POST":
        print('post-method')
        bookmark_write(postid)
    if request.method == "GET":
        post_comments = post_comment_func(comments, postid)
        return render_template("post.html", posts=posts[postid-1], comments=post_comments)


'''
@app.route("/posts/<int:post_id>/like/", methods=["POST"])
def post_like(post_id):
    """ Ставим лайк. """
    return jsonify()


@app.route("/posts/<int:post_id>/dislike/", methods=["POST"])
def post_dislike(post_id):
    """ Ставим дизлайк. """
     return jsonify()
'''


if __name__ == "__main__":
    app.run(debug=True)
# app.run(debug=True)
