import pandas.io.sql
import pyodbc
import pandas as pd
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
server = 'tcp:LHTU05CG84218GH' 
database = 'mydb' 
username = 'pyuser' 
password = 'pyuser123' 
cnxn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

df= pandas.io.sql.read_sql('SELECT * from sys.sysobjects;', cnxn)
print(df.head(5))
#Sample select query
#cursor.execute("SELECT * from sys.sysobjects;") 
#row = cursor.fetchall() 
#while row: 
    #print(row[0])
    #row = cursor.fetchall()