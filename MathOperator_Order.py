Math_1 = (9-7)*2**3+10%6//-1*2-1
print(Math_1) # Result: 7

Math_2 = 15 / 3 * 2 * 2 - (3 + 4)
print(Math_2) # Result: 248.96

# Orders
# 1st -> ()
# 2nd -> **
# 3rd -> %,/,//,*
# 4rd -> + & -

# Steps how system calculate base on above order
# Example: (9-7) * 2 ** 3 + 10 % 6 // - 1 * 2 - 1

# Step 1: 2 * 2 ** 3 + 10 % 6 // -1 * 2 - 1
# Step 2: 2 * 8 + 10 % 6 // -1 * 2 -1
# Step 3: 16 +- 8 - 1
# Step 4: 7