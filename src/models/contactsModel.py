from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Contacts(db.Model):
  __tablename__ = 'contacts'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(60), unique=False, nullable=False)
  email = db.Column(db.String(120), unique=True, nullable=False)
  phone_number = db.Column(db.String(20), nullable=False)
  create_date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
  update_date = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
  
  def __repr__(self):
    return '<Contacts %r>' % self.id

  def serialize(self):
    return {
      "id": self.id,
      "name":self.name,
      "email": self.email,
      "phone_number": self.phone_number,
      "create_date": self.create_date.isoformat(),
      "update_date": self.update_date.isoformat()
    } 