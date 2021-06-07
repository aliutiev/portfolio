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


from asgn01 import member_expertise

from Connect import Connect



tunnel = Connect("dcris.txt")


cols = member_expertise(tunnel) 


for c in cols:

    print(c)

    

tunnel = Connect("dcris.txt")

cols = member_expertise(tunnel,member_id= 111) 

print("----------------------------------------Member_id")

for c in cols:

    print(c)







tunnel = Connect("dcris.txt")
cols = member_expertise(tunnel,keyword_id = 18) 
print("----------------------------------------Key")



for c in cols:
    print(c)

 



tunnel = Connect("dcris.txt")

cols = member_expertise(tunnel,member_id= 111, keyword_id= 18 ) 
print("----------------------------------------MEMBER & KEY")



for c in cols:

    print(c)

    
