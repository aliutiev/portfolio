"""
from asgn01 import keyword_table
from Connect import Connect
the_tunnel = Connect("dcris.txt")
rs = keyword_table(the_tunnel) 

for r in rs:
    print(r)
the_tunnel = Connect("dcris.txt")
rows = keyword_table(the_tunnel,keyword_id= 35) 
for r in rs:
    print(r)


