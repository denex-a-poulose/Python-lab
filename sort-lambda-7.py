# Sort strings by length using lambda function

strings = input("Enter strings: ").split()

strings.sort(key=lambda x: len(x))

print(strings)
