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
from asgn04 import foreign_key_info

conn = Connect("dcris.txt")
constraint_schema = "dcris"
table_name = "member_keyword"
ref_table_name = None

print("When table name & ref table name = {}, {}".format(table_name, ref_table_name))

rows = foreign_key_info(conn, constraint_schema, table_name, ref_table_name)

for row in rows:
    print(row)

conn.close()

