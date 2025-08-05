from PetShop import *

if __name__ == '__main__':
    # ======================== PART A ========================
    catID = ['C1', 'C2', 'C3', 'C4', 'C5']
    catName = ['Tabby', 'Kitty', 'Tommy', 'Tikki', 'Tammy']
    catAge = [3, 1, 2, 6, 7]

    catDict = {}
    for i in range(len(catID)):
        catDict[catID[i]] = Cat(
            catID[i],
            catName[i],
            catAge[i],
            )
        

    catAgeDict = {}
    for i in range(len(catID)):
        catAgeDict[catID[i]] = catAge[i]

    newCatMonitor = CatMonitor(catDict, catAge, catAgeDict)

    catAvgAge = newCatMonitor.getAverageAge()
    print(f'The average age of the cat is {catAvgAge:.1f} years old.\n')

    catOldestName, catOldestAge = newCatMonitor.getOldestAge()
    print(f'The cat with the oldest age is {catOldestName} at {catOldestAge} years old.\n')

    newCat = newCatMonitor.new()
    print(f'The new cat added is {catDict[newCat.id].name}.\n')


    # ======================== PART B ========================
    # PART B, Q1a (Data structure: Hash map / Dictionary (Python))
    catNameDict = {
        'C1': 'Tabby',
        'C2': 'Kitty',
        'C3': 'Tommy',
        'C4': 'Tikki',
        'C5': 'Tammy',
    }

    # Alternatively:
    # catNameDict = {}
    # for i in range(len(catID)):
    #     catDict[catID[i]] = catName[i]


    # PART B, Q1b (Data structure: Hash map / Dictionary (Python))
    catAgeDict = {
        'C1': 3,
        'C2': 1,
        'C3': 2,
        'C4': 6,
        'C5': 7,
    }

    # Alternatively:
    # catAgeDict = {}
    # for i in range(len(catID)):
    #     catDict[catID[i]] = catAge[i]


    # PART B, Q1c (Data structure: List / List (Python))
    catAgeList = [3, 1, 2, 6, 7]


    # PART B, Q1d (Data structure: List / List (Python))
    catAgeList = ['C1', 'C2', 'C3', 'C4', 'C5']


    # ======================== PART C ========================
    # PART C, Q1a (Data type: string)
    catID = 'C7' # or "C7" <- either works in python


    # PART C, Q1b (Data type: string)
    catName = 'Yeontan'


    # PART C, Q1c (Data type: integer)
    catAge = 5 # <- not float since this is AGE!


    # PART C, Q1d (Data type: integer)
    oldestCatAge = 38


    # ======================== PART D ========================
    # Part D, Q1
    newCatAgain = Cat('C7', 'Yeontan', 5)

    # Part D, Q2
    newCatMonitor.printAverageAge()

    # Part D, Q3
    newCatAgain.showInfo()

    # ======================== PART E ========================
    # Part E, Q1
    newCatAnother = newCatMonitor.new()
    print(f'The new cat added is {catDict[newCatAnother.id].name}.\n')

    # Part E, Q2
    catAvgAgeUpdated = newCatMonitor.getAverageAge()
    print(f'The updated average age of the cat is {catAvgAgeUpdated:.1f} years old.\n')