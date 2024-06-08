from flask import  Flask, request, jsonify
from models import db, contactsModel
from utils import upsert_contact, update_hubspot
from . import app

'''
@app.route('/contacts', methods=['POST'])
def create_or_update_contact():
  #Extrae datos del cuero de la solicitud 
  body = request.get_json(silent=True)
  email = body.get('email')
  name = body.get('name')

  contact = contactsModel.query.filter_by(email=email).first() #Busca si ya existe un contacto con el email proporcionado
  if contact:
    contact.name = name #Si el contacto existe, actualiza el nombre
  else:
    contact = contactsModel(email=body['email'], name=body['name']) #Si no existe, crearlo
  db.session.add(contact)
  db.session.commit()
  #update_hubspot(email, name)
  return jsonify('OK'), 200
'''
@app.route('/webhook', method=['POST'])
def webhook():
  body = request.get_json(silent=True)
  email = body.get('email')
  name = body.get('name')

  if not email:
    return jsonify("Email is required"), 400
  if not name:
    return jsonify("Name is required"), 400
  
  contact = upsert_contact(email, name)
  update_hubspot(email, name)

  return jsonify({"message": "Contact processed successfully", "contact": {"email": contact.email, "name": contact.name}}), 200
