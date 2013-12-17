#
# Sumukha TV sumukhatv@outlook.com
#
import paramiko
import sys

class RemoteFileTranfer:
    """Creates a connection to a remote machine and transfers the required file from local machine to the remote machine for testing"""
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
#            print "Connection could not be established"
            return 1
        
    
    def upload(self, remotePath, localPath):
        self.hostPath = remotePath
        self.clientPath = localPath
        try:
           self.sftp = self.client.open_sftp()
           self.sftp.put(self.clientPath, self.hostPath)
           return 0
        except:
#           print "Upload failed"
#           print sys.exc_info()
            return 2


