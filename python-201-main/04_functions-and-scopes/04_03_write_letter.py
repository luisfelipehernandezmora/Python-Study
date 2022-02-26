# Define a function called `write_letter()` that takes as input a `name`
# and a `text` argument. In the body of the function, create a greeting
# message with the `name` input, as well as a goodbye message that uses
# the `name` again. Combine that with the input `text` to return a
# complete `letter`.
def write_letter(name, text):
    message=f"""Hello {name}! Always nice to greet you, 
    
    As always we love to comunicate important information in the right manner, so:
    
    {text}
    
    Thank you {name} for always being the excellent person you are    
    """
    return(message)

a=write_letter("All mother's children out there", "India open 3 months visas again!")
print(a)