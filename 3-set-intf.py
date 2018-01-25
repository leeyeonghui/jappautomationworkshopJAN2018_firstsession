from jnpr.junos import Device
from jnpr.junos.utils.config import Config

hostname = '172.16.0.20'
username = 'harry'
password = 'abc123'

# NETCONF session over SSH
dev = Device(host=hostname, user=username, passwd=password)

#Initiate connection
dev.open()

#set to Configure (edit) mode
cu=Config(dev)

#set interface
cu.load('set interfaces ge-0/0/2 unit 0 family inet address 1.2.3.4/24', format='set')

#commit
cu.commit()

#close connection
dev.close()
