"""
Understand:
    Goal:
        * Create a class that consume an ip address or range of address or has a default value range
        * Scans the designated ip address or range
            * returns:
                * if an IP address is active
                * the device it is assigned to
                * the device-related information such:
                    * as Operating System
                    * vendor
                    * MAC address
                      * description of the device

    Plan:
        + instantiate the class with:
            + ip address (optional)
            + ip address range (optional)
            + local subnet if you did not specify the IP range which you want to scan
"""


class IpScanner:
    ipaddress_data = {}

    #Todo: update these parameters
    def __init__(self):
        self.ip_address = None
        self.ip_range = None
        self.local_subnet = None

    def ping_ip(self):
        pass

    def scan_ip_address(self):
        pass
