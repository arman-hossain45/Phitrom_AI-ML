# length = int(input("lenght of a rectangle: "))
# breadth = int(input("Breadth of a rectangle: "))
# area = length * breadth
# print("Area of a rectangle is: ", area)

# number = eval(input("Enter a number: "))
# string = input("Enter a string: ")
# print(type(number))
# print(type(string))

# x = 20.345123
# x = format(x, ".3f")
# print(x)

# x = 20.345123
# x = format(x, "<7.3f")

# print(x)
# print(type(x))

# x = 20.345123
# x = eval (format(x, "<7.3f"))
# print(type(x))

#python inbuilt function
# import math
# print(math.ceil(10.23))#here print 11
# print(math.floor(10.23))#here print 10 
# print(math.exp(10.23))
# print(math.log(2.7))
# print(math.log(10, 10))
# print(math.sqrt(16))

#the ord and chr functions

# print(ord("A")) #Returns ACII value of Character 'A' is 65
# print(ord("z")) 
# print(chr(65)) #returns character A which assci value is 65
#print(round(1.5))#it wil print 2 as usall ceil function 

# print("{:,}".format(100000))#100,000

# print(min(10,10,10))
# print(max(-1,-4,-10))


# from math import pi
# radius = eval(input("Enter radius of a circle: "))
# if radius > 0:
#  area = pi * radius * radius
#  print("Area of the circule is = ", format(area,".2f"))
#  circumference = 2*pi*radius
#  print("Circumference of the circule is = ", format(circumference,".2f"))
# else:
#  print("Please give right input")

 
 
# x = 10
# tst = isinstance(x, int)
# print(tst)


#PROGRAM 02: Write a program to calculate the salary of a medical representative considering
#the sales bonus and incentives offered to him are based on the total sales. If the sales exceed or
#equal to ‘1,00,000 follow the particulars of Column 1, else follow Column 2

# sales = float(input("Enter total sales of the month: "))
# basic = 4000

# conveyance = 500
# da = 110 * basic / 100   # DA = 110% of basic

# if sales >= 100000:
#     hra = 20 * basic / 100
#     incentive = sales * 10 / 100
#     bonus = 1000
# else:
#     hra = 10 * basic / 100
#     incentive = sales * 4 / 100
#     bonus = 500

# salary = basic + hra + incentive + bonus + conveyance + da

# print("Salary Receipt of Employee")
# print(" Total Sales       = ", sales)
# print(" Basic             = ", basic)
# print(" HRA               = ", hra)
# print(" DA                = ", da)
# print(" Incentive         = ", incentive)
# print(" Bonus             = ", bonus)
# print(" Conveyance        = ", conveyance)
# print(" Gross Salary      = ", salary)

#ROGRAM 3: Write a program that prompts a user to enter two different numbers. Perform basic
#arithmetic operations based on the choices.

# first_number = float(input("Enter the first number: "))
# second_number = float(input("Enter the second number: "))

# print("Which operation you want to do: ")
# print("1) Addition")
# print("2) Subtraction")
# print("3) Multiplication")
# print("4) Division")

# choice = int(input("Enter your choice: "))

# if choice == 1:
#     text = f"Addition of {first_number} and {second_number} is: {first_number + second_number}"
#     print(text)
# elif choice == 2:
#     text = f"Subtraction between {first_number} and {second_number} is: {first_number - second_number}"
#     print(text)
# elif choice == 3:
#     text = f"Multiplication of {first_number} and {second_number} is: {first_number * second_number}"
#     print(text)
# elif choice == 4:
#     if second_number != 0:
#         text = f"Division of {first_number} and {second_number} is: {first_number / second_number}"
#     else:
#         text = "Error! Division by zero is not allowed."
#     print(text)
# else:
#     print("Invalid choice! Please select 1, 2, 3, or 4.")


#Write a program to determine the character entered by user
# char = input("Press any key: ")
# if(char.isalpha()):
#  print("You entered a character")
# elif(char.isdigit()):
#  print("You entered a digit")
# elif(char.isspace()):
#  print("You entered a space")
# elif(char.isdecimal()):
#  print("You entered a decimal")

#loop control statement in python 
#1 write a program to add 10 consecute numbers starting from 1 using while loop
# count=0
# sum=0

# while count<=10:
#  sum=sum+count 
#  count=count+1

# print(sum)

# #using for loo[p
# sum=0
# for i in range(11):
#  sum=sum+i

# print(sum)



# d=dict(name="arman",age=27)
# print(d)

# text="my name is %(name)s.I am %(age)d years old"%d

# print(text)#here s for string and d for int 


#write a program that store a number square in a dictionany 

# def square(num):
#     d=dict()
#     for i in range(1,num+1):
#         if i  not in d:
#             d[i]=i*i
#     return d

# print("Square of the number is :")
# a=square(5)
# print(a)

#Program 04: Write a program to pass a list to a function. Calculate the total number of positive
#and negative numbers from the list and then display the count in terms of dictionary

# def posNeg(lst):
#     d=dict()
#     d["pos"]=0
#     d["neg"]=0
#     for i in lst:
#         if i>0:
#             d['pos']+=1
#         else:
#              d["neg"]+=1

#     return d
# lst=[1,-2]
# a=posNeg(lst)
# print(a)

#excricise in list 

#Problem 01: Create a list of five elements. Pass the list
#to a function and compute the average of five numbers.


# def avg(lst):
#     n=len(lst)
#     print('lst = ',lst)
#     m=sum(lst)
#     a=m/n
#     return a

# lst=[1,23,45,56]
# b=avg(lst)
# print('avarage of the all list element is =',b)

#Problem 02: Write a function that accepts two positive integers, viz. a and b and returns a list of
#all the even numbers between a and b (including a and not including b).

# lst=list(range(10,20))
# print(lst)

# def evenlist(start,end):
#     even=[]
#     lst=list(range(start,end))
#     print('list is =',lst)
#     for item in lst:
#         if item%2==0:
#             even.append(item)
#     return even

# a=evenlist(10,20)
# print('Even list of the given range is =',a)

#Problem 03: Write a function is_Lst_Palindrome(Lst) to check whether a list is palindrome. It
#should return True if Lst is palindrome and False if Lst is not palindrome

# def palindrome(lst):
#     reverse=lst[::-1]
#     if lst==reverse:
#         print('lst is a palimdrome ')
#     else:
#         print('list is a not palindrome')

# lst=[1,1,1,1,1]
# print(palindrome(lst))

#Write a function check_duplicate(Lst) which returns True if a list Lst contains duplicate elements. 
#It should return False, if all the elements in the list Lst are unique.

# def duplicate(lst):
#     n=len(lst)
#     temp=0
#     print('list is = ',lst)

#     for i in range(0,n):
#         for j in range(i,n-1):
#             if lst[i]==lst[i+1]:
#                 temp+=1
#                 return True
#             else:
#               return False

# l=[1,1,2,3,4,2,3,4]
# print(duplicate(l))
# l1=[1,23,4,5,6,78,9]
# print(duplicate(l1))

#Problem 01: Write the function countB(word) which takes a word as the argument
#and returns the number of ‘b’ in that word.
# def countB(word):
#  print(word)
#  count = 0
#  for char in word:
#   if char == "b":
#    count += 1
#  return count
# countOfB = countB("abba abbabababab")
# print("Number of 'b' = ", countOfB)


# print("Hollow Rectangle pattern")
# def hollow_rectangle(total_rows, total_colums):
#    for i in range(1, total_rows+1):
#     for j in range(1, total_colums+1):

#      if i==1 or i==total_rows or j==1 or j==total_colums:

#            print("*", end=" ")
#     else:
#       print(" ", end=" ")
#    print()
# hollow_rectangle(4,5)

# nums = [10, 20, 30, 40, 50, 60]
# print(nums[1:4])   # middle slice
# print(nums[-3:])   # last 3
# print(nums[::2])   # step slice
# print(nums[::-1])  # reverse
# print(nums[:-3])


# Sample data: list of user dictionaries with a list of orders for each user
# users_data = [
#     {"user_id": 1, "name": "Alice", "orders": [{"order_id": "A1", "amount": 150}, {"order_id": "A2", "amount": 200}]},
#     {"user_id": 2, "name": "Bob", "orders": [{"order_id": "B1", "amount": 50}]},
#     {"user_id": 3, "name": "Charlie", "orders": []}
# ]

# # Calculate the total amount spent by each user using a loop
# print("Total amount spent by each user (using loop):")
# for user in users_data:
#     total_spent = 0
#     for order in user.get("orders", []): # Use .get() for safe access
#         total_spent += order.get("amount", 0) # Use .get() for safe access
#     print(f"{user.get('name', 'N/A')}: ${total_spent}")

# # Get a list of all order amounts across all users using a nested comprehension
# all_order_amounts = [order.get("amount", 0) for user in users_data for order in user.get("orders", [])]
# print("\nAll order amounts:", all_order_amounts)

# # Create a dictionary mapping user_id to the number of orders using a dictionary comprehension
# orders_count_by_user = {user.get("user_id"): len(user.get("orders", [])) for user in users_data}
# print("Number of orders per user:", orders_count_by_user)

# nested_sequence=[[x**2 for x in range(i,i+5)if x%2==0] for i in range(1,10,3) ]

# print(nested_sequence)

# square=[x**2 for x in range(6)]
# print(square)
# evens=[x for x in range(10) if x%2==0]
# print(evens)

# map={x:x**2 for x in range(5)}#here its a dictionary 
# print(map)

# print(7/2)
# print(7//2)


#list comprehention 
#normal way to declaire a list in sample way

# lst=[10,20,30,40,50,60,70,80,90,100]

# for i in lst:
#     a=i*(9/5)+32
#     print(a)


# farhen=[i*(9/5)+32 for i in lst]
# print(farhen)

lst=[10,20,30,40,50,60,70,80,90,100]
#print only even index as a list comprehention 

farhen=[i*(9/5)+32 for i in lst if i%2==0]
print(farhen)

