# Use a built-in Python module to tell you the current date and time.
# Research online, so you can print it in a readable manner.
from datetime import date
today=date.today()
d1=today.strftime(" %d %b %Y")

print(f"Today's date is {d1}")