# File: notifications.py
# Author: Jon Catanio
# Description: API endpoints to get notifications

from pymysql import MySQLError
from flask import Blueprint, request
import connection
import json

notifications_api = Blueprint('notifications_api', __name__)

@notifications_api.route("/notifications/<user_id>")
def get_notifications(user_id):
   try:
      with connection.mysql_conn.cursor() as cur:
         sql = '''
            SELECT id, text
            FROM Notifications
            WHERE
               user_id = %s
               AND has_read = FALSE
         '''

         cur.execute(sql, [user_id])
         records = cur.fetchall()
         notifications = []

         for record in records:
            notification = {}
            notification['id'] = record['id']
            notification['notification_text'] = record['text']

            notifications.append(notification)

         return json.dumps(notifications), 200
   except MySQLError as err:
      print(err)
      return json.dumps({}), 500
