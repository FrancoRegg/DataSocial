from flask import request, jsonify, Blueprint
from src.utils.functionHubSpot import update_hubspot
from src.utils.functionUpsertContact import upsert_contact

app = Blueprint("app", __name__)

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
  update_hubspot(email, name)

  return jsonify({"message": "Contact processed successfully", "contact": {"email": contact.email, "name": contact.name}}), 200
