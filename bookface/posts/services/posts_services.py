from flask import session
from bookface.misc import singleton
from bookface import db

class PostsServices(metaclass=singleton.Singleton):
    def addPost(self, post):
        self._engine.session.add(post)

    def removePost(self, postId):
        self._engine.session.remove(postId)

    def getAllPosts(self):
        self._engine.session.getAllPosts()

    def getPost(self, postId):
        self._engine.session.getPost(postId)

    def flush(self):
        self.session.commit()