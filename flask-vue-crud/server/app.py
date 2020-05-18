# -------------------------------- #
#              app.py              #
#       Author: Aaron Hebson       #
#    Entry point of the server     #
# -------------------------------- #

from flask import Flask, jsonify, request
from flask_cors import CORS

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
  return jsonify('pong!')

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
@app.route('/sections', methods=['get','post'])
def all_sections():
  response_object = {'status': 'success'}
  if request.method == 'POST':
    post_data = request.get_json()
    SECTIONS.append({
      'title': post_data.get('title'),
      'author': post_data.get('author'),
      'purpose': post_data.get('purpose')
    })
    response_object['message'] = 'section added!'
  else:
    response_object['sections'] = SECTIONS
  return jsonify(response_object)

if __name__ == '__main__':
  app.run()