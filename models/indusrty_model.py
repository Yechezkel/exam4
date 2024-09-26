

from data.db import db

class Industry(db.Model):
    __tablename__ = 'Industries'
    id = db.Column(db.Integer, primary_key=True)
    industry = db.Column(db.String(80), nullable=False, unique=True)


    def to_dict(self):
        return {
            'id': self.id,
            'industry': self.industry
        }