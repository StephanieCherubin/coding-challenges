def defangIPaddr(address):
    """
    Given a valid (IPv4) IP address, return a defanged version of that IP address.

    A defanged IP address replaces every period "." with "[.]".
    """
    #Loop through the address
    # If character is .
        #   replace .with [.]
        # return new address
    return address.replace(".", "[.]")
    # address = ''.join(address)
    # return address
            
print(defangIPaddr(address = "1.1.1.1"))
# Output: "1[.]1[.]1[.]1"
print(defangIPaddr(address = "255.100.50.0"))
# Output: "255[.]100[.]50[.]0"
