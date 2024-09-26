from sqlalchemy import UniqueConstraint

from data.db import db

class Target(db.Model):
    __tablename__ = 'Targets'
    id = db.Column(db.Integer, primary_key=True)
    location_id = db.Column(db.Integer, db.ForeignKey('Locations.id'), nullable=True)
    type_id = db.Column(db.Integer, db.ForeignKey('Targets.id'), nullable=True)
    industry_id = db.Column(db.Integer, db.ForeignKey('Industries.id'), nullable=True)

    __table_args__ = (UniqueConstraint('type_id', 'location_id', 'industry_id', name='uix_Target'),)

    def to_dict(self):
        return {
            'id': self.id,
            'location_id': self.location_id,
            'type_id': self.type_id,
            'industry_id': self.industry_id
        }