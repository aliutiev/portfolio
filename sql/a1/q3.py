"""
from asgn01 import member_expertise
from Connect import Connect

the_connector_tunnel = Connect("dcris.txt")
cols = member_expertise(the_connector_tunnel) 
for c in cols:
    print(c)
    
the_connector_tunnel = Connect("dcris.txt")
cols = member_expertise(the_connector_tunnel,member_id= 111) 
print("----------------------------------------Member_id")
for c in cols:
    print(c)



the_connector_tunnel = Connect("dcris.txt")
cols = member_expertise(the_connector_tunnel,keyword_id = 18) 
print("----------------------------------------Key")
for c in cols:
    print(c)
 

the_connector_tunnel = Connect("dcris.txt")
cols = member_expertise(the_connector_tunnel,member_id= 111, keyword_id= 18 ) 
print("----------------------------------------MEMBER & KEY")
for c in cols:
    print(c)
    