# What are classes and objects?
# - Classes are essentially *blueprints* for creating objects
#   - You can define attributes (variables) and methods (functions) within a class
# - Objects are instances of classes
# Reference: https://www.enjoyalgorithms.com/blog/classe-and-object-in-oops

class User:
    # The User class contains the attributes: userID, username and diskspace
    userID = '' # <- these values represent default values if no values are provided for an instance of this class
    username = ''
    diskspace = 0
    
    # Why is `__init__` used?
    # TLDR: `__init__` is similar to constructor in Java
    # - Constructors are called whenever an object is created
    # - It initializes the attributes of the class when an object is created
    # Java:
    # User(userID, username, diskspace) {
    #     this.userID = userID;
    #     this.username = username;
    #     this.diskspace = diskspace;
    # }
    # Python:
    def __init__(self, userID, username, diskspace):
        self.userID = userID
        self.username = username
        self.diskspace = diskspace
    # When a new object is created from the User class:
    # user1 = User('001', 'Bruce Wayne', 1000)
    # >> underneath, python calls User.__init__(user1, userID='001', username='Bruce Wayne', diskspace=1000)
    # Note: `self` is a reference to the current instance of the class, similar to `this` in Java

    # This is a method of the User class
    def showInfo(self):
        msg = '''
        User ID: {0}
        User Full Name: {1}
        Disk Space Used: {2} MB
        '''.format(self.userID, self.username, self.diskspace)
        print(msg)

# Side note: Indentation is v important in Python!!!