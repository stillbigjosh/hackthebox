#!/usr/bin/env python

import pymysql
from craft_api import settings

# test connection to mysql database

connection = pymysql.connect(host=settings.MYSQL_DATABASE_HOST,
                             user=settings.MYSQL_DATABASE_USER,
                             password=settings.MYSQL_DATABASE_PASSWORD,
                             db=settings.MYSQL_DATABASE_DB,
                             cursorclass=pymysql.cursors.DictCursor)
cmd = ''
while cmd != 'st0p':
    cmd=input("SQL: ")
    try:
        with connection.cursor() as cursor:
            sql = cmd
            cursor.execute(sql)
            result = cursor.fetchall()
            print(result)

    finally:
        print('__)')
