# File: cards.py
# Author: Jon Catanio
# Description: API to pull relevant data from cards table.

from pymysql import MySQLError
from flask import Blueprint, request
import connection
import json

cards_api = Blueprint('cards_api', __name__)

@transaction_api.route("/cards/<user_id>")
def get_user_cards(user_id):
   print("hi")
