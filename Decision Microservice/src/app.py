from flask import Flask
from views.api_view import api_blueprint

# flask --app src/app.py run --debug --port 8002

app = Flask(__name__)

app.register_blueprint(api_blueprint)

print("Listening on http://localhost:8002")