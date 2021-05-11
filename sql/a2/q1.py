"""
-------------------------------------------------------
q1.py
[¯\_(ツ)_/¯ ¯\_(ツ)_/¯ ¯\_(ツ)_/¯ ¯\_(ツ)_/¯ ¯\_(ツ)_/¯]
-------------------------------------------------------
Author:  Andrew Liutiev
ID:      180635320    
Email:   liut5320@mylaurier.ca 
updated = "2020-03-10"
-------------------------------------------------------
"""

from Connect import Connect

from asgn02 import publications

the_connector_tunnel = Connect("dcris.txt")


print("When title = the and pub_type_id = a")

the_rows_of_rows = publications(the_connector_tunnel, title="the", pub_type_id="b")

for the_rows_in_rows in the_rows_of_rows:


    print(the_rows_in_rows)
    

the_connector_tunnel.close()