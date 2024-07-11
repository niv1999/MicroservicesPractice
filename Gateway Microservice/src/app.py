from fastapi import FastAPI
from fastapi.responses import JSONResponse
from requests import post # pip install requests
from http import HTTPStatus
from .utils.app_config import AppConfig

# Running on port 8000:
# uvicorn src.app:server --reload

# Running on port 4000:
# uvicorn src.app:server --reload --port 4000

server = FastAPI()

# POST http://localhosts:8000/api/attacks
@server.post("/api/attacks")
def attack_detected(body: dict): # the body type is a dictionary
    try:
        # Make request to Radar Microservice
        response = post(AppConfig.attacks_url, json = body)

        # Response back the result:
        return JSONResponse(content = response.json(), status_code = response.status_code)
    
    except Exception as err:
        json = {"error": str(err)}
        return JSONResponse(content = json, status_code = HTTPStatus.INTERNAL_SERVER_ERROR)
    

# POST http://localhosts:8000/api/decisions
@server.post("/api/decisions")
def make_decision(body: dict): # the body type is a dictionary
    try:
        # Make request to Radar Microservice
        response = post(AppConfig.decisions_url, json = body)

        # Response back the result:
        return JSONResponse(content = response.json(), status_code = response.status_code)
    
    except Exception as err:
        json = {"error": str(err)}
        return JSONResponse(content = json, status_code = HTTPStatus.INTERNAL_SERVER_ERROR)
    
# POST http://localhosts:8000/api/intercept
@server.post("/api/intercept")
def intercept_attack(body: dict): # the body type is a dictionary
    try:
        # Make request to Radar Microservice
        response = post(AppConfig.intercept_url, json = body)

        # Response back the result:
        return JSONResponse(content = response.json(), status_code = response.status_code)
    
    except Exception as err:
        json = {"error": str(err)}
        return JSONResponse(content = json, status_code = HTTPStatus.INTERNAL_SERVER_ERROR)