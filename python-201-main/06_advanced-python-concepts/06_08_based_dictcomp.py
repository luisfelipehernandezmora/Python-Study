# Using the given variables `base` and `digits`, write a dictionary comprehension
# that maps each integer between `0` and `999` to the list of three digits 
# that represents that integer in base 10. That is, the value should be:
#
# {0: [0, 0, 0], 1: [0, 0, 1], 2: [0, 0, 2], 3: [0, 0, 3], ...,
# 10: [0, 1, 0], 11: [0, 1, 1], 12: [0, 1, 2], ...,
# 999: [9, 9, 9]}
#
# Your expression should work for any base. For example, 
# if you instead assign 2 to base and assign {0,1} to digits, 
# the value should be:
#
# {0: [0, 0, 0], 1: [0, 0, 1], 2: [0, 1, 0], 3: [0, 1, 1],
# ..., 7: [1, 1, 1]}

base = 10
digits = set(range(base))
