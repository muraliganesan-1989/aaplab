#!/usr/bin/env python3
"""Simple dynamic inventory for AAP lab - outputs Ansible JSON inventory."""
import json
import os

# In production, this would call AWS API, Azure API, or a CMDB
# For lab, we use environment variables or a config file
hosts = {
    "webservers": ["web1.lab.local", "web2.lab.local"],
    "appservers": ["app1.lab.local"],
    "databases": ["db1.lab.local"],
}

# Build Ansible inventory structure
inventory = {
    "_meta": {"hostvars": {}},
    "all": {"children": ["webservers", "appservers", "databases"]},
    "webservers": {"hosts": hosts["webservers"]},
    "appservers": {"hosts": hosts["appservers"]},
    "databases": {"hosts": hosts["databases"]},
}

# Add host vars (replace with your IPs)
ip_map = {
    "web1.lab.local": "10.0.8.164",
    "web2.lab.local": "192.168.1.21",
    "app1.lab.local": "192.168.1.22",
    "db1.lab.local": "192.168.1.23",
}
for h in sum(hosts.values(), []):
    inventory["_meta"]["hostvars"][h] = {"ansible_host": ip_map.get(h, h)}

print(json.dumps(inventory, indent=2))
