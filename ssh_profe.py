import sys
import paramiko as p

try:

	client = p.SSHClient()
	client.load_system_host_keys()
	client.set_missing_host_key_policy(p.WarningPolicy)

	client.connect('192.168.1.59', port='22', username='oracle', password='oracle')

	stdin, stdout, stderr= client.exec_command(sys.argv[1])
	print stdout.read(),

finally:
	client.close()
