#A: Парні індекси

a = ['a', 'b', 'c', 'd']
print(a[::2])

#B: Парні елементи
b = [1,2,2,3,3,3,4]
for el in  b:
   if  el  % 2 == 0:
     print((el))

# C: Більше попереднього
c = [1, 5, 2 ,4, 3]
for el in  c:
   if  el > c[0] :
     print((el))

#F: Найбільший елемент
f = [-1,-2,-2,3,3,3,4]
print( max(f),f.index(max(f)))

#G: Більше своїх сусідів
g = [1, 0, 1, 0, 1]
for el in  g:
   if  el  > g[g.index(el)-1] and el > g[g.index(el)+1]:
     print((el))
x = len(g)
print(x)

#H: Найменший додатний
h = [1, 3, -1, 0, -1]
for el in  h:
   if  el  < 0:
       h.remove(el)
       print(min(h))

# I: Найближче число
i = [6, 5, 4, 2, 1, 3] #3
for el in  i:
   if  el- i[-1] == 1 or el- i[-1] == -1:
       print(el)


#  K: Кількість різних елементів
k =[1, 2, 2, 3, 3, 3]
print(len(set(k)))

#O: Переставити min і max
o =[1, 2, 3]
s = min(o)
z = max(o)
o[s] = z
print(o)
