from flask import request, jsonify, Blueprint
from src.models.contactsModel import db, Contacts
from src.utils.functionHubSpot import sync_with_hubspot
from src.utils.functionUpsertContact import upsert_contact

app = Blueprint("app", __name__)
#ENDPOINT PARA PROBAR LA CREACION DE CONTACTOS
@app.route('/contactsName', methods=['GET'])
def getcontacts():
  contacts = Contacts.query.all()
  if contacts is None:
      return jsonify('there are no contacts')
  
  return jsonify([contact.serialize() for contact in contacts])

@app.route('/contacts', methods=["POST"])
def create_or_update_contact():
  body = request.get_json(silent=True)

  if not body:
    return jsonify("Invalid JSON data"), 400
  
  email = body.get("email")
  name = body.get("name")

  if not email:
    return jsonify("Email is required"), 400
  if not name:
    return jsonify("Name is required"), 400
  
  contact = Contacts.query.filter_by(email=email).first()
  if contact:
    if name:
      contact.name = name
  else:
    new_contact = Contacts(email=email, name=name)
    db.session.add(new_contact)
  
  try:
    db.session.commit()
  except Exception as e:
    db.session.rollback()
    return jsonify({"error": str(e)}), 500

  return jsonify("Contact created/updated"), 200
  

@app.route('/sync_contacts', methods=["POST"])
def sync_contacts():
  body = request.get_json(silent=True)

  if not body:
    return jsonify("Invalid JSON data"), 400
  
  email = body.get('email')
  name = body.get('name')

  if not email:
    return jsonify("Email is required"), 400
  if not name:
    return jsonify("Name is required"), 400
  
  hubspot_response = sync_with_hubspot(email, name)
  return jsonify(hubspot_response), 200


@app.route('/webhook', methods=['POST'])
def webhook():
  body = request.get_json(silent=True)
  email = body.get('email')
  name = body.get('name')

  if not email:
    return jsonify("Email is required"), 400
  if not name:
    return jsonify("Name is required"), 400
  
  contact = upsert_contact(email, name)
  #update_hubspot(email, name)

  return jsonify({"message": "Contact processed successfully", "contact": {"email": contact.email, "name": contact.name}}), 200


