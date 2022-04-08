
from netmiko import ConnectHandler
from ttp import ttp
import json

ttp_template = """
<group name="PORT_INFO">
<snipped>
</group>
"""

def port_forwarding_engine_parser(data_to_parse):
    parser = ttp(data=data_to_parse, template=ttp_template)
    parser.parse()

    # print result in JSON format
    results = parser.result(format='json')[0]
    #print(results)

    #converting str to json. 
    result = json.loads(results)
    with open("test.txt", "a") as f:
        f.write(results)
    return(result)

SR = {
    'device_type': 'device_type',
    'ip': '172.29.6.30',
    'username': 'admin',
    'password': 'admin',
    'port': 22
}

net_connect = ConnectHandler(**SR)
net_connect.send_command('environment no more \n')
output = net_connect.send_command('show port detail')

#print(output)

parsed_port_forwarding_engine_parser = port_forwarding_engine_parser(output)

#print(parsed_port_forwarding_engine_parser)

counter = False

for i in parsed_port_forwarding_engine_parser[0]['PORT_INFO']:
    if 'PORT_FORWARDING_ENGINE_DROP' not in i:
        continue
    #print(i)
    for j in i['PORT_FORWARDING_ENGINE_DROP']:
        #print(j.items())
        for k,v in j.items():
            if int(v) != 0:
                #print(v)
                counter = True
                print(f"""We have Forwarding Engine Drops under port {i['PORT_ID']}. 
                The drops are observed for {k}. 
                The number of the errors are {v}. 
                This needs to be checked from troubleshooting guide.\n
                """)

if counter == False:
    print("There is no Forwarding Engine Drop is observed.")

# See sample .json file when the code is run. 

[
    {
        "PORT_INFO": [
            {
                "PORT_FORWARDING_ENGINE_DROP": [
                    {
                        "IPv4_Header_Drop": "0",
                        "IPv4_Inv_Addr": "0"
                    },
                    {
                        "ACL_Filter_Discards": "0",
                        "BFD_Spoof": "0",
                        "ICMP": "0",
                        "IP_Route_Blackholed": "0",
                        "IPv4_Header_Drop": "0",
                        "IPv4_Inv_Addr": "0",
                        "L2_Service_MTU": "0",
                        "Multicast_MAC_Unicast": "0",
                        "Unicast_MAC_Destination": "0",
                        "Unicast_RPF": "0",
                        "Unknown_MAC_Destination_VPLS": "0"
                    }
                ],
                "PORT_ID": "4/1/1"
            },
            {
                "PORT_FORWARDING_ENGINE_DROP": [
                    {
                        "IPv4_Header_Drop": "0",
                        "IPv4_Inv_Addr": "0"
                    },
                    {
                        "ACL_Filter_Discards": "0",
                        "BFD_Spoof": "0",
                        "ICMP": "0",
                        "IP_Route_Blackholed": "42",
                        "IPv4_Header_Drop": "0",
                        "IPv4_Inv_Addr": "0",
                        "L2_Service_MTU": "0",
                        "Multicast_MAC_Unicast": "0",
                        "Unicast_MAC_Destination": "0",
                        "Unicast_RPF": "0",
                        "Unknown_MAC_Destination_VPLS": "0"
                    }
                ],
                "PORT_ID": "4/1/2"
            },
            {
                "PORT_FORWARDING_ENGINE_DROP": [
                    {
                        "IPv4_Header_Drop": "0",
                        "IPv4_Inv_Addr": "0"
                    },
                    {
                        "ACL_Filter_Discards": "0",
                        "BFD_Spoof": "0",
                        "ICMP": "0",
                        "IP_Route_Blackholed": "0",
                        "IPv4_Header_Drop": "108",
                        "IPv4_Inv_Addr": "0",
                        "L2_Service_MTU": "0",
                        "Multicast_MAC_Unicast": "0",
                        "Unicast_MAC_Destination": "0",
                        "Unicast_RPF": "0",
                        "Unknown_MAC_Destination_VPLS": "0"
                    }
                ],
                "PORT_ID": "4/1/3"
            },
            {
                "PORT_FORWARDING_ENGINE_DROP": [
                    {
                        "IPv4_Header_Drop": "0",
                        "IPv4_Inv_Addr": "0"
                    },
                    {
                        "ACL_Filter_Discards": "0",
                        "BFD_Spoof": "0",
                        "ICMP": "0",
                        "IP_Route_Blackholed": "0",
                        "IPv4_Header_Drop": "0",
                        "IPv4_Inv_Addr": "0",
                        "L2_Service_MTU": "0",
                        "Multicast_MAC_Unicast": "0",
                        "Unicast_MAC_Destination": "38",
                        "Unicast_RPF": "0",
                        "Unknown_MAC_Destination_VPLS": "0"
                    }
                ],
                "PORT_ID": "4/1/4"
            },
            {
                "PORT_FORWARDING_ENGINE_DROP": [
                    {
                        "IPv4_Header_Drop": "0",
                        "IPv4_Inv_Addr": "0"
                    },
                    {
                        "ACL_Filter_Discards": "0",
                        "BFD_Spoof": "0",
                        "ICMP": "0",
                        "IP_Route_Blackholed": "0",
                        "IPv4_Header_Drop": "0",
                        "IPv4_Inv_Addr": "0",
                        "L2_Service_MTU": "0",
                        "Multicast_MAC_Unicast": "0",
                        "Unicast_MAC_Destination": "89",
                        "Unicast_RPF": "0",
                        "Unknown_MAC_Destination_VPLS": "0"
                    }
                ],
                "PORT_ID": "4/1/5"
            },
            {
                "PORT_FORWARDING_ENGINE_DROP": [
                    {
                        "IPv4_Header_Drop": "0",
                        "IPv4_Inv_Addr": "0"
                    },
                    {
                        "ACL_Filter_Discards": "0",
                        "BFD_Spoof": "0",
                        "ICMP": "0",
                        "IP_Route_Blackholed": "40",
                        "IPv4_Header_Drop": "0",
                        "IPv4_Inv_Addr": "0",
                        "L2_Service_MTU": "0",
                        "Multicast_MAC_Unicast": "0",
                        "Unicast_MAC_Destination": "0",
                        "Unicast_RPF": "0",
                        "Unknown_MAC_Destination_VPLS": "0"
                    }
                ],
                "PORT_ID": "4/1/6"
            },
            {
                "PORT_FORWARDING_ENGINE_DROP": [
                    {
                        "IPv4_Header_Drop": "0",
                        "IPv4_Inv_Addr": "0"
                    },
                    {
                        "ACL_Filter_Discards": "0",
                        "BFD_Spoof": "0",
                        "ICMP": "0",
                        "IP_Route_Blackholed": "0",
                        "IPv4_Header_Drop": "0",
                        "IPv4_Inv_Addr": "0",
                        "L2_Service_MTU": "0",
                        "Multicast_MAC_Unicast": "49",
                        "Unicast_MAC_Destination": "0",
                        "Unicast_RPF": "0",
                        "Unknown_MAC_Destination_VPLS": "0"
                    }
                ],
                "PORT_ID": "4/1/7"
            },
            {
                "PORT_FORWARDING_ENGINE_DROP": [
                    {
                        "IPv4_Header_Drop": "0",
                        "IPv4_Inv_Addr": "0"
                    },
                    {
                        "ACL_Filter_Discards": "0",
                        "BFD_Spoof": "0",
                        "ICMP": "0",
                        "IP_Route_Blackholed": "0",
                        "IPv4_Header_Drop": "0",
                        "IPv4_Inv_Addr": "0",
                        "L2_Service_MTU": "0",
                        "Multicast_MAC_Unicast": "0",
                        "Unicast_MAC_Destination": "39",
                        "Unicast_RPF": "0",
                        "Unknown_MAC_Destination_VPLS": "0"
                    }
                ],
                "PORT_ID": "4/1/8"
            },
            {
                "PORT_FORWARDING_ENGINE_DROP": [
                    {
                        "IPv4_Header_Drop": "0",
                        "IPv4_Inv_Addr": "0"
                    },
                    {
                        "ACL_Filter_Discards": "26",
                        "BFD_Spoof": "0",
                        "ICMP": "0",
                        "IP_Route_Blackholed": "0",
                        "IPv4_Header_Drop": "0",
                        "IPv4_Inv_Addr": "0",
                        "L2_Service_MTU": "0",
                        "Multicast_MAC_Unicast": "0",
                        "Unicast_MAC_Destination": "0",
                        "Unicast_RPF": "0",
                        "Unknown_MAC_Destination_VPLS": "0"
                    }
                ],
                "PORT_ID": "4/1/9"
            },
            {
                "PORT_FORWARDING_ENGINE_DROP": [
                    {
                        "IPv4_Header_Drop": "0",
                        "IPv4_Inv_Addr": "0"
                    },
                    {
                        "ACL_Filter_Discards": "0",
                        "BFD_Spoof": "0",
                        "ICMP": "0",
                        "IP_Route_Blackholed": "17",
                        "IPv4_Header_Drop": "0",
                        "IPv4_Inv_Addr": "0",
                        "L2_Service_MTU": "0",
                        "Multicast_MAC_Unicast": "0",
                        "Unicast_MAC_Destination": "0",
                        "Unicast_RPF": "0",
                        "Unknown_MAC_Destination_VPLS": "0"
                    }
                ],
                "PORT_ID": "4/1/10"
            },
    
