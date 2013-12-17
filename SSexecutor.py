# Sumukha TV sumukhatv@outlook.com

import RemoteFileTransfer
import RemoteSecureShell

def testConnection(ipaddr, uName, pWord):
    try:
        paramiko.util.log_to_file('ssh.log')
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname = ipaddr, port = 22, username = uName, password = pWord)
        return 0
    except:
        return 1

def main(ipaddr, uName, pWord, locPath, fileExtn, compressionType = None, triggerFile = None):
    str = locPath
    str = str.split("\\")
    remPath = str.pop()
    
    rft = RemoteFileTransfer.RemoteFileTranfer(ipaddr, uName, pWord)
    code = rft.upload(remPath, locPath)
    if(code == 1):
        print "Connection could not be established"
        return 1
    if(code == 2):
        print "Upload failed"
        return 2
        
    if(compressionType != None):
        output = handleCompression(ipaddr, uName, pWord, remPath, fileExtn, compressionType, triggerFile)
        return output
    
    sshClient = RemoteSecureShell.RemoteSecureShell(ipaddr, uName, pWord)
    pgmLang = fileExtn
    if(pgmLang == "C"):
        command = "cc "+remPath
        outPut = sshClient.executeCommand(command)
        if(len(outPut[1]) == 0):
            command = "./a.out"
            outPut = sshClient.executeCommand(command)
            command = "rm ./a.out"
            sshClient.executeCommand(command)
    if(pgmLang == "CPP"):
        command = "g++ "+remPath
        outPut = sshClient.executeCommand(command)
        if(len(outPut[1]) == 0):
            command = "./a.out"
            outPut = sshClient.executeCommand(command)
            command = "rm ./a.out"
            sshClient.executeCommand(command)
    if(pgmLang == "PYTHON"):
        command = "python "+remPath
        outPut = sshClient.executeCommand(command)
    #print outPut[0]
    command = "rm "+remPath
    sshClient.executeCommand(command)
    return uName+"@"+ipaddr+":~$ $#$"+outPut[0]+"$#$"+outPut[1]

def handleCompression(ipaddr, uName, pWord, remPath, fileExtn, compressionType, triggerFile):
    sshClient = RemoteSecureShell.RemoteSecureShell(ipaddr, uName, pWord)
    dir = remPath.split(".")[0]
    command = ""
    if(compressionType == "zip"):
        command = "unzip "+remPath
        sshClient.executeCommand(command)
    if(compressionType == "rar"):
        return 
    command = "cd "+dir+";"
    if(fileExtn == "C"):
        command = command+"gcc "+triggerFile+";"
        outPut = sshClient.executeCommand(command)
        #print "Output before ./a.out stdout = "+outPut[0]+"stderr = "+outPut[1]
        #print len(outPut[1])
        if(len(outPut[1]) == 0):
            command = "cd "+dir+"; ./a.out"
            outPut = sshClient.executeCommand(command)
            command = "rm -r "+dir+"; rm "+remPath
            sshClient.executeCommand(command)
            #print "output: "+outPut[0]
    if(fileExtn == "CPP"):
        command = command+"g++ "+triggerFile+";"
        outPut = sshClient.executeCommand(command)
        #print "Output before ./a.out stdout = "+outPut[0]+"stderr = "+outPut[1]
        #print len(outPut[1])
        if(len(outPut[1]) == 0):
            command = "cd "+dir+"; ./a.out"
            outPut = sshClient.executeCommand(command)
            command = "rm -r "+dir+"; rm "+remPath
            sshClient.executeCommand(command)
            #print "output: "+outPut[0]
    if(fileExtn == "PYTHON"):
        command = command+"python "+triggerFile
        outPut = sshClient.executeCommand(command)
        command = "rm -r "+dir+"; rm "+remPath
        sshClient.executeCommand(command)
    return uName+"@"+ipaddr+":~$ $#$"+outPut[0]+"$#$"+outPut[1]
        


if __name__ == '__main__':
    ipaddr = "" # insert IP of the remote machine here
    uName = "" # insert the username of the remote machine here
    pWord = "" # insert the password of the remote machine here
    locPath = r"" # insert the local path to the file here
	triggerFile = "" # insert the triggerFile name here
    print main(ipaddr, uName, pWord, locPath, fileExtn = "", compressionType = "zip", triggerFile) # use this if you are sending a zip file to the remote machine
    print main(ipaddr, uName, pWord, locPath, fileExtn = "") # use this if you are sending a single file to the remote machine

