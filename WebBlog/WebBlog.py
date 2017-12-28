from flask import Flask, request, session , make_response
from flask import render_template
from common.database import Database
from models.user import User
from models.blogs import Blogs
from models.blogs import Posts
app = Flask(__name__)  # '__main__'
app.secret_key = "ascsssqs"




@app.route('/')
def home_templet():
    return render_template('home.html')


# API Endpoints: www.mysite.com/api/login <- this / is the end point for the api


@app.route('/login')
def login_method():
    return render_template('login.html')

# API Endpoints: 127.0.0.1:5000/register <- this / is the end point for the api


@app.route('/register')
def register_method():
    return render_template('register.html')


@app.before_first_request
def initilize_database():
    Database.initialize()


@app.route('/auth/login', methods=['POST'])
def login_user():
    email = request.form['email']
    password = request.form['password']

    if User.valid_login(email, password):
        User.login(email)
    else:
        session['email'] = None

    return render_template("profile.html", email=session['email'])


@app.route('/auth/register', methods=['POST'])
def register_user():
    email = request.form['email']
    password = request.form['password']

    User.register(email, password)

    return render_template("profile.html", email=session['email'])

@app.route('/blogs/<string:user_id>')
@app.route('/blogs')
def user_blogs(user_id=None):
    if user_id is not None:
        user = User.get_by_id(user_id)
    else:
        user = User.get_by_email(session['email'])

    blogs = user.get_blogs()

    return render_template("user_blogs.html",blogs=blogs, email= user.email)


@app.route('/blogs/new',methods = ['POST','GET'])
def create_new_blog():
    if request.method == 'GET':
        return render_template('new_blog.html')
    else:
        title = request.form['title']
        description = request.form['description']
        user = User.get_by_email(session['email'])

        new_blog = Blogs(user.email, title, description, user._id)
        new_blog.save_blog_to_db()
        return make_response(user_blogs(user._id))


@app.route('/posts/<string:blog_id>')
def blog_posts(blog_id):
    blog = Blogs.get_single_blog(blog_id)
    posts = blog.get_posts()

    return render_template('user_posts.html', posts=posts, blog_name=blog.title, blog_id=blog._id)


@app.route('/posts/new/<string:blog_id>',methods=['POST','GET'])
def create_new_post(blog_id):
    if request.method == 'GET':
        return render_template('new_post.html', blog_id=blog_id)
    else:
        title = request.form['title']
        content = request.form['content']
        user = User.get_by_email(session['email'])
        new_post = Posts(user.email, blog_id, title, content)
        new_post.save_to_db()
        return make_response(blog_posts(blog_id))



if __name__ == '__main__':
    app.run(port=4100)
