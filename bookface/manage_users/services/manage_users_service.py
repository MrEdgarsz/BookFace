from bookface import db
from bookface.auth.models.user import User
from bookface.misc import singleton
from bookface.roles.models.role import Role



class ManageUsersService(metaclass=singleton.Singleton):
    def __init__(self):
        self.session=db.session
    
    def get_all_users(self):
        return User.query.all()
    
    def ban_user(self,user_id):
        user = self.session.query(User).filter_by(id=user_id).first()
        role = self.session.query(Role).filter_by(name="Zablokowany").first()
        user.role = role
        return self.session.merge(user)

    def unban_user(self, user_id):
        user = self.session.query(User).filter_by(id=user_id).first()
        role = self.session.query(Role).filter_by(name="Użytkownik").first()
        user.role = role
        return self.session.merge(user)

    def promote(self,user_id,role):
        user = self.session.query(User).filter_by(id=user_id).first()
        role = self.session.query(Role).filter_by(name=role).first()
        user.role = role
        return self.session.merge(user)

    def flush(self):
        self.session.commit()
