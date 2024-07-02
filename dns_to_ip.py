import socket
import argparse


def convert_to_ip(hostname):
    try:
        # create socket obj
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # set connection timeout
        sock.settimeout(1)
        # convert domain name to ip
        ip_addr = socket.gethostbyname(hostname)
        # display the result
        print(f"""
===========================================
|~| Host    |=|> {hostname}
-------------------------------------------
|~| Ip-addr |=|> {ip_addr}
===========================================
""")
    except socket.gaierror:
        print(r"""
================================
|| Error! |> Connection Error ||
================================
""")


banner = r"""
----------------------------------------------------------------
|-|----------------------------------------------------------|-|
[~|        ____                 ______            ________   |~]
|~]       / __ \____  _____    /_  __/___        /  _/ __ \  [~|
[~|      / / / / __ \/ ___/_____/ / / __ \______ / // /_/ /  |~]
|~]     / /_/ / / / (__  )_____/ / / /_/ /_____// // ____/   [~|
[~|    /_____/_/ /_/____/     /_/  \____/     /___/_/        |~]
|-|----------------------------------------------------------|-| 
|~]  Domain name to ip address convert                       |~]
|-|----------------------------------------------------------|-|
[~|     Created by: Ibrahim Ajimati                          [~|
|-|----------------------------------------------------------|-| 
[~|                 A.K.A f3ar_0f_th3_unkn0wn @github        |~]
----------------------------------------------------------------                                                 
                          +---------+         -----
                         +-----------+        |   |
                        +-------------+       -----
=================================================================
=================================================================
"""

print(banner)

parser = argparse.ArgumentParser(prog="Dns-To-Ip",
                                 description="Domain name to ip address converter")
parser.add_argument("-d", "--host", help="Host name ", required=True)
args = parser.parse_args()

host = args.host

if __name__ == "__main__":
    convert_to_ip(hostname=str(host))
