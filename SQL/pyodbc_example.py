import pyodbc
from configparser import ConfigParser
import os


########################################################
parser = ConfigParser()
parser.read(r'..\setup\user.ini')
database = parser.get('DBdetails', 'database')[1:-1]
username = parser.get('DBdetails', 'usr')[1:-1]
server = parser.get('DBdetails', 'server')[1:-1]
print('Type in password')
password = input()
driver= '{ODBC Driver 13 for SQL Server}'

with pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
    with conn.cursor() as cursor:
        cursor.execute("SELECT TOP 3 name, collation_name FROM sys.databases")
        row = cursor.fetchone()
        while row:
            print (str(row[0]) + " " + str(row[1]))
            row = cursor.fetchone()
