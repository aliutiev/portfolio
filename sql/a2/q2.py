"""
-------------------------------------------------------
q2.py
[¯\_(ツ)_/¯ ¯\_(ツ)_/¯ ¯\_(ツ)_/¯ ¯\_(ツ)_/¯ ¯\_(ツ)_/¯]
-------------------------------------------------------
Author:  Andrew Liutiev
ID:      180635320    
Email:   liut5320@mylaurier.ca 
updated = "2020-03-10"
-------------------------------------------------------
"""

from Connect import Connect


from asgn02 import pub_counts


the_connector_tunnel = Connect("dcris.txt")


oof = pub_counts(the_connector_tunnel, member_id=74, pub_type_id="b")

"""
[¯\_(ツ)_/¯ ¯\_(ツ)_/¯ ¯\_(ツ)_/¯ ¯\_(ツ)_/¯ ¯\_(ツ)_/¯]
"""

for the_rows_in_rows in oof:


    print(the_rows_in_rows)


the_connector_tunnel.close()