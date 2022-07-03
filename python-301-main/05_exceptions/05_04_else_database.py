# Write a script that demonstrates a try/except/else statement.
# For example, you can revisit the course module about database interactions
# and include a try/except/else statement based on what to do whether or not
# the database connection can be established.

import webbrowser
while True:
    try:
        web=input("Insert a wikipedia website you want to open ")
        if "/wiki/" not in web:
            raise Exception("Oh is not a wikipedia link")
    except Exception:
        print("it should be a wikipedia link, try again ")
        continue
    else:
        print("good job! let's go to the page ")
        webbrowser.open(web,new=0,autoraise=True)
        break