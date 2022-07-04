# In this exercise, you will practice both File I/O as well as using Exceptions
# in a real-world scenario.

# This folder contains another folder called `books/` that contains three text files
# of books from Project Gutenberg:
# 1. war_and_peace.txt
# 2. pride_and_prejudice.txt
# 3. crime_and_punishment.txt

# 1) Open `war_and_peace.txt`, read the whole file content and store it in a variable
# 2) Open `crime_and_punishment.txt` and overwrite the whole content with an empty string
# 3) Loop over all three files and print out only the first character each. Your program
#    should NEVER terminate with a Traceback.
#     a) Which exception can you expect to encounter? Why?
#     b) How do you catch it to avoid the program from terminating with a traceback?


# 1) Open `war_and_peace.txt`, read the whole file content and store it in a variable
books="/home/luis/Python-Study/python-301-main/05_exceptions/books"
with open (books+"/war_and_peace.txt","r")as file:
    a=file.read()

# 2) Open `crime_and_punishment.txt` and overwrite the whole content with an empty string
b=""
with open(books+"/crime_and_punishment.txt","w") as file:
    file.write(b)

# 3) Loop over all three files and print out only the first character each.
book1=books+"/war_and_peace.txt"
book2=books+"/crime_and_punishment.txt"
book3=books+"/pride_and_prejudice.txt"
all_books=[book1,book2,book3]

for each_book in all_books:
    with open (each_book,"r") as file:
        reading_test=file.read()
        first_char=reading_test[0:1]
        print(first_char)