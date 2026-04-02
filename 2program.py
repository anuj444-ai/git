# a = 5
# b = 10

# sum = a + b
# print(sum)


# #more lines of code

# a = 2
# b = 10

# sum = a + b
# print(sum)

# def calc_sum(a, b):
#     sum = a + b
#     print(sum)
#     return sum

# calc_sum(5, 10)


# #more lines of code

# calc_sum(2, 10)

# #more lines of code

# calc_sum(12, 17)

# #function definition
# def calc_sum(a, b): #paraemeters
#     return a + b

# sum = calc_sum(178, 2) #function call; arguments
# print(sum)


# def  print_hello():
#     print("hello")

# print_hello()


#average of 3 numbers

# def calc_avg(a, b, c):
#     sum = a + b + c
#     avg = sum / 3
#     print (avg)
#     return avg

# calc_avg(98, 97, 95)

# print("globalcollege","anujdubey") #sep = " "

# print("globalcollege") #sep = " "
# print("anujdubey") #end = "\n"

# print("globalcollege", end="$") #sep = " "
# print("anujdubey") #end = "\n"

# def cal_prod(a=1, b=1):
#     print(a * b)
#     return a * b

# cal_prod(1)

# def cal_prod(a=4, b=2):
#     print(a * b)
#     return a * b

# cal_prod(10)

# cities = ["jabalpur", "bhopal", "indore", "gwaliour", "katni", "rewa"]
# heros = ["thor" , "ironman", "captain america"]

# def print_len(list):
#     print(len(list))

# print_len(cities)
# print_len(heros)


# cities = ["jabalpur", "bhopal", "indore", "gwaliour", "katni", "rewa"]
# heros = ["thor" , "ironman", "captain america"]

# def print_len(list):
#    print(len(list))

# def print_list(list):
#    for item in list:
#         print(item, end=" ")

# print_list (heros)
# print_list (cities)   
# print() 


# n = 5

# def cal_fact(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact *= i

#     print(fact)

# cal_fact(6)    


# def converter(usd_val):
#     inr_val = usd_val * 83
#     print(usd_val, "USD =", inr_val, "INR")

# converter(100)
    
# def show(n):
#     print(n)

# show(5) # 5, 4, 3, 2, 1    


# def show(n):
#     if(n ==0):
#         return
#     print(n)
#     show(n-1)

# show(5) # 5, 4 = n-1, 3 =n-2, 2 = n-3, 1   

# def show(n):
#     if(n ==0):
#         return
#     print(n)
#     show(n-1)
#     print("END")

# show(3) # 5, 4 = n-1, 3 =n-2, 2 = n-3, 1  

# def fact(n):
#     if(n == 1 or n ==0):
#         return 1
#     return fact(n-1) * n

# print(fact(2))

# def fact(n):
#     if(n == 1 or n ==0):
#         return 1
#     return fact(n-1) * n

# print(fact(4)) 


# def fact(n):
#     if(n == 1 or n ==0):
#         return 1
#     return fact(n-1) * n

# print(fact(5))


# def fact(n):
#     if(n == 1 or n ==0):
#         return 1
#     return fact(n-1) * n

# print(fact(6))


# def calc_sum(n):
#     if(n == 0):
#         return 0
#     return calc_sum(n-1) + n

# sum = calc_sum(1)
# print(sum)

# def calc_sum(n):
#     if(n == 0):
#         return 0
#     return calc_sum(n-1) + n

# sum = calc_sum(10)
# print(sum)

# def print_list(list,idx=0):
#     if(idx == len(list)):
#         return
#     print(list[idx])
#     print_list(list, idx+1)

# fruits = ["mango", "litichi", "apple", "banana"]

# print_list(fruits)

# f = open("demo.txt", "r")
# data = f. read()
# print(data)
# print(type(data))
# f.close()




# f = open("demo.txt", "r")

# data = f.read()
# print(data)

# line1 = f. readline()
# print(line1)



# f = open("demo.txt", "r")
# line2 = f. readline()
# print(line2)

# f.close()


# f = open("demo.txt", "r")

# data = f. read(5)
# print(data)

# f.close

# f = open("demo.txt", "r")

# line1 = f.readline()
# print(line1) 

# line2 = f.readline()
# print(line2)

# f.close


# f = open("demo.txt", "r")

# data = f.read()
# print(data)

# line1 = f.readline()
# print(line1) 

# line2 = f.readline()
# print(line2)

# f.close

# f = open("demo.txt", "r")

# line1 = f.readline()
# print(line1) 

# line2 = f.readline()
# print(line2)

# line3 = f.readline()
# print(line3)

# line4 = f.readline()
# print(line4)

# line5 = f.readline()
# print(line5)

# f.close


# f = open("demo.txt", "w")

# f.write("I want learn javascript  tommorw. 123")

# f.close


# f = open("demo.txt", "a")

# f.write("jai shree ram jai hanuman jai maa kaali jai jagdamb. 123456789")

# f.close



# f = open("demo.txt", "a")

# f.write("\n jai shree ram jai hanuman jai maa kaali jai jagdamb. 123456789")

# f.close


# f = open("sample.txt", "a")
# f.close()


# f = open("sample.txt", "w")
# f.close()


# f= open("demo.txt", "r+")
# f.write ("abc")
# print(f.read())
# f.close()

# f= open("demo.txt", "w+")
# # f.write ("abc")
# print(f.read())
# f.write("abc")
# f.close()

# with open("demo.txt", "r") as f:
#     data = f.read()
#     print(data)

# with open("demo.txt", "w") as f:
#     f.write("new data")

# import os

# os.remove("sample.txt")


# with open("practice.txt", "w") as f:
#     f.write("this is a practice file for python programming. 1234567890")
#     f.write("hi everyone, welcome to global college. 1234567890/n")


# with open("practice.txt", "w") as f:
#     f.write("Hi evryone/nwe are learningfile I/O/n")
#     f.write("using java./nI like programming in java.")
    

# with open("practice.txt", "r") as f:
#     data = f.read()

# new_data = data.replace("java", "python")    
# print(new_data)

# with open("practice.txt", "w") as f:
#     f.write(new_data)

# word = "learning"
# with open("practice.txt", "r") as f:
#     data = f.read() 
#     if(data.find(word) != -1):
#         print("found")
#     else:
#         print("not found")    
        

# def check_for_word(word):
#     word = "xlearning"
#     with open("practice.txt", "r") as f:
#         data = f.read() 
#         if(data.find(word) != -1):
#             print("found")
#         else:
#             print("not found")
# check_for_word("learning")

# def check_for_word(word):
#     word = "xlearning"
#     with open("practice.txt", "r") as f:
#         data = f.read() 
#         if(data.find(word) != -1):
#             print("found")
#         else:
#             print("not found")

# def check_for_line():
#     word = "programming"
#     data = True
#     line_no = 1
#     with open("practice.txt", "r") as f:
#         while data:
#             data = f.readline()
#             if(word in data):
#                 print( line_no)
#                 return
#             line_no += 1

#     return -1

# check_for_line()



# with open("practice.txt", "r") as f:
#     data = f.read()
    
#     print(data)
            
# class Student:
#     name = "Anuj Dubey"

# s1 = Student()
# print(s1.name)

# s2 = Student()
# print(s2.name)

# class car:
#     colour = "red"

# car1 = car()
# print(car1.colour)

# class car:
#     colour = "black"
#     brand = "scorpio"


# car1 = car()
# print(car1.colour)
# print(car1.brand)


# class car:
#     colour = "black"
#     brand = "scorpio"


# car1 = car()
# print(car1.colour)
# print(car1.brand)

# class car:
#     colour = "grey"
#     brand = "scorpio"

# car2 = car()
# print(car2.colour)
# print(car2.brand)


# class student:
#     name = "Anuj Dubey"
#     def __init__(self):
#         print("self")
#         print("adding new student in database..")
    
# s1 = student()
# print(s1)


# class student:
#     name = "Anuj Dubey"
#     def __init__(self, name):
#         self.name = name
#         print("self")
#         print("adding new student in database..")
    
# s1 = student("Anuj Dubey")
# print(s1.name)

# class student:
    
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#         print("adding new student in database..")
    
# s1 = student("Anuj Dubey", 85)
# print(s1.name)
# print(s1.marks)

# s2 = student("Rahul Dubey", 90)
# print(s2.name)  
# print(s2.marks)



# class student:

#     #default constructor
#     def __init__(self):
#         pass
    
#     #parameterized constructor
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#         print("adding new student in database..")
    
# s1 = student("Anuj Dubey", 85)
# print(s1.name)
# print(s1.marks)

# s2 = student("Rahul Dubey", 90)
# print(s2.name)  
# print(s2.marks)







