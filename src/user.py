# File: user.py
# Author: Jon Catanio
# Description: API endpoints returning information for a given user

from pymysql import MySQLError
from flask import Blueprint, request
import connection
import json
import pprint

user_api = Blueprint('user_api', __name__)

@user_api.route("/user/<user_id>")
def get_user(user_id):
   try:
      doc = connection.mongo_data.find_one({ 'UID': int(user_id)})
      user = {
         'fullname': doc['GivenName'] + " " + doc['Surname'],
         'age': doc['Age'],
         'city': doc['City'],
         'email': doc['EmailAddress'],
         'state': doc['State'],
         'street_address': doc['StreetAddress'],
         'phone': doc['TelephoneNumber'],
         'title': doc['Title'],
         'zipcode': doc['ZipCode']
      }

      pprint.pprint(doc)

      return json.dumps(user), 200
   except Exception:
      return {}, 404
