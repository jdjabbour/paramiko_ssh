# A simple application to connect to a server via Python library paramiko
# This application sends a simple command to the server and store the output
# and prints it to the console.

import paramiko

# Set the ssh client
ssh = paramiko.SSHClient()

# Override the missing hostkey exception
# Whithout this you would not connect and get an error instead
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Set up connection parameters - (IP, Port=22, Username, Password)
ssh.connect('**', port=22, username='frank', password='prank')

# Set up the line to enter commands to the server
# You can run scripts or retrive information from the server at this point
stdin, stdout, stderr = ssh.exec_command('whoami')
output = stdout.readlines()
print '\n'.join(output)

# To get a dedicated channel
channel = ssh.invoke_shell()


