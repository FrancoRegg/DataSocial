from hubspot import HubSpot
import os

hubspot_client = HubSpot( secret_key=os.environ["API_KEY"],)
def update_hubspot(email, name):
  contacts_api = hubspot_client.crm.contacts()
  existing_contact = contacts_api.basic_api.get_by_id(email)

  if existing_contact:
    contact_id = existing_contact.id
    update_data = {"properties": {"email": email}}
    if name:
      update_data["properties"]["name"] = name
      contacts_api.basic_api.update(contact_id, update_data)
    else:
      create_data = {"properties": {"email": email}}
      if name:
        create_data["properties"]["name"] = name
      contacts_api.basic_api.create(create_data)
