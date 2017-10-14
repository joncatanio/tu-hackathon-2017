# File: connection.py
# Author: Jon Catanio
# Description: Simple and inefficient global db connection

import pymysql
from pymongo import MongoClient

def init_connection():
   global mysql_conn
   mysql_conn = pymysql.connect(host='localhost',
                                user='tu-hacker',
                                password='tu-hackathon-pw',
                                db='TU2017',
                                cursorclass=pymysql.cursors.SSDictCursor,
                                charset='utf8')

   global mongo_data
   user="hackee"
   password="password1"
   host="54.193.64.159"
   client = MongoClient("mongodb://" + user + ":"
      + password + "@" + host + ":27017/hackathon")
   mongo_data = client.hackathon.creditfit
   #cursor = mongo_data.find()
