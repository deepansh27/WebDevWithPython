'''
Blog will contain the following:
blog_id
author
title
description

'''

import uuid
import datetime
from common.database import Database
from models.posts import Posts

class Blogs(object):

    def __init__(self, author, title, description, author_id,  _id=None):
        self.author = author
        self.author_id = author_id
        self.title = title
        self.description = description
        self._id = uuid.uuid4().hex if _id is None else _id

    def new_post(self, post_title, post_content, date = datetime.datetime.utcnow()):
        post = Posts(blog_id=self._id,
                     title=post_title,
                     content = post_content,
                     author= self.author,
                     date= date
                     )

        post.save_to_db() #saving to the database

    def get_posts(self):
        return Posts.get_posts_from_blog(self._id)

    def return_json(self):
        return {
            'author': self.author,
            'author_id': self.author_id,
            'title': self.title,
            'description': self.description,
            '_id': self._id
        }

    def save_blog_to_db(self):
        Database.insert(collection='blogs', data=self.return_json())

    @classmethod
    def get_single_blog(cls,blog_id):
        blog_data = Database.find_one(collection='blogs', query={'_id':blog_id})

        return cls(**blog_data)

    @classmethod
    def find_blog_by_author_id(cls, author_id):
        blog_data = Database.find(collection='blogs', query={'author_id': author_id})
        return [cls(**blog) for blog in blog_data]
