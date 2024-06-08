from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Contacts(db.Model):
  __tablename__ = 'contacts'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(60), unique=False, nullable=False)
  email = db.Column(db.String(120), unique=True, nullable=False)
  
  def __repr__(self):
    return '<Contacts %r>' % self.id

  def serialize(self):
    return {
      "id": self.id,
      "name":self.name,
      } 