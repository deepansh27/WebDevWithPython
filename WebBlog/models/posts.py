'''

The user must have the following common data which can be put in init class:
author
blog_id
post_id using uuid.uuid4().hex
title
content
date  using datatime

apart from this we need a database connection
'''

import datetime
import uuid
from common.database import Database


class Posts(object):

    def __init__(self, author, blog_id, title, content, date = datetime.datetime.utcnow(), _id=None):
        self.author = author
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.date = date
        self._id = uuid.uuid4().hex if _id is None else _id


    def save_to_db(self):
        Database.insert(collection='posts', data=self.return_json())


    @staticmethod
    def get_posts_from_blog(blog_id):
        return [post for post in Database.find(collection='posts', query={'blog_id': blog_id})]

    @classmethod
    def get_single_post(cls, post_id):
        post_data = Database.find_one(collection='posts', query={'_id': post_id})
        return cls(**post_data)

    def return_json(self):
        return {
            'author':self.author,
            'blog_id':self.blog_id,
            'title':self.title,
            'content':self.content,
            'date':self.date,
            '_id':self._id
        }



