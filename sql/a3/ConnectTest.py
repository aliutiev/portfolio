"""
-------------------------------------------------------
Connect Test
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2020-03-23"
-------------------------------------------------------
"""
# Imports
from Connect import Connect
from Tunnel import Tunnel


def test_connect_tunnel():
    print("SSH Tunnel Connection")

    try:
        tunnel = Tunnel("hopper.txt")

        with tunnel.tunnel:
            # Connect to the DCRIS database with an option file
            conn = Connect("dcris.txt", tunnel.tunnel.local_bind_port)
            # Define a SQL query
            sql = "SELECT * FROM keyword"
            # Execute the query from the connection cursor
            conn.cursor.execute(sql)
            # Print the column names from the query result
            print("Columns:")
            print(conn.cursor.column_names)
            # Get and print the contents of the query results (raw results)
            print("Data:")
            rows = conn.cursor.fetchall()

            for row in rows:
                print(row)
            # Close the Connect object
            conn.close()
    except BaseException as e:
        print(str(e))


# Test both connections
# test_connect()
print("-" * 80)
test_connect_tunnel()
