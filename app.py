from flask import Flask
from flask_restful import Api
from db import db
from decouple import config
import psycopg2

# VARIABLES
password = config('PASSWORD')
port = config('PORT')
database = config('DATABASE')

# RESOURCES
from resources.electric_service import ElectricCityValue, ElectricCityValueList

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://joshue:{password}@Localhost:{port}/{database}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = "JOSHUE"
api = Api(app)

# ENDPOINTS
api.add_resource(ElectricCityValue, '/electric/<string:city>')
api.add_resource(ElectricCityValueList, '/electric_service')


if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)
