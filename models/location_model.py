from sqlalchemy import UniqueConstraint

from data.db import db

class Location(db.Model):
    __tablename__ = 'Locations'
    id = db.Column(db.Integer, primary_key=True)
    longitude = db.Column(db.String(80), nullable=False)
    latitude = db.Column(db.String(80), nullable=False)
    city_id = db.Column(db.Integer, db.ForeignKey('Cities.id'), nullable=True)

    city = db.relationship('City', backref='locations', lazy=True)

    __table_args__ = (UniqueConstraint('longitude', 'latitude', name='uix_Location'),)

    def to_dict(self):
        return {
            'location_id': self.id,
            'longitude': self.longitude,
            'latitude': self.latitude,
            'city': self.city.to_dict() if self.city else None
        }