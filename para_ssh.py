# A simple application to connect to a server via Python library paramiko
# This application sends a simple command to the server and store the output
# and prints it to the console.
# https://www.youtube.com/watch?v=kvPa85M9z2Q


import paramiko

# Set the ssh client
ssh = paramiko.SSHClient()

# Override the missing hostkey exception
# Whithout this you would not connect and get an error instead
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Set up connection parameters - (IP, port=22, Username, Password)
ssh.connect('**', port=22, username='frank', password='prank')


# Set up the line to enter commands to the server
# You can run scripts or retrive information from the server at this point
stdin, stdout, stderr = ssh.exec_command('whoami')
output = stdout.readlines()
print '\n'.join(output)

'''
# To get a dedicated channel and to send strings to the shell
channel = ssh.invoke_shell() # This opens the shell


channel.send() # Sends string to shell
channel.recv(9999) # Retrives output from sent string
channel.recv_ready() # Says if the server is able to receive information

channel_data = str()
host = str()
scrfile = str()

while True:
    if channel.recv_ready():
        channel_data += channel.recv(9999)
    else:
        continue

    if channel_data.endswith('root@ubuntu-s-1vcpu-1gb-nyc3-01:~#'):
        channel.send('ifconfig\n')
'''
