# PART A, Q2
class CatMonitor:
    dict = {}
    age = []
    ageDict = {}

    def __init__(self, dict, age, ageDict):
        self.dict = dict
        self.age = age
        self.ageDict = ageDict

    # PART A, Q3b 
    def getAverageAge(self):
        totalAge = sum(self.age)
        averageAge = totalAge / len(self.age)
        return averageAge
    
    # PART A, Q3c
    def getOldestAge(self):
        oldestAge = max(self.age)
        oldestAgeIndex = list(self.ageDict.values()).index(oldestAge)
        oldestAgeName = list(self.dict.values())[oldestAgeIndex].name
        return oldestAgeName, oldestAge
    
    # PART A, Q3d
    def new(self):
        newID = input('Enter new ID: ')
        newName = input('Enter new name: ')
        newAge = int(input(f'Enter age of {newName}: '))

        new = Cat(newID, newName, newAge)
        self.dict[newID] = new
        self.age.append(newAge)
        self.ageDict[newID] = newAge

        return new
    
    # PART D, Q2
    def printAverageAge(self):
        averageAge = self.getAverageAge()
        print(f'Total average age - {averageAge:.1f} years old.\n')


    
# PART A, Q3a
class Cat:
    id = ''
    name = ''
    age = 0

    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age

    def showInfo(self):
        print('''Cat ID: {0}
Cat Name: {1}
Cat Age: {2} years old
'''.format(self.id, self.name, self.age))