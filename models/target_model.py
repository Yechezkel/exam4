from sqlalchemy import UniqueConstraint

from data.db import db

class Target(db.Model):
    __tablename__ = 'Targets'
    id = db.Column(db.Integer, primary_key=True)
    location_id = db.Column(db.Integer, db.ForeignKey('Locations.id'), nullable=True)
    type_id = db.Column(db.Integer, db.ForeignKey('Types.id'), nullable=True)
    industry_id = db.Column(db.Integer, db.ForeignKey('Industries.id'), nullable=True)

    location = db.relationship('Location', backref='targets', lazy=True)
    industry = db.relationship('Industry', backref='targets', lazy=True)
    type = db.relationship('Type', backref='targets', lazy=True)

    __table_args__ = (UniqueConstraint('type_id', 'location_id', 'industry_id', name='uix_Target'),)

    def to_dict(self):
        return {
            'target_id': self.id,
            'location': self.location.to_dict() if self.location else None,
            'industry': self.industry.to_dict() if self.industry else None,
            'type': self.type.to_dict() if self.type else None
        }


