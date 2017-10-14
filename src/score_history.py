# File: score_history.py
# Author: Jon Catanio
# Description: API endpoints to interact with a user's credit score history

from pymysql import MySQLError
from flask import Blueprint, request
import connection
import json

score_history_api = Blueprint('score_history_api', __name__)

@score_history_api.route("/scorehistory/<user_id>")
def get_score_history(user_id):
   try:
      with connection.mysql_conn.cursor() as cur:
         sql = '''
            SELECT id, score, archive_date, move_reason
            FROM ScoreHistory
            WHERE user_id = %s
         '''

         cur.execute(sql, [user_id])
         records = cur.fetchall()
         histories = []

         for record in records:
            history = {}
            history['id'] = record['id']
            history['score'] = record['score']
            history['archive_date'] = record['archive_date'].isoformat()
            history['move_reason'] = record['move_reason']

            histories.append(history)

         return json.dumps(histories), 200
   except MySQLError as err:
      print(err)
      return json.dumps({}), 500
