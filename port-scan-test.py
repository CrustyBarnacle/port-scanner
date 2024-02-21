# echo-client.py

import socket
from common_ports import ports_and_services

def get_input():
    target = input('Enter the target IP or URL: ')
    try:
        socket.inet_aton(target)
        return target
    except socket.error:
        return "Error: Invalid IP address"

# host = get_input()
host = "137.74.187.104"  # Sever hostname or IP address
ports = [20, 450]  # Port range to connect to on the server
open_ports = []

# scan_ports(host, ports, verbose=False)
for port in range(ports[0], ports[1]):
    timeout = 2

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as connection:
        try:
            connection.settimeout((timeout))
            connection.connect((host, port))
            open_ports.append(port)

        except Exception as error:
            #print(f"Error for port {port}: {error}")
            pass

# generate_report(open_ports)
port_report = {key: ports_and_services[key] for key in open_ports}

print(f"Open ports:\n {port_report}")
