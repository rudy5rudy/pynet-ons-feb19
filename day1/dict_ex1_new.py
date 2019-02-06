#Dict Ex1
#---------

#a. Create a dictionary representing a network device
#b. Assign it an ip address, a username, a password, a vendor, and a model 
#   field.
#c. Loop over this dictionary printing out all of the keys, and values
#d. Update the password to be a new value
#e. Add a secret field to the dictionary
#f. Use the .get() method to try to retrieve a non-existent ‘device_type’ 
#   field. Return a default value of ‘cisco_ios’ when the .get() key lookup 
#   fails.


net_device = {
    "ip_addr": "192.168.1.100",
    "username": "rudy",
    "password": "great",
    "vendor": "Kraft",
    "model": "asr1001hx"}

banner = "-|-:" * 55

print(banner)

print()
for k,v in net_device.items():
    print("{:^20}  (┛ಠ_ಠ)┛彡┻━┻  {:^20}".format(k,v))

print(banner)

net_device["password"] = "new_value"
net_device["secret"] = "some secret"

print(banner)

device_type = net_device.get("device_type", "Kraft_ios")
print("\nDefault device type: {}\n".format(device_type))







