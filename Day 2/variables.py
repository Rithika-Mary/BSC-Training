#How variables are stored in memory and retrieved
x = [10, 20, 30]
y = x

print(id(x))
print(id(y))

y.append(40)

print(x)
print(y)