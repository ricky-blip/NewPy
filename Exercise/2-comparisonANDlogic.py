# Exercise 2

print ("==========#1==========")
# Checking in between number
# +++++7-------20++++++++++
# <7 >20

# CONVERSION
inputUser = int(input("Type number less than 7 or more than 20 :"))
print("Your Input Number is =", inputUser)

# +++++7-------
# Checking less than 7
isLessThan = (inputUser < 7)

print("Less Than 7 =", isLessThan)

# ---------20++++++++++
# Checking more than 20
isMoreThan = (inputUser > 20)

print("More Than 20 =", isMoreThan)

# LOGICAL
# +++++7-------20++++++++++
# <7 OR >20
isCorrect = isLessThan or isMoreThan
print(isLessThan, "OR", isMoreThan, "=", isCorrect)
print("Number Your Input is =", isCorrect)

print ("==========#2==========")
# Checking in between number
# ------5+++++++30--------
# Slicing >5 <30

# CONVERSION
inputUser = int(input("Type number more than 5 and less than 30 :"))
print("Your Input Number is =", inputUser)

# -----5+++++++
# Checking more than 5
isMoreThan = (inputUser > 5)

print("More Than 5 =", isMoreThan)

# ++++++++++30-------
# Checking less than 30
isLessThan = (inputUser < 30)

print("Less Than 30 =", isLessThan)

# LOGICAL
# ------5+++++++30--------
# >5 AND <30
isCorrect = isMoreThan and isLessThan
print(isMoreThan, "AND", isLessThan, "=", isCorrect)
print("Number Your Input is =", isCorrect)

print ("\n====================#3====================\n")
# -------0++++++++++5----------8+++++++++++11-----------
# >0 <5 >8 <11
# (>0 AND <5) | OR | (>8 AND <11)

# CONVERSION
inputUser = int(input("Type number (more than 0 and less than 5) OR (more than 8 and less than 11 :"))
print("Your Input Number is =", inputUser)

# -------0++++++++++
# Checking more than 0
isMoreThan0 = (inputUser > 0)
print("More Than 0 =", isMoreThan0)

# ++++++++++5----------
# Checking less than 5
isLessThan5 = (inputUser < 5)
print("Less Than 5 =", isLessThan5)

zeroANDfive = isMoreThan0 and isLessThan5
print(isMoreThan0, "AND", isLessThan5,"=","-----",zeroANDfive)

print("------------------------OR")

# ----------8+++++++++++
# Checking more than 8
isMoreThan8 = (inputUser > 8)
print("More Than 8 =", isMoreThan8)

# +++++++++++11-----------
# Checking less than 11
isLessThan11 = (inputUser < 11)
print("Less Than 11 =", isLessThan11)

eightANDeleven = isMoreThan8 and isLessThan11
print(isMoreThan8, "AND", isLessThan11,"=","-----",eightANDeleven)

print("------------------------===RESULT")
# LOGICAL
# -------0++++++++++5----------8+++++++++++11-----------
# >0 AND <5 OR >8 AND <11
isCorrect = zeroANDfive or eightANDeleven
print(zeroANDfive,"OR",eightANDeleven, "=", isCorrect)
print("Number Your Input is =", "-----",isCorrect)


print ("\n====================#4====================\n")
# +++++++0----------5++++++++++8-----------11+++++++++++
# <0 >5 <8 >11
# (<0 OR >5) AND (<8 OR >11)

# CONVERSION
inputUser = int(input("Type number (lessThan 0 OR moreThan 5) AND (lessThan 8 OR moreThan 11)"))
print("Your Input Number is =", inputUser)

# +++++++0----------
# Checking less than 0
islessThan0 = (inputUser < 0)
print("Less Than 0 =", islessThan0)

# ----------5++++++++++
# Checking more than 5
ismoreThan5 = (inputUser > 5)
print("More Than 5 =", ismoreThan5)

zeroORfive = islessThan0 or ismoreThan5
print(islessThan0, "OR", ismoreThan5,"=","-----",zeroORfive)

print("------------------------AND")

# ++++++++++8-----------
# Checking less than 8
islessThan8 = (inputUser < 8)
print("Less Than 8 =", islessThan8)

# -----------11+++++++++++
# Checking more than 11
ismoreThan11 = (inputUser > 11)
print("More Than 11 =", ismoreThan11)

eightOReleven = islessThan8 or ismoreThan11
print(islessThan8, "OR", ismoreThan11,"=","-----",eightOReleven)

# LOGICAL
# +++++++0----------5++++++++++8-----------11+++++++++++
# <0 OR >5 AND <8 OR >11
isCorrect = zeroORfive and eightOReleven
print(zeroORfive,"and",eightOReleven, "=", isCorrect)
print("Number Your Input is =", isCorrect)
