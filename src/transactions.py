# File: transactions.py
# Author: Jon Catanio
# Description: API endpoints for the transactions page in TU Hub

from pymysql import MySQLError
from flask import Blueprint, request
import connection
import json

transaction_api = Blueprint('transaction_api', __name__)

@transaction_api.route('/transactions/<user_id>')
def get_transactions(user_id):
   try:
      with connection.mysql_conn.cursor() as cur:
         sql = '''
            SELECT
               T.amount AS amount,
               T.merchant AS merchant,
               T.timestamp AS timestamp,
               C.name AS card_name
            FROM
               Transactions AS T
               JOIN Cards AS C ON T.card_id = C.id
            WHERE
               T.user_id = %s
         '''

         cur.execute(sql, [user_id])
         records = cur.fetchall()
         transactions = []

         for record in records:
            print(record)
            transaction = {}
            transaction['amount']    = str(record['amount'])
            transaction['merchant']  = record['merchant']
            transaction['timestamp'] = record['timestamp'].isoformat()
            transaction['card_name'] = record['card_name']

            transactions.append(transaction)

         return json.dumps(transactions), 200
   except MySQLError as err:
      print(err)
      return json.dumps({}), 500
