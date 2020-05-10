from flask import Flask, jsonify
from flask_cors import CORS

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# add predefined sections for now
SECTIONS = [
  {
    'title': 'Web Development',
    'author': 'Aaron Hebson',
    'purpose': 'A place for all web development read articles',
  },
  {
    'title': 'History',
    'author': 'Aaron Hebson',
    'purpose': 'A place to store any articles about history at.',
  },
  {
    'title': 'Economics',
    'author': 'Aaron Hebson',
    'purpose': 'A place to store any articles about economics at.',
  },
]

# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
  return jsonify('pong!')

# sanity check route
@app.route('/sections', methods=['GET'])
def all_sections():
  return jsonify({
    'status': 'success',
    'sections': SECTIONS,
  })

if __name__ == '__main__':
  app.run()