# #1
# def number_of_food_groups(): 
#     return 5
# print(number_of_food_groups())
# this will only show 5 in the terminal


# # #2
# def number_of_military_branches():
#     return 5
# print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches()) 
# # error number of days is not defined 


# #3
# def number_of_books_on_hold():
#     return 5
#     return 10
# print(number_of_books_on_hold()) 
# # will return 5 in the terminal the return statement ends the function no other code will output


# #4
# def number_of_fingers():
#     return 5
#     print(10)
# print(number_of_fingers()) 
# # will show 5 in the terminal for reasons stated above


# #5
# def number_of_great_lakes():
#     print(5)
# x = number_of_great_lakes()
# print(x) 
# # 5 will print to the console, none will print for x number of great lakes not defined


# #6
# def add(b,c):
#     print(b+c)
# print(add(1,2) + add(2,3))
# #error not the proper way to add


# #7
# def concatenate(b,c):
#     return str(b)+str(c)
# print(concatenate(2,5))
# #25 is printed to the terminal


# #8
# def number_of_oceans_or_fingers_or_continents():
#     b = 100
#     print(b)
#     if b < 10:
#         return 5
#     else:
#         return 10
#     return 7
# print(number_of_oceans_or_fingers_or_continents())
# #the if statement is not true, and return 10 to the terminal


# #9
# def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
#     if b<c:
#         return 7
#     else:
#         return 14
#     return 3
# print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
# print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
# print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
# #7,14,21 prints to terminal

# #10
# def addition(b,c):
#     return b+c
#     return 10
# print(addition(3,5))
# #8 prints to terminal


# #11
# b = 500
# print(b)
# def foobar():
#     b = 300
#     print(b)
# print(b)
# foobar()
# print(b)
# # 500, 500, 300, 500, prints to the terminal


# #12
# b = 500
# print(b)
# def foobar():
#     b = 300
#     print(b)
#     return b
# print(b)
# foobar()
# print(b)
# # 500, 500, 300, 500, prints to the terminal

# #13
# b = 500
# print(b)
# def foobar():
#     b = 300
#     print(b)
#     return b
# print(b)
# b=foobar()
# print(b)
# # 500, 500, 300, 500, prints to the terminal

# #14
# def foo():
#     print(1)
#     bar()
#     print(2)
# def bar():
#     print(3)
# foo()
# 1, 2, 3, prints to the terminal

#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)
#1, 3, 5, 10 prints the the terminal