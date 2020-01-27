#!/usr/bin/env python

from ipaddress import ip_address, IPv4Address, IPv6Address
class Solution:
    def validIPAddress(self, IP: str) -> str:
        if '::' in IP:
            return "Neither"
        try:
            t = ip_address(IP)
            if type(t) == IPv4Address:
                ips = IP.split('.')
                for ip in ips:
                    if len(ip) > 1 and ip[0] == '0':
                        return "Neither"
                return "IPv4"
            elif type(t) == IPv6Address:
                return "IPv6"
            else:
                return "Neither"
        except:
            return "Neither"