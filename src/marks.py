# File: marks.py
# Author: Jon Catanio
# Description: API endpoints to interact with user derogatory marks

from pymysql import MySQLError
from flask import Blueprint, request
import connection
import json

marks_api = Blueprint('marks_api', __name__)

@marks_api.route("/marks/<user_id>")
def get_marks(user_id):
   try:
      with connection.mysql_conn.cursor() as cur:
         sql = '''
            SELECT id, received, expires, description
            FROM Marks
            WHERE user_id = %s
         '''

         cur.execute(sql, [user_id])
         records = cur.fetchall()
         marks = []

         for record in records:
            mark = {}
            mark['id'] = record['id']
            mark['date_received'] = record['received'].isoformat()
            mark['date_expires'] = record['expires'].isoformat()
            mark['description'] = record['description']

            marks.append(mark)

         return json.dumps(marks), 200
   except MySQLError as err:
      print(err)
      return json.dumps({}), 500
