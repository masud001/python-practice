# identity operator

# s = input()
# e = input()
# w = input()
# 36
# 618
# 78
import math

for num in range(36, 618, 78):
    f_value = (num - 32) * 5 / 9
    if(f_value > 0):
        print(num, math.floor(f_value))
    else:
        print(num, math.ceil(f_value))




