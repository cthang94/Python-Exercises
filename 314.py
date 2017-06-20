smallest = 0
largest = 0

line_one = [79, 82, 34, 83, 69]


for line in line_one:
    line_min = min(line_one)
    if line >= line_min:
        smallest = line
        print(smallest)
