import uuid
from post import Post
import datetime
from Database import Database

class Blog(object):

    def __init__(self, author, title, description , id = None):
        self.author = author
        self.title = title
        self.description = description
        self.id = uuid.uuid4().hex if id is None else id

    def new_post(self):
        title = raw_input("Enter the title ")
        content = raw_input("Enter the content ")
        date = raw_input("Enter the date in format( DD:MM:YYYY ) or leave blank ")
        if date == "":
            date= datetime.datetime.utcnow()
        else:
            date = datetime.datetime.strptime(date, "%d%m%Y")


        post = Post(blog_id=self.id,
                    title=title,
                    contents=content,
                    author=self.author,
                    date= date )
        post.save_to_mongo()



    def get_posts(self):
        return Post.from_blog(self.id)

    def save_to_mongo(self):
        Database.insert(collection='blogs', query=self.return_json())

    def return_json(self):
        return {
            'author':self.author,
            'title':self.title,
            'description':self.description,
            'id':self.id
        }


    @classmethod
    def from_mongo(cls,id):
        blog_data = Database.find_one(collection='blogs', query={'id':id})

        return cls(author= blog_data['author'],
                   title = blog_data['title'],
                   description = blog_data['description'],
                   id= blog_data['id'])



