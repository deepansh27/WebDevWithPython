from models.blog import Blog
import models.blog
from Database import Database

class Menu(object):
    def __init__(self):
        # Ask the user for author name

        self.user = raw_input("Enter your author name: ")
        self.user_blog = None

        # Check if they have already got an account

        if self._user_has_account():
            print("welcome back {}".format(self.user))
        else:
            # If not, prompt them to create one
            self._prompt_user_for_account()

    def _user_has_account(self):
        blog =  Database.find_one('blogs',{'author':self.user})
        if blog is not None:
            self.user_blog = Blog.from_mongo(blog['id'])
            return True
        else:
            return False

    def _prompt_user_for_account(self):
        title = raw_input("Enter blog title: ")
        description = raw_input("Enter blog description: ")
        blog = Blog(author=self.user,
                    title= title,
                    description= description)
        blog.save_to_mongo()
        self.user_blog = blog




    def run_menu(self):
        # Ask user if its will read or write a blog?
        user_input = 'C'
        while user_input == 'C':
            read_or_write = raw_input("Do you want to read(R) or write(W) blogs?: ")


            # if read:

            # allow user to pick one
            # display posts
            if read_or_write == 'R':
                # list all the blogs in from the database
                self._list_blogs()
                self._view_blogs()



            elif read_or_write == 'W':
                # check if the user has a blog
                self._prompt_write_post()

                self._view_blogs()

                    # if they do, prompt the user to write a post
                    # if not, prompt the user to create a blog

            else:
                print('Thank you for blogging..!!')
            user_input = raw_input("Press (C) to continue or (E) to exit:")


    def _prompt_write_post(self):
        self.user_blog.new_post()

    def _list_blogs(self):
        blogs = Database.find(collection='blogs', query={})

        for blog in blogs:
            print("ID: {} \nTitle: {} \nAuthor: {} \n".format(blog['id'], blog['title'], blog['author']))

    def _view_blogs(self):
        blog_to_see = raw_input("Enter the id of the blog you would like to read: ")
        blog = Blog.from_mongo(blog_to_see)
        posts = blog.get_posts()
        for post in posts:
            print("Date: {} \nTitle: {} \nContent: {}".format(post["date"],post["title"], post["content"]))



