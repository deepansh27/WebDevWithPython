
from database import Database
import uuid
import datetime

class Post(object):

   def __init__(self, blog_id, author, title, contents, date= datetime.datetime.utcnow(), post_id=None):
       self.blog_id = blog_id
       self.author = author
       self.dateCreated = date
       self.post_id = uuid.uuid4().hex if post_id is None else post_id
       self.title = title
       self.contents = contents

   def save_to_mongo (self):
       Database.insert(collection='posts', query=self.return_json())


   def return_json(self):
        return {
            'post_id': self.post_id,
            'blog_id':self.blog_id,
            'date':self.dateCreated,
            'author':self.author,
            'title':self.title,
            'content':self.contents
        }

   @staticmethod
   def from_mongo(id):

        # Post.from_mongo('123')
        return Database.find_one('posts', query={'post_id': id})


   @staticmethod
   def from_blog(id):
        return [post for post in Database.find('posts', query= {'blog_id':id})]








