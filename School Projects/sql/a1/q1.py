"""
-------------------------------------------------------
Provides Python mysql.connector connection to a database.
-------------------------------------------------------
Author:  Andrew Liutiev
ID:      180635320
Email:   liut5320@wlu.ca
__updated__ = "2020-02-05"
-------------------------------------------------------
"""


from asgn01 import keyword_table

from Connect import Connect

tunnel = Connect("dcris.txt")

rs = keyword_table(tunnel) 



for r in rs:

    print(r)


tunnel = Connect("dcris.txt")

rows = keyword_table(tunnel,keyword_id= 35) 

print("----------------------------------------")

for r in rs:
    print(r)







