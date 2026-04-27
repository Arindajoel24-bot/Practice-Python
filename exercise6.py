word = input("Enter a word: ")

wordReversed = (word[::-1])

if wordReversed == word:
    print("palindrome")
else: 
    print("Not palindrome")