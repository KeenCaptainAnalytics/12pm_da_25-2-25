# logical operators => and or not  comparision

# Q= > take an input from user and tell if its an odd number 
#     2> even number 
    
#     num = 56
#     even ? True
#     odd?   False
    
# num = 23+34+23

# num = input("enter some number  :  ") 
# num = int(num)

# isEven = (num % 2) == 0
# print("is the number even? : ", isEven)

# # isOdd = (num % 2 ) ==1
# print("is the number odd? : ", not isEven)

# Q = > num => divisible by (2 and 3) or  (2 and 5) 
# 1: is my number divisible by either (2 and 3) or  (2 and 5)?
# 2: 1: is my number not divisible by either (2 and 3) or (2 and 5)?

a = input("enter a number : ")
num = int(a)

isDiv = ((num % 2 ==0 ) and    (num % 3 == 0) )
                        or
        ((num % 2 == 0) and (num % 5 == 0))

print("is my number divisible by 2 and 3 or 2 and 5? : ", isDiv)
print("is my num not divisible by 2 and 3 or 2 and  5? : ", not isDiv)




# Q = > num => divisible by 2 3 5 all
# 1: is my number divisible by 2 3 and 5?
# 2: is my num not divisible by 2 3 and 5?

# a = input("enter a number : ")
# num = int(a)

# isDiv = (num % 2 ==0 ) and    (num % 3 == 0) and (num % 5 == 0)

# print("is my number divisible by 2 3 and 5? : ", isDiv)
# print("is my num not divisible by 2 3 and 5? : ", not isDiv)


# True True True => True 
# True False True = > False









