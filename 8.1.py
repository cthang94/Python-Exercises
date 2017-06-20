list_one = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_two = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

def chop(myList):
    lastListIndex = len(myList) - 1
    del myList[lastListIndex]
    del myList[0]
    return None
    

chop(list_one)
print(list_one)
print(chop(list_one))


def middle(myOtherList):
    list_two = myOtherList.pop(0)
    list_two = myOtherList.pop(-1)
    return

middle(list_two)
print(list_two)
