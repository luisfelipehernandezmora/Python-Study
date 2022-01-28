text=input("Give me your text to analyze it ")
upper=lower=punct=char=0
symbols=[".",",","!","?"]
for let in text:
    if let.isupper():
        upper+=1
    if let.islower():
        lower+=1
    if let in symbols:
        punct+=1
    if let!=" ":
        char+=1
print(f"""So you have {upper} upper cases, 
{lower} lower cases, 
{punct} punctuation marks
and {char} characters witout counting the spaces!""")