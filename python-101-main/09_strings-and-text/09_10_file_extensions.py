# Use a Python string method to prove which of the following files
# are .pdf files, and which aren't.
# Call the method on each file string and print() Python's response.

file_1 = "operators.pdf"
file_2 = "snowfall.jpg"
file_3 = "uncle-joes-wedding.doc"
file_4 = "invitation.pdf"
pdf_docs=[]
Not_pdf_docs=[]

list1=[file_1,file_2,file_3,file_4]
print(list1)
for x in list1:
    if x.endswith(".pdf"):
        print(x+" document is a pdf!")
        pdf_docs.append(x)
    else:   
        print(x+" document isn't a pdf!")    
        Not_pdf_docs.append(x)
print("pdf_docs are:",pdf_docs)
print("Not_pdf_docs are:",Not_pdf_docs)


