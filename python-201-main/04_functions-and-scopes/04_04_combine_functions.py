# Combine the `greet()` function that you developed in the course materials
# with the `write_letter()` function from the previous exercise.
# Write both functions in this script and call `greet()` within `write_letter()`
# to let `greet()` take care of creating the greeting string.

def greet(name):
    hello=f"Hey {name}! Nice to see you around!"
    return(hello)
def write_letter(name, text):
    
    hola=greet(name)
    body=f"""    
    As always we love to comunicate important information in the right manner, so:
    
    {text}
    
    Thank you {name} for always being the excellent person you are    
    """
    return(hola+body)

a=write_letter("All mother's children out there", "India open 3 months visas again!")
print(a)