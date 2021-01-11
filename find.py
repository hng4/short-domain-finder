import re
from dns.resolver import Resolver, NXDOMAIN, NoNameservers, Timeout, NoAnswer
from dns.resolver import *

FILE="list.txt"
TLD="gy"

with open(FILE) as f:
    content = f.readlines()
    content = [x.strip() for x in content] 
    for i in content:
        domain = i+"."+TLD
        try:
            host_record = dns.resolver.query(domain, "soa")
        except NXDOMAIN:
            file_object = open('results.txt', 'a+')
            file_object.write(domain+"\n")
            file_object.close()
            print(domain+" - NXDOMAIN")
        except NoNameservers:
            print(domain+" - NoNameservers")
        except Timeout:
            print(domain+" - Timeout")
        except NameError as error:
            print(domain+" - NameError")
        except NoAnswer:
            print(domain+" - NoAnswer")
