print(1)
a = True
b = False
c = False

print(a or b)
print(a and b)
print(b or c)


print(6)
x = False
y = False
z = True

print((x or z) and (not z))
print(not x and (not y))
print(not (x and z) or y)

print(x and (not y) or z)
print(y and (not y or z))
print(x or (not (y or z)))

print(8)
x = False
y = True
z = False

print(x and (not (z or y)) or (not z))
print((not x or x) and (y or z))
print((x or y and (not z)) and z)

print(11)
print('а')
x = 1
y = -1
if x ** 2 + y ** 2 <= 4:
    print(True)
else:
    print(False)
print('б')
x = 1
y = 2
if x >= 0 or y ** 2 != 4:
    print(True)
else:
    print(False)
print('в')
x = 1
y = 2
if x >= 0 and y ** 2 != 4:
    print(True)
else:
    print(False)
print('г')
x = 2
y = 1
if x * y != 0 and y > x:
    print(True)
else:
    print(False)
print('д')
x = 2
y = 1
if x * y != 0 and y < x:
    print(True)
else:
    print(False)
print('е')
x = 2
y = 1
if not x * y < 0 and y > x:
    print(True)
else:
    print(False)
print('ж')
x = 1
y = 2
if not x * y < 0 and y > x:
    print(True)
else:
    print(False)


print(14)
print('TT')
x = True
y = True

print(not (x or y))
print(not x and y)
print(x and not y)

print('TF')
x = True
y = False

print(not (x or y))
print(not x and y)
print(x and not y)


print('FF')
x = False
y = False

print(not (x or y))
print(not x and y)
print(x and not y)


print('FT')
x = False
y = True

print(not (x or y))
print(not x and y)
print(x and not y)

print(18)
print('TT')
x = True
y = True

print(not (x and not y) or x)
print(y and not x or not y)
print(not y and not x or y)

print('TF')
x = True
y = False

print(not (x and not y) or x)
print(y and not x or not y)
print(not y and not x or y)


print('FF')
x = False
y = False

print(not (x and not y) or x)
print(y and not x or not y)
print(not y and not x or y)



print('FT')
x = False
y = True

print(not (x and not y) or x)
print(y and not x or not y)
print(not y and not x or y)

print(23)
print('TTT')
a = True
b = True
c = True

print(not ((a or not b) and c) or c)
print(not (a and not b or c) and b)
print(not (not a or b and c) or a)

print('FTT')
a = False
b = True
c = True

print(not ((a or not b) and c) or c)
print(not (a and not b or c) and b)
print(not (not a or b and c) or a)

print('TFT')
a = True
b = False
c = True

print(not ((a or not b) and c) or c)
print(not (a and not b or c) and b)
print(not (not a or b and c) or a)

print('TTF')
a = True
b = True
c = False

print(not ((a or not b) and c) or c)
print(not (a and not b or c) and b)
print(not (not a or b and c) or a)

print('FFT')
a = False
b = False
c = True

print(not ((a or not b) and c) or c)
print(not (a and not b or c) and b)
print(not (not a or b and c) or a)

print('TFF')
a = True
b = False
c = False

print(not ((a or not b) and c) or c)
print(not (a and not b or c) and b)
print(not (not a or b and c) or a)

print('FTF')
a = False
b = True
c = False

print(not ((a or not b) and c) or c)
print(not (a and not b or c) and b)
print(not (not a or b and c) or a)

print('FFF')
a = False
b = False
c = False

print(not ((a or not b) and c) or c)
print(not (a and not b or c) and b)
print(not (not a or b and c) or a)


print(26)
print('TTT')
x = True
y = True
z = True

print(not (x or y) and (not x or not z))
print(not (not x and y) or (x and not z))
print((x or not y) and not (x or not z))

print('FTT')
x = False
y = True
z = True

print(not (x or y) and (not x or not z))
print(not (not x and y) or (x and not z))
print((x or not y) and not (x or not z))

print('TFT')
x = True
y = False
z = True

print(not (x or y) and (not x or not z))
print(not (not x and y) or (x and not z))
print((x or not y) and not (x or not z))

print('TTF')
x = True
y = True
z = False

print(not (x or y) and (not x or not z))
print(not (not x and y) or (x and not z))
print((x or not y) and not (x or not z))

print('FFT')
x = False
y = False
z = True

print(not (x or y) and (not x or not z))
print(not (not x and y) or (x and not z))
print((x or not y) and not (x or not z))

print('TFF')
x = True
y = False
z = False

print(not (x or y) and (not x or not z))
print(not (not x and y) or (x and not z))
print((x or not y) and not (x or not z))

print('FTF')
x = False
y = True
z = False

print(not (x or y) and (not x or not z))
print(not (not x and y) or (x and not z))
print((x or not y) and not (x or not z))

print('FFF')
x = False
y = False
z = False

print(not (x or y) and (not x or not z))
print(not (not x and y) or (x and not z))
print((x or not y) and not (x or not z))