largest = None
print("Before: ", largest)

for itervar in [3, 19, 6, 24, 5]:
    if largest is None or itervar > largest:
        largest = itervar
    print("Loop: ", itervar, largest)
print("Largest: ", largest)
