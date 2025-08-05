from User import User

class UserManager():
    # Difference between class UserManager() vs class User:
    # - No difference in this case, but it is possible to pass objects in the parentheses (Inheritance in OOP)
    # Reference: https://en.wikipedia.org/wiki/Inheritance_(object-oriented_programming)
    userList = {}
    userUsageList = {}
    diskspaceList = []

    def __init__(self, userList, userUsageList, diskspaceList):
        self.userList = userList
        self.userUsageList = userUsageList
        self.diskspaceList = diskspaceList

    def getAvgDiskSpace(self):
        # Calculate the average disk space used by all users
        totalDiskSpace = sum(self.diskspaceList)
        avgDiskSpace = totalDiskSpace / len(self.diskspaceList)
        return avgDiskSpace
    
    def getLargestSpaceUser(self):
        largestSpaceUser = max(self.diskspaceList)
        keyList = list(self.userUsageList.keys()) # <- return  dict_keys view (dynamic), that is casted into a list type (static)
        keyIndex = list(self.userUsageList.values()).index(largestSpaceUser) # <- get the index of the largest space user
        key = keyList[keyIndex] # <- get the key of the largest space user
        return self.userList[key] # <- return the User object of the largest space user

    def addNewUser(self):
        newUserID = input('Enter new user ID: ')
        newUsername = input('Enter new user name: ')
        newDiskSpace = int(input('Enter disk space used by the user (in MB): ')) # <- converts user input into int

        newUser = User(newUserID, newUsername, newDiskSpace) # <- create a new User object
        self.userList[newUserID] = newUser # <- add the new User to dictionary
        self.userUsageList[newUserID] = newDiskSpace
        self.diskspaceList.append(newDiskSpace) 