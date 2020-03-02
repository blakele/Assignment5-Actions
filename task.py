def firstrun():
    return "success"


def area(radius):
    return radius * radius * 3.14


def firstLastList(listA):
    first = listA[0]
    last = listA[len(listA)-1]
    return (first, last)


def date(dateA, dateB):
    a1 = dateA.find('/') + 1
    listA = dateA[a1:]
    b1 = listA.find('/')
    listA1 = listA[:b1]
    numA = int(listA1)

    a2 = dateB.find('/') + 1
    listB = dateB[a2:]
    b2 = listA.find('/')
    listB1 = listB[:b2]
    numB = int(listB1)

    temp = numA - numB
    numC = abs(temp)
    return numC
