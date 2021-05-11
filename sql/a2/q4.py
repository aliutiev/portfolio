"""
-------------------------------------------------------
q4.py
[¯\_(ツ)_/¯ ¯\_(ツ)_/¯ ¯\_(ツ)_/¯ ¯\_(ツ)_/¯ ¯\_(ツ)_/¯]
-------------------------------------------------------
Author:  Andrew Liutiev
ID:      180635320    
Email:   liut5320@mylaurier.ca 
updated = "2020-03-10"
-------------------------------------------------------
"""

from Connect import Connect



from asgn02 import all_expertise



the_connector_tunnel = Connect("dcris.txt")


the_rows_of_rows = all_expertise(the_connector_tunnel, member_id=74)



for the_rows_in_rows in the_rows_of_rows:

    print(the_rows_in_rows)


the_connector_tunnel.close()