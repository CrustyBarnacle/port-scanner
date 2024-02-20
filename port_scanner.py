#!/usr/bin/env python3
import socket

def get_open_ports(target, port_range, verbose = False):
    open_ports = []

    # validate URL or IP address, else return "Error: Invalid hostname" or "Error: Invalid IP address"
    
    # validate port range, else exception (not required/expected in assignment)

    # scan target:port-range
    scan_ports(host, ports)

    # return confirmed open ports
    # if `verbose = True`, the function should return a descriptive string with each port.
    return
    
    generate_report(open_ports, verbose)


def scan_ports(host, ports):
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


def generate_report(open_ports, verbose):
    port_report = {key: ports_and_services[key] for key in open_ports}
    # print Header row with {URL} OR {IP address}
    print (f'Open ports for {target}\nPORT\tSERVICE')
    # for port:'service' in port_report

    # print as per:
    # PORT     SERVICE
    # {port}   {service name}
    # {port}   {service name}