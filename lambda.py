points = [{ 'x' : 2, 'y' : 3 }, { 'x' : 4, 'y' : 1 }]
points.sort(key = lambda i : i['y'])
print(points)
print()

points = [{ 1 : 2, 2 : 3 }, { 1 : 4, 2 : 1 }]
points.sort(key = lambda i : i[2], reverse = True)
print(points)
print()

# Пробую со словарём
dic = {2 : 1, 5 : 3, 4 : 6, 1 : 9}
result = sorted(dic)
print(result)


