from flask import Flask, escape, request, jsonify
from flask_restplus import Api, Resource, reqparse
from werkzeug.utils import cached_property  # werkzeug==0.16.1
from werkzeug.exceptions import BadRequest
from generator import *

# flask app configuration
app = Flask(__name__)
api = Api(app, doc="/swagger/")

# generator configuration
model_path = os.path.realpath('./poke_gen_model.h5')
input_names_path = os.path.realpath('./input/names.txt')
generator = NameGenerator(model_path, input_names_path)

# routes
@api.route('/names')
class Names(Resource):
    @api.doc(params={'amount': 'number of generated names (default: 1)'})
    def get(self):

        # parse the request
        amount = request.args.get('amount')
        
        # set the default
        if amount == None:
            amount = 1

        # try to typecast
        try:
            amount = int(amount)
        except (ValueError, TypeError):
            raise BadRequest("Bad request: check your query parameter. Expected query string: '.../names?amount=5'") 

        # generate the names
        names = generator.generate_names(amount)
        return jsonify(names)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)