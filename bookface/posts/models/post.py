from bookface import db
from sqlalchemy.orm import backref
from datetime import datetime, timedelta

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
        time_difference = datetime.now() - self.created_at
        time_difference_sec = time_difference.seconds

        MIN = 60
        HOUR = 60*MIN
        DAY = 24*HOUR
        MONTH = 30*DAY
        YEAR = 12*MONTH

        if (time_difference_sec < MIN):
            result = "Przed chwilą"
        elif (time_difference_sec >= MIN and time_difference_sec < HOUR):
            result = f"{int(time_difference_sec/MIN)} min temu"
        elif (time_difference_sec >= HOUR and time_difference_sec < DAY):
            result = f"{int(time_difference_sec/HOUR)} godz. temu"
        elif (time_difference_sec >= DAY and time_difference_sec < (2*DAY)):
            creation_date = self.created_at.strftime("%H:%M")
            result = f"Wczoraj o {creation_date}"
        elif (time_difference_sec >= (2*DAY) and time_difference_sec < MONTH):
            result = time_difference.strftime("%d.%B %H:%M")
        elif (time_difference_sec >= MONTH and time_difference_sec < YEAR):
            result = time_difference.strftime("%d.%B")
        else:
            result = time_difference.strftime("%d %B %Y")
        return result