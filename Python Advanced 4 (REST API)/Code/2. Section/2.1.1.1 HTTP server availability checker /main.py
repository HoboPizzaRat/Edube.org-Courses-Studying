import sys
import utility.http as http

def checkPortValidity(port):
    portNumber = int(port)
    if portNumber < 1 or portNumber > 65535:
        return False
    return True

def checkIpValidity(ipAddress):
    octet_range_min = 0
    octet_range_max = 255
    ip_octets = ipAddress.split(".")
    if len(ip_octets) != 4:
        return False
    for octet in ip_octets:
        value = int(octet)
        if not (str(value) == octet \
                and value >= octet_range_min \
                and value <= octet_range_max):
            return False
    return True
    
# pass true for now
def checkDomainValidity(domainName):
    parts = domainName.split(".")
    if not (parts[0] != None and parts[1] != None and parts[2] != None):
        return False
    return True

def checkWebsiteValidity(website):
    isIpValid = checkIpValidity(website)
    isDomainValid = checkDomainValidity(website)
    if not(isIpValid or isDomainValid):
        return False
    return True

def printAllArguments(options):
    print("PRINTING GIVEN ARGUMENTS")
    for key, value in options.items():
        print(f"{key} : {value}")

def checkAreAgumentsValid(options):
    for key, value in options.items():
        if value == None:
            return False
    return True


if __name__ == "__main__":
    path = 80
    arguments = sys.argv[1:]

    options = {
        "-site": None,
        "-port": 80
        }

    for argument in arguments[::2]:
        if argument in options.keys():
            arg_data = None
            try:
                arg_data = arguments[arguments.index(argument)+1]
                options[argument] = arg_data
                print(f"Argument parsed: ({argument} : {arg_data})")
            except Exception as e:
                print("You must specify argument for option: "+argument)
                exit(-1)
        else:
            print(argument + "is invalid argument")
            exit(-1)

    if not checkAreAgumentsValid(options):
        print("You must specify all required arguemnts")
        printAllArguments(options)
        exit(2)
            
    if not checkPortValidity(options["-port"]):
        print("Port must be in range 1-65535")
        exit(2)
    if not checkWebsiteValidity(options["-site"]):
        print("Website must be either an valid ip address or the whole domain name! (www.example.com)")
        exit(2)

    http.checkServerStatus(options)
        


        
        