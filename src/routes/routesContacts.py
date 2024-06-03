from flask import  Flask, request, jsonify
from models import db, contactsModel
from . import app


@app.route('/contacts', methods=['GET','POST'])
def create_or_update_contact():
  data = request.get_json(silent=True)
  email = data.get('email')
  name = data.get('name')

  contact = contactsModel.query.filter_by(email=email).first()
  if contact:
    contact.name = name
  else:
    contact = contactsModel(email=data['email'], name=data['name'])
  db.session.add(contact)
  db.session.commit()
  return jsonify('OK'), 200

#@app.route('/webhook', method=['POST'])
#def webhook():
