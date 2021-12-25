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
    searched_posts = []
    if search_query:
        for post in posts:
            if search_query in post["content"]:
                post["content"] = post["content"][:50]
                searched_posts.append(post)

    return render_template("search.html", posts=searched_posts[:9], num=len(searched_posts))    # цифра - количество постов

@app.route("/user_feed/<username>/")
def user_feed(username):
    user_posts = []
    for post in posts:
        if post["poster_name"] == username:
            post["content"] = post["content"]#[:50]
            user_posts.append(post)
    return render_template("user-feed.html", posts=user_posts)

@app.route("/posts/<postid>/", methods=["GET", "POST"])
def post(postid=1):
    if request.method == "GET":
        # print(posts[int(postid)-1])
        # print(posts[int(postid)-1].get('pk'))
        post_comments = []
        for post_comment in comments:
            if post_comment['post_id'] == int(postid):
                post_comments.append(post_comment)
        # print(post_comments)
        return render_template("post.html", posts=posts[int(postid)-1], comments=post_comments)


# with app.test_request_context():
#     print(url_for('/search/'))

if __name__ == "__main__":
    app.run()
# app.run(debug=True)
