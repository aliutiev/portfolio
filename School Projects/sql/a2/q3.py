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
from asgn04 import constraint_info

conn = Connect("dcris.txt")
table_schema = "dcris"
constraint_type = None

print("When constraint type = {}".format(constraint_type))

rows = constraint_info(conn, table_schema, constraint_type)

for row in rows:
    print(row)

conn.close()

