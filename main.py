# Function related to numbers
import math

print("\n==Math Functions==")

num = float(input("\n 1) Input a number to process: "))

print("\nRound | round(num)")
print(round(num))

print("\nRound up | math.ceil(num)")
print(math.ceil(num))

print("\nRound down | math.floor(num)")
print(math.floor(num))

print("\nAbsolute(positive value) | abs(num)")
print(abs(num))

print("\nThe power of a number by n | pow(number, n)")
n = int(input("input a integer to power the number by: "))
print(pow(num,n))

print("\nSqrt value of a number | math.sqrt(num)")
print(math.sqrt(num))

print("\nDetermine biggest & smallest number from 3 different values | max(x,y,z) - min(x,y,z)")
x = float(input("input x val: "))
y = float(input("input y val: "))
z = float(input("input z val: "))
print("\nMax: " + str((max(x,y,z))))
print("Min: " + str(min(x,y,z)))

numT = float(input("\n 2) Input a number to process: "))
print("\nRound | round(num)")
print(round(num))

print("Round up | math.ceil(num)")
print(math.ceil(numT))

print("\nRound down | math.floor(num)")
print(math.floor(numT))

print("\nAbsolute(positive) value | abs(num)")
print(abs(numT))

print("The power of a number by n | pow(num)")
m = int(input("Input an integer to power the number by: "))
print(pow(numT, m))

print("\nSqrt value of a number | math.sqrt(num)")
print(math.sqrt(numT))

print("\nDetermine biggest & smallest number from 3 different value | max(x,y,z) - min(x,y,z)")
xT = float(input("input x val; "))
yT = float(input("input y val: "))
zT = float(input("input z val: "))
print("\nMax: " + str(max(xT,yT,zT)))
print("Min: " + str(min(xT,yT,zT)))









