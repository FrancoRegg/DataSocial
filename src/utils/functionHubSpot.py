'''from hubspot import HubSpot
import os

hubspot_client = HubSpot( api_key=os.environ["HUBSPOT_API_KEY"],) #Inicializo el cliente de HubSpot
def update_hubspot(email, name):
  contacts_api = hubspot_client.crm.contacts() #Accedo a la API de contactos
  
  try:
    existing_contact = contacts_api.basic_api.get_by_id(email) #Obtenemos el contacto existente en HubSpot

    if existing_contact:
      contact_id = existing_contact.id
      update_data = {"properties": {"email": email}} #Si el contacto existe, se actualizan los datos

      if name:
        update_data["properties"]["name"] = name #Si se proporciona un nombre, tambien se actualiza
        contacts_api.basic_api.update(contact_id, update_data)
      else:
        create_data = {"properties": {"email": email}} #Si el contacto no exite, se crea uno nuevo con los datos proporcionados
        if name:
          create_data["properties"]["name"] = name #Si se proporciona un nombre, se añade a los datos de creacion
        contacts_api.basic_api.create(create_data)

  except Exception as e: #Captura cualquier excepcion que pueda ocurrir
    print("Error", e)'''

import requests, os

Api_Key = os.environ["HUBSPOT_API_KEY"]
URL_HubSpot = 'https://api.hubapi.com/crm/v3/objects/contacts'

def sync_with_hubspot(name, email):
  headers = {
    'Content-type': "application/json",
    'Authorization': f'Bearer {Api_Key}'
  }
  data = {
    "properties": {
      'email': email,
      'name': name
    }
  }

  response = requests.post(URL_HubSpot, json=data, headers=headers)
  try:
    response.raise_for_status()
    return response.json()
  except requests.exceptions.HTTPError as e:
    return {"error": str(e), "response": response.text}
