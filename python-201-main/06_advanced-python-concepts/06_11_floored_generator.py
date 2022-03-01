# Adapt your Generator expression from the previous exercise:
# Don't print anything, and run a floor division by 1111 on it.
# What numbers do you get?
nums = range(1, 1000)

gen=(num//111 for num in nums)
for nume in gen:
    print(nume)