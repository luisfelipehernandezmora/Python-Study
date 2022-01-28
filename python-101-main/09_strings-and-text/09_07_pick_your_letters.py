# Use string indexing and string concatenation
# to write the sentence "we see trees" only by picking
# the necessary letters from the given string.

word = "tweezers "

result=word[1:3]+' '+word[-2]+word[2:4]+' '+word[0]+word[-3]+word[2:4]+word[-2]

print(result)
