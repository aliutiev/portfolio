"""
from asgn01 import expertise

the_connector_tunnel = Connect("dcris.txt")
cols = expertise(the_connector_tunnel) 

for col in cols:
    print(col)
    
the_connector_tunnel = Connect("dcris.txt")
cols = expertise(the_connector_tunnel,supp_key= 112) 
print("----------------------------------------supp")
for col in cols:
    print(col)



the_connector_tunnel = Connect("dcris.txt")
cols = expertise(the_connector_tunnel,keyword = 9) 
print("----------------------------------------Key")
for col in cols:
    print(col)
 

the_connector_tunnel = Connect("dcris.txt")
cols = expertise(the_connector_tunnel,supp_key= 112, keyword= 9 ) 
print("----------------------------------------supp & KEY")
for col in cols:
    print(col)
    