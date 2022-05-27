print(27)
print("а")
x = float(input())  # 3
y = float(input())  # 4

if x > 2 and y > 3:
    print(True)
else:
    print(False)

print("б")
x = float(input())  # 2
y = float(input())  # 4

if x > 1 or y > -2:
    print(True)
else:
    print(False)

print("в")
x = float(input())  # 0
y = float(input())  # 6

if x >= 0 and y > 5:
    print(True)
else:
    print(False)

print("г")
x = float(input())  # 4
y = float(input())  # -3

if x > 3 or y < -1:
    print(True)
else:
    print(False)

print("д")
x = float(input())  # 4
y = float(input())  # 9

if x > 3 and y < 10:
    print(True)
else:
    print(False)

print("е")
x = float(input())  # 1

if not x > 2:
    print(True)
else:
    print(False)

print("ж")
x = float(input())  # 1

if not x > 2 and x < 5:
    print(True)
else:
    print(False)

print("з")
x = float(input())  # 20


if 10 < x and x <= 20:
    print(True)
else:
    print(False)

print("и")
x = float(input())  # 4
y = float(input())  # 4

if 0 < y <= 4 and x < 5:
    print(True)
else:
    print(False)

print(28)
print("а")
a = float(input())  # 101
b = float(input())  # 102

if a > 100 and b > 100:
    print(True)
else:
    print(False)

print("б")
a = float(input())  # 2
b = float(input())  # 5

if a % 2 == 0 and b % 2 == 0:
    print(False)
elif a % 2 == 0 or b % 2 == 0:
    print(True)
else:
    print(False)

print("в")
a = float(input())  #
b = float(input())  #

if a > 0 or b > 0:
    print(True)
else:
    print(False)

print("г")
a = float(input())  # 9
b = float(input())  # 3
c = float(input())  # 18

if a % 3 == 0 and b % 3 == 0 and c % 3 == 0:
    print(True)
else:
    print(False)

print("д")
a = float(input())  # 96
b = float(input())  # 24
c = float(input())  # 54

if a < 50 and b < 50 and c < 50:
    print(False)
elif a < 50 or b < 50 or c < 50:
    print(True)
else:
    print(False)

print("е")
a = float(input())  # 5
b = float(input())  # -26
c = float(input())  # 55

if a < 0 or b < 0 or c < 0:
    print(True)
else:
    print(False)


print(30)
print("а")
a = float(input())

if a % 2 == 0 or a % 3 == 0:
    print(True)
else:
    print(False)

print("б")
a = float(input())

if a % 10 != 0:
    print(False)
elif a % 3 != 0:
    print(True)
else:
    print(False)