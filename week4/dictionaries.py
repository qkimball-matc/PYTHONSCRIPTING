#!/usr/bin/env python3

# Task 1
servers = {"server1.testlab.com" : "192.168.1.10", "server2.testlab.com" : "192.168.1.11",
"server3.testlab.com" : "192.168.1.12", "server4.testlab.com" : "192.168.1.13",
"server5.testlab.com" : "192.168.1.14", "server6.testlab.com" : "192.168.1.15"}

print(servers)
print(type(servers))

# Task 2
print(f"\nAll of the FQND's in the servers dictionary are:")
for key in sorted(servers):
    print(f"{key}")

# Task 3
print(f"\nAll of the IP Addresses in the servers dictionary are:")
for key in sorted(servers):
    print(f"{servers[key]}")

# Task 4
print(f"\nThe full records of the servers dictionary are:")
for key in sorted(servers):
    print(f"{key, servers[key]}")

# Task 5
servers["server7.testlab.com"] = "192.168.1.16"
servers["server8.testlab.com"] = "192.168.1.17"

print(f"\nHere are the updated records of the servers dictionary:")
for key in sorted(servers):
    print(f"{key, servers[key]}")

# Task 6
print(f"\nT/F, server2.testlab.com is contained in the servers dictionary:")
print(f"server2.testlab.com" in servers)

# Task 7
print(f"\nT/F, server10.testlab.com is contained in the servers dictionary:")
print(f"server10.testlab.com" in servers)