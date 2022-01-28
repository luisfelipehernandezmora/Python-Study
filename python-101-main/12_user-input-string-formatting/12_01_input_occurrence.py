# Write a script that takes a string of words and a letter from the user.
# Find the index of first occurrence of the letter in the string. For example:
#
# String input: hello world
# Letter input: o
# Result: 4

text=input("Please write a sentence here: ")
word=input("And now give me a word that is in the sentence! ")

while True:
    word=input("And now give me a word that is in the sentence! ")
    if word in text:    
        num=text.find(word)
        print(f"The Result is {num}")
        break
    else: 
        print("Hey that letter is not in the sentence! ")
        continue