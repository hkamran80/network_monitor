"""
Network Connection Monitor
Contributors:
    :: H. Kamran [@hkamran80] (author)
Version: 1.0.0
Last Updated: 2020-07-22, @hkamran80
"""

import os
import json
import requests
import termcolor
import subprocess

CONFIG_FILE = "config.json"

def ping(server: str, packet_count: int, timeout: int):
    command = ["ping", "-c", str(packet_count), "-t", str(timeout), server]
    return subprocess.call(command, stdout=open(os.devnull, "wb"), stderr=subprocess.PIPE) == 0

def head_request(host: str, timeout: int):
    return requests.head(host, timeout=timeout).status_code

def public_ip_address(host: str, timeout: int, key: str):
    ip_request = requests.get(host, timeout=timeout)
    if ip_request.status_code != 200:
        return False

    return ip_request.json()[key]


if __name__ == "__main__":
    with open(CONFIG_FILE, "r") as config_file:
        config = json.loads(config_file.read())

    if config["public_ip"]["print"]:
        public_ip = public_ip_address(
            host=config["public_ip"]["server"],
            timeout=config["timeout"],
            key=config["public_ip"]["json_key"]
        )
        
        pipa_text = termcolor.colored("Public IP Address:", attrs=["bold"])
        print(f"{pipa_text} {public_ip}")
        print("="*(len(pipa_text) + len(public_ip) - 7))

    if config["head_requests"]:
        print(termcolor.colored("HEAD Requests", color="blue", attrs=["bold", "underline"]))
        for site_name in config["sites"]:
            request = head_request(
                host=config["sites"][site_name],
                timeout=config["timeout"]
            )
            request_message = termcolor.colored("Success" if request else "Unsuccessful", color=("green" if request else "red"))

            print(f"  - {site_name}: {request_message}")
        
        print()

    if config["ping_requests"]:
        print(termcolor.colored("Ping Requests", color="blue", attrs=["bold", "underline"]))
        for server_name in config["ping_servers"]:
            request = ping(
                server=config["ping_servers"][server_name],
                packet_count=config["packet_count"],
                timeout=config["timeout"]
            )
            request_message = termcolor.colored("Success" if request else "Unsuccessful", color=("green" if request else "red"))

            print(f"  - {server_name}: {request_message}")
        
        print()