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
from asgn03 import keyword_member_count


conn = Connect("dcris.txt")
keyword_id = None

print("When keyword id  = {}".format(keyword_id))

rows = keyword_member_count(conn, keyword_id)

for row in rows:
    print(row)

conn.close()

