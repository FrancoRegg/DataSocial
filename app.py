from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
  return "Hello, Flask!"

if __name__ == '__main__':
  PORT = int(os.environ.get('PORT', 3001))
  app.run(host='0.0.0.0', port=PORT, debug=True)
