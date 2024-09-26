from data.db import db

class Country(db.Model):
    __tablename__ = 'Countries'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)



    def to_dict(self):
        return {
            'country_id': self.id,
            'country_name': self.name
        }
