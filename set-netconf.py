import time
from getpass import getpass
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException, NetMikoAuthenticationException

def enable_netconf(net_device):
	print ("{} Connecting to {}".format(time.asctime(), net_device['ip']))
	junos_device = ConnectHandler(**net_device) #(5)
	configure = junos_device.config_mode() #(6)
	print ("{} Applying configuration to {}".format(time.asctime(), net_device['ip']))
	setssns = junos_device.send_command("set system services netconf ssh") #(7)
	print ("{} Committing configuration to {}".format(time.asctime(), net_device['ip']))
	junos_device.commit(comment='Enabled NETCONF service', and_quit=True) #(8)
	print ("{} Closing connection to {}".format(time.asctime(), net_device['ip']))
	junos_device.disconnect() #(9)

def main():
	user_login = input('Username: ') #(1)
	user_pass = getpass('Password: ')

	with open('inventory.txt') as f: #(2)
		device_list = f.read().splitlines()
		for device in device_list:
			net_device = {
				'device_type': 'juniper', #(3)
				'ip': device,
				'username': user_login,
				'password': user_pass,
			}
			enable_netconf(net_device) #(4)

if __name__ == '__main__':
	main()
