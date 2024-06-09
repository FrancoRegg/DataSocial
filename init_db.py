from app import app
from src.models.contactsModel import db

with app.app_context():
    db.create_all()