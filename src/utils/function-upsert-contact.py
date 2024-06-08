from models import db, contactsModel

def upsert_contact(email, name):
  contact = contactsModel.query.filter_by(email=email).first()
  if contact:
    if name:
      contact.name = name
    db.session.commit()
  else:
    new_contact = contactsModel(email=email, name=name)
    db.session.add(new_contact)
    db.session.commit()

  return contact or new_contact