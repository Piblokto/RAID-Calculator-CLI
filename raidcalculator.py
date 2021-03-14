# Check if RAID has minimum number of drives
def compatible(num_disks, raid_type):
    minimum_drives = {
        "raid0": 2,
        "raid1": 2,
        "raid10": 4,
        "raid5": 3,
        "raid50": 6,
        "raid6": 4,
        "raid60": 8 
    }   
    # Check if RAID Type is in dict
    if raid_type in minimum_drives.keys():
        min_raid_drives = minimum_drives[raid_type]
        # Check if RAID Type will work
        if (num_disks >= min_raid_drives):
            return True
        else:
            return False
    else:
        print("The RAID Type you have inputted is not compatible, please read the documentation for more information.")

# Check RAID Fault Tolerance
def fault_tolerance(raid_type):
    tolerance = {
        "raid0": 0,
        "raid1": 1,
        "raid10": 1,
        "raid5": 1,
        "raid50": 1,
        "raid6": 2,
        "raid60": 2 
    }

    if raid_type in tolerance.keys():
        return tolerance[raid_type]
    else:
        print("Error finding fault tolerance")

# Calculate Overhead for RAID Type
def overhead(raid_type, disks, disk_size):
    raw = disks * disk_size
    if raid_type == "raid0":
        return 0
    elif raid_type == "raid1":
        overhead = raw * 0.5
        return overhead
    elif raid_type == "raid10":
        overhead = raw * 0.5
        return overhead
    elif raid_type == "raid5":
        overhead = disk_size
        return overhead
    elif raid_type == "raid50":
        overhead = disk_size * 2
        return overhead
    elif raid_type == "raid6":
        overhead = disk_size * 2
        return overhead
    elif raid_type == "raid60":
        overhead = disk_size * 4

# User Input
disks = int(input("Number of Disks "))
disk_size = int(input("Individual Disk Size (TB) "))
raid_type_input = input("RAID Type (e.g. 1, 5, 60) ")
# Append RAID level to string for dict lookup
raid_type = "raid" + str(raid_type_input)

# Check if RAID1 or RAID10 have even drives
if raid_type == 'raid1' or raid_type == 'raid10':
    if disks % 2:
        # Odd
        print("RAID", raid_type_input, "requires an even amount of drives")
        exit()
    else: 
        # Even
        compatible = compatible(disks, raid_type)
# If not RAID 1 or 10
else:
    compatible = compatible(disks, raid_type)

# RAID compatible
if compatible == True:
    fault_tolerance = fault_tolerance(raid_type)
    overhead = overhead(raid_type, disks, disk_size)
    raw_capacity = disks * disk_size
    array_capacity = raw_capacity - overhead
    print("\n")
    print("Capacity:", array_capacity, "TB out of", raw_capacity, "TB")
    print("RAID Type: RAID", raid_type_input)
    print("Fault Tolerance:", fault_tolerance, "Drive('s)")

else:
    print("You do not have enough drives to use RAID", raid_type_input)
    exit()