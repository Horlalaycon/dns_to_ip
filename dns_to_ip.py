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
        print(f"""+==================================
|    
|   Result:
+----------------------------------
|        Host: {hostname}
+----------------------------------
|        Ip-addr: {ip_addr}
+==================================
""")

    except socket.gaierror:
        print(r"""|
+==================================
|    Error!: Connection Error 
+==================================
""")

# CLI Options
parser = argparse.ArgumentParser(prog="Dns-To-Ip",
                                 description="Domain name to ip address converter")
parser.add_argument("-d", "--host", help="Specify Target's Domain name", required=True)
args = parser.parse_args()

host = args.host

if __name__ == "__main__":
    # banner
    print("\n+==================================")
    print("|   *****(DNS-TO-IP)*****")
    print("+----------------------------------")
    print("|   By: sys_br3ach3r")

    convert_to_ip(hostname=str(host))
