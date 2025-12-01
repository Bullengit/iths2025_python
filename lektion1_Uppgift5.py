Scanned_hosts = 50
found_vulnerable = 8

vulnerable_machines = found_vulnerable / Scanned_hosts * 100

print(vulnerable_machines > 10 )
print (f"{vulnerable_machines:g}% of the scanned hosts were vulnerable")
