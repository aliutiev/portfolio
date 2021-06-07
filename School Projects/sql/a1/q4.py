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
from Connect import Connect
from asgn01 import expertise



tunnel = Connect("dcris.txt")
cols = expertise(tunnel) 






for col in cols:
    print(col)

    

tunnel = Connect("dcris.txt")
cols = expertise(tunnel,supp_key= 112) 


print("----------------------------------------supp")



for col in cols:
    print(col)







tunnel = Connect("dcris.txt")
cols = expertise(tunnel,keyword = 9) 
print("----------------------------------------Key")



for col in cols:
    print(col)

 





tunnel = Connect("dcris.txt")

cols = expertise(tunnel,supp_key= 112, keyword= 9 ) 
print("----------------------------------------supp & KEY")

for col in cols:

    print(col)

    
