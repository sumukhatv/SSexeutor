#
# Sumukha TV sumukhatv@outlook.com
#

import paramiko
import sys

class RemoteSecureShell:
    """Creates a connection to a remote machine and executes commands"""
    def __init__(self, hName, uName, pWord):
        try:
            self.hostname = hName
            self.port = 22
            self.username = uName
            self.password = pWord
            paramiko.util.log_to_file('ssh.log') 
            self.client = paramiko.SSHClient()
            self.client.load_system_host_keys()
            self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.client.connect(hostname = self.hostname, port = self.port, username = self.username, password = self.password)
        except:
            print "Connection could not be established"
            sys.exit

    def executeCommand(self, command):
        stdin, stdout, stderr = self.client.exec_command(command)
        #print "stout = "+stdout.read()
        return [stdout.read(), stderr.read()]



