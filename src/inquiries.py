# File: inquiries.py
# Author: Jon Catanio
# Description: API endpoints to interact with user inquiries

from pymysql import MySQLError
from flask import Blueprint, request
import connection
import json

inquiries_api = Blueprint('inquiries_api', __name__)

@inquiries_api.route("/inquiries/<user_id>")
def get_inquiries(user_id):
   try:
      with connection.mysql_conn.cursor() as cur:
         sql = '''
            SELECT id, text, inq_type, date
            FROM Inquiries
            WHERE user_id = %s
         '''

         cur.execute(sql, [user_id])
         records = cur.fetchall()
         inquiries = []

         for record in records:
            inquiry = {}
            inquiry['id'] = record['id']
            inquiry['text'] = record['text']
            inquiry['type'] = record['inq_type']
            inquiry['date'] = record['date'].isoformat()

            inquiries.append(inquiry)

         return json.dumps(inquiries), 200
   except MySQLError as err:
      print(err)
      return json.dumps({}), 500
