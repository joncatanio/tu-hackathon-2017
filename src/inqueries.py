# File: inqueries.py
# Author: Jon Catanio
# Description: API endpoints to interact with user inqueries

from pymysql import MySQLError
from flask import Blueprint, request
import connection
import json

inqueries_api = Blueprint('inqueries_api', __name__)

@inqueries_api.route("/inqueries/<user_id>")
def get_inqueries(user_id):
   try:
      with connection.mysql_conn.cursor() as cur:
         sql = '''
            SELECT id, text, inq_type, date
            FROM Inqueries
            WHERE user_id = %s
         '''

         cur.execute(sql, [user_id])
         records = cur.fetchall()
         inqueries = []

         for record in records:
            inquery = {}
            inquery['id'] = record['id']
            inquery['text'] = record['text']
            inquery['type'] = record['inq_type']
            inquery['date'] = record['date'].isoformat()

            inqueries.append(inquery)

         return json.dumps(inqueries), 200
   except MySQLError as err:
      print(err)
      return json.dumps({}), 500
