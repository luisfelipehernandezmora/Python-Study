# Demonstrate how to create a generator object.
# Print the object to the console to see what you get.
# Then iterate over the generator object and print out each item.
gen=(x for x in range(10))
print(gen, "    ",type(gen))
print()
for x in gen:
    print(x)