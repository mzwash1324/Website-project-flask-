from flask import Flask, redirect, url_for, render_template, request, session
from flask.globals import session
from datetime import timedelta, date

app = Flask(__name__)
app.secret_key = "Safi04985"
app.permanent_session_lifetime = timedelta(hours=100)

@app.route("/", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["nm"]
        session['user'] = user
        return redirect(url_for("user"))
    else:
        if "user" in session:
            return redirect(url_for("user"))
        return render_template("login.html")

@app.route("/user/")
def user():
    if "user" in session:
        user = session['user']
        return render_template("home.html", usr = user)
    else:
        return redirect(url_for("login"))

@app.route("/<user>-diary/")
def diary(user):
    if "user" in session:
        #check if user has a file then show his diary file
        return 
    else:
        return redirect(url_for("login"))

@app.route("/add-diary/")
def add_diary(user):
    if "user" in session:
        #make a new file named with the input taken from ttl
        #add the content in blog_content to that same file
        return
    else:
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))
#========================================
if __name__ == "__main__":
    app.run(debug=True)