from jnpr.junos import Device
from jnpr.junos.op.phyport import PhyPortStatsTable
from lxml import etree
from pprint import pprint
import jxmlease

dev = Device(host='172.16.0.20',user='harry',password='abc123', gather_facts=False)
dev.open()

#op = PhyPortStatsTable(dev)
#op.get('ge-0/0/0')
#print(op.to_json())

###############################

#op = dev.rpc.get_interface_information()
#op = dev.rpc.get_interface_information({'format': 'text'})
op = dev.rpc.get_interface_information(interface_name='ge-0/0/0')
parser=jxmlease.EtreeParser()
response=parser(op)
#pprint(response)

intf=response['interface-information']['physical-interface']['logical-interface']['name']
traffic_in=response['interface-information']['physical-interface']['logical-interface']['traffic-statistics']['input-packets']
traffic_out=response['interface-information']['physical-interface']['logical-interface']['traffic-statistics']['output-packets']

print('Interface ' + str(intf) + ' traffic pattern:\n'
'packets-in : ' + str(traffic_in) + '\n'
'packets-out: ' + str(traffic_out))

#for i in op.xpath('.//link-level-type'):
#    print i.text
dev.close()
