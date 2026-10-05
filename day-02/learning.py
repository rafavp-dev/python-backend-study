#==========================================================
# DAY 2 - Goal is to study and understand PYTHON CONDITIONS
#==========================================================

# Topics studied:
# - if 
# - elif 
# - else
# - <
# - >
# - ==
# - !=
# - <=
# - >=
# - comparison operators
# - and
# - or 
# - not


##IF: an “if statements” is to compare… So A = 3 and B = 40 so when need to print we create the code with IF to print/check IF A is bigger than B. ##
# Example:
a = 3
b = 400
if b > a:
  print("b is greater than a")

##ELSE: Else is for to catch anything which that is not caught by the code that you have. ##
# Example:
a = 100
b = 50
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

## in this case we have else to print "a is greater than b" because on the line with ELSE or ELIF we would not get any answer. ##
## Just for remark, we don’t need to have a IF and ELIF to have a ELSE, we can have an ELSE sentence without an ELIF. Also the ELSE statement need to be the last in the code. ##
a = 100
b = 50
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

## ELIF: It’s a IF but a second comparison. So is kind  like…. if the previous conditions were not true, then try this condition (elif) ##
# Example:

a = 50
b = 50
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
#we can have as many elif statements as we need. Python will check all the condition from the top to the bottom and as soon as find a condition that is true, will show the result. Just have in mind that only the first true condition will be executed. So In case you have multiple true conditions, Python will stop on the first matching.

## COMPARISON OPERATORS: ##
# > : Greater than: ex: x > y 
# < : Less than: ex: x < y
# == : Equal: ex: x == y 
# != : Not equal: ex: x != y
# >= : Greater than or equal to: ex: x >= y 
# <= : Less than or equal to: ex: x <= y 

# Example would be:
x = 5
y = 3

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)


## LOGICAL OPERATORS: ##
## All will return as true or false, will be comparing the code and check if is true or false. ##
## And: it will return as true if both statements are true  ## 

x = 56
print(x > 0 and x < 10)

## Or:  it will return as true if one of the statements is true ##

x = 5
print(x < 5 or x > 10)

## Not: Its reverse the result, return FALSE if the result is TRUE ##

x = 5
print(not(x > 3 and x < 10))

# PYTHON INDENTATION: # 
# Indentation is about the space at the begin of a code line, and for Python is important as t uses indentation to indicate the block of a code. #
# So in case you get a IndentationError, it is because a line in your code is with space wrong. #
# Ex of syntax error:
if 5 > 2:
print("Five is greater than two!")
 or
if 5 > 2:
 print("Five is greater than two!")
        print("Five is greater than two!")


# EXERCISES DAY 2

# If condition, wrote below as first attemp:
age = 30
if age > 18:
  print ("You are an adult")

# Got error, after checking notes, realised that had letters I for if and P for print in capital letters, i amended and worked.

age = 30
if age > 18:
	print (“You are an adult”)


# ELSE condition, wrote below as first attempt:

age = 16
if age > 18:
  print ("You are an adult")
else:
  print ("You are not an adult")


# Elif condition, wrote below as first attempt:

age = 15
if age > 18:
  print ("You are an adult")
if age 13 >= 17:
print ("You are a teenager")
elif:
	print ("You are a child")


# Got syntax error, had to check notes again:

age = 15
if age >= 18:
    print("You are an adult")
elif age <= 13 <= 17:
    print("You are a teenager")
else:
    print("You are a child")

# Got error again, line 1, age not defined… checking…
# Got right on third attempt. Correct was  age >= and not only >

age = 15
if age >= 18:
    print("You are an adult")
elif 13 <= age <= 17:
    print("You are a teenager")
else:
    print("You are a child")



# Comparison operators, wrote below as first attempt:
# Equal ==
age = 30
if age == 30:
	print ("age is correct")


# Not equal to !=
age = 25
if age != 30:
	print ("age is not 30")


# < and <=

Temperature = 15
If temperature <= 20:
	print (“Cold”)


# Also did 

temperature = 25
if temperature <= 20:
    print("Cold")
elif temperature > 20:
    print("Warm")


temperature = 25
if temperature <= 20:
    print("Cold")
else:
    print("Warm") 


# Now practising logical operators:

age = 25
has_ticket = True
if age >= 18 and has_ticket == True:
    print("You can enter") 
 


has_cash = False
has_card = True
if has_card or has_cash:
    print("Payment possible") 
is_raining = False
if not is_raining:
    print("You can go outside") 


Combining what was studied today:

age = 25
has_ticket = True
is_banned = False
if age >= 18 and has_ticket and not is_banned:
    print("You can enter the event")
else:
    print("Access denied")

# Today's learning focused on IF, ELSE, ELIF, COMPARISON OPERATORS,
# LOGICAL OPERATORS and PYTHON INDENTATION.
# I was able to understand and apply these concepts through exercises.