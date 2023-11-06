# tower of hanoi
# creating a recursive function
def tower_of_hanoi (disks, source, auxiliary, target):
    if(disks == 1):
        print("Move Disk from rod {} to {}." .format(source, target))
        return
    
    # function calls itself
    tower_of_hanoi(disks-1, source, target, auxiliary)
    print("Move disk {} from rod {} to rod {}.".format(disks, source, target))
    tower_of_hanoi(disks-1, auxiliary, source, target)

# we are reffering source as A , auxiliary as b, target as C    
disks = int(input("Enter Number of disks: "))
tower_of_hanoi(disks, "A", "B", "C")