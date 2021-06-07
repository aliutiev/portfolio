"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author: Andrew Liutiev
ID:    180635320
Email:    liut5320@mylaurier.ca
__updated__ = "2018-09-17"
-------------------------------------------------------
"""

from Connect import Connect
from asgn04 import column_info

conn = Connect("dcris.txt")
table_schema = "dcris"
table_name = 'member'

print("When table name = {}".format(table_name))

rows = column_info(conn, table_schema, table_name)

for row in rows:
    print(row)

conn.close()

