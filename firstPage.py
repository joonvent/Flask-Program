from flask import Flask , redirect , url_for , render_template

app = Flask(__name__)

@app.route("/")
def home():

    return render_template('index.html')

if __name__ == '__main__':
    app.run()

@app.route("/<name>")
def user(name):
    return (f"Hello {name} Welcome to This Cruel World")

app.route("/admin")
def admin():
    return redirect(url_for("/home"))














