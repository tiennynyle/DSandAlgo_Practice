def tower_of_Hanoi(num_disks):
    Hanoi_helper(num_disks, 'S', 'A', 'D')
def Hanoi_helper(num_disks, source, auxiliary, destination):
    # Base case
    if num_disks == 0:
        return
    # When there's one disk left, move it from source to destination
    if num_disks == 1:
        print("{} {}".format(source, destination))
        return
    # Move n-1 disks from source to auxiliary:
    Hanoi_helper(num_disks - 1, source, destination, auxiliary)
    print("{} {}".format(source, destination))
    # Move n-1 disks from auxiliary to destination
    Hanoi_helper(num_disks - 1, auxiliary, source, destination)
tower_of_Hanoi(2)
'''Credit to Udacity and this youtube vid: https://www.youtube.com/watch?v=buWXDMbY3Ww'''
