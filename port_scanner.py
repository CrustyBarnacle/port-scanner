#!/usr/bin/env python3
import socket

def get_open_ports(target, port_range, verbose = False):
    open_ports = []

    # validate URL or IP address, else return "Error: Invalid hostname" or "Error: Invalid IP address"
    if valid_input(target): # or URL
        # scan target:port-range
        scan_ports(target, port_range)
    else:
        return "Error: Invalid IP address"

    # return confirmed open ports
    # if `verbose = True`, the function should return a descriptive string with each port.
    return generate_report(target, open_ports, verbose)


def valid_input(host):
    try:
        socket.inet_aton(host)
        return True
    except socket.error:
        return False


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


def generate_report(host, open_ports, verbose):
    port_report = {key: ports_and_services[key] for key in open_ports}

    if verbose:
        # print Header row with {URL} OR {IP address}
        print (f'Open ports for {host}\nPORT\tSERVICE')
        # for port:'service' in port_report

        # print as per:
        # PORT     SERVICE
        # {port}   {service name}
        # {port}   {service name}

    else:
        return port_report