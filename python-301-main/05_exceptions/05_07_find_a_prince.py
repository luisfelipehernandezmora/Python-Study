# Write a custom exception  that inherits from `Exception()`
# Open and read in the content of the book `.txt` files in the `books/` folder
# like you did in the previous exercise.
# Raise your `PrinceException()` if the first 100 characters of a book
# contain the string "Prince".

class PrinceException(Exception):
    """Exception to see if you have a prince in the first 100 words of your text
        
    Returns:
        Yes there is a prince!
        """
    def __init__(self,text,index):
        self.text=text
        self.msg=f"\nOh you have a prince in the {index}th word, catch him!\n"
    
def find_prince(text:str):
    """Finds a prince in the first 100 words of the given text and gives you the position of it!
    
        Returns:
        Yes there is a prince!
    """
    a=text.split(" ")
    a=a[0:100]
    indexes=[]
    for i in enumerate(a):
        if i[1]=="Prince":
            index=i[0]+1
            indexes.append(index)

    return(indexes)

books="/home/luis/Python-Study/python-301-main/05_exceptions/books"
book1=books+"/war_and_peace.txt"
book2=books+"/crime_and_punishment_copy.txt"
book3=books+"/pride_and_prejudice.txt"
all_books=[book1,book2,book3]

for each_book in all_books:
    with open (each_book,"r") as file:
        try:
            text=file.read()
            a=text.split(" ")
            a=a[0:100]
            if "Prince" in a:
                raise PrinceException(text,find_prince(text))
        except PrinceException:
            print (PrinceException(text,find_prince(text)).msg)


