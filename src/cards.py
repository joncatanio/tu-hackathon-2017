# File: cards.py
# Author: Jon Catanio
# Description: API to pull relevant data from cards table.

from pymysql import MySQLError
from flask import Blueprint, request
import connection
import json

cards_api = Blueprint('cards_api', __name__)

@cards_api.route("/cards/<user_id>")
def get_user_cards(user_id):
   merchant_url = request.headers['Merchant_Url'] \
      if 'Merchant_Url' in request.headers else None

   try:
      with connection.mysql_conn.cursor() as cur:
         sql = '''
            SELECT
               id,
               user_id,
               balance,
               credit_limit,
               type,
               name,
               benefit_type,
               multiplier,
               quarter_mult,
               quarter_type
            FROM
               Cards
            WHERE
               user_id = %s
         '''

         cur.execute(sql, [user_id])
         records = cur.fetchall()
         cards = []

         for record in records:
            card = {}
            card['id'] = record['id']
            card['user_id'] = record['user_id']
            card['balance'] = str(record['balance'])
            card['credit_limit'] = str(record['credit_limit'])
            card['usage'] = round(float(str(record['balance'])) / \
               -float(str(record['credit_limit'])) * 100, 2)
            card['type'] = record['type']
            card['name'] = record['name']
            card['benefit_type'] = record['benefit_type']
            card['multiplier'] = record['multiplier']
            card['quarter_mult'] = record['quarter_mult']
            card['quarter_type'] = record['quarter_type']

            # Annoying negation thing...
            card['usage'] = 0.00 if card['usage'] == 0 else card['usage']

            cards.append(card)

         if merchant_url:
            return get_ranked_cards(cards, merchant_url)
         else:
            return json.dumps(cards), 200

   except MySQLError as err:
      print(err)
      return json.dumps({}), 500

def get_ranked_cards(cards, merchant_url):
   try:
      with connection.mysql_conn.cursor() as cur:
         sql = '''
            SELECT merchant_type
            FROM Merchants
            WHERE base_url = %s
         '''

         cur.execute(sql, [merchant_url])
         result = cur.fetchone()

         if not result:
            return json.dumps({}), 404
         merchant_type = result['merchant_type']

         result = []
         rank = 1
         print("CARDS", cards, "TYPE", merchant_type)
         type_cards = [c for c in cards if c['benefit_type'] in
            ['quarterly', 'miles'] and c['quarter_type'] == merchant_type]
         print("TYPE CARDS", type_cards)
         type_cards.sort(key=lambda x: (x['quarter_mult'], x['usage']))

         for type_card in type_cards:
            result.append({
               'rank': rank,
               'card_name': type_card['name'],
               'card_usage': type_card['usage'],
               'percent_savings': type_card['quarter_mult'] * 100,
               'message': 'This card has benefits that apply to the elements in your cart!'
            })

            rank = rank + 1

         remaining = [e for e in cards+type_cards if (e not in cards) or (e not in type_cards)]
         for card in remaining:
            result.append({
               'rank': rank,
               'card_name': card['name'],
               'card_usage': card['usage'],
               'percent_savings': card['multiplier'] * 100,
               'message': 'You might want to utilize this card more' if \
                  card['usage'] < 30.00 else 'The usage on this card is a bit high, maybe consider other options!'
            })

         return json.dumps(result), 200
   except MySQLError as err:
      print(err)
      return json.dumps({}), 500
