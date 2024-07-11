from flask import request
from logic.decision_logic import DecisionLogic
from models.geo_model import GeoModel
from models.client_errors import ValidationError

class DecisionFacade:

    def __init__(self):
        self.logic = DecisionLogic()

    def launch_missile(self):
        json = request.get_json()
        latitude = json.get("latitude")
        longitude = json.get("longitude")
        geo = GeoModel(latitude, longitude)
        error = geo.validate()
        if error: raise ValidationError(error, geo)
        return self.logic.launch_missile(geo)