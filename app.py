from flask import Flask
import os
from config import Config
from src.models.contactsModel import db
from src.routes.routesContacts import app as contacts_blueprint

app = Flask(__name__)

app.config.from_object(Config)
db.init_app(app)

app.register_blueprint(contacts_blueprint)

@app.route('/')
def home():
  return "Hello, Flask!"

if __name__ == '__main__':
  PORT = int(os.environ.get('PORT', 3001))
  app.run(host='localhost', port=PORT, debug=True)
