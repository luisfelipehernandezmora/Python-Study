user_input=input("Write the test text: ")
ICAPS=user_input.upper()
print(ICAPS)
second_caps=""
for i in range(len(user_input)):
    if i%2==0:
        second_caps+=user_input[i]
print(second_caps)
