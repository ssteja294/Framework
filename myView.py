# Mysql Use of View 

import mysql.connector

DbConnection = mysql.connector.connect(host='138.68.140.83', user='saiteja', password='Saiteja@123', database='dbSaiteja')
DbCursor = DbConnection.cursor()
DbCursor.execute("DROP VIEW IF EXISTS FrameworkTable2")
DbCursor.execute("CREATE view FrameworkTable2 as SELECT * FROM Item")
DbCursor.execute("insert into FrameworkTable2 values('TV1397', 'Telivision', 29000, 'LG123', 100)")
DbCursor.execute("SELECT * from FrameworkTable2")
Items = DbCursor.fetchall()
for Item in Items:
	print(Item)

