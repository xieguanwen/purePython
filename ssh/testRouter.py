#!/usr/bin/python
from paramiko import SSHClient,AutoAddPolicy

try:
    client = SSHClient()
    client.set_missing_host_key_policy(AutoAddPolicy())
    client.connect('192.168.1.180',username='root', password='Br1sjhhrhl!',port=22)
    stdin, stdout, stderr = client.exec_command('show zone')
    print(stdout)
except Exception:
    print(Exception.message)

