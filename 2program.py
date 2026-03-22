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
