from User import User # <- Imports the User class from User.py
from UserManager import * # <- Imports everything from UserManager.py

if __name__ == '__main__':
# Why is `if __name__  == '__main__'` needed?
# - The if statement checks if the script is being run directly as the main program or imported as a module.
#   - If run directly, it executes the code block under the if statement.
#   - If imported, it does not execute that code block, allowing the module to be used without running the script.
# - Reference: https://stackoverflow.com/questions/419163/what-does-if-name-main-do
    user1 = User('001', 'Bruce Wayne', 1000)
    user2 = User('002', 'Clark Kent', 500)
    user3 = User('003', 'Diana Prince', 750)
    user4 = User('004', 'Barry Allen', 300)
    user5 = User('005', 'Arthur Curry', 600)

    # Dictionary in python is essentially a map (data structure)
    # Reference: https://techdevguide.withgoogle.com/paths/data-structures-and-algorithms/
    userDict = {
        'User1': user1,
        'User2': user2,
        'User3': user3,
        'User4': user4,
        'User5': user5
    }

    spaceUsedDict = {
        'User1': 1000,
        'User2': 500,
        'User3': 750,
        'User4': 300,
        'User5': 600
    }

    # List in python is essentially an array)
    spaceList = [1000, 500, 750, 300, 600]

    newManager = UserManager(userDict, spaceUsedDict, spaceList)

    avgUsage = UserManager(userDict, spaceUsedDict, spaceList)

    avgUsage = newManager.getAvgDiskSpace()
    print(f'Average disk space used by all users: {avgUsage} MB')

    largestUser = newManager.getLargestSpaceUser()
    print('User with the largest disk space usage:')
    largestUser.showInfo()

    newManager.addNewUser()
    avgUsage = newManager.getAvgDiskSpace()
    print(f'Average disk space used by all users after adding a new user: {avgUsage} MB')