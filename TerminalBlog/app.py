from models.post import Post
import pymongo
from database import Database

from models.blog import Blog
from menu import Menu
Database.initialize()

'''

post = Post(blog_id='123',
            title="Deepansh's great books",
            contents= "This containts blog by deepansh parab",
            author="Deepansh Parab")

post1 = Post(blog_id='555',
            title="Vaibhavs's great books",
            contents= "This containts blog by vaibhav desai",
            author="Vaibhav Desai")

post.save_to_mongo()
post1.save_to_mongo()

post = Post.from_blog('555')
print(post)


blog = Blog(
    author = "Deepansh Parab",
    title = "Title goes here",
    description = "This is my blog for web-development")

blog.new_post()

blog.save_to_mongo()

database = Blog.from_mongo(blog.id)
# Note:- here we are referencing a class object thus we are using capital Blog instead of normal blog

print(blog.get_posts())
'''


menu = Menu()

menu.run_menu()

