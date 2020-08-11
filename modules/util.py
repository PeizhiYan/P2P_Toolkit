import ifaddr


def print_msg(msg):
	print("==============================")
	print(msg)
	print("++++++++++++++++++++++++++++++")

def get_ip_info():
	result = ''
	adapters = ifaddr.get_adapters()
	for adapter in adapters:
		result += "IPs of network adapter " + adapter.nice_name + '\n'
		for ip in adapter.ips:
			result += "   %s/%s" % (ip.ip, ip.network_prefix) + '\n\n'
	return result
	


