from db import db


class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client = db.Column(db.String(200))
    product = db.Column(db.String(200), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    priority = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(300), nullable=False)
    user_story = db.Column(db.String(500), nullable=False)
    feedback_type = db.Column(db.String(50), nullable=False)
    posted = db.Column(db.Boolean, default=False)
