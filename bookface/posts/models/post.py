from bookface import db
from sqlalchemy.orm import backref
from datetime import datetime
import locale
from calendar import isleap, monthrange

class Post(db.Model):
    __tablename__ = "posts"
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text, nullable=False)
    likes = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    user = db.relationship('User', uselist=False, backref=backref('posts'))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_time_difference(self):
        locale.setlocale(locale.LC_ALL, "")
        time_difference = datetime.now() - self.created_at

        MIN = 60
        HOUR = 60*MIN
        DAYS_OF_CURRENT_MONTH = monthrange(int(self.created_at.year), int(self.created_at.month))[1]

        if isleap(self.created_at.year):
            DAYS_OF_YEAR = 366
        else:
            DAYS_OF_YEAR = 365

        if (time_difference.seconds < MIN and time_difference.days < 1):
            result = "Przed chwilą"
        elif (time_difference.seconds >= MIN and time_difference.seconds < HOUR and time_difference.days < 1):
            result = f"{int(time_difference.seconds/MIN)} min temu"
        elif (time_difference.seconds >= HOUR and time_difference.days < 1):
            result = f"{int(time_difference.seconds/HOUR)} godz. temu"
        elif (time_difference.days == 1 and time_difference.days < 2):
            creation_date = self.created_at.strftime("%H:%M")
            result = f"Wczoraj o {creation_date}"
        elif (time_difference.days >= 2 and time_difference.days < DAYS_OF_CURRENT_MONTH):
            result = self.created_at.strftime("%d %b %H:%M")
        elif (time_difference.days >= DAYS_OF_CURRENT_MONTH and time_difference.days < DAYS_OF_YEAR):
            result = self.created_at.strftime("%d %b")
        else:
            result = self.created_at.strftime("%d %b %Y")
        return result