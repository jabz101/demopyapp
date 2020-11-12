from flask import Flask, jsonify
from flask_restful import Resource, Api
app = Flask(__name__)
api = Api(app)


class Quotes(Resource):
    def get(self):
        return {
            'William Shakespeare': {
                'quote': ['Love all,trust a few,do wrong to none',
                'Some are born great, some achieve greatness, and some greatness thrust upon them.']
        },
        'Linus': {
            'quote': ['Talk is cheap. Show me the code.']
            }
        }

api.add_resource(Quotes, '/api/test')

@app.route('/hello/<int:number>/', methods=['GET', 'POST'])
def welcome(number):
    return "Hello World! this is a response from invoking the API and adding 10 to the integer passed on the API route which makes it the  number: " + str(number+10)

@app.route('/<int:number>/')
def incrementer(number):
    return "Incremented number is " + str(number+10)

@app.route('/<string:name>/')
def hello(name):
    return "Hello there my name is " + name

@app.route('/person/')
def helloperson():
    return jsonify({'first name':'Jabed', 
                    'surname':'Miah'}, {'first name':'Sadiq', 'surname':'Rahman'})

@app.route('/numbers/')
def print_list():
    return jsonify(list(range(4))) 

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
