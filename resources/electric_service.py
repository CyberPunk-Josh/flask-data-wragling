from flask_restful import Resource, reqparse
from models.electric_service import ElectricServiceModel


class ElectricCityValue(Resource):
    parser = reqparse.RequestParser()

    def get(self, city):
        city = ElectricServiceModel.find_by_city_name(city)
        if city:
            return city.json()
        return {"message": "City not found"}, 404


class ElectricCityValueList(Resource):
    def get(self):
        return {'cities': [x.json() for x in ElectricServiceModel.query.all()]}
