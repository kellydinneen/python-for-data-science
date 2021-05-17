# Addition, subtraction
print(5 + 5)
print(5 - 5)

# Multiplication, division, modulo, and exponentiation
print(3 * 5)
print(10 / 2)
print(18 % 7)
print(4 ** 2)

# How much is your $100 worth after 7 years?
print(100 * 1.1 ** 7)

# ----------------------------------------------------------------------------

# Variable assignment
savings = 100
growth_multiplier = 1.1
desc = "compound interest"

# Assign product of growth_multiplier and savings to year1
year1 = growth_multiplier * savings

# Print the type of year1
print(type(year1))

# Assign sum of desc and desc to doubledesc ==> concatenate
doubledesc = desc + desc

# Print out doubledesc
print(doubledesc)

# ----------------------------------------------------------------------------
year7 = savings * growth_multiplier ** 7

# Fix the printout
print("I started with $" + str(savings) + " and now have $" + str(year7) + ". Awesome!")

# Definition of pi_string
pi_string = "3.1415926"

# Convert pi_string into float: pi_float
pi_float = float(pi_string)