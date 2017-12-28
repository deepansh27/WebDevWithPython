from common.database import Database
import uuid
from flask import session
import datetime
from models.blogs import Blogs
from models.blogs import Posts


class User(object):
    def __init__(self, email, password, _id=None):
        self.email = email
        self.password = password
        self._id = uuid.uuid4().hex if _id is None else _id

    @classmethod
    def get_by_email(cls, email):  # filter by email
        email_found = Database.find_one(collection="users", query={'email': email})
        if email_found is not None:
            return cls(**email_found)
        else:
            return None

    @classmethod
    def get_by_id(cls, user_id): # filter by id
        id_data = Database.find_one(collection="users", query={'_id': user_id})
        if id_data is not None:
            return cls(**id_data)
        else:
            return None

    @staticmethod
    # User.valid_login("dparab@stevens.edu", "1234")
    # check if the users login matches its password
    def valid_login(email, password):
        has_email = User.get_by_email(email)
        if has_email is not None:
            # check for the password
            return has_email.password == password
        else:
            return False

    @classmethod
    def register(cls, email, password):
        user_exists = cls.get_by_email(email)
        if user_exists is None:
            # the user doest not exists, so we can create one
            new_user = cls(email, password)
            session['email'] = email
            new_user.save_user_to_db()
            return True

        else:
            return False

    @staticmethod
    def login(user_email):
        # to help the user login
        # when we call this login valid has already been called
        session['email'] = user_email

    @staticmethod
    def logout():
        session['email'] = None

    def get_blogs(self):
        return Blogs.find_blog_by_author_id(self._id)

    def new_blog(self,title, description):
        # author, title, description, author_id
        blog = Blogs(
            author=self.email,
            title=title,
            description=description,
            author_id=self._id
        )
        blog.save_blog_to_db()

    @staticmethod
    def new_post(blog_id, title, content, date= datetime.datetime.utcnow()):
        # post_title, post_content, date = datetime.datetime.utcnow()
        blog = Blogs.get_single_blog(blog_id)
        blog.new_post(
            title=title,
            content=content,
            date=date
        )

    def return_json(self):
        return {
            'email':self.email,
            '_id':self._id,
            'password':self.password
        }

    def save_user_to_db(self):
        Database.insert(collection='users', data = self.return_json())