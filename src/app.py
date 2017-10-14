# File: app.py
# Author: Jon Catanio
# Description: Main Flask driver

from flask import Flask
import connection as conn

# Import blueprints
from welcome import welcome_api
from transactions import transaction_api
from cards import cards_api

app = Flask(__name__)

# Register blueprints
app.register_blueprint(welcome_api)
app.register_blueprint(transaction_api)
app.register_blueprint(cards_api)

@app.route("/")
def main():
   return "TU Hub", 200

if __name__ == "__main__":
   app.debug = True
   conn.init_connection()
   app.run(host='0.0.0.0', port=80)
