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

@app.route("/user_feed/<username>/")
def user_feed(username):
    user_posts = user_posts_func(posts, username)
    return render_template("user-feed.html", posts=user_posts)

@app.route("/posts/<postid>/", methods=["GET", "POST"])
def post(postid):
    if request.method == "GET":
        post_comments = post_comment_func(comments, postid)
        return render_template("post.html", posts=posts[int(postid)-1], comments=post_comments)



if __name__ == "__main__":
    app.run()
# app.run(debug=True)
