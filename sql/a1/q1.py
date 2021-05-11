"""-------------------------------------------------------Provides Python mysql.connector connection to a database.-------------------------------------------------------Author:  Andrew LiutievID:      180635320Email:   liut5320@wlu.ca__updated__ = "2020-02-05"-------------------------------------------------------"""
from asgn01 import keyword_table
from Connect import Connect
the_tunnel = Connect("dcris.txt")
rs = keyword_table(the_tunnel) 

for r in rs:
    print(r)
the_tunnel = Connect("dcris.txt")
rows = keyword_table(the_tunnel,keyword_id= 35) print("----------------------------------------")
for r in rs:
    print(r)



