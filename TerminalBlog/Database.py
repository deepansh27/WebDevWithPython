
import pymongo

class Database(object):
    URI = "mongodb://127.0.0.1:27017"
    DATABASE = None


    @staticmethod   #this is used to tell python that we are not going to use any self parameter because this method will belong only to the database class
    # as a whole and never to an instance of a database
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client['fullstack']


    @staticmethod
    def insert(collection, query):
        Database.DATABASE[collection].insert(query)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)



'''
# to check if there any service running on a given port..and free that port by killing the existing serivce
Find the process using port 8080:

sudo lsof -i:8080
Kill it:

kill XXXX

'''