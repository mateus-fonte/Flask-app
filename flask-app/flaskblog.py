from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {"author": "Carlos Pereira",
     "title":   "Blog Post 1",
     "content": "First post content",
     "date_posted": "April 21, 2018"},

    {"author": "Hakuna Matata",
     "title":   "Blog Post 2",
     "content": "Second post content",
     "date_posted": "April 22, 2018"},

    {"author": "Carlos Pereira",
     "title":   "Blog Post 3",
     "content": "Third post content",
     "date_posted": "April 23, 2018"}
]

lista = [1,2,3,4]

@app.route("/")
def home():
    return render_template("home.html",posts=posts)

@app.route("/about")
def about():
    return  render_template("about.html",title="About")

if __name__ == "__main__":
    app.run(debug=True)

