from pprint import pprint
filename = "show_ip_int_brief.txt"
with open(filename) as some_var:
    show_ip_int = some_var.read()

show_ip_int = show_ip_int.strip()
output_dict = {} 
for line in show_ip_int.splitlines():
    if 'interface' in line:
        continue
    fields = line.split()
    interface = fields[0]
    ip_addr = fields[1]
    line_status = fields[4]
    line_protocol = fields[5]
    output_dict[interface] = {}
    output_dict[interface]["ip_addr"] = ip_addr
    output_dict[interface]["line_status"] = line_status
    output_dict[interface] ["line_protocol"] = line_protocol
    #print(output_dict)
    #break

#or
    #fields = line.split()
    # interface, ip_addr, junkl, junk2, line_status, line_protocol = fields.split()


pprint(output_dict)
