########### IMPORTS ########################
from models.posts import Posts
from common.database import Database

############################################

database = Database.initialize()

post2= Posts(
    "Vaibhav",
    "B02",
    "Vaibhav's Blog Title",
    "Vaibhav's Blog Content",
)

posts = Posts.get_posts_from_blog('B02')

print(posts)

print('success')

