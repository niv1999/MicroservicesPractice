from flask import Blueprint, jsonify, make_response
from facades.decision_facade import DecisionFacade
from models.client_errors import ValidationError
from http import HTTPStatus

api_blueprint = Blueprint("api_view", __name__)
decision_facade = DecisionFacade()

# POST http://localhost:8002/api/decisions
@api_blueprint.route("/api/decisions", methods = ["POST"])
def make_decision():
    try:
        launch = decision_facade.launch_missile()
        json = jsonify({"launch": launch})
        return json
    except ValidationError as err:
        json = jsonify({"error": err.message})
        return make_response(json, HTTPStatus.BAD_REQUEST)