from flask import *
from scripts import *
from api_wikipedia import *
import jsonpickle
from flask_cors import *


app = Flask(__name__)
cors = CORS(app)

@app.route('/')
def hello():
    return "Hello World!"


@app.route('/get_search_results', methods=['POST'])
@cross_origin(origin='localhost')

def get_search_results():
    entities = request.json['entities']
    synonyms = ''
    if not entities[1]:
        synonyms = '5'
    else:
        synonyms = int(entities[1])
    res = get_search_result(entities[0], int(synonyms))
    response = make_response(str(jsonpickle.encode(
        res, unpicklable=False)))
    response.mimetype = 'application/json'
    
    print(response.headers)
    return response
     

if __name__ == '__main__':
    app.run()
