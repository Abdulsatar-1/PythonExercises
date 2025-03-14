# example = "Hello world"
#
# def loc_ex():
#     example = "This is a string"
#     return example
#
# print(example)
# print(loc_ex())


# --------------------------------------------------------------------------
# Local variable cannot be used by code in the global scope
# def loc_ex():
#     breakfast = "eggs"
#     return breakfast
#
# loc_ex()
# print(breakfast)

# --------------------------------------------------------------------------
# Local variable cannot be accessed by code in a local scope
# def print_glob():
#     print(glob_var)
#
# glob_var = "Hello world"
# print_glob()

# --------------------------------------------------------------------------
# def loc_ex1():
#     fruit = ("Apple")
#     print(fruit)
#
# def loc_ex2():
#     fruit = ("Banana")
#     print(fruit)
#
# fruit = ("Orange")
# loc_ex1()
# loc_ex2()
# print(fruit)
# --------------------------------------------------------------------------

# Global Statement
def loc_ex():
    fruit = ("Apple")
    print(fruit)

fruit = "Orange"
loc_ex()
print(fruit)
