# File: welcome.py
# Author: Jon Catanio
# Description: API endpoints for the welcome splash page

from pymysql import MySQLError
from flask import Blueprint, request
import connection
import json

welcome_api = Blueprint('welcome_api', __name__)

@welcome_api.route('/welcome/<user_id>')
def welcome(user_id):
   try:
      doc = connection.mongo_data.find_one({ 'UID': int(user_id)})
      user = { 'name': doc['GivenName'] + " " + doc['Surname'] }

      return json.dumps(user), 200
   except Exception:
      return {}, 404
