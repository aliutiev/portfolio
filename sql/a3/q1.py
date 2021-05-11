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
from asgn03 import pub_counts_all


conn = Connect("dcris.txt")
member_id = None

print("When member id  = {}".format(member_id))

rows = pub_counts_all(conn, member_id)

for row in rows:
    print(row)

conn.close()

