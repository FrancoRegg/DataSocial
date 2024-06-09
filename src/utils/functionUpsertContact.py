from src.models.contactsModel import db, Contacts

def upsert_contact(email, name):
  contact = Contacts.query.filter_by(email=email).first()
  if contact:
    if name:
      contact.name = name
    db.session.commit()
  else:
    new_contact = Contacts(email=email, name=name)
    db.session.add(new_contact)
    db.session.commit()

  return contact or new_contact