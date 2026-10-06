# Write a program to count word frequency using a dictionary

text = input("Enter a sentence: ")
words = text.split()

freq = {}

for word in words:
    freq[word] = freq.get(word, 0) + 1

print(freq)
