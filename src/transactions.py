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

@transaction_api.route('/transactions/add', methods = ['POST'])
def add_transaction():
   req = request.get_json(True, True, False)
   if req == None:
      return json.dumps(response), 500

   try:
      with connection.mysql_conn.cursor() as cur:
         sql = '''
            INSERT INTO Transactions
               (user_id, card_id, amount, merchant, timestamp)
            VALUES
               (%s, %s, %s, %s, NOW())
         '''
         cur.execute(sql, [req['user_id'], req['card_id'],
            req['amount'], req['merchant']])

         sql = '''
            UPDATE Cards
            SET balance = balance + %s
            WHERE id = %s
         '''
         cur.execute(sql, [req['amount'], req['card_id']])

         sql = '''
            SELECT balance, credit_limit, name
            FROM Cards
            WHERE id = %s
         '''
         cur.execute(sql, [req['card_id']])
         record = cur.fetchone()
         cur.fetchall()

         if not record:
            return json.dumps({}), 500

         usage = float(record['balance']) / float(record['credit_limit']) * 100

         if usage > 30.0:
            sql = '''
               INSERT INTO Notifications
                  (user_id, text, timestamp, has_read)
               VALUES
                  (%s, %s, NOW(), FALSE)
            '''
            long_notification = record['name'] + ' exceeds 30% usage at ' + str(round(usage,2)) + '%'
            short_notification = '30% usage exceeded'
            cur.execute(sql, [req['user_id'], short_notification])

         connection.mysql_conn.commit()

         return json.dumps({}), 200
   except MySQLError as err:
      print(err)
      return json.dumps({}), 500
