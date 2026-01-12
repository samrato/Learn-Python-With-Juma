# # # def lastCharater(text):
# # #     return len(text) > 0 and text[-1] == ";"
     
# # # print(lastCharater("hello;"))
# # # Check if the string is not empty AND last character is a colon
# # # a code that will add space to that if its passs option 1 using elif 



# # def Lastcharacer(text):

# #     # Check if the last character is a colon
# #     if len(text) > 0 and text[0] == "=+:
# #         return  text + "\t "
# #     elif len(text) == 0:
# #         return text 
# #     else:
# #         return text  
# # print(Lastcharacer("Hellojuma;"))


# print("hello")
# name="Juma"
# print(name.capitalize())
# print(name.capitalize())
# print(name.upper())
# print(name.lower())
# print("hello this is the next line ",end='')
# print("hello juma ")
# a=10
# b=20
# if a==b:
#     print("a is equal to be ")
# else:
#     print("its not equal to 10")   


# # gender=input("Please can u input ur gender ")
# # profit=input("Enter the profit u earn")
# # age=input("Enter ur age")
# # age=int(age)
# # profit=int(profit)
# # if gender== "M":
# #     if age >26:
# #         dis=profit*0.09
# #         print(dis)
# #     elif age <26:
# #         dis=profit*0.23
# #         print(dis)
# #     else :
# #         print("Incorrect loops ") 
# # elif gender== "F":
# #     if age >26:
# #         dis=profit*0.09
# #         print(dis)
# #     elif age <26:
# #         dis=profit*0.23
# #         print(dis)
# #     else :
# #         print("Incorrect loops ")             
# # else:
# #     print("No lopps")

# for i in range(10):
#     print(i+10)
juma=[1,2,3,45,6,77,8]
print(max(juma))
# for i in range(len(juma)):
#     print(juma[i])


# value=10
# while value > 0:
#     value=int(input("Enter a value "))

# def odd( number):
#     if number%2==0:
#         print("Its even number")
#     else:
#         print("Its odd number ")    

# odd(2)




# import math
# pe=math.pi
# # 2*pe=math.tau
# # inputs of the data from the usetr
# radius=float(input("Enter the radius :"))
# Height=float(input("Enter the Height :"))
# #calculation of the surface are 
# area=(pe*radius**2)
# #printing the are of the programs
# print(f"The are is :{area}")
# surface_are=(2*pe*radius*radius)+(pe*(radius+radius)*Height)
# #printing of the results outputs 
# print("The surface are is :",surface_are)
# volume=area*Height
# #printing out the volume 
# print(f"The volume is :{volume}")

#having a mobile device can be a life saver on long road trips 
#programs like google mpas finds the shortest routes and estimates the time of the arrival
#Find the shortest route 
#The time of arrival is best on the current time + How long the trip will take 
#Write a program thats inputs the current time and estimate the lenght of a trip ,calculate the time of arrivall
#and outputs the results in ours and minutes 
#Th prompts _____
# import time 
# from datetime import datetime,timedelta
# curenttimes=datetime.now().time(
# fredyy={
#     "mumbo":45,
#     "kakameg":65
# }
# print(fredyy)

# # for keys in fredyy.keys()
# destination=input("Enter the destination from our platform")
# curenttime=3 
# routes="Mombasa"
# if routes== "Mombasa":
#     curenttime+fredyy["mumbo"]
# else :
#     curenttime+fredyy["kakameg"]

# print("The current time is :",curenttime)
import math

# Input values
a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))
# Check if quadratic equation is valid
if a == 0:
    print("Invalid input: 'a' cannot be 0 in a quadratic equation.")
else:
    discriminant = (b ** 2) - (4 * a * c)
    if discriminant <0:
        print("No real solutions (discriminant is negative).")
    else:
        sqrt_disc = math.sqrt(discriminant)
        denominator = 2 * a
        root1 = (-b + sqrt_disc) / denominator
        root2 = (-b - sqrt_disc) / denominator
        print("The first value is:", root1)
        print("The second value is:", root2)
        

