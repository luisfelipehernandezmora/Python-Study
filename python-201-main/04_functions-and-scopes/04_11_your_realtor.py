# Write a function that prints out nicely formatted information about a
# real estate advertisement. The information can vary for every advertisement, which
# is why your function should be able to take an arbitrary amount of
# keyword arguments, and display them all in a list form with some 
# introductory information.

title="A REWARDING ESCAPE PEACEFULLY SITUATED"
locality="Los Altos"
description="""Luxurious and upgraded, this 4 bedroom,
4.5 bathroom home of 5,281 sq. ft. (including poolhouse, per independent third-party measurement)
rests on a lot of 1.23 acres (per county) on a peaceful cul-de-sac in the Lakeside neighborhood.
Richly-appointed spaces include large gathering areas, a bright, professional-grade kitchen,
spectacular dining room, two walk-out master suites, and a home theater. Contemporary amenities
include solar PV and a Tesla EV charging station. The expansive backyard includes a sparkling
pool and spa plus a comfortable poolhouse all in private, verdant surroundings. You’ll 
appreciate the short drive to downtown Los Altos, Rancho Shopping Center, access to Interstate 
280, and numerous parks and preserves."""
price="125 000"
contacts="Mat +1 874-452-541"

def nice_print(title, locality,description, price, contacts):
    body=f"""
Don't let go this oportunity

{title}

This is beautiful property in located at {locality}

A bit about the place:

{description}

This unit is being sell in {price} USD 

And please feel free to call {contacts} for any aditional information
"""
    return(body)

mesage=nice_print(title,locality,description,price,contacts)
print(mesage)