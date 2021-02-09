# Write Python 3 code in this online editor and run it.
import random
import string 

#how many passwords and lenth
a = how_many_passwords_do_you_want = 15
b = how_long_do_you_want_the_password_to_be = 22
#keep this empty if you dont want any padding. NOTE: password lenth will change 
p = padding_after_each_random_letter = ""

#if you dont want symbols for example, change the 4th True to False
upper, lower, digit, symbol = True, True, True, False

#this will consist of all the options you enabled
mix = ""


#this will check if its true or not and if its true it will add it to mix variable 
if (upper):
    mix += string.ascii_uppercase
if (lower):
    mix += string.ascii_lowercase
if (digit):
    mix += string.digits
if (symbol):
    mix += string.punctuation


#prints certain amount of passwords with a specific length
for i in range(a):
    print(p.join(random.sample(mix, b)))


