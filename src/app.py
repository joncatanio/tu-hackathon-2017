# File: app.py
# Author: Jon Catanio
# Description: Main Flask driver

from flask import Flask
import connection as conn

# Import blueprints
from welcome import welcome_api

app = Flask(__name__)

# Register blueprints
app.register_blueprint(welcome_api)

@app.route("/")
def main():
   return "TU Hub", 200

if __name__ == "__main__":
   app.debug = True
   conn.init_connection()
   app.run()
