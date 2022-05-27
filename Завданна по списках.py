
#111111111111
Language =['Ukrainian', 'French', 'Bulgarian', 'Norwegian', 'Latvian']
print(Language)

sorted_Language = sorted(Language)
print(sorted_Language)
Language.sort()
print(Language)
Language.sort(reverse=True)
print(Language)


#22222222222222
a = '1 2 3 4'
b = a.split(' ')
print(b)
print(b[1]+b[0]+b[2]+b[3])
c = list(b)
print(c)


# 33333333
cities = ['Budapest', 'Rome', 'Istanbul', 'Sydney', 'Kyiv', 'Hong Kong']
a =cities[0:4]
b = cities[5]
print(a, "and", b)

#4444444444444
a = list('12345')
print(list('12345'))
a.sort(reverse=True)
print(a)
print(a[0],a[1],a[2],a[3],a[4])
print(''.join(a))

#555555555555555
cities = ['Budapest', 'Rome', 'Istanbul', 'Sydney', 'Kyiv', 'Hong Kong']
sorted_cities = sorted(cities)
print(sorted_cities)
cities.sort()
print(cities)
cities.sort(reverse=True)
print(cities)

b = cities.copy()
c = list(cities)
d = cities[:]
print(c)
print(b)
print(d)

print(len(cities))
print(','.join(cities))
print(cities[1])
print(cities.index('Rome'))

cities[1] = 'Chernivtsi'
print(cities)

cities = ['Budapest', 'Rome', 'Istanbul', 'Sydney', 'Kyiv', 'Hong Kong']
print(cities.append('Lviv'))
print(cities.insert(3, 'Lviv'))
print(cities.remove('Rome'))
print('Rome' in cities )
print(cities.count('Rome'))

