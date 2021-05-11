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
from asgn03 import supp_key_member_count


conn = Connect("dcris.txt")
supp_key_id = None

print("When supp_key id  = {}".format(supp_key_id))

rows = supp_key_member_count(conn, supp_key_id)

for row in rows:
    print(row)

conn.close()

