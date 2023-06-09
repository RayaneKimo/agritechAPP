import time
from flask import Flask, render_template, request, url_for, redirect
from flask_restx import Api, Resource, fields
from config import DevelopmentConfig
from models import esp2, db
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

db.init_app(app)
CORS(app)

api = Api(app, version='1.0', title='Agritech API',
          description='Agritech API) ', doc='/docs')


@app.route('/')
def index():
    return 'Hello World'


esp2_serialiser = api.model('esp2', {
    "ID": fields.Integer,
    "Moisture": fields.Integer,
    "temperature": fields.Integer,
    "humidity": fields.Integer,
    "light": fields.Integer
})


@api.route('/esp2')
class helloResource(Resource):
    # this decorator is used to serialise the data that means it will convert the data into json format
    @api.marshal_list_with(esp2_serialiser)
    def get(self):
        data = esp2.query.limit(30).all()
        return data


if __name__ == '__main__':
    app.run(debug=True)
