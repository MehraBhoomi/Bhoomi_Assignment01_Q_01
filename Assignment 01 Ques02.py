# Write a Python program that accepts a word from the user and reverse it.
# Sample Test Case
# Input : Edyoda
# output: adoydE


# method 1
word = input("Input a word to reverse: ")
for char in range(len(word) - 1,-1, -1):
    print(word[char], end="")


# method 2
x = input("Enter the word whose reverse you want:\n")
print(x[-1:-len(x)-1:-1])