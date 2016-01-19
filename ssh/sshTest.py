#!/usr/bin/env python
import paramiko, threading, time
import sys

def ssh_cmd(ip, username, password, cmd):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, 22, username, password, timeout=5)
        if(ssh._transport is None):
            print(' connect is null')
            sys.exit(0)
        for i in cmd:
            stdin, stdout, stderr = ssh.exec_command("ls -l")
            out = stderr.readlines()
            print(out[0])
            sys.exit(0)
            # for line in stdout.readlines():
            #     print line
            # for lines in stderr.readlines():
            #     print lines
        ssh.close()
        print "%s connect OK!" % ip
    except:
        print '%s\tError\n' % ip


def main():
    print "Begin......"
    # Device_Infos = [{'IP': '192.168.0.1', 'user': 'backup', 'password': 'Br1sjhhrhl!', 'models': 'E1600'},
    #                 {'IP': '10.30.1.254', 'user': 'backup', 'password': 'Br1sjhhrhl!', 'models': 'E1700'}]
    # Device_Info1 = [{'IP': '192.168.1.108', 'user': 'root', 'password': '123456'},
    #                 {'IP': '192.168.1.194', 'user': 'root', 'password': 'root123'}]
    Device_Info = [{'IP': '192.168.0.1', 'user': 'backup', 'password': 'Br1sjhhrhl!', 'models': 'E1600'}]
    FTP_Info = {'IP': '192.168.1.106', 'user': 'backup', 'password': 'Br1sjhhrhl!'}
    for d in Device_Info:
        file_name = 'config_' + d['models'] + "_" + time.strftime("%Y%m%d%H%M%S", time.localtime())
        export_cmd = "export configuration startup to ftp server %s user %s password %s %s" % (FTP_Info['IP'], FTP_Info['user'], FTP_Info['password'], file_name)
        export_cmd = 'ls -l'
        cmd = [export_cmd]
        print(d['IP'])
        sys.exit(0)
        a = threading.Thread(target=ssh_cmd, args=(d['IP'], d['user'], d['password'], cmd))
        a.start()


if __name__ == '__main__':
    main()