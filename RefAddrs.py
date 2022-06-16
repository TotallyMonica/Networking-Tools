from ipaddress import ip_address
import csv, json, sys

ips = []

def readIPS():
    with open("ip_table.json", 'r') as ip:
        ips = json.load(ip)

def writeIPS():
    with open("ip_table.json", "w") as file:
        json.dump(ips, file)

def addIP():
    print("Input the MAC Address:")
    newMAC = input()

    print("Input the IP Address for the device")
    print("Note: it is generally okay for you to leave this blank if you do not have the IP address for this device just yet.")
    newIP = input()

    print("Optional: Input a brief description for this device, such as ownership, subnet, connection type, etc.")
    newDesc = input()

    print("Does this look correct to you?")
    print("Device MAC: " + newMAC)
    print("Device IP: " + newIP)
    print("Device Description: " + newDesc)

    choice = input()

    if choice.lower() != 'y':
        print("Verifying again, apologies...")
        return(addIP())
    
    device = {
        "MAC": newMAC,
        "IP": newIP,
        "Desc": newDesc
    }

    return device

def PrintDevices():
    count = 1
    for i in ips:
        print("MAC for device number " + str(count) + ": " + i['MAC'])
        print("IP for device number " + str(count) + ": " + i['IP'])
        print("Description for device number " + str(count) + ": " + i['Desc'])
        count += 1

def RemoveDevice():
    print("How would you like to identify the device? MAC, IP, or Description?")
    searchMethod = input()

    index = 1
    for dev in ips:
        if searchMethod.lower.contains('mac'):
            print(f"{str(index)}: {dev['MAC']}")
        elif searchMethod.lower.contains('ip'):
            print(f"{str(index)}: {dev['IP']}")
        elif searchMethod.lower.contains('desc'):
            print(f"{str(index)}: {dev['Desc']}")
        index += 1

    print("Select the index of the device you'd like to remove")
    ips[int(input())] = None
    ips.remove(None)

def main(args):
    beta = False

    print("What would you like to do with your reference table?")
    print("1. Load a file")
    print("2. Save a file")
    print("3. Add a device")
    print("4. Remove a device")
    print("5. Print devices")
    if "--beta" in args:
        beta = True
        print("6: Save to CSV")
        print("7: Check completeness")
        print("8: Modify existing entries")
        print("9: Set subnet")
    print("0: Exit")

    try:
        choice = int(input())
    except ValueError:
        choice = -1
    
    print(choice)
    print(type(choice))

    if choice == 0:
        return False
    elif choice == 1:
        readIPS()
    elif choice == 2:
        writeIPS()
    elif choice == 3:
        ips.append(addIP())
    elif choice == 4:
        print("Error: Not implemented yet")
    elif choice == 5:
        PrintDevices()
    elif choice == 6:
        if beta:
            print("Error: Saving to CSVs have not been implemented yet, even in a beta form.")
        else:
            print(f"This option is accessible with the beta flag (try {args[0]} --beta")
    elif choice == 7:
        if beta:
            print("Error: Completeness has not been entered just yet.")
        else:
            print(f"This option is accessible with the beta flag (try {args[0]} --beta")
    elif choice == 8:
        if beta:
            print("Error: Modifying existing entries have not been implemented just yet.")
        else:
            print(f"This option is accessible with the beta flag (try {args[0]} --beta")
    elif choice == 9:
        if beta:
            print("Error: Setting the subnet is not supported just yet.")
        else:
            print(f"This option is accessible with the beta flag (try {args[0]} --beta")
    else:
        print("Error: Invalid entry.")
    
    return True

if __name__ == "__main__":
    NoExit = True
    args = sys.argv

    while NoExit:
        NoExit = main(args)