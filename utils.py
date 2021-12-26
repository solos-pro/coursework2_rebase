import json
from pprint import pprint


def load_data():
    with open('data/data.json') as fp:
        posts = json.load(fp)

    with open('data/comments.json') as fp:
        comments = json.load(fp)

    posts = prepare_posts(posts, comments)

    with open('data/bookmarks.json') as fp:
        bookmark = json.load(fp)

    return posts, comments, bookmark



def prepare_posts(posts, comments):
    for i, post in enumerate(posts):
        pk = post.get('pk')
        post_comments = []
        for comment in comments:
            if comment.get('post_id') == pk:
                post_comments.append(comment)
            posts[i]['comment_count'] = len(post_comments)

        posts[i]['content'] = tegify_content(posts[i]['content'])
    return posts


def tegify_content(content):
    words = content.split(" ")
    for i, word in enumerate(words):
        if word.startswith("#"):
            tag = word.replace("#", "")
            link = f"<a href=/tag/{tag}>{word}</a>"
            words[i] = link
    return " ".join(words)

def search_func(posts, search_query):
    searched_posts = []
    if search_query:
        for post in posts:
            if search_query in post["content"]:
                post["content"] = post["content"][:50]
                searched_posts.append(post)
    return searched_posts


def user_posts_func(posts, username):
    user_posts = []
    for post in posts:
        if post["poster_name"] == username:
            post["content"] = post["content"]#[:50]
            user_posts.append(post)
    return user_posts

def post_comment_func(comments, postid=1):
    post_comments = []
    for post_comment in comments:
        if post_comment['post_id'] == int(postid):
            post_comments.append(post_comment)
    return post_comments
