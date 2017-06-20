string = ("X-DSPAM-Confidence: 0.8475")
index = string.find("0" [:])
number = float(string[20:26])
print(number)
