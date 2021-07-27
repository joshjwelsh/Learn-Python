# Basic Data Types
# Check out the full list of types https: // www.w3schools.com/python/python_datatypes.asp

str_var_1 = 'Hello World' 

# Strings can be created using double quotes "" or single quotes ''
str_var_2 = "I won't be going to Rolling Loud this year." 

float_var = 3.142857
int_var = 33_144_224 # This is the same thing as 33144224 


# Valid Variable Names

balance = 400
currentBalance = 200
current_balance = 400
_spam = '2222'
_ = False
SPAM = int(_spam)
prime_1st = "2 is a prime number"


# variables can be assigned new types during runtime
# However it is good practices for a variable to maintain its type throughout runtime

var_1 = 10
print(var_1)
print("The type: ", type(var_1))
var_1 = 3.14
print(var_1)
print("The type: " ,type(var_1))






















# Use commma to add output
sVar = 'Hello World'
print(sVar)



# Arthmetic 
x = 1 + 2
y = x * 2
z = y ** x # Power y ^ x 

a = 5 
b = a / 2 # Division with remainder: it will return a float
c = a // 2 # Floored division 
d = a % 2 # Modulus: return the remainder

print('a: ', a, '\n', 'b:',b, '\n', 'c:', c, '\n', 'd:', d, '\n')

# Multiplication is applicable to strings
print(sVar * 10) 





# Formating Strings in Python3
formatedString = f"Variable: {a}\nNormal Division: {b}\nFloored Division: {c}\nModulo: {d}\n"
print(formatedString)
print("Length of formated string is ", len(formatedString), " characters")



