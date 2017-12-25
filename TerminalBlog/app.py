from models.post import Post
from Database import Database



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

'''

post = Post.from_blog('555')
print(post)
