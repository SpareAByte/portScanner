import socket
import subprocess
import sys
from datetime import datetime

remote_server = input('Enter host to be scanned: ')
range_search = input('\n(1.) Single port\n(2.) Custom port range\n(3.) All the ports.')

if range_search == 1:
    user_range = input('Enter a single port (1 - 65,535): ')
elif range_search == 2:
    

remote_server_ip = socket.gethostbyname(remote_server)

print('\n\n' + '_'*60 + '\n')
print(f'Scanning: {remote_server_ip}')
print('_'*60 + '\n')

t1 = datetime.now()

try:
    for port in range(1, 10):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remote_server_ip, port))
        service = getser
        if result == 0:
            print(f'Port {port}: open')
        sock.close()
        
except KeyboardInterrupt:
    print('Exiting....')
    sys.exit()
    
except socket.gaierror:
    print('Host could not be resolved, exiting...')
    sys.exit()
    
except socket.error:
    print('Could not connect to server, exiting...')
    sys.exit()
    
t2 = datetime.now()
total = t2 - t1
    
print(f'Scan completed in: {total}')

