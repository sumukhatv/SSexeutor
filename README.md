SSexeutor
=========

SSexecutor is a remote program executor. The main purpose of this is to enable multi-platform testing. 
It will execute a program or a project on a remote machine and transfer the output from remote machine back to your local machine.

Currently C, C++ and Python programs are supported.

SSexecutor uses the Paramiko module. 

SSexecutor.py cointains a function calles "main" which is used to trigger the project.

Usage:
  SSexecutor can be used to transfer a single file from local machine to a remote machine and execute it or a whole     project can be transferred and executed.

  Insert the IP Address, Username and Password of the remote machine in the placeholders provided in __main__ of SSexectuor.py 
  
  Insert the path to file in the local machine in the placeholder provided in the __main__ of SSexecutor.py
  
  If you are sending a .zip file to the remote machine you must provide the name of the file which must be executed as well. This is called "triggerFile"
