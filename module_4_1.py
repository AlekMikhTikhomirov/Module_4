from fake_math import divide as fd
from true_math import divide as td

result1 = fd(first = int(input("Enter divisible number: ")), second = int(input("Enter divider number: ")))
print(result1)
result2 = td(first = int(input("Enter divisible number: ")), second = int(input("Enter divider number: ")))
print(result2)