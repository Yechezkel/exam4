from sqlalchemy import UniqueConstraint

from data.db import db

class City(db.Model):
    __tablename__ = 'Cities'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    country_id = db.Column(db.Integer, db.ForeignKey('Countries.id'), nullable=True)

    country = db.relationship('Country', backref='cities', lazy=True)

    __table_args__ = (UniqueConstraint('name', 'country_id', name='uix_City'),)


    def to_dict(self):
        return {
            'city_id': self.id,
            'city_name': self.name,
            'country': self.country.to_dict() if self.country else None
        }