largest = None
print("Before: ", largest)
for itervar in [4, 6, 12, 29, 36, 2]:
    if largest is None or itervar > largest:
        largest = itervar
    print("Loop: ", itervar, largest)
print("Largest: ", largest)
