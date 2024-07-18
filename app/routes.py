from flask import Flask, render_template, request, redirect, url_for, session
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import Users , Books
from app import db, app
from app.forms import RegisterForm


with app.app_context():
    db.create_all()

@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("home.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        user = Users.query.filter_by(username=username).first()
        if user and check_password_hash(user.password , password):
            session["username"]=user.username
            session["user_id"] = user.id
            return redirect(url_for("user_menu"))
        else:
            return "Invalid Username or Password", 401
    return render_template("login.html")



@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    else:
        hashed_password = generate_password_hash(request.form.get("password"), method='pbkdf2:sha256')
        hashed_confing_password = generate_password_hash(request.form.get("confirm_password"), method='pbkdf2:sha256')
        u1 = Users(username=request.form.get("username"), email=request.form.get("email"),
                          password=hashed_password,
                          confirm_password=hashed_confing_password)
        db.session.add(u1)
        db.session.commit()
        message = "User successfully created"

        return render_template("login.html" , message=message)

@app.route("/user_menu", methods=["GET", "POST"])
def user_menu():
    return render_template("user_menu.html")


@app.route("/add_book", methods=["GET", "POST"])
def add_book():
    if request.method == "GET":
        return render_template("book.html")
    else:
        book = Books(title=request.form.get("title"), author=request.form.get("author"), page_count=request.form.get("page_count"),)
        db.session.add(book)
        db.session.commit()
        message = "User successfully created"

        return render_template("add_book.html" , message=message)


@app.route("/my_book", methods=["GET", "POST"])
def my_book():
    if request.method == "POST":
        username = session["username"]
        book1 = Books.query.filter_by(title=request.form.get("title")).first()
        if username == session["username"]:
                return render_template("my_book.html",title=book1.title , author=book1.author , page_count=book1.page_count)
        else:
            message = ("You Don't have any book")
            return render_template("my_book.html", message=message)
    return render_template("my_book.html")

@app.route("/update_book", methods=["GET", "POST"])
def update_book():
    if request.method == "GET":
        render_template("update.html")
    else:
        pass

@app.route("/delete", methods=["GET", "POST"])
def delete():
    if request.method == "POST":
        username = session["username"]
        user = Users.query.filter_by(username=username).first()
        if user:
            db.session.delete(user)
            db.session.commit()
            message = "User successfully deleted"
        else:
            message = "User not found"
            return render_template("delete.html", message=message)
    else:
         return render_template("delete.html")
