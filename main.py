from flask import Flask, render_template
from post import Blog

app = Flask(__name__)
blog = Blog()


@app.route("/")
def home():
    return render_template("index.html",
                           all_post=blog.posts,
                           )


@app.route("/post/<int:post_id>")
def post_page(post_id):
    return render_template("post.html",
                           post_id=post_id,
                           all_post=blog.posts,
                           )


if __name__ == "__main__":
    app.run(debug=True)
