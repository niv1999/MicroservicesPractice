from fastapi import FastAPI
from fastapi.responses import JSONResponse
from http import HTTPStatus

# uvicorn src.app:server --reload --port 8003

server = FastAPI()

# POST http://localhosts:8003/api/intercept
@server.post("/api/intercept")
def intercept_attack(body: dict): # the body type is a dictionary
    try:

        print(body)

        json = {"intercept": True}

        # Response back the result:
        return JSONResponse(content = json, status_code = HTTPStatus.OK)
    
    except Exception as err:
        json = {"error": str(err)}
        return JSONResponse(content = json, status_code = HTTPStatus.INTERNAL_SERVER_ERROR)