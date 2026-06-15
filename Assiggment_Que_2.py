#Write a code  a= 10 , b=10 using id function.It is int data type which stores data/value in same memory address.

a = 10
b = 10 

print(id(a))  # a=10 - output - Returns same Memory Address - 140726350103960
print(id(b))  # b=10 - output - Returns same Memory Address - 140726350103960

# Writa a code a= [10] and b = [10] using id function. It is list data type which stores data/value in different memory address for each list. 

a = [10]
b = [10]

print(id(a)) # a = [10] # a=[10] - output - Returns different Memory Address - 2684403758528
print(id(b)) # b = [10] # b=[10] - output - Returns different Memory Address - 2684403642688
