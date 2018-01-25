from jnpr.junos import Device
from jnpr.junos.utils.config import Config

hostname = '172.16.0.20'
username = 'harry'
password = 'abc123'

# NETCONF session over SSH
dev = Device(host=hostname, user=username, passwd=password, gather_facts=False)

#Initiate connection
dev.open()

#set to Configure (edit) mode
cu=Config(dev)

#check for candidate configuration...if exist, rollback

#cu.pdiff()

diff = cu.diff()
if diff:
	cu.rollback()

#close connection
dev.close()
