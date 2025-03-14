# SOLUTION WITH INTEGER
# Variables holding the prices of the six items:
# All of the variables were multiplied by 100 to make them into integers so that there would be no approximation errors
# when they were added together.

pasta = 16.68 * 100  # penne 16 oz, pack of 12
sauce = 6.98 * 100  # Arrabiata sauce 24oz
garlic = 16.78 * 100  # 20 pack garlic clove
seasoning = 15.26 * 100  # Italian Seasoning
bread = 3.00 * 100  # Baguette twin pack
meatballs = 4.39 * 100  # 12 oz bag of meatballs
# subtotal is the sum of all prices before any sales taxes or discounts are added

subtotal_Integer = (pasta + sauce + garlic + seasoning + bread + meatballs) / 100
print(subtotal_Integer)

# SOLUTION WITH ROUND
pasta = 16.68  # penne 16 oz, pack of 12
sauce = 6.98  # Arrabiata sauce 24oz
garlic = 16.78  # 20 pack garlic clove
seasoning = 15.26  # Italian Seasoning
bread = 3.00  # Baguette twin pack
meatballs = 4.39  # 12 oz bag of meatballs
# A subtotal is the sum of all prices before any sales taxes or discounts are added.

# round() was used to round the subtotal to 2 decimal places since the sum of any amount of numbers that all have 2
# numbers after the decimal will always have 2 numbers after its decimal point.

subtotal_Round = round((pasta + sauce + garlic + seasoning + bread + meatballs), 2)
print(subtotal_Round)