"""
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
Term:    Winter 2020
__updated__ = "2020-03-23"
-------------------------------------------------------
"""
# Imports
from configparser import ConfigParser

from sshtunnel import SSHTunnelForwarder


class Tunnel:
    """
    -------------------------------------------------------
    Defines SSH Tunnel for use with Laurier wireless connections.
    Laurier allows ssh connections to hopper, but not to any
    other ports. Tunnelling allows ssh port to act as proxy
    for any other port on hopper.
    Requires option file of the form:

[ssh]
ssh_address_or_host = hopper.wlu.ca
ssh_username = Laurier network name
ssh_password = Laurier network password
remote_bind_address = hopper.wlu.ca
remote_port = 3306
    -------------------------------------------------------
    """
    tunnel = None

    def __init__(self, option_file):
        try:
            # Read the contents of the option file
            config = ConfigParser()
            config.read_file(open(option_file))
            # Extract the ssh section into a dictionary
            params = dict(config['ssh'])
            params['remote_bind_address'] = (
                params['remote_bind_address'], int(params['remote_port']))
            # Remove the remote_port entry
            del params['remote_port']
            # Create the tunnel
            self.tunnel = SSHTunnelForwarder(**params)
            self.tunnel.start()
        except BaseException as e:
            print(str(e))
