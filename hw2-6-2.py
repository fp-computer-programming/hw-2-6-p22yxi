# Author : Yongdong Xi (Sep 22 2021)

radius = float(input("what is the radius"))
height = float(input("what is the height"))

V = 3.14 * (radius ** 2) * height
S = 2 * 3.14 *radius * (radius + height)

print(V)
print(S)