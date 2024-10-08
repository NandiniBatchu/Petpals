import pyodbc
try:
    conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=Nandini;'
                      'Database=petpals;'
                      'Trusted_Connection=yes;')
    print("Connected Successfully")
except:
    print("Connection failed")