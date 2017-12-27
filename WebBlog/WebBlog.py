from flask import Flask, request, session
from flask import render_template
from common.database import Database
from models.user import User

app = Flask(__name__)  # '__main__'
app.secret_key = "ascsssqs"




# API Endpoints: www.mysite.com/api/ <- this / is the end point for the api
@app.route('/')
def hello_method():
    return render_template('login.html')


@app.before_first_request
def initilize_database():
    Database.initialize()


@app.route('/login', methods=['POST', "GET"])
def login_user():
    email = request.form['email']
    print(email)
    password = request.form['password']
    print(password)
    if User.valid_login(email, password):
        User.login(email)
    else:
        session['email']= None
    return render_template("profile.html", email =session['email'])


if __name__ == '__main__':
    app.run()
